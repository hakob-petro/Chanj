# Three experiments worth testing before adding hormones

**Final proposals after three search branches and three dedicated critic reviews · 26 September 2026**

The strongest first candidate is **visual motion opponency: test how a small fly circuit handles conflicting motion, then block a particular neural output and compare the result with real recordings**. The other finalists are a neural compass benchmark and, conditionally, a feeding motor-sequence experiment. Each can make the measured biological signal central to the demonstration.

This changes our research recommendation, not the implementation: we have not started any of these experiments. The search inspected papers, selected code, actual numerical artifacts, and model/data compatibility. No model was executed or fitted, and no new biological result was obtained. Two candidates are ready for a bounded reproduction attempt; the feeding candidate needs an intervention-correspondence decision first. Runtime and porting effort remain unmeasured.

| Final proposal | Question we can test | Demonstration | Readiness |
|---|---|---|---|
| **1. Conflicting motion** | Can a specified visual circuit account for lost and preserved responses after a targeted output block, and for spatially mixed motion? | Moving dots, circuit activity, and measured versus modeled neural responses | Best first reproduction; compact code and biological arrays inspected |
| **2. Neural compass** | How well does a recurrent ring predict recorded compass activity during turning and pauses in darkness? | Heading replay beside real and modeled activity rings, with prediction errors | Accessible benchmark; input/output data inspected; needs strict calibration and observation rules |
| **3. Feeding sequence** | Can a small motor circuit account for the timing changes caused by selectively silencing an identified motor neuron? | Feeding-chain spike raster, intervention toggle, and delay measurements | Conditional; published code and biological intervention differ |

These proposals deliberately allow a small circuit. None validates the entire MaleCNS connectome. A trained or fitted model is acceptable when its fitting information and evaluation target are explicit; avoiding machine learning does not itself establish accuracy.

## 1. Conflicting motion: the strongest first project

Imagine two sets of dots moving in opposite directions. We change whether they overlap or occupy different parts of the visual field, and observe the fly's neural response. We then block the output of one direction-selective cell class. The experiment asks whether one frozen circuit explains the pattern of responses across these conditions.

**Biological anchor.** Ammer et al. measured responses in a visual circuit containing T4/T5 direction-selective cells, LPi interneurons, and VS output cells. T4/T5c output block affected the corresponding directional responses while sparing opposite-direction responses. Separate recordings measured VS voltage and conductance during spatially mixed motion. The intervention measurements use ArcLight voltage imaging; the mixed-motion measurements include whole-cell electrophysiology. These are distinct assays and cohorts. [Primary study](https://www.nature.com/articles/s41593-023-01443-z)

**What we actually have.** We downloaded the author's code/data repository and compact source-data packages. Selected arrays contain electrical voltage measurements from 16 cells, and intervention arrays are also accessible. The published model uses a small, manually parameterized circuit motif; it is not a full connectome or a trained locomotion decoder. Both the searcher and critic inspected actual numerical arrays. [Pinned repository](https://gin.g-node.org/gammer/Ammer_et_al_2023/src/db1f8089b697d1b19da1394ef94450bbec24f32b), [data record](https://doi.gin.g-node.org/10.12751/g-node.7v3pe6/)

**Proposed demonstration.** Four synchronized panels show the stimulus, a compact circuit, real recordings, and model responses with their errors. A control/output-block switch changes explicitly identified connections. A second view compares overlapping and spatially separated opposing motion. The display needs no speculative movement decoder: the neural response is the measured endpoint.

**First experiment.** Extract a minimal model function and reproduce the published data summaries and fixed-parameter outputs. Then declare which baseline conditions may set parameters, freeze the stimulus and observation rules, and evaluate reserved conditions. Compare the full circuit with a simpler feedforward circuit and a linear subtraction model under the same fitting allowance. The paper's model was developed with these results in view; this remains a retrospective benchmark even if our refit reserves conditions.

**The critic's strongest objection:** removing a pathway can guarantee the disappearance of its signal. That alone is weak evidence. We should require the *joint* pattern: affected responses, preserved responses, and the nonlinear response to mixed motion. A claim that the larger circuit helps requires a measurable improvement over the simpler alternatives, with uncertainty and failures reported.

There are concrete implementation corrections. The notebook named `VSconductances_feedback_block` defaults to `condition=6`, which removes LPi→VS influence; its feedback block is `condition=3`. Modeled conductance is in arbitrary units, while experimental plots use nS. Use declared dimensionless ratios or one independently calibrated scale. Keep ArcLight normalization separate from electrical voltage, and do not silently replace invalid tail samples in conductance arrays. These findings make a small audited extraction preferable to treating notebook execution as sufficient reproduction. [Inspected notebook](https://gin.g-node.org/gammer/Ammer_et_al_2023/src/db1f8089b697d1b19da1394ef94450bbec24f32b/Figure_7/Modelling/Modelling_Figure7_VSconductances_feedback_block.ipynb)

**Proceed when** the baseline reproduction works and the actual intervention, units, and analysis windows are explicit. Before new fitting, derive an acceptance tolerance from measurement variability. **Narrow the claim if** success needs condition-specific normalization, a simpler model performs equally well, or only a guaranteed pathway deletion works. Any modeled feedback manipulation lacking a matched biological experiment remains a simulation prediction.

This route removes the Hh concentration-to-sensory and mouth-readout problems from the first milestone. A later octopamine experiment would still require its own receptor, intervention, and measurement compatibility work; passing this benchmark would not automatically validate modulation.

## 2. Neural compass: a clear demonstration with simultaneous measurements

A localized patch of neural activity can represent heading, moving around a ring as the fly turns. The proposed display makes this easy to see while asking a quantitative question: given measured turning, how accurately does a specified dynamical model predict the recorded neural representation?

**Biological anchor.** Noorman et al. released simultaneous turning and EPG calcium measurements from ten walking female flies in darkness, with five 20-minute trials per animal. The accompanying theory studies small recurrent ring models; it does not supply a detailed reconstructed fly circuit. [Primary study](https://www.nature.com/articles/s41593-024-01766-5)

**What we actually have.** The approximately 172.5 MB processed MATLAB file was downloaded and parsed. It includes measured rotation, neural phase, confidence, and a fluorescence array with dimensions 32 × 12,000 × 50. The 32 entries are imaging bins, not 32 independently identified neurons. The author model and analysis code are available. [Actual dataset](https://doi.org/10.25378/janelia.26169355), [pinned code](https://github.com/HermundstadLab/DiscreteRingAttractor/tree/1d9e83af0d71e8ab828563b991655341eea68fc7)

**Proposed demonstration.** Replay measured turning in a heading icon. Beside it, show actual neural fluorescence, the model's activity ring, and accumulated circular error. Include all ten animals and a trial selector that exposes failures. Movement is the input; neural activity is the prediction. This is not an autonomous navigating fly. All these recordings are in darkness, so switching a lamp off cannot be presented as a tested condition from this dataset.

**First experiment.** Reproduce the basic measured summaries, then compare the small ring with a scalar angular integrator and a leaky integrator. Fit gains, lag, and any observation parameters only on declared calibration trials. For a within-animal test, the first trial could calibrate the remaining trials; that tests transfer across trials, not across unseen animals. Allow each model one disclosed initial neural phase per test trial, then forbid resets and evaluation-window alignment. Report both short-horizon errors and accumulated drift.

**The critic's strongest objection:** a simple integrator can retain heading too. An attractive activity ring does not establish that this neural architecture is necessary. Moreover, fluorescent reporters and smoothing retain a signal after the underlying activity changes. Include an observation-aware null and stationary intervals longer than the approximately one-second smoothing window before attributing persistence to recurrent neural dynamics.

The code inspection found a specific leakage hazard. The published plotting helper computes an offset using neural phases inside each displayed 40-second segment. Its original gain analysis also pools all trials per fly. Those procedures can describe the data, but cannot be imported as our prediction protocol. Use raw measured angular velocity; do not treat the unresolved `_aligned` heading field as an independent input. An apparent logical-indexing error in the plotting helper also needs checking before reuse. [Plot helper](https://github.com/HermundstadLab/DiscreteRingAttractor/blob/1d9e83af0d71e8ab828563b991655341eea68fc7/auxFunctions/Plot_Bump_Examples.m), [trial pooling](https://github.com/HermundstadLab/DiscreteRingAttractor/blob/1d9e83af0d71e8ab828563b991655341eea68fc7/auxFunctions/Combine_Data_Across_Trials.m)

**Proceed when** the data summaries reproduce and all competing models can be scored with frozen calibration and disclosed initial conditions. **Narrow the claim if** the ring needs local phase resets, apparent persistence is explained by the observation process, or the scalar model performs equally well. That last result would still be informative: these observations would not establish the added value of a neural ring model. Matching the full fluorescence heatmap would require an additional independently constrained observation mapping.

This is a strong data-and-model comparison project with a legible visualization. It is weaker than proposal 1 as a matched causal-intervention experiment. New splits of the published dataset remain retrospective evaluation, not new prospective biological evidence.

## 3. Feeding sequence: closest to the original idea, with a real gate

Instead of adding a hormonal loop immediately, investigate a smaller question inside feeding: how are successive motor actions timed, and how does changing one motor neuron affect the later sequence?

**Biological anchor.** Sui et al., published on 24 August 2026, combined simultaneous recordings and perturbations to study a disinhibitory feeding motor chain. In five paired flies, selective MN12V silencing changed the mean MN12D–MN11D first-spike delay from approximately 68.58 to 53.68 ms. Histamine was used with a genetically introduced silencing receptor; this is not evidence about generic histamine injection. [Primary study](https://pubmed.ncbi.nlm.nih.gov/42637923/), [intervention figure](https://www.nature.com/articles/s41593-026-02412-y/figures/5)

**What we actually have.** Published numerical workbooks and a compact spiking model are accessible. The critic independently recalculated the paired biological means and the supplied simulation means. The latter are approximately 88.54 and 79.75 ms: the same direction of change, but different absolute timing and effect size. One thousand simulated trials do not add biological specimens, and the later figure reuses earlier biological observations. [Biological workbook](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41593-026-02412-y/MediaObjects/41593_2026_2412_MOESM9_ESM.xlsx), [simulation workbook](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41593-026-02412-y/MediaObjects/41593_2026_2412_MOESM11_ESM.xlsx)

**Proposed demonstration.** Show an identified motor chain, published example rasters, simulated rasters, and a delay plot with paired biological points. We acquired the intervention cohort's delay summaries, not its underlying spike trains. A small feeding-pump illustration can explain the sequence, but quantitative claims stay with neural timing. The supplied model uses an imposed current pulse; it does not establish autonomous pumping or food ingestion.

**The critic's strongest objection:** the inspected code's `ort` parameter affects every modeled motor layer, while the biological perturbation targets MN12V. A cell-selective replacement would be a new model specification. Unknown intervention strength cannot become a free parameter fitted to the very delay change we call a prediction. Full main Methods were not accessible in this review; public captions, supplementary tables, reporting information, workbooks, and code were inspected. [Pinned intervention implementation](https://github.com/Junjie-Yi/Motoneurons-generate-motor-sequences-via-a-feedforward-disinhibition-cascade/blob/c2f846ffcaf32f5f4ad215262ac877fbb69b5fc0/modeling/LIF_FD_exp.m)

**First experiment, conditional on that gate.** Reproduce the original fixed-parameter outputs and display their discrepancies honestly. Specify a separately labeled cell-selective model only if target identity and an independently constrained perturbation range are defensible. Calibrate baseline timing on declared data, then freeze parameters before evaluating the paired intervention. Compare a fair small alternative and report the full prediction range if intervention efficacy remains uncertain. Retuning separately for each biological condition would invalidate the prediction claim.

**Proceed when** the selective intervention and allowable strength are explicit, and the original numerical implementation has been reproduced or ported with parity checks. **Defer the predictive experiment if** those constraints cannot be obtained. A published-model reproduction can still be delivered, but should not be advertised as an accurate digital feeding circuit. MATLAB toolbox calls and parallel sweeps require environment work; execution time has not been measured.

This is attractive because it directly addresses motor sequencing using measured spikes, without first reconstructing gut secretion and a spike-to-mouth-angle mapping. Its correspondence problem keeps it behind proposals 1 and 2 for immediate implementation.

## What would make the project useful?

The first contribution would be a reproducible benchmark: pinned measurements, a documented model, fixed interventions, simpler competing explanations, and visible prediction errors. A reproduction can be scientifically useful without being a new discovery. The existing papers already establish the target effects; implementing their models does not let us claim those effects as our discoveries.

A stronger subsequent contribution would identify a condition on which plausible models disagree, make a frozen prediction, and compare it with compatible independent measurements. Generating the prediction alone is not its validation. None of the current proposals has produced that result yet.

The first reviewable deliverable should therefore be a figure of **measurement versus prediction**, including failures. The interactive demonstration should expose the same inputs, interventions, uncertainty, and errors. It should not acquire its apparent success from a freely adjustable action decoder.

Our recommendation is to start with proposal 1's minimal numerical reproduction. Proposal 2 is the alternative if the team prefers memory and state dynamics. Proposal 3 is the conditional route if feeding remains central. Hedgehog stays a possible later physiology study; the earlier recommendation to start there has been superseded by this broader comparison. No implementation pivot or new success is assumed.

## Review coverage and provenance

Three search agents explored sensorimotor/feeding, visual, and other behavioral/dynamical assays. Each submitted three candidates to a dedicated critic. The final selection prioritizes inspected evidence and fewer untested interfaces, followed by implementation burden and demonstration clarity. We did not assign numerical scientific-validity scores or estimate delivery times from code size.

The [source and decision audit](alternative-experiments-audit.json) records all nine shortlist decisions, pinned repositories, artifact URLs and hashes, concrete critic findings, and access limitations. Other reviewed candidates remain conditional or deferred; a failed data download is recorded as a session access problem, not proof that public data are unavailable generally. In particular, odor-on/off navigation remains a possible moving-agent alternative after acquiring its actual behavioral data, but its present model is behavioral rather than a neural reconstruction.

The new evidence review supplements the original 96-entry repository inventory; it does not change that catalog or pretend its historic count covers every later code inspection. No models were run, no training or fitting was performed, and no runtime benchmark was completed. Numerical data inspection and descriptive calculations are explicitly distinguished from simulation. The HTML presentation remains the preserved earlier snapshot.
