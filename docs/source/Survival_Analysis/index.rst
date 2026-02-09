Survival Analysis
=================

Welcome to the Survival Analysis module of **PyBH**.

While our core expertise and the heart of this library lie in **Bayesian Inference**,
we recognize the importance of established frequentist methods for benchmarking,
validation, and speed.

Our `SurvivalAnalysis` module provides a bridge between these two worlds,
offering a unified interface to both advanced Bayesian models and standard
frequentist approaches.

Strategic Approach
------------------

* **Expert Bayesian Modeling**: We leverage **PyMC** to provide sophisticated
  survival models that handle complex priors, hierarchical structures, and
  provide a complete picture of uncertainty via posterior distributions.
* **Frequentist Compatibility**: To ensure your workflow is complete, we
  integrate the **Lifelines** library. This allows you to run classical
  statistical tests and models (like standard Kaplan-Meier or Cox PH)
  directly through our API.



Core Capabilities
-----------------

* **Seamless Comparison**: Easily compare Bayesian posterior estimates against
  Frequentist point estimates and confidence intervals.
* **Non-parametric & Regression**: Support for Kaplan-Meier, Weibull,
  and Cox Proportional Hazards across both engines.
* **Unified API**: Maintain a consistent coding style regardless of the
  mathematical engine running under the hood.

Available Models
-----------------

.. toctree::
   :maxdepth: 1
   :titlesonly:
   :caption: Models:

   Kaplan_Meier/Kaplan_Meier
   Cox/Cox
   Weibull/Weibull
