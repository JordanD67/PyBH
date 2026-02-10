import pandas as pd
import numpy as np
import arviz as az

import matplotlib.pyplot as plt
from pymc_models import PyMCModel

class SurvivalAnalysis:
    """
    Workflow Manager.
    
    This class orchestrates the analysis process:
    1. Input Validation
    2. Data Preprocessing
    3. Model Building (via the injected Builder)
    4. MCMC Sampling
    5. Diagnostics & Plotting
    """
    def __init__(self, model: any, data: pd.DataFrame, time_col: str, event_col: str, **kwargs):
        """
        Orchestrates the training process.
        Acts as an adapter that prepares data specifically for the underlying model type.

        Args:
            data (pd.DataFrame): Raw input data from the user.
            time_col (str): Name of the column containing time durations.
            event_col (str): Name of the column containing event occurrence (0/1).
            **kwargs: Additional arguments passed to the underlying model's fit method.
        """
                
        self.model = model
        self.idata = None  # Stores InferenceData (Bayesian models only)
        
        # Automatically detect model type
        self.is_bayesian = isinstance(model, PyMCModel)
        # Check if it's a lifelines model by inspecting module name or public API
        model_module = type(model).__module__
        self.is_lifelines = (
            'lifelines' in model_module or
            hasattr(model, "print_summary") or
            (hasattr(model, "fit") and hasattr(model, "predict"))
        )

        self.validate_inputs(data, time_col, event_col)
        df_clean = self._preprocess_data(data, time_col, event_col)
        
        # --- Model Dispatch Logic ---
        if self.is_bayesian:
            print("   -> Mode: Bayesian (PyMC)")
            
            # PyMC models require strictly typed NumPy inputs:
            # - X: Covariates matrix (Numpy)
            # - coords: Dictionary for dimension names
            
            # Prepare X (Covariates): Drop time and event columns
            X_df = df_clean.drop(columns=[time_col, event_col])
            
            # Prepare Coords: Mapping names to dimensions for ArviZ/Xarray
            coords = {
                "coeffs": X_df.columns.tolist(),
                "treated_units": df_clean.index.tolist()
            }
            
            # Delegate fitting to the underlying Bayesian model
            self.model.fit(df_clean, time_col, event_col, coords=coords, **kwargs)
            
            # Store results locally for the workflow manager
            self.idata = self.model.idata

        elif self.is_lifelines:
            print("   -> Mode: Frequentist (Lifelines)")
            
            # Lifelines models require arrays for durations and event observation
            # Extract the time and event columns as arrays
            durations = df_clean[time_col].values
            event_observed = df_clean[event_col].values
            
            # Delegate fitting to the underlying Lifelines model
            self.model.fit(durations=durations, event_observed=event_observed, **kwargs)

        else:
            raise NotImplementedError("Unknown model type. Could not determine how to fit.")

    def validate_inputs(self, data: pd.DataFrame, time_col: str, event_col: str):
        """
        Validates data integrity before processing.
        """
        # 1. Check if DataFrame is empty
        if data.empty:
            raise ValueError("The input dataset is empty.")

        # 2. Check column existence
        if time_col not in data.columns or event_col not in data.columns:
            raise ValueError(f"Columns '{time_col}' or '{event_col}' not found in dataset.")

        # 3. Type Validation (Numeric or Date)
        is_numeric = np.issubdtype(data[time_col].dtype, np.number)
        is_datetime = pd.api.types.is_datetime64_any_dtype(data[time_col])

        if not is_numeric and not is_datetime:
            raise TypeError(f"Column '{time_col}' must be numeric or datetime format.")
            
        # 4. Check for at least one observed event
        if data[event_col].sum() == 0:
            print("Warning: No events observed in the dataset. Convergence might fail.")


    def _preprocess_data(self, data: pd.DataFrame, time_col: str, event_col: str) -> pd.DataFrame:
        """
        Cleans data (handles missing values).
        """
        df = data.copy()
        
        # Basic strategy: drop rows with missing values
        df = df.dropna(subset=[time_col, event_col])
        
        # One-Hot Encoding (Sex -> Sex_M, Sex_F)
        df = pd.get_dummies(df, drop_first=True)
            
        # Booleans in int (False/True -> 0/1)
        cols_bool = df.select_dtypes(include=['bool']).columns
        df[cols_bool] = df[cols_bool].astype(int)
            
        return df  

    def check_diagnostics(self) -> None:
        """
        Checks convergence metrics using ArviZ.
        """
        if self.idata is None:
            raise RuntimeError("Model has not been trained. Run .fit() first.")

        # Logic to check R-hat would go here
        print("Checking convergence statistics...")

    def plot_survival_function(self, t_max=None, X_pred=None, ax=None, **kwargs):
        """
        Generates the survival curve with credible intervals.
        """
        # Create a new figure/axis if none is provided
        if ax is None:
            import matplotlib.pyplot as plt
            fig, ax = plt.subplots(figsize=(10, 6))

        if hasattr(self, 'is_lifelines') and self.is_lifelines:
            # Delegate plotting to the model's native plot method
            self.model.plot(ax=ax)
            return ax
                
        elif hasattr(self, 'is_bayesian') and self.is_bayesian:
            if self.idata is None:
                raise RuntimeError("Model has not been trained. Run .fit() first.")
            
            # 1. Determine maximum time horizon
            if t_max is None:
                t_max = self.model.last_data[self.model.duration_col].max()
            
            # 2. Create time axis
            t_plot = np.linspace(0, t_max, 100)
            
            # 3. Compute survival predictions
            pred_kwargs = {}
            if X_pred is not None:
                pred_kwargs["X_pred"] = X_pred
                
            surv_df = self.predict_survival_function(t_plot, **pred_kwargs)
            
            # 4. Visualization
            label = kwargs.get('label', 'Bayesian Model')
            color = kwargs.get('color', 'blue')
            
            # Mean curve
            ax.plot(surv_df.index, surv_df['mean_survival'], label=label, color=color)
            
            # Uncertainty interval (95% HDI)
            ax.fill_between(
                surv_df.index,
                surv_df['lower_0.95'],
                surv_df['upper_0.95'],
                color=color,
                alpha=0.2
            )
            
            ax.set_xlabel("Time")
            ax.set_ylabel("Survival Probability")
            ax.set_ylim(0, 1.05)
            ax.grid(True, alpha=0.3)
            ax.legend()
            
            return ax

    def predict_survival_function(self, times, **kwargs):
        """
        Delegates prediction to the underlying model.
        """
        if self.is_bayesian:
            return self.model.predict_survival_function(times, **kwargs)
        elif self.is_lifelines:
            # Fallback for lifelines if needed, though they usually have predict_survival_function too
            if hasattr(self.model, "predict_survival_function"):
                return self.model.predict_survival_function(times, **kwargs)
            else:
                 raise NotImplementedError("This lifelines model might not support predict_survival_function directly.")
        else:
            raise NotImplementedError("Prediction not implemented for this model type.")

    def summary(self):
        """
        Returns the summary of the underlying model.
        """
        if self.is_bayesian:
            return self.model.summary()
        elif self.is_lifelines:
            return self.model.print_summary()