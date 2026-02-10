Hypothesis
==========

**Here is an extensive list of hypotheses you should check on your data before using Cox's model**

    - :ref:`Non-informative censoring <NIC>`
    - :ref:`Proportional hazard assumption <PHA>`
    - :ref:`Linearity <L>`

.. _NIC:
1 - Non-informative Censoring
-----------------------------

In survival analysis, we often deal with **censoring**. A patient is "censored" when we stop
following them before the event of interest (like a relapse or recovery) happens.

However, for a Cox Regression model to be accurate, it relies on a silent but vital assumption:
**Non-informative (or Random) Censoring.**

The core idea
^^^^^^^^^^^^^

In a clinical setting, informative censoring occurs when a **patient’s exit from a study is directly
tied to their medical condition or the treatment itself**, such as dropping out due to intolerable
side effects or becoming too weak to attend follow-up appointments.

This creates a major problem for Cox regression because the **"censored" patients are not a
random loss**. They are often the ones for whom the treatment is failing or causing harm.
By removing them from the analysis, the study is left with a "filtered" group of the healthiest
survivors, **which artificially inflates the drug's perceived safety and efficacy**.

How to tackle this issue
^^^^^^^^^^^^^^^^^^^^^^^^

The trickiest part about this assumption is that **it cannot be tested with math**. Why? Because
once a patient is censored, we have **no data on what happened to them next**. We cannot "prove"
they didn't have the event five minutes after leaving.

Because we can't test it with a formula, we must guarantee it through **rigorous data collection**:
    - Researchers must try their best to keep patients in the study.
    - They must document why someone left.
    - If a patient leaves due to a reason related to the study (like side effects), the assumption is
    violated, and the results become "biased."

.. _PHA:
2 - Proportional Hazard assumption
----------------------------------

The Cox model, as it was proposed in 1972 [Cox1972]_ by Pr. Cox, was made on the assumption that the hazard
function for the two groups should remain proportional, **which means that the hazard ratio is
constant over time**.

**These assumptions should be tested prior to application of COX regression analysis routinely.**

How to tackle this issue
^^^^^^^^^^^^^^^^^^^^^^^^

*Testing and interpreting assumptions of COX regression analysis* (2019) [ST2019]_ gives two way
to check that assumption :

a - **Examination of the Kaplan–Meier curves**. If the below‑mentioned features are seen, then the
probability of violation of this assumption is high :
    - There is a crossing of the Kaplan–Meier curves of the two groups.
    - The curve of one arm drops down, while the other plateaus.
b - **Scaled Schoenfeld residuals**. These are statistical tests and graphical displays which check the
proportional hazard assumption.

.. _L:
3 - Linearity
^^^^^^^^^^^^^^

The Cox model assumes a **linear relationship between any continuous covariates and the log-hazard.**
This means that a one-unit increase in a covariate is assumed to have a constant multiplicative
effect on the hazard rate across its entire range.

How to tackle this issue
^^^^^^^^^^^^^^^^^^^^^^^^

To determine if a continuous variable (e.g., age, weight) requires transformation, **we use
Martingale residuals as a visual diagnostic tool**. These residuals represent the "unexplained"
risk, the difference between observed events and those predicted by a null model. **By plotting these
residuals against the covariate, we reveal the true functional form of the relationship.**

**Interpretation of the Plot**
When you look at your scatter plot with a smoothed line, here is what the shape tells you:
    - **A Straight Line**: The assumption is satisfied. You can include the covariate as it is (linear form).
    - **A Clear Curve** (U-shape or S-shape): The assumption is violated. A unit increase at the low end of the scale doesn't have the same impact as a unit increase at the high end.
    - **Threshold effect**: The plot stays flat then suddenly jumps. This suggests you should probably categorize the variable (e.g., "Low" vs "High" based on a cutoff).

.. [Cox1972] Cox, D. R. (1972). Regression Models and Life-Tables.
   Journal of the Royal Statistical Society.
.. [ST2019] Dessai S, Patil V (2019) *Testing and interpreting assumptions of COX regression
    analysis*. Cancer Res Stat Treat 2019;2:108-11
|
|
|
    | *Signé :*
    | **Jean Van Dyk**
    | *Etudiant IMT Atlantique*
