Cox Proportional Hazards
=========================

.. toctree::
   :maxdepth: 1
   :titlesonly:
   :hidden:

   Hypothesis

Hypothesis
----------

**The Cox model relies on multiple hypotheses that need to be verified for it to be valid.**
There are multiple ways to verify each of them. While the solutions to verify these assumptions
range from quick approximate checks to sophisticated statistical tests, none are implemented in
this library at the moment.
:doc:`Here, you will find an extensive list of these hypotheses along with existing solutions to test them. <Hypothesis>`

Model
-----

.. autoclass:: PyBH.SurvivalAnalysis.pymc_models.Cox
   :members:
   :special-members: predict_survival_function
   :exclude-members: build_model

   The Cox model uses a piecewise constant baseline hazard and exploits the mathematical
   equivalence between the Cox Proportional Hazards model and Poisson regression.

   The docstring above contains detailed mathematical formulations showing how the Cox model
   is equivalent to a Poisson regression model under the piecewise constant hazard assumption.
