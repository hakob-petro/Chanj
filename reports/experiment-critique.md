# Critical review of the Hedgehog and neuromodulation proposals

**Separate critic-agent review and revised project recommendation · 26 September 2026**

**Scope note:** this critique compared the two original proposals. The subsequent [broader search and dedicated reviews](alternative-experiment-proposals.md) supersede its initial project priority with a visual neural benchmark; the objections and conditions below remain relevant to any later Hedgehog or neuromodulation experiment.

The recommendation is to **start with a small Hedgehog feasibility and model-comparison study, assess octopamine only as an alternative visual-circuit experiment, and defer dopamine–Doom**. Neither proposed physiological extension is implemented or biologically validated. This review narrows the next milestone; it does not show that either biological idea is false.

The common risk is circularity: prescribe how a chemical changes neural activity, fit an output rule, observe the expected behavior, and interpret that behavior as evidence for the prescribed mechanism. Prediction on data excluded from fitting is necessary for our proposed validation, but competing models and independently supported measurements are also needed.

This document records the critique requested by the user. It distinguishes published or inspected **facts**, the critic's **inferences**, and **unresolved questions**. The original proposals and source-data details remain in the [Hedgehog report](hedgehog-experiment-data-and-value.md), [neuromodulation report](neuromodulation-doom-experiment.md), and [comprehensive report](session-research-report.md).

## 1. Hedgehog: history and timing change the interpretation

**Fact.** The 2022 study reports persistent effects of early dietary exposure. Gut Hh overexpression throughout development increased the proboscis-extension response, whereas adult-restricted overexpression suppressed it. Adult-restricted knockdown also affected the response. Later diet switches produced transient expression changes, and the authors left aspects of secretion regulation unresolved. These findings support adult modulation while also making developmental and dietary history consequential. [Zhao et al., 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9763350/)

**Inference.** One universal slider meaning “more Hh means less sweetness” cannot represent the full intervention set. A model restricted to specified adult conditions may remain useful. A continuously feeding simulation would additionally assume how meals change secretion, transport, receptor effects, and later intake. The selected measurements do not determine all those dynamics.

**Decision.** Begin with defined histories and adult interventions. Treat an intake-driven endocrine cycle as a later hypothesis requiring temporal and consumption measurements. Do not assume that feedback must oscillate or that an observed gene-expression time course measures hormone release after a meal. Persistent dietary history may be the better first scientific question.

**Severity.** This blocks a claim that we have reproduced meal-driven endocrine cycling. It does not block a bounded sensory-state or history experiment.

## 2. Hedgehog: the input and output interfaces could determine the result

### Sensory averages do not specify a unique spike train

**Fact.** The selected sensory observations summarize evoked spikes during three seconds after contact. The source table does not itself provide a complete temporal input for every identified neuron in our model. [Recording methods](https://pmc.ncbi.nlm.nih.gov/articles/PMC9763350/), [extracted measurements](data/hedgehog-sensory-fig7b.csv)

**Inference.** An initial burst, sustained firing, and correlated firing across cells can share an average while producing different downstream activity. Using independent Poisson events at a matching mean adds a modeling assumption. Moreover, the repository's stochastic input-event rate is not automatically the resulting sensory-neuron spike rate. [Pinned neural implementation](https://github.com/dicnunz/fly-brain-feeding/blob/86c7d84fccb1269842c8520846fc006a79fb3487/model.js)

**Unresolved question.** Can compatible temporal recordings or independently justified input statistics constrain the encoder? If not, test plausible timing and correlation assumptions and report whether the conclusion changes. The existing L-glucose-versus-sucrose, age, sex, and sampling differences remain separate compatibility problems; they are listed in the [data report](hedgehog-experiment-data-and-value.md#3-the-data-compatibility-work-that-comes-first).

### MN9 activity is not a calibrated full-extension probability

**Fact.** MN9 controls rostrum lifting, one part of proboscis movement. Other motor neurons participate in the full movement. Shiu and colleagues explicitly state that the precise relationship between MN9 firing and rostrum-lifting probability is unknown. The feeding prototype converts MN9 spikes into a simplified force, spring, and damping model. [Shiu et al., 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11446845/), [pinned body implementation](https://github.com/dicnunz/fly-brain-feeding/blob/86c7d84fccb1269842c8520846fc006a79fb3487/body.js)

**Inference.** Fitting an animation threshold to the Hedgehog assay's full-extension endpoint could absorb the effect we intend to explain. Freezing that threshold afterward prevents retuning; it does not establish that the initial mapping was biologically correct.

**Decision.** Treat sensory and MN9 responses as intermediate model outputs. Claim quantitative PER prediction only when the sensory-to-motor and motor-to-assay mappings have independent support. If such support is unavailable, narrow the endpoint and explicitly state what remains untested.

**Severity.** This is a blocker for the current end-to-end quantitative feeding claim, not for investigating the circuit's response to uncertain sensory inputs.

## 3. Hedgehog: the connectome must earn its explanatory role

**Inference.** If an externally fitted function determines how Hh changes sensory activity, and a fitted monotonic readout converts that activity into extension, a small model might explain the same observations without the large neural graph. The animation would then show a consequence already determined by its interfaces.

Compare a simple diet-to-response model with a history-dependent physiological model under the same fitting and evaluation conditions. Add the feeding circuit for a separately justified downstream prediction. If claiming that the wiring adds mechanistic value, seek an outcome that depends on it—preferably a cell-specific intervention—and compare fairly against an appropriate simpler alternative. Predicting another intermediate concentration can test generalization but may distinguish the competing mechanisms poorly.

Equivalent performance would still support a useful benchmark or indicate that a simpler model is sufficient for the chosen assay. It would not establish an advantage from the connectome. Novelty should come from a discriminating prediction, reusable evaluation, or informative model comparison, rather than reproducing an already published qualitative effect.

## 4. Doom: a fixed interface does not make game performance biological

**Fact.** The pinned DOOMFLY implementation uses engineered neural-to-button assignments, already includes experimental dopamine-dependent plasticity, and reports failed visual, conditioning, and survival validation. Those failures are the repository authors' reports; neither this critique nor our earlier review independently reran them. [Pinned README](https://github.com/nftechie/doomfly/blob/71ecf53d78eaffaf1a57ed7b0ccf5d458abc9f33/README.md), [training protocol](https://github.com/nftechie/doomfly/blob/71ecf53d78eaffaf1a57ed7b0ccf5d458abc9f33/docs/doom-live-training.md), [learning implementation](https://github.com/nftechie/doomfly/blob/71ecf53d78eaffaf1a57ed7b0ccf5d458abc9f33/doom_learning_v6/rule.py)

**Inference.** Freezing the decoder permits a controlled comparison within that engineered agent. Another reasonable mapping could turn the same neural change into a different game outcome. “Dopamine improved this agent's score” therefore cannot establish what dopamine improves in a living fly. Neural stimulation also does not by itself represent a measured chemical concentration or drug dose.

**Decision.** Validate the relevant sensory or learning effect in a defined assay first. Report game performance as a separate engineering result, with its decoder dependence explicit. If making a broader claim about agent performance, examine sensitivity to reasonable interfaces specified before evaluating the result.

**Severity.** The biological interpretation of a game-score difference is unsupported. An explicitly engineered-agent comparison remains legitimate. Adding dopamine alone also lacks novelty relative to the existing experimental mode.

## 5. Octopamine: plausible mechanisms and better starting models

**Fact.** The selected visual study reports state-dependent activity and temporal tuning, discusses limits in separating baseline from response-amplitude changes, and includes a simple motion-detector model. Its measurements do not uniquely identify every dynamic parameter of a proposed modulation mechanism. [Strother et al., 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5776785/)

The scope of an intervention also matters. Tdc2-GAL4 labels both tyraminergic and octopaminergic neurons. Broad silencing using that driver should not be equated with selective removal of octopamine action at Mi4. This limits what a single manipulation identifies; it does not negate the visual study's other evidence. [Babski et al., 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11064449/), [visual-study methods](https://pmc.ncbi.nlm.nih.gov/articles/PMC5776785/)

**Inference.** A chosen Mi4 gain adjustment reproducing a turning deficit would not uniquely establish that adjustment as the cause. Compare explanations involving excitability, temporal filtering, and generic gain, and preserve the difference between pharmacological exposure, neuronal activation, and broad silencing.

**Fact.** Connectome-constrained models of the fly visual system already predict cell-specific neural responses. They offer candidate starting points and comparisons; they do not arrive with our proposed octopamine experiment validated. [Lappalainen et al., 2024](https://www.nature.com/articles/s41586-024-07939-3)

**Decision.** Assess an established visual model or a smaller circuit before committing to repair DOOMFLY's visual baseline. This remains a compatibility review, not an automatic choice of simulator. Dopamine adds sensory discrimination, learning, and retention requirements. Tyramine and cortisol would each require their own justified assay and mechanism, so neither belongs as an extra slider in the first experiment.

## 6. Smallest defensible experiments and decision criteria

| Route | Minimum useful experiment | Proceed when | Narrow or stop the claim when |
|---|---|---|---|
| Hedgehog | Compare a small history-dependent sensory model with a simpler diet-to-response model on compatible measurements; add the feeding circuit for a justified downstream prediction | A reserved measurement, encoder, and observable are defensible without fitting the desired intervention outcome; uncertainty is reported | Matching requires an unsupported tastant/age transfer or condition-specific readout; the result depends on one unverified timing assumption |
| Octopamine | Reproduce a specified modulation effect in a visual circuit while comparing alternative mechanisms | Baseline direction, speed, and recovery responses work; reserved measurements constrain the proposed modulation relative to suitable alternatives | Generic gain explains the same observations equally well, or the baseline fails; in either case do not claim the specific mechanism has been identified |
| Dopamine–Doom | Establish cue-specific conditioning and later retention without imposed stimulation before introducing game complexity | Sensory discrimination and conditioning pass reproducibly, including unpaired exposure and frozen-plasticity controls | Only scores, movement, or weights change, or apparent learning survives controls that should distinguish association from nonspecific effects |

The criteria are about the claims, not a requirement that every prototype succeed. Accurate prediction does not uniquely identify a mechanism when alternatives agree. Failed prediction rejects that candidate model for the tested assay but does not alone disprove the biological mechanism: the encoder, neural dynamics, missing cells, or observation rule may be responsible. Do not change the interpretation of the test after seeing the result.

## 7. Revised next deliverable and practical value

The next artifact worth reviewing is a **reproducible comparison plot**: biological observations, declared fitting and evaluation conditions, predictions from competing models, and uncertainty. It should expose where explanations agree, where they diverge, and which additional measurement would distinguish them. No such fitted comparison has been produced yet.

For Hedgehog, the immediate work is to select compatible measurements and define the competing small models before extending embodiment. If the available data cannot support the intended downstream prediction, document that limitation and use a narrower sensory endpoint. For a visual alternative, first assess octopamine in an established visual assay. Defer dopamine–Doom until its basic discrimination and learning tests are credible.

The practical contribution could be a reusable benchmark, a demonstrated limit of a proposed model, or a specific prediction that helps prioritize a real experiment. The moving fly or game playback should explain the measured result once available. It should not determine the scientific question or stand in for validation.

## Review scope

The critic inspected the two focused reports, their source audits, relevant portions of the core report, the feeding body implementation, selected pinned DOOMFLY files, and relevant primary literature. The parent review checked the developmental/adult Hh distinction and the MN9 observation limitation against the papers, and checked the additional visual-model and driver-specificity references while documenting the critique.

This was a literature and code review by a separate agent, with no new simulations, fitted models, biological measurements, or independent reproduction of reported failures. The original 96-repository inventory and extracted Hedgehog data are preserved. The HTML presentation remains the earlier snapshot.
