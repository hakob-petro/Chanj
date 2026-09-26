# From a fly connectome to a physiological experiment

**Comprehensive session report · Collection reviewed 25 September 2026 · Feeding, neuromodulation, and critic follow-ups 26 September 2026 · Firebird project exploration**

This report brings together our analysis of Google's fly-connectome announcement, the complete review of repositories linked from Awesome Fly, and the discussion of an embodied fly model with physiological feedback. Subsequent focused reviews identify an existing taste-to-mouth implementation in dicnunz/fly-brain-feeding, assess chemical modulation of the DOOMFLY model, and inspect the actual Hedgehog source-data workbook. The report includes proposed experiments and a path toward social simulations. A [focused project-and-data report](hedgehog-experiment-data-and-value.md) connects the original idea, validation criteria, available measurements, and practical value.

The revised central recommendation is a **small Hedgehog feasibility and model-comparison study before extending embodiment**. Select compatible measurements, compare a history-dependent sensory model with a simpler explanation, and establish whether the existing **taste-to-mouth simulation in fly-brain-feeding** can support a separately justified downstream prediction. Its 15 included software tests passed, but the physiological extension is unimplemented and has no biological validation. A separate [critic review](experiment-critique.md) identifies why developmental history, uncertain sensory timing, and the mouth-motion readout must be resolved before claiming a quantitative feeding model or an intake-driven endocrine cycle.

An alternative focused on rapid visual behavior would assess **octopamine and motion processing in an established visual model or smaller circuit**, with Doom as a later exploratory environment. Defer dopamine–Doom until sensory discrimination and conditioning pass reproducibly; the existing repository already attempts dopamine-dependent learning and reports failed validation. These alternatives are assessed in [Section 12](#12-alternative-experiment-neuromodulation-and-doom), the [dedicated report](neuromodulation-doom-experiment.md), and the [critic's decision criteria](#13-critical-review-and-revised-priorities). No pivot or additional implementation is assumed.

**Navigate:** [Key learnings](#1-what-we-learned) · [Evidence scope](#2-scope-evidence-and-provenance) · [Google's release](#3-what-google-and-its-collaborators-actually-released) · [Modeling and compute](#4-anatomy-executable-dynamics-and-an-embodied-fly) · [Community lessons](#5-what-people-have-already-tried) · [Existing feeding prototype](#a-directly-reusable-baseline-fly-brain-feeding) · [Proposed experiment](#6-the-proposed-experiment-dietary-history-changes-sugar-response) · [Validation](#7-what-would-count-as-a-meaningful-result) · [Social extension](#8-extending-toward-interacting-flies) · [Project sequence](#9-a-practical-sequence-for-the-project) · [Open questions](#10-open-questions-and-risks) · [Glossary](#11-terms-used-in-the-reports) · [Neuromodulation and Doom](#12-alternative-experiment-neuromodulation-and-doom) · [Critique and priorities](#13-critical-review-and-revised-priorities) · [Original 96 repositories](#appendix-complete-inventory-of-96-reviewed-repositories)

## 1. What we learned

1. **The September release is an anatomical resource.** MaleCNS maps a male fly's brain and ventral nerve cord. Executable physiology has to be supplied by a model; a wiring diagram alone does not specify a behaving animal.
2. **The ecosystem contains several different scientific and engineering tasks.** We reviewed 96 distinct repositories directly linked from Awesome Fly. Many use older female FlyWire data, partial circuits, or synthetic models. Games, visualizers, neural engines, physical bodies, and data tools should be evaluated according to their actual roles.
3. **A successful demonstration does not identify its biological cause.** Inputs, artificial action decoders, pretrained motor controllers, and learning rules often explain a large part of the visible result. Using a circuit, learning a task, and benefiting from biological wiring are separate claims.
4. **Physiological feedback is a promising focus for our project.** The same food can evoke a different response as an animal's state changes. A model that predicts this change and a relevant intervention would answer a clear biological question.
5. **A specific experimental target already exists.** Published work connects dietary sugar, gut-derived Hedgehog signaling, sweet-sensory responses, and feeding initiation in adult male flies. This is much narrower than recreating an entire endocrine system.
6. **A close implementation of the initial prototype already exists.** The additional fly-brain-feeding review found contact-driven sugar sensing, a fixed Shiu neural model, and MN9-driven mouth movement that changes subsequent contact. Ingestion, gut state, and Hedgehog signaling are absent. Our proposed contribution is the physiological extension and its biological evaluation.
7. **Social experiments are a later stage.** Fly-specific studies of social isolation offer a better validation target than transferring rodent population-collapse stories directly to flies. Multiple simulated animals do not automatically supply social or reproductive biology.
8. **Chemical modulation needs a specified mechanism.** Neural stimulation, chemical exposure, and arbitrary gain changes are different experiments. A game-performance difference alone cannot validate the mechanism or demonstrate learning. The neuromodulation follow-up separates those questions and proposes independent biological benchmarks.
9. **Real Hedgehog data are available, but their layers need alignment.** We inspected the ten-sheet source workbook and extracted selected protein, sensory, and behavioral measurements. Tastants, ages, units, genetic controls, and replicate structure differ across assays. Resolving those differences is part of building a defensible experiment.
10. **The critique narrows the immediate milestone.** Compare plausible explanations before adding embodiment. A fitted sensory encoder and motor readout could determine the apparent effect, leaving the connectome with little explanatory role. A game-score difference also remains dependent on its engineered action mapping.

The detailed evidence and boundaries for these conclusions follow. The appendix preserves the original 96-repository inventory; the additional feeding-repository review appears in Section 5.

## 2. Scope, evidence, and provenance

The session began with three research stages: understanding the connectome release; surveying the complete Awesome Fly collection; and assessing the user's proposed body–brain and multi-fly experiments. September 26 follow-ups inspected and tested fly-brain-feeding, then researched neuromodulation and reinspected DOOMFLY. The HTML companion is a shorter explanation for a mixed technical audience, preserved at the feeding-review snapshot. At the user's request, subsequent updates affect written reports only; its embedded Markdown download therefore also remains the earlier version.

| Evidence type | What we did | What it can support |
|---|---|---|
| Official releases and primary research | Read official announcements, data documentation, accessible papers and methods | Claims about measured anatomy and the cited experiments |
| Selected code and data inspection | Inspected the original Shiu implementation, official counting outputs and capture CSVs, and selected community methods | Specific statements about those versions and files |
| Repository review | Retrieved a README and root listing for all 96 distinct directly linked repositories; read selected additional files | High-level descriptions and qualified reports of authors' results |
| Focused feeding-repository review | Inspected model, body, integration, packing, documentation, and tests at commit 86c7d84; ran all 15 included tests | Behavior of the tested software and its documented boundaries; no new biological validation |
| Neuromodulation follow-up | Read primary studies and inspected DOOMFLY protocol, v6 code, and reported failures at commit 71ecf53 | Scientific motivation, implementation boundaries, and proposed tests; no Doom experiment rerun |
| Hedgehog source-data inspection | Verified matching publisher/mirror workbooks and extracted selected observations with source-cell provenance | Actual available measurements, descriptive summaries, and compatibility gaps; no model fit or biological validation |
| Engineering calculations | Calculated matrix storage and an illustrative edge-sweep workload | Estimates under the stated assumptions |
| Proposed research | Designed an experiment and validation strategy | A plan to test; no demonstrated outcome |

The complete published Cell methods were not directly accessible during the initial review. We used the published summary and labeled detailed measurements taken from the accessible October 2025 preprint. The original collection review did not install or run projects, audit every line of code, or recursively expand every outgoing link. Its game scores and simulator performance remain authors' reports. The separately identified fly-brain-feeding test outcomes below were rerun locally; its published browser-performance claims were not remeasured.

Original session artifacts: [connectome analysis](../research/fruit-fly-brain-analysis.md), [repository review](../research/awesome-fly-repository-review.md), [96-entry CSV](../research/awesome-fly-repositories.csv), [technical source audit](../research/source-audit.json), and [repository provenance audit](../research/awesome-fly-review-sources.json). The audits preserve inspected versions, file hashes, source locations, and coverage. All repository descriptions are a snapshot of the session review, not a promise about later commits.

The additional [feeding-repository audit](../research/fly-brain-feeding-audit.json) records its pinned commit, inspected-file hashes, test command, and observed outputs. There are 97 distinct repositories reviewed across the original collection and this follow-up; the original collection's 96-entry count and source CSV are unchanged.

The [neuromodulation source audit](neuromodulation-source-audit.json) records the later focused code inspection and literature review. DOOMFLY was already in the collection, so this reinspection does not increase the distinct-repository count.

The [Hedgehog data audit](hedgehog-data-audit.json) records the pinned 2022 workbook, selected CSV exports, units, and data-quality questions. It does not add a repository to the collection or establish a completed physiological simulation.

## 3. What Google and its collaborators actually released

The project was led by HHMI Janelia with Google Research, Cambridge, MRC LMB, and other collaborators. The September 3, 2026 announcement concerns MaleCNS: a reconstructed male fly central nervous system, including the brain and ventral nerve cord. Google's contribution includes image segmentation and tools for exploring very large volumes; the result also depends on microscopy, extensive human proofreading, annotation, and biological analysis. [Google announcement](https://research.google/blog/a-connectomics-milestone-mapping-the-complete-male-fruit-fly-brain/), [Janelia account](https://www.janelia.org/news/researchers-reveal-connectome-of-the-male-fruit-fly-central-nervous-system)

### Release chronology

| Milestone | Date | Interpretation |
|---|---|---|
| MaleCNS v0.9 | October 2025 | Initial public release; project pages differ on the exact day |
| MaleCNS v1.0 | June 8, 2026 | Updated reconstruction and annotations |
| Cell publication and Google announcement | September 3, 2026 | Publication and publicity milestone, following earlier data availability |

This explains why some experiments predate the September announcement. [Project homepage](https://male-cns.janelia.org/), [release notes](https://male-cns.janelia.org/release/)

### From tissue to graph

The workflow starts with fixed tissue imaged using electron microscopy, then aligns images, segments neuronal processes, identifies synaptic partners, repairs errors, and assigns cell labels. Flood-filling networks help reconstruct individual cells through a three-dimensional image volume. The AI used for segmentation is solving an anatomical reconstruction problem. [Segmentation method](https://www.nature.com/articles/s41592-018-0049-4)

The preprint reports 8-nanometre imaging, 160 teravoxels, and roughly 44 person-years of proofreading. The published summary reports approximately 166,700 neurons and 11,710 cell types; exact counts depend on version and inclusion rules. These figures describe reconstruction scale. They do not measure behavioral fidelity. [Preprint methods](https://pmc.ncbi.nlm.nih.gov/articles/PMC12636603/), [published paper](https://doi.org/10.1016/j.cell.2026.08.015)

The graph is usefully represented as C[j,i], the number of reconstructed contacts from neuron j onto neuron i. Twelve contacts between two cells form one directed neuron-pair edge with weight twelve. Neuron counts, contact counts, and edge counts are different quantities. Some release tables include segments outside a chosen set of annotated neurons, so a loader needs a documented inclusion rule. [Data formats](https://male-cns.janelia.org/download/)

Neurotransmitter annotations provide another constraint, sometimes through image-based prediction. They still do not identify every postsynaptic receptor or establish a universal sign, strength, or time course for every interaction. [Transmitter-classification research](https://www.repository.cam.ac.uk/items/c285907d-ed80-4dbd-9bd2-a0bd10abd238), [male optic-lobe methods](https://www.nature.com/articles/s41586-025-08746-0)

### Completeness is different from accuracy

The preprint's approximately 40.1% connection-capture figure concerns detected connections whose endpoints are both traced neurons. It is not a statement that retained connections are 40.1% correct. The inspected v1.0 capture CSV gives region-specific fractions: central brain 35.10%, left optic regions 42.97%, right optic regions 53.79%, and ventral nerve cord 37.23%. These cannot be combined into a global percentage by taking their arithmetic mean. [Preprint definitions](https://pmc.ncbi.nlm.nih.gov/articles/PMC12636603/), [pinned capture table](https://raw.githubusercontent.com/flyconnectome/2025malecns/67767d2233657983993ff6c2be48e836a935863c/supplemental_data/male-cns-v1.0-traced-synapse-capture-by-roi.csv)

The practical consequence is to preserve uncertainty and graph boundaries. A missing connection, a wrong transmitter assignment, and an incorrect physiological gain can each affect a simulation differently.

### Why the resource matters

Whole-CNS anatomy makes it possible to trace candidate routes from sensory input to motor output and compare male and female organization. The published comparison reports 8,069 isomorphic, 138 dimorphic, 289 male-specific, and 71 female-specific types within its comparison set. These are not a partition of every CNS cell type. Companion research follows visual and gustatory pathways, including links from taste to feeding and other behaviors. [Published comparison](https://doi.org/10.1016/j.cell.2026.08.015), [visual pathways](https://www.janelia.org/publication/the-organization-of-visual-pathways-in-the-drosophila-brain), [gustatory pathways](https://www.janelia.org/publication/the-complete-gustatory-connectome-of-adult-drosophila-reveals-how-taste-guides-feeding)

Our interpretation: the strongest immediate use is to nominate specific circuit mechanisms and interventions, then compare their consequences with physiology or behavior.

## 4. Anatomy, executable dynamics, and an embodied fly

Several resources are often conflated under the phrase “fly brain model.”

| Resource | Provides | Boundary |
|---|---|---|
| [MaleCNS](https://male-cns.janelia.org/) | Male brain and nerve-cord anatomy | Does not specify all neuronal dynamics |
| [FlyWire](https://flywire.ai/) | Female brain reconstruction and annotations | Different specimen and identifiers |
| [BANC](https://github.com/htem/BANC-project) | A separate female brain-and-nerve-cord dataset | Not interchangeable with MaleCNS or earlier FlyWire |
| [Shiu brain model](https://github.com/philshiu/Drosophila_brain_model) | Executable spiking model using FlyWire | Validation is specific to tested behaviors and assumptions |
| [Flybody](https://github.com/TuragaLab/flybody) / [FlyGym](https://github.com/NeLy-EPFL/flygym) | Bodies, mechanics, environments, and control infrastructure | A physical body does not establish connectome-driven motor control |
| [Flyvis](https://github.com/TuragaLab/flyvis) | A specialized visual-system model | Does not supply an entire embodied CNS |

A runnable experiment adds several layers:

~~~text
measured graph + modeled dynamics + sensory encoding
          → neural activity → action readout → body/environment
                      ↑                         ↓
                physiological and sensory feedback
~~~

In compact notation, state_next = F(state, C, physiology, input), while action = D(state). The connectome constrains C. It does not uniquely identify F, D, receptor kinetics, metabolism, or the input transformation. The distinction between anatomical and effective coupling is itself an active research problem. [Effectome study](https://www.nature.com/articles/s41586-024-07982-0)

### What the original spiking model assumes

The inspected Shiu code uses a leaky integrate-and-fire formulation, synaptic decay, contact-count scaling, transmitter-based signs, and Poisson stimulation. Common parameter values include:

| Parameter | Inspected value |
|---|---:|
| Membrane time constant | 20 ms |
| Synaptic decay | 5 ms |
| Resting and reset potential | −52 mV |
| Spike threshold | −45 mV |
| Synaptic delay | 1.8 ms |
| Refractory period | 2.2 ms |
| Scale per synaptic contact | 0.275 mV |

These are model choices, not separately measured values for every reconstructed neuron. The inspected silencing routine zeros outgoing weights, although the README describes incoming and outgoing connections. An intervention must therefore be defined operationally. [Pinned implementation](https://github.com/philshiu/Drosophila_brain_model/blob/91bdd1e7dcf193f3e7ca5a8933497fcef63b7960/model.py)

Shiu et al. report 91% agreement across 164 experimentally testable predictions involving feeding and grooming; a subset excluding one experiment set dominated by negative outcomes gives 84%. This is valuable task-specific evidence. It does not establish equivalent accuracy for arbitrary games, endocrine feedback, or a port to MaleCNS. The model omits important physiological mechanisms, including internal-state and long-range neuropeptide dynamics. [Shiu et al., 2024](https://www.nature.com/articles/s41586-024-07763-9)

### Three different meanings of change

- **Activity changes:** membrane potentials and spikes evolve with fixed parameters.
- **Readout learning:** an artificial decoder learns how to use neural activity.
- **Circuit plasticity:** selected connections change under a specified learning rule.

A fourth relevant process is **physiological modulation**: internal state changes how particular cells respond. It can change behavior without changing synaptic weights. Calling every state change “learning” hides the mechanism we are trying to test.

### Compute and data implications

The inspected official counting notebook is configured for v0.9. Its saved output reports 166,391 neurons and 25,563,426 edges under its superclass filter, falling to 6,237,402 edges under a five-contact threshold. We inspected the saved output; we did not rerun a full graph count. A project using v1.0 must compute its own version-specific totals. [Pinned notebook](https://github.com/flyconnectome/2025malecns/blob/67767d2233657983993ff6c2be48e836a935863c/supplemental_data/quantify-neuron-connections.ipynb)

Using an illustrative size of 166,700 cells and 25,582,938 directed edges, a dense float32 matrix occupies about 111 GB, while a minimal sparse CSR representation occupies about 205 MB with 32-bit weights, indices, and row pointers. These are our array-storage calculations, excluding states, delays, framework copies, and training. A full edge sweep at every 0.1 ms step would visit about 256 billion edges per simulated second. This is a workload estimate, not a benchmark; event-driven and reduced models differ.

Implementation implications: preserve large neuron IDs exactly; pin releases and annotations; record filtering and normalization; separate simulated time from display frame rate; and benchmark the actual experiment. For a circuit subset, document omitted inputs and boundary conditions. For groups, immutable connectivity can be shared while each animal retains its own neural and physiological state.

## 5. What people have already tried

The reviewed collection is [cobanov/awesome-fly](https://github.com/cobanov/awesome-fly). It contains applications, research models, datasets, and infrastructure rather than 96 independent biological validations.

<!-- CATEGORY_TABLE -->

Four recurring approaches organize the experiments:

| Approach | What is authored or trained? | Example |
|---|---|---|
| Fixed controller | Input gains and action mappings; no learning required | [Fly64](https://github.com/ornata/fly) |
| Fixed graph with learned readout | An artificial policy or decoder | [Fly Dino](https://github.com/cobanov/flyjump) |
| Internal modeled plasticity | Selected weights under an engineered rule | [Fly Blackjack](https://github.com/WilliamJones/fly-blackjack) |
| Biological topology used for ML | Trainable weights constrained by a measured graph | [Train Your Fly](https://github.com/eudald-seeslab/train-your-fly) |

Representative lessons from the authors' own documentation:

- **Fly Dino:** a small circuit supports a trained readout and strong reported course performance; the reviewed protocol does not establish superiority over equally trained alternative wirings.
- **DOOMFLY and FlyPong:** implemented plasticity and reward signals coexist with documented failed learning checks. This is useful negative evidence.
- **Fly Craftax:** reported achievements need its image-removal controls for interpretation; those controls suggest limited reliance on vision.
- **Closed Loop Fly:** an apparent sensory benefit was traced to a decoder artifact, illustrating why interface code matters.
- **Flybody and FlyGym:** realistic body and environment infrastructure already exists; connecting a circuit to it is a separate scientific and engineering task.
- **Flyvis:** specialized visual models can be constrained by anatomy and evaluated against physiology. Vision need not begin from scratch.
- **Fly Lab, Fly Escape, and paired-brain experiments:** multiple simulated flies or states already appear in the collection. Their presence does not establish a validated social population model.

Each example's source, implementation summary, and limitations appear in the appendix. We should not claim to be the first to combine embodiment, modulation, or multiple agents; our review is not an exhaustive novelty search across all neuroscience literature.

The opportunity we identified is a specific contribution: combine a measured feeding circuit with a justified physiological mechanism and test it against published biological interventions. It is the validation target, rather than the size of the simulated graph, that gives the project a clear purpose.

### A directly reusable baseline: fly-brain-feeding

**Finding: much of our initial taste-to-mouth prototype already exists.** [dicnunz/fly-brain-feeding](https://github.com/dicnunz/fly-brain-feeding/tree/86c7d84fccb1269842c8520846fc006a79fb3487), reviewed on September 26 at commit `86c7d84fccb1269842c8520846fc006a79fb3487`, is a browser experiment with a stationary fly and moving mouthparts. It implements sensory and mechanical feedback, while leaving the dietary-history and gut-signaling extension to be built.

The repository ports the Shiu 2024 model using the **female FlyWire v630** graph: **127,400 neurons, 14,687,178 directed neuron-pair connections, and 52,793,639 anatomical synaptic contacts**. These counts describe the supplied model files. This is a different specimen and dataset from MaleCNS. The JavaScript solver retains fixed signed weights and uses simplified spiking dynamics; there is no RL-trained movement controller. [Data metadata](https://github.com/dicnunz/fly-brain-feeding/blob/86c7d84fccb1269842c8520846fc006a79fb3487/data/metadata.json), [neural implementation](https://github.com/dicnunz/fly-brain-feeding/blob/86c7d84fccb1269842c8520846fc006a79fb3487/model.js)

Its loop is:

1. A virtual droplet overlaps the moving mouth's sensory surface.
2. Contact supplies stochastic 200 Hz stimulation to 21 identified sugar neurons; adding bitter also stimulates 21 bitter neurons.
3. Spikes propagate through the recurrent neural network.
4. Activity from two identified MN9 motor neurons drives a damped, spring-return approximation of proboscis movement.
5. The mouth's new position changes contact and therefore the next sensory input.

The body receives motor-neuron spikes rather than a scripted extension trajectory. Bitter stimulation acts through the neural network. Contact detection, sensory stimulation strength, muscle gain, damping, and joint geometry are modeling assumptions. [Body and sensory interface](https://github.com/dicnunz/fly-brain-feeding/blob/86c7d84fccb1269842c8520846fc006a79fb3487/body.js), [integrated simulation loop](https://github.com/dicnunz/fly-brain-feeding/blob/86c7d84fccb1269842c8520846fc006a79fb3487/app.js#L45)

| Component | Already implemented | What our proposal adds or must validate |
|---|---|---|
| Taste input | Sugar and optional bitter stimulation during contact | Concentration-dependent responses constrained by sensory measurements |
| Neural processing | Fixed Shiu model with identified taste and motor cells | Suitability for the chosen physiological benchmark and sex |
| Mouth movement | MN9-driven simplified mechanics | Calibrated behavioral readout, held fixed across conditions |
| Sensory feedback | Mouth movement changes later contact | Retain this existing loop as a baseline |
| Ingestion and gut state | Absent | Explicit intake model and slow gut dynamics at a later stage |
| Hedgehog and dietary history | Absent | Gut-specific physiological modulation and tests against published interventions |

The repository also omits hunger, digestion, learning, and active visual or olfactory input. Its contact stimulus is fixed, so it does not yet map sugar concentration or prior diet into sensory response. [Scope and limitations](https://github.com/dicnunz/fly-brain-feeding/blob/86c7d84fccb1269842c8520846fc006a79fb3487/README.md)

**What we verified.** We ran `node --test tests/*.test.cjs` in a clean checkout using Node v26.7.0: all **15 tests passed**. The suite checks numerical integration, a small stored Brian2 reference, packed-data integrity, reproducibility, neural interventions, and the integrated body feedback. We reproduced these three-second outputs at seed 123:

| Test condition | MN9 spikes across both cells | Mean normalized mouth extension |
|---|---:|---:|
| Sustained sugar contact | 466 | 0.85045 |
| Sustained sugar plus bitter contact | 52 | 0.09825 |

These are **simulation outputs**, not animal measurements. MN9 clamping prevented movement while upstream taste activity continued. A separate stationary-droplet test produced 13 contact transitions as mouth movement broke and restored contact. [Body tests](https://github.com/dicnunz/fly-brain-feeding/blob/86c7d84fccb1269842c8520846fc006a79fb3487/tests/body.test.cjs), [solver tests](https://github.com/dicnunz/fly-brain-feeding/blob/86c7d84fccb1269842c8520846fc006a79fb3487/tests/model.test.cjs)

Passing these tests establishes the tested software behavior. We did not independently regenerate the packed graph from the original source files, rerun a full-network Brian2 comparison, or validate its movement against tracked flies. The underlying Shiu model has task-specific biological evidence; the added contact encoder and mechanics do not automatically inherit quantitative biological accuracy. [Shiu et al., 2024](https://www.nature.com/articles/s41586-024-07763-9), [repository validation boundaries](https://github.com/dicnunz/fly-brain-feeding/blob/86c7d84fccb1269842c8520846fc006a79fb3487/docs/validation.md)

**Implication for our project.** Retain this as a candidate engineering starting point and acknowledge its existing taste-to-mouth loop. First establish a compatible benchmark and compare a small physiological model with simpler alternatives. A circuit extension would then make sensory input depend on concentration and the appropriate gut-dependent state, with independently supported input and output mappings. Ingestion and time-dependent gut updates remain later work. The female model versus male Hedgehog benchmark is a scientific compatibility question, not a drop-in assumption.

## 6. The proposed experiment: dietary history changes sugar response

**Research question:** Can a connectome-based taste/feeding circuit, combined with one gut-feedback mechanism, predict how prior diet changes the response to the same sugar stimulus and what happens when that feedback is blocked?

This narrows the user's whole-organism idea to one mechanism that can be built, explained, and challenged. The long-term aspiration remains a body–brain system with meaningful internal state. A complete biological clone is not an established or near-term deliverable.

The feeding-repository review supplies an engineering candidate, but the critique adds a preceding feasibility stage: select compatible measurements, compare competing small models, and justify the downstream observable before extending the contact-to-neuron-to-mouth implementation. Existing movement-to-contact feedback and proposed intake-to-gut feedback are two distinct loops. Adding taste sensing and a moving mouth is already demonstrated prior work.

### Published biological target

Zhao et al. studied adult male flies and found that dietary sugar induces gut Hedgehog expression and secretion into circulation, suppressing sweet-sensory responses. Gut-specific knockdown increased sugar-evoked proboscis extension on a standard diet and removed the usual suppression under a high-sugar diet. Local Hedgehog signaling inside taste neurons has a different role; the gut and sensory compartments must be distinguished. The study also shows early-adult timing effects. This is dietary-history biology over hours and days, not a generic instantaneous meal-satiety switch. [Gut–taste study](https://www.nature.com/articles/s41467-022-35527-4)

| Diet history | Intact gut feedback | Gut Hedgehog suppressed |
|---|---|---|
| Standard sugar | Reference response | Increased response |
| High sugar | Reduced sweet response | Usual diet-dependent suppression lost |

These qualitative findings are benchmarks to reproduce under matched experimental conditions, not simulated results from our project. The September 26 data follow-up downloaded and inspected the ten-sheet workbook, verified matching publisher/mirror hashes, and exported selected protein, sensory, and PER observations. No physiological model has been fitted and no curves have been reproduced by a neural simulation. [Study and source-data links](https://www.nature.com/articles/s41467-022-35527-4), [data audit](hedgehog-data-audit.json)

### How the measured data connect to the experiment

The proposed chain is dietary history → a relative gut/circulating Hh state → a measured sensory-response model → the fixed feeding circuit → a calibrated PER observation. Different datasets constrain different links. Relative expression and protein measurements constrain physiology; sensory recordings constrain the neural input; PER supplies a behavioral target. They are not interchangeable values to inject into the connectome.

Our extraction reveals an essential compatibility gap: the main sensory dose-response assay uses L-glucose, whereas the principal PER curves use sucrose. Assay ages and genetic backgrounds also require alignment. We should not treat those measurements as paired observations from the same flies or substitute equal numerical concentrations. The first benchmark may need to remain at the sensory level until a quantitative sensory-to-behavior bridge is justified.

The detailed [data-to-model plan](hedgehog-experiment-data-and-value.md#2-the-practical-connection-to-the-neural-model) includes exact example values, units, the existing stochastic-input interface, and the PER observation rule. Its audit identifies reused control observations and ambiguous metadata that must be excluded from an independent evaluation split until resolved.

### Practical value of the first experiment

The eventual circuit question is whether measured changes at the sensory periphery can explain altered feeding initiation through an unchanged neural circuit. The first feasibility question is whether compatible measurements and independently supported interfaces permit that test. Failure would challenge the combined model, without identifying whether sensory mapping, central dynamics, motor readout, or physiology caused the mismatch. Comparing alternatives could help select laboratory experiments where their predictions differ.

The reusable deliverable is a reproducible physiology-to-neural-input benchmark with fixed observation rules and controls. Its value depends on predicting measurements withheld from fitting and testing whether a simpler model does equally well. Recreating a known qualitative result in an animation alone would not be new biological knowledge. The [practical-value assessment](hedgehog-experiment-data-and-value.md#6-what-is-the-practical-value) distinguishes this near-term purpose from later whole-organism or population aspirations.

### Why taste is the initial modality

The proposed assay can present a controlled sugar stimulus at a known sensory surface and measure a bounded response. That makes the input–output relationship easier to investigate before adding visual navigation or a complete motor apparatus. This is a scope decision, not a claim that vision is unimportant.

Naturalistic sensing requires modality-specific interfaces. Taste should depend on chemical contact at the represented organ. Smell would need local odor concentrations and receptor tuning; vision would need an optical input and an appropriate retinal/visual model; mechanical sensing would need contact or strain variables. A simulator-provided distance to food may be a useful engineering input, but it should not be described as biological taste or vision.

The recent gustatory connectome supplies an anatomical route into feeding circuits. The first gate is to select a dataset and identify the relevant sensory, intermediate, and motor cells. Both fly-brain-feeding's neural reconstruction and the 2022 feeding-circuit study concern females, while the proposed Hedgehog benchmark used males. Cell matching and sex-specific transfer must be checked rather than assumed. We can retain the female model as an engineering baseline while resolving whether the biological benchmark requires an appropriate male circuit. [Gustatory connectome](https://www.janelia.org/publication/the-complete-gustatory-connectome-of-adult-drosophila-reveals-how-taste-guides-feeding), [feeding-circuit experiments](https://elifesciences.org/articles/79887)

### Proposed implementation layers

| Layer | Minimal implementation | Scientific status |
|---|---|---|
| Stimulus | Sugar concentration and physical contact at a represented taste organ | Controlled experimental input |
| Sensory encoding | Concentration-to-activity relationship for selected gustatory neurons | Fit or constrain using physiology |
| Neural circuit | Versioned measured connectivity with documented dynamics | Anatomy measured; dynamics modeled |
| Physiological state | A gut-signal state that changes the appropriate sensory response | Simplification to calibrate and test |
| Motor readout | Relevant motor activity and proboscis-extension proxy | Requires independent support; freezing a fitted threshold alone is insufficient |
| Ingestion | Optional explicit model converting successful feeding into intake | Additional assumption, not implied by extension |
| Gut update | Intake history changes the modeled gut state | Later closed-loop stage requiring temporal data |

In the existing repository, `FlyBody.sensoryRates()` supplies a fixed 200 Hz input during contact. The extension should replace this assumption with a calibrated concentration-and-state response, without adding a direct diet-to-mouth command. The repository's normalized joint extension is also not yet a measured probability of proboscis extension; that observation mapping needs its own calibration.

The long-term loop is sugar contact → sensory activity → feeding circuit → mouth action → modeled intake and gut state → altered sensory responsiveness. Begin with data compatibility and small-model comparison. Sensory-state replay can follow for a justified circuit question; an intake-to-gut loop additionally requires consumption and temporal data. Reproducing the direction of a prescribed state change would not validate those kinetics.

Proboscis extension measures feeding initiation. It must not silently stand in for food consumption, digestion, energy storage, or reproduction. Until the behavioral observation mapping is supported, report sensory and MN9 activity as intermediate model outputs. Probability or latency of extension requires a justified connection to the actual assay; ingestion adds separately identified parameters and its own validation target.

### Endocrine signaling and neuromodulation

Both can alter behavior, but they are not interchangeable mechanisms. A circulating gut signal is endocrine feedback. Dopamine can alter responsiveness locally in a circuit; it is not automatically a global reward variable. Food-deprivation-dependent dopamine signaling in sugar-sensing neurons provides an alternative, more acute preliminary benchmark, but it should not be merged with the longer-term Hedgehog mechanism into one undifferentiated hunger scalar. [Inagaki et al., 2012](https://pubmed.ncbi.nlm.nih.gov/22304923/)

We recommend one mechanism first. Adding insulin, AKH, dopamine, neuropeptides, metabolism, and every muscle simultaneously would add many parameters before we know which observation the model explains.

## 7. What would count as a meaningful result?

The central trap is circularity: programming a suppressive feedback and then observing suppression only demonstrates the encoded rule. The model gains scientific value when it predicts a measurement or intervention that was withheld during fitting.

### Proposed evaluation protocol

1. **Choose the benchmark and split before fitting.** Identify the exact stimulus, age, sex, strain, diet history, and manipulation in the target experiment. Reserve some concentrations, conditions, or interventions for evaluation.
2. **Validate the unmodulated circuit.** Establish an interpretable sensory-to-motor response using fixed dynamics and a documented readout. If this fails, resolve it before adding feedback.
3. **Calibrate a small number of physiological parameters.** Use appropriate sensory measurements where possible. Do not convert gene-expression levels directly into concentrations or receptor gains without an explicit mapping assumption.
4. **Freeze the model and evaluate held-out behavior.** Keep the input encoder and readout constant across diet and intervention conditions. Align the physiological and behavioral assays before using one to predict the other.
5. **Run matched controls.** Compare the model with fixed physiology, with a simple model lacking the connectome, and, if claiming a topology advantage, with appropriately retrained matched rewired circuits.
6. **Report uncertainty and failure.** Vary plausible gains, signs, thresholds, boundary inputs, and random seeds. Show where the conclusions change.

| Claim | Suitable evidence | Insufficient evidence |
|---|---|---|
| Circuit activity influences the output | A defined circuit intervention changes the output | An animated brain beside a behaving body |
| Physiology explains a condition difference | Held-out condition or intervention prediction | Hardcoding a different action for each condition |
| Biological wiring is useful | Matched alternative models under equal calibration budgets | Rewiring only after training the original decoder |
| Behavior resembles the target animal | Agreement with relevant biological endpoints | High score in an unrelated game |
| A closed loop has been implemented | Action changes body state, which changes later neural input | Switching a label between hungry and fed |

These biological evaluation criteria remain outstanding for our physiological extension. The 15 passing feeding-repository tests establish software behavior and sensory feedback, not a replicated Hedgehog experiment. An informative negative result is acceptable: for example, a simple sensory gain model might predict the benchmark as well as the full circuit. That would limit the role we can attribute to the connectome and help choose the next experiment.

## 8. Extending toward interacting flies

The user proposed abundant-resource population experiments inspired by rodent studies. The famous Universe 25 case involved mice; Calhoun also studied rats. It was a confined population experiment, not a clean demonstration that food abundance alone causes depression or reproductive collapse. Fly simulations cannot inherit rodent-specific social mechanisms by analogy. [Calhoun, 1973](https://pubmed.ncbi.nlm.nih.gov/4734760/)

A more relevant bridge is the fly study in which chronic social isolation increased feeding and reduced sleep despite uninterrupted food access. It reported a starvation-like signature and implicated peptidergic fan-shaped-body P2 neurons. This supplies measurable endpoints and a causal circuit target. It does not establish a subjective emotional diagnosis. [Li et al., 2021](https://pubmed.ncbi.nlm.nih.gov/34408325/)

Our proposed progression is: validated individual taste/feeding model → explicit social-input and state mechanism → isolated-versus-grouped comparison. The gut-feedback loop alone does not imply that isolation effects will emerge. A separate model must connect sensory interactions and social history to the relevant neural or physiological state.

For a population model, each individual needs its own position, sensory observations, neural state, physiological history, and any mutable weights. Shared immutable connectivity can save memory. Noise seeds create model realizations, not independent biological specimens. Parameter and model uncertainty remain shared across a thousand copies.

Reproduction requires additional sex-specific anatomy or models, mating behavior, reproductive physiology, development, and population bookkeeping. Copies of a male connectome do not supply those components. Start with contact rates, spatial distributions, feeding, or carefully defined sleep-related endpoints. Add egg production or reproductive success only when the necessary mechanisms and validation exist.

At scale, fast neural dynamics and slow physiological histories may need different integration rates or validated reduced models. We have not measured throughput, and should not promise a specific number of real-time flies before benchmarking the intended workload.

## 9. A practical sequence for the project

The event's website describes a short build sprint. Our proposed hackathon deliverable is deliberately smaller than the complete scientific program. [Firebird event](https://hackathon.firebird.ai/)

| Stage | Deliverable | Exit condition |
|---|---|---|
| Feasibility and model comparison | Compatible measurements, small competing models, and a fitting/evaluation plan | The observable is defensible; additional circuit complexity has a stated predictive purpose |
| Data and circuit selection | Pinned fly-brain-feeding baseline and a decision on female-to-male transfer | Relevant cells, benchmark compatibility, and input/output semantics are documented |
| Baseline assay | Extend the existing contact loop with calibrated sugar stimulation and motor readout | Sensory and behavioral mappings agree with relevant measurements |
| Physiological replay | Standard/high-sugar states and gut-specific intervention | All conditions use one frozen model and readout |
| Validation | Published and simulated response curves, baselines, uncertainty | Held-out performance and failures are reported |
| Dynamic feedback | Explicit ingestion and time-dependent gut state | Temporal behavior is tested against suitable data |
| Social extension | A small interacting group with a stated social mechanism | Individual and group endpoints have separate validation |

The next reviewable deliverable is a comparison plot showing observations, predictions from competing explanations, and uncertainty, with fitting and evaluation conditions identified. A later presentation can show one virtual fly, two diet histories, a gut intervention, and biological-versus-model responses if their connection is justified. If calibration is incomplete, identify the traces as hypothetical model outputs. The current HTML report explains the earlier proposal and published qualitative patterns; it is not a neural prototype and remains unchanged.

### Components worth reusing

| Need | Candidate resources | What to verify before adoption |
|---|---|---|
| Cell identity and graph access | MaleCNS tools, annotations, Connectome Interpreter, data-prep utilities | Release, identifiers, inclusion rules, and authentication |
| Initial taste-to-mouth prototype | [fly-brain-feeding at 86c7d84](https://github.com/dicnunz/fly-brain-feeding/tree/86c7d84fccb1269842c8520846fc006a79fb3487) | Female v630 compatibility; concentration encoding and behavioral calibration; separate code/data terms |
| Neural dynamics | Original Shiu model; Eon and other optimized implementations | Numerical equivalence, assumptions, device support, and licenses |
| Visual explanation | Fly Connectome Template | Activity interface, anatomy coverage, and attribution terms |
| Future body/environment | Flybody or FlyGym | Which actions use trained controllers and which use the circuit |
| Future vision | Flyvis | Input conventions, cell mapping, and scope of validated predictions |

fly-brain-feeding remains the candidate engineering starting point if the feasibility study justifies a circuit extension. The biological dataset and physiological interfaces remain to be resolved; the other resources are candidates for specific layers. Selecting a runtime or obtaining a body model does not validate the biological interface between them.

## 10. Open questions and risks

| Question or risk | Why it matters | Next resolving action |
|---|---|---|
| Which dataset and sex? | The available circuit and physiological studies are not all from the same specimen or sex | Select the benchmark first, then verify homologous cells |
| Are numerical benchmark data compatible? | Available sensory, protein, and PER data differ in tastant, age, genotype, units, and replicate structure | Use the extracted source tables to select a matched benchmark and resolve identified ambiguities |
| Where does the hormone act? | A global gain can mimic an outcome while misrepresenting the mechanism | Constrain targets using receptor and intervention evidence |
| Are slow kinetics identifiable? | Several different dynamic models may fit the same endpoints | Begin with state replay; seek temporal measurements before claiming kinetics |
| Does the readout dominate? | A fitted movement threshold can absorb the target effect; a fixed game interface still has engineered semantics | Obtain independent support for the biological observable, freeze the mapping, and test alternatives |
| Does timing alter the result? | Developmental and adult Hh interventions differ; sensory averages leave spike timing uncertain | Restrict biological scope and assess plausible temporal encoders |
| What does a reduced circuit omit? | Missing inputs may produce misleading dynamics | Document boundaries and test sensitivity to plausible external drive |
| Is there a wiring advantage? | A simpler model may explain the same data | Use matched baselines; limit the claim if the advantage is absent |
| Can it run at the desired scale? | Fast spiking, slow physiology, and many animals multiply work | Benchmark the chosen experiment before choosing population size |
| Is the idea novel? | fly-brain-feeding already implements the taste-to-mouth loop; the collection is not the entire literature | Frame our contribution around calibrated gut feedback and held-out biological evaluation; continue focused prior-art review |

Our recommendation remains provisional in the scientific sense: the selected circuit and source data may reveal a better bounded assay. The broader design principle is durable—choose one mechanism, one causal intervention, and an independent measurement that could show the model is wrong.

## 11. Terms used in the reports

| Term | Meaning here |
|---|---|
| Connectome | A reconstructed map of cells and their anatomical connections |
| VNC | Ventral nerve cord, part of the fly central nervous system |
| GRN | Gustatory receptor neuron, a sensory neuron involved in taste |
| PER | Proboscis extension response; a feeding-initiation measure |
| Endocrine signal | A signal acting through circulation on target tissues |
| Neuromodulation | A change in how cells or circuits respond, through a specified chemical mechanism |
| DAN | Dopamine neuron; its modeled firing is not itself a measured dopamine concentration |
| KC / MBON | Kenyon cell / mushroom body output neuron, cell classes involved in the memory experiments discussed here |
| Readout | The rule converting neural activity into an observable action or prediction |
| Closed loop | Actions alter the world or body, which changes later sensory or physiological input |
| Ablation/intervention | A precisely defined change used to test a component's role |
| Held-out evaluation | Testing against data not used to fit the model |

## 12. Alternative experiment: neuromodulation and Doom

**The idea is scientifically useful if the intervention and its neural effects are independently constrained.** Comparing a fixed connectome model under different chemical states could reveal useful or harmful behavioral changes. The game is an observable test environment; biological credibility comes from reproducing an appropriate real-fly assay before interpreting game performance.

The existing DOOMFLY experiment already stimulates selected dopamine neurons after damage and changes a restricted set of memory-related connections. Its current README explicitly reports failed visual, conditioning, and survival validation. Adding dopamine alone is therefore not the new contribution. A calibrated mechanism, controlled comparison, and independent prediction could be. [Pinned current status](https://github.com/nftechie/doomfly/blob/71ecf53d78eaffaf1a57ed7b0ccf5d458abc9f33/README.md)

| Candidate | Proposed role | Key boundary |
|---|---|---|
| Octopamine | Candidate for a visual-motion assay before a game demonstration | Assess an established visual model; compare alternative modulation mechanisms |
| Dopamine | Cue-specific learning and later retention | Location and timing matter; acute performance must be separated from memory |
| Tyramine | A later adult behavioral-choice experiment | Larval motor effects do not establish an adult game-control mechanism |
| Cortisol | Defer from the first experiment | No calibrated endogenous fly stress-to-neural-performance pathway established by this review |

Real-fly evidence motivates both leading options: octopamine application can change visual motion responses, and specified dopamine signals participate in visual associative learning. Neither result predicts that our Doom model will score better. [Octopamine experiment](https://pubmed.ncbi.nlm.nih.gov/23142045/), [visual learning experiment](https://pmc.ncbi.nlm.nih.gov/articles/PMC4135349/)

Cortisol needs a qualification: a study reported cortisone-acetate effects on fly susceptibility to fungal infection involving dmERR. That finding does not establish a cortisol-driven adult neural stress model, and the study left direct receptor binding unresolved. [Steroid study](https://link.springer.com/article/10.1186/s12866-020-01848-x)

The proposed sequence is: establish a small visual assay; fit one specified modulatory mechanism using biological measurements; reserve independent conditions for evaluation; freeze the game interface; then compare matched model runs. For dopamine, add training followed by testing without imposed stimulation, paired versus unpaired exposure, and frozen-plasticity controls. For octopamine, first compare identical visual input with learning disabled, then evaluate closed-loop behavior.

The demonstration would show baseline and intervention side by side, with actual intervention timing, selected neural responses, behavior, and results across repeated runs. A higher firing rate, more shooting, or a longer individual round would not by itself demonstrate better perception or learning. Unchanged or worse performance is a legitimate outcome.

The [detailed neuromodulation report](neuromodulation-doom-experiment.md) explains the code findings, chemical candidates, controls, visualization, and comparison with gut–Hedgehog feedback. This alternative has not been implemented or simulated here. The HTML presentation is intentionally unchanged.

### What would establish scientific grounding?

The decisive evidence would be a fixed model predicting real-fly measurements and intervention effects withheld from calibration. We should first choose one biological assay, acquire its quantitative data, declare the fitting/evaluation split and acceptance criteria, and freeze the model and readout before evaluation. Compare with simpler explanations and report errors and uncertainty. A modeled pathway ablation is only biologically informative when it predicts the relevant experimental result; disabling an encoded effect alone checks implementation.

Validation applies to the specific neural or behavioral assay tested. It does not automatically validate an entire fly or predict how living flies would perform in Doom. Our present work establishes scientific motivation and a proposed validation protocol, not a validated neuromodulation model. The [concrete validation criteria](neuromodulation-doom-experiment.md#9-how-we-would-establish-scientific-grounding) cover measurement compatibility, failures, retrospective versus prospective evidence, and the claims each stage would support.

## 13. Critical review and revised priorities

At the user's request, a separate critic agent challenged both proposals against the reports, selected code, and primary literature. Its recommendation is to **start a small Hedgehog feasibility study, assess octopamine as an alternative circuit experiment, and defer dopamine–Doom**. This review produced no new simulations or biological validation. The [full critique](experiment-critique.md) distinguishes facts, inferences, unresolved questions, and blockers for specific claims.

For Hedgehog, developmental timing changes the result: gut overexpression throughout development increased PER, while adult-restricted overexpression suppressed it. Adult interventions remain meaningful, but a universal hormone slider and meal-driven secretion dynamics are not established by the selected data. MN9 adds a separate observation problem: it controls rostrum lifting, and its firing-to-movement probability relationship is explicitly uncertain in Shiu's study. Fitting a full-extension threshold could absorb the physiological effect. [Hedgehog study](https://pmc.ncbi.nlm.nih.gov/articles/PMC9763350/), [Shiu et al., 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11446845/)

The critic also identified two modeling risks. Three-second sensory averages leave spike timing and correlations unspecified. Separately, fitted sensory and motor interfaces might explain the data without the connectome. Test plausible encoders and simpler alternatives; a cell-specific intervention would make a stronger test of the wiring's predictive value than reproducing another qualitative diet difference.

For Doom, a fixed neural-to-button mapping controls one source of variation but does not supply biological semantics. A different reasonable mapping could change the game consequence of the same neural intervention. DOOMFLY's authors already report failed visual and conditioning validation; those failures were not independently rerun here. [Pinned repository status](https://github.com/nftechie/doomfly/blob/71ecf53d78eaffaf1a57ed7b0ccf5d458abc9f33/README.md)

For octopamine, compare mechanisms affecting excitability, temporal filtering, and generic gain. A broad neuronal silencing experiment is not a selective Mi4 receptor intervention. Existing visual models with cell-specific response predictions are candidates to assess before repairing a failing whole-brain visual implementation; their prior validation does not automatically extend to our proposed modulation. [Visual-modulation study](https://pmc.ncbi.nlm.nih.gov/articles/PMC5776785/), [visual model](https://www.nature.com/articles/s41586-024-07939-3)

| Route | Next milestone | Condition for proceeding |
|---|---|---|
| Hedgehog | Compare a small history-dependent sensory model with a simpler diet-to-response model | Compatible evaluation measurements and independently supported interfaces; no condition-specific readout tuning |
| Octopamine | Establish baseline visual responses and compare modulation mechanisms | Reserved biological responses constrain the mechanism relative to alternatives |
| Dopamine–Doom | Demonstrate sensory discrimination, cue-specific learning, and retention | Reproducible paired/unpaired and frozen-plasticity controls pass before game claims |

The next scientific deliverable should be an observation-versus-prediction plot that exposes where explanations agree and differ. If simple models perform equally well, retain the benchmark but narrow the claim about the connectome. If predictions fail, investigate the combined model's assumptions; that failure alone does not refute the biological mechanism. Neither a fitted curve nor a convincing animation uniquely identifies a cause.

## Appendix: complete inventory of 96 reviewed repositories

Every entry below comes from the session's reviewed CSV and source audit. Descriptions and evidence limits are preserved together. IDs follow first appearance in Awesome Fly, while the entries are grouped by purpose. The collection's own repository is the index; the 96 count covers its distinct directly linked repositories, including the starter template and related resource lists.

The additional September 26 review of fly-brain-feeding is documented in Section 5 and is not part of this original collection inventory.

<!-- REPOSITORY_CATALOG -->

## Provenance and reproducibility notes

The repository audit records the original collection URL, retrieved content hashes, observed commits, inspected source files, and one-to-one coverage. The original technical audit pins, among other sources, the Shiu implementation at 91bdd1e7dcf193f3e7ca5a8933497fcef63b7960 and the MaleCNS supplementary repository at 67767d2233657983993ff6c2be48e836a935863c. Performance figures in the original collection remain authors' reports. The additional fly-brain-feeding audit pins commit 86c7d84fccb1269842c8520846fc006a79fb3487 and records the 15 locally rerun tests and the model outputs explicitly labeled above. No Hedgehog replication or population-throughput benchmark has been performed.

The Hedgehog follow-up pins the source workbook at SHA-256 41deeecbecbcc97d0c1336c4b1aaf009b3723b93c396086c0cc0ba1fb4866667 and supplies a reproducible extraction script and selected numerical tables. These are published observations and descriptive calculations, not outputs from a new biological model.

The report builder preserves the 96-entry source CSV. Written-report updates preserve the HTML companion and its previously embedded Markdown snapshot; a presentation rebuild requires an explicit request. The current written reports include the neuromodulation follow-up, Hedgehog data mapping, and critic review. The critique is a separate agent's literature/code assessment, not an independent experimental replication. External citations require internet access; the preserved HTML and its earlier embedded report remain usable offline.
