# From a fly connectome to a physiological experiment

**Comprehensive session report · Collection reviewed 25 September 2026 · Feeding, neuromodulation, critique, and alternative-experiment search 26 September 2026 · Firebird project exploration**

This report brings together our analysis of Google's fly-connectome announcement, the complete review of repositories linked from Awesome Fly, and the discussion of an embodied fly model with physiological feedback. Subsequent focused reviews identify an existing taste-to-mouth implementation in dicnunz/fly-brain-feeding, assess chemical modulation of the DOOMFLY model, and inspect the actual Hedgehog source-data workbook. The report includes proposed experiments and a path toward social simulations. A [focused project-and-data report](hedgehog-experiment-data-and-value.md) connects the original idea, validation criteria, available measurements, and practical value.

The latest recommendation is to **first reproduce a small visual motion-opponency experiment against actual neural recordings**. A broader search, with three search agents and a dedicated critic for each branch, found a shorter inspected path to an evidence-based demonstration than the initial hormone proposals. The other finalists are a neural compass benchmark and a conditional feeding motor-sequence experiment. The [final proposal report](alternative-experiment-proposals.md) explains the demonstrations, measurements, strongest objections, and conditions for proceeding. No model was run or fitted during this search; the recommendation is not a completed implementation or biological validation.

The earlier Hedgehog feasibility plan remains documented as a possible later physiology study. The existing **taste-to-mouth simulation in fly-brain-feeding** passed its 15 included software tests, but our physiological extension remains unimplemented. Developmental history, uncertain sensory timing, and the mouth-motion readout remain unresolved. Octopamine also requires a separately matched modulation assay; a working visual baseline would not validate a chemical intervention automatically. Defer dopamine–Doom until its sensory and conditioning prerequisites pass. Sections 6, 9, 12, and 13 preserve those earlier proposal-specific plans; [Section 14](#14-broader-search-and-final-alternative-proposals) gives the current comparison.

**Navigate:** [Key learnings](#1-what-we-learned) · [Evidence scope](#2-scope-evidence-and-provenance) · [Google's release](#3-what-google-and-its-collaborators-actually-released) · [Modeling and compute](#4-anatomy-executable-dynamics-and-an-embodied-fly) · [Community lessons](#5-what-people-have-already-tried) · [Existing feeding prototype](#a-directly-reusable-baseline-fly-brain-feeding) · [Proposed experiment](#6-the-proposed-experiment-dietary-history-changes-sugar-response) · [Validation](#7-what-would-count-as-a-meaningful-result) · [Social extension](#8-extending-toward-interacting-flies) · [Project sequence](#9-a-practical-sequence-for-the-project) · [Open questions](#10-open-questions-and-risks) · [Glossary](#11-terms-used-in-the-reports) · [Neuromodulation and Doom](#12-alternative-experiment-neuromodulation-and-doom) · [Earlier critique](#13-critical-review-and-revised-priorities) · [Final alternative proposals](#14-broader-search-and-final-alternative-proposals) · [Original 96 repositories](#appendix-complete-inventory-of-96-reviewed-repositories)

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
11. **The broader search changes the recommended starting point.** Direct neural benchmarks in visual motion, compass dynamics, and feeding sequences offer fewer untested interfaces. Published models still need careful reproduction: critics found intervention mismatches, evaluation-data alignment, incompatible units, and fitting provenance that could otherwise create misleading agreement.

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
| Alternative-experiment search and critique | Three search branches, nine shortlisted candidates, three dedicated critics; selected numerical artifacts and code inspected | Final proposals and concrete feasibility gates; no model execution, fitting, or new biological evidence |
| Engineering calculations | Calculated matrix storage and an illustrative edge-sweep workload | Estimates under the stated assumptions |
| Proposed research | Designed an experiment and validation strategy | A plan to test; no demonstrated outcome |

The complete published Cell methods were not directly accessible during the initial review. We used the published summary and labeled detailed measurements taken from the accessible October 2025 preprint. The original collection review did not install or run projects, audit every line of code, or recursively expand every outgoing link. Its game scores and simulator performance remain authors' reports. The separately identified fly-brain-feeding test outcomes below were rerun locally; its published browser-performance claims were not remeasured.

Original session artifacts: [connectome analysis](../research/fruit-fly-brain-analysis.md), [repository review](../research/awesome-fly-repository-review.md), [96-entry CSV](../research/awesome-fly-repositories.csv), [technical source audit](../research/source-audit.json), and [repository provenance audit](../research/awesome-fly-review-sources.json). The audits preserve inspected versions, file hashes, source locations, and coverage. All repository descriptions are a snapshot of the session review, not a promise about later commits.

The additional [feeding-repository audit](../research/fly-brain-feeding-audit.json) records its pinned commit, inspected-file hashes, test command, and observed outputs. The original collection plus this feeding follow-up contains 97 distinct repositories; this historical inventory count does not include code inspected in the later alternative-experiment search. The original collection's 96-entry count and source CSV are unchanged.

The [neuromodulation source audit](neuromodulation-source-audit.json) records the later focused code inspection and literature review. DOOMFLY was already in the collection, so this reinspection does not increase the distinct-repository count.

The [Hedgehog data audit](hedgehog-data-audit.json) records the pinned 2022 workbook, selected CSV exports, units, and data-quality questions. It does not add a repository to the collection or establish a completed physiological simulation.

The [alternative-experiment audit](alternative-experiments-audit.json) separately records all nine shortlisted candidates, dedicated critic decisions, pinned code, verified artifacts, and unresolved access or assay issues. Downloaded measurements were inspected and some descriptive summaries recalculated; no model was executed or trained.

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

| Category | Repositories |
|---|---:|
| Starter template | 1 |
| Games and control experiments | 20 |
| Models, simulation engines and research | 18 |
| Desktop pets and interactive worlds | 10 |
| Language, art and other experiments | 13 |
| Datasets and annotations | 8 |
| Analysis and visualization tools | 21 |
| Tutorials | 3 |
| Related resource lists | 2 |
| **Total** | **96** |

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

This section preserves the original Hedgehog proposal. The broader comparison in Section 14 now recommends a neural benchmark as the first project; the physiology plan below remains conditional.

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

The stages below describe the earlier Hedgehog route if selected later. For the current recommended first experiment, follow the reproduction and model-comparison sequence in the [alternative proposals](alternative-experiment-proposals.md).

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

At the user's request, a separate critic agent challenged both original proposals against the reports, selected code, and primary literature. At that stage, its recommendation was to **start a small Hedgehog feasibility study, assess octopamine as an alternative circuit experiment, and defer dopamine–Doom**. The broader search in Section 14 supersedes that project priority while preserving these objections. This review produced no new simulations or biological validation. The [full critique](experiment-critique.md) distinguishes facts, inferences, unresolved questions, and blockers for specific claims.

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

## 14. Broader search and final alternative proposals

We broadened the search beyond hormones and game performance. Three search agents explored sensorimotor/feeding, visual, and other behavioral/dynamical assays; a dedicated critic reviewed each branch's three candidates. Selection prioritized compatible inspected measurements, fewer untested interfaces, reproducibility, and demonstration clarity. It did not require a whole-brain model or exclude trained models.

| Final proposal | Evidence-facing demonstration | Main gate |
|---|---|---|
| **Visual motion opponency — recommended first** | Moving dots and a small circuit beside real and modeled neural responses; targeted output block and spatial-arrangement controls | Reproduce the correct intervention and observation rules, then compare against simpler models without condition-specific tuning |
| **Neural compass** | Measured turning replay beside actual EPG fluorescence, modeled ring activity, and prediction errors | Calibration-only gains and lag, one disclosed initial phase, no evaluation-window realignment, and observation-aware scalar baselines |
| **Feeding motor sequence — conditional** | Published example rasters, simulated spikes, paired measured delays, and a schematic feeding chain | Match selective biological silencing to the model and constrain its strength independently of the desired outcome |

The visual candidate has parsed neural data and compact author code, but its notebook intervention defaults and conductance units need correction before reuse. The compass has simultaneous movement and neural measurements, but published descriptive alignment must not leak into evaluation. The feeding model and measurements agree qualitatively on one delay change while differing quantitatively, and its supplied intervention acts more broadly than the biological manipulation. These are feasibility findings, not completed experimental results. [Visual study and data](https://doi.gin.g-node.org/10.12751/g-node.7v3pe6/), [compass study data](https://doi.org/10.25378/janelia.26169355), [feeding study](https://pubmed.ncbi.nlm.nih.gov/42637923/)

Start by reproducing an existing result, then freeze the model and compare reserved conditions against simpler explanations. A retrospective benchmark can be valuable without constituting a new discovery. A model's failure would identify limits of that specification for that assay, not by itself refute the biological mechanism. Any animated body motion beyond the measured endpoint must remain an illustration.

The [final proposal report](alternative-experiment-proposals.md) supplies the readable ideas and detailed protocols. Its [audit](alternative-experiments-audit.json) preserves all nine shortlist dispositions and artifact provenance. No simulation, training, parameter fitting, or runtime benchmark was performed during this search. The recommendation changes our proposed priority; it does not imply that implementation has begun.

## Appendix: complete inventory of 96 reviewed repositories

Every entry below comes from the session's reviewed CSV and source audit. Descriptions and evidence limits are preserved together. IDs follow first appearance in Awesome Fly, while the entries are grouped by purpose. The collection's own repository is the index; the 96 count covers its distinct directly linked repositories, including the starter template and related resource lists.

The additional September 26 review of fly-brain-feeding is documented in Section 5 and is not part of this original collection inventory.

### Starter template

#### 1. [Fly Connectome Template](https://github.com/cobanov/fly-connectome-template)

Repository: cobanov/fly-connectome-template

**Purpose.** A browser workbench for showing a fly body beside activity in its nervous system.

**Biological substrate.** MaleCNS soma positions; Flybody surface mesh.

**Method.** React/Three.js viewer accepts body-ID activity frames or replay data from a separately supplied model. The supplied atlas contains 124,289 classified soma positions.

**Evidence and limits.** Visualization starter. It does not include a brain simulator or trained controller; anatomical points are not measured neural activity. Its custom attribution terms deserve checking before reuse.

**Potential reuse.** Ready-made body/brain presentation and activity-input format.

### Games and control experiments

#### 2. [DOOMFLY](https://github.com/nftechie/doomfly)

Repository: nftechie/doomfly

**Purpose.** Connect a simulated fly nervous system to Doom pixels, movement, turning and firing.

**Biological substrate.** MaleCNS; full retained graph.

**Method.** Modeled photoreceptors drive the graph; fixed neuron-to-action mappings control Doom. Damage drives an engineered dopamine signal, with experimental plasticity on selected KC-to-MBON synapses.

**Evidence and limits.** The current v6 documentation reports failed visual, conditioning and survival checks. A running Doom integration does not establish learned survival.

**Potential reuse.** Whole-graph importer, sensory/action adapters, native runtime and a documented failure-analysis workflow.

#### 3. [FlyDoom](https://github.com/eganeganegan/flydoom)

Repository: eganeganegan/flydoom

**Purpose.** Test whether biological wiring helps reinforcement learning in VizDoom.

**Biological substrate.** MaleCNS; selected subgraphs.

**Method.** Sparse recurrent controllers with fixed or trainable internal weights, readout-only training, PPO and an optional three-factor plasticity mode; compares against rewired graphs and conventional networks.

**Evidence and limits.** Research framework. Its documentation explicitly leaves topology advantage as an experimental question; implemented training options are not a demonstrated positive result.

**Potential reuse.** Controlled RL comparisons with matched graph and neural-network baselines.

#### 4. [Fly64](https://github.com/ornata/fly)

Repository: ornata/fly

**Purpose.** Let a fly circuit move Mario in Super Mario 64.

**Biological substrate.** MaleCNS; simulated neural controller.

**Method.** Six rendered views feed a compound-eye approximation; selected descending neurons map to forward motion, steering and jumps. Background drive and noise sustain activity.

**Evidence and limits.** Untrained demo with no reward or star-collection objective. Movement can include walking into walls; game completion is not demonstrated.

**Potential reuse.** A visual game interface and transparent mappings from named neurons to controller buttons.

#### 5. [Fly Brain Minecraft](https://github.com/blendi-remade/fly-brain-minecraft)

Repository: blendi-remade/fly-brain-minecraft

**Purpose.** Put neural flies into Minecraft, with feeding, grooming, escape and a walk-through brain display.

**Biological substrate.** MaleCNS; graph filtered to connections with at least five contacts.

**Method.** Java LIF simulation plus modeled senses and an authored body decoder. Looming signals are injected into higher visual cells; food approach uses an added reflex controller.

**Evidence and limits.** Contains simulation assays and software tests. The authors report olfactory saturation and a silent early motion pathway; approach to food is not produced by the connectome. Courtship is not demonstrated.

**Potential reuse.** Runnable Minecraft integration, circuit assays and unusually explicit descriptions of failed sensory pathways.

#### 6. [Fly Flappy](https://github.com/ns2250225/fly-flappy)

Repository: ns2250225/fly-flappy

**Purpose.** Use a fly network to play Flappy Bird in a browser.

**Biological substrate.** MaleCNS; whole retained network with sensory-input edge modifications.

**Method.** Engineered game-state inputs stimulate visual populations. Modes include a fixed escape-neuron controller and online/accelerated training of a logistic action readout.

**Evidence and limits.** The trained readout operates under hard flap-safety rules, so score cannot be attributed solely to neural learning. Incoming connections to sensory cells are removed in the configured graph.

**Potential reuse.** Browser-worker simulation, interactive training and saved/importable action-readout weights.

#### 7. [Flyhard](https://github.com/MarkUnthank/flyhard)

Repository: MarkUnthank/flyhard

**Purpose.** Make a simulated fly steer a car by physically touching a steering wheel.

**Biological substrate.** MaleCNS; embodied foreleg controller.

**Method.** A trained neural controller drives a foreleg; contact turns a passive wheel coupled to CARLA. This introduces a physical intermediate step between neural output and vehicle control.

**Evidence and limits.** Reports 100/100 held-out requested-angle targets after one training run; removing body contact eliminates over 99% of steering. The target is commanded steering, not visual autonomous driving or coordinated pedal use.

**Potential reuse.** A concrete embodiment test with an intervention that checks whether physical contact causes control.

#### 8. [Fly Escape](https://github.com/dzhng/fly-escape)

Repository: dzhng/fly-escape

**Purpose.** A browser puzzle where players arrange objects to influence flies finding an exit.

**Biological substrate.** MaleCNS; selected subgraph.

**Method.** Rust/WASM neural state for each fly, coupled to modeled sensory inputs and movement; includes inspection and replay.

**Evidence and limits.** Playable prototype. Consistent repulsion, puzzle difficulty and feeding effects are not all established; no learning result is claimed.

**Potential reuse.** Small-subgraph browser deployment, separate per-fly state and puzzle-based interaction.

#### 9. [Swat](https://github.com/hrook1/Swat)

Repository: hrook1/Swat

**Purpose.** A swatter game in which a fly reacts to a pursuing threat.

**Biological substrate.** MaleCNS; approximately 6,000-cell subnetwork.

**Method.** A modeled visual pathway, including an LC16-to-MDN route, influences retreats and evasive bursts. Cruising, collisions and animation are authored.

**Evidence and limits.** Fixed-circuit game demo. Neither whole-brain control nor biologically validated flight is established.

**Potential reuse.** A narrowly scoped reflex circuit with a clear, visible consequence.

#### 10. [FlyBrain](https://github.com/Jhongdlp/FlyBrain)

Repository: Jhongdlp/FlyBrain

**Purpose.** A boss-fight arena plus a laboratory for stimulating and training neural flies.

**Biological substrate.** MaleCNS; large LIF network.

**Method.** Rust/WASM simulation receives engineered egocentric features. Escape and motor populations drive actions; experiments add reward/punishment signals and KC-to-MBON plasticity.

**Evidence and limits.** Includes internal assays and controls, but those validate behavior within the project, not biological fidelity. Some attack/learning behavior remains experimental.

**Potential reuse.** Combined game, stimulus sequencer, neural telemetry and training tools.

#### 11. [FlyPong](https://github.com/jonatasperaza/FlyPong)

Repository: jonatasperaza/FlyPong

**Purpose.** Make a fly circuit control a Pong paddle and investigate dopamine-modulated learning.

**Biological substrate.** MaleCNS; selected circuit, with explicitly labeled synthetic fallback.

**Method.** Ball position is encoded as neural input; paddle direction is decoded from activity. Many reward schedules, plasticity settings and normalization changes are investigated.

**Evidence and limits.** The documented circuit can convey the direction signal, but successful dopamine-driven learning was not demonstrated. Several experiments instead produce systematic synaptic depression.

**Potential reuse.** Detailed negative-result log showing why plausible plasticity rules can fail.

#### 12. [Connectome Fighter](https://github.com/Unjuno/connectome-fighter)

Repository: Unjuno/connectome-fighter

**Purpose.** Connect a fly neural controller to the FightingICE fighting-game environment.

**Biological substrate.** MaleCNS; filtered graph; optional Flybody spectator.

**Method.** Numeric observations become Poisson inputs to a Shiu-style LIF model; predefined output populations map to game actions. Body animation uses a separate bounded adapter.

**Evidence and limits.** Research integration with provenance and validation ledgers. Continuous learning is off in the production configuration; public end-to-end production validation is still pending.

**Potential reuse.** Explicit observation/action contracts, intervention logs and separation of policy from spectator body.

#### 13. [Fly Chess](https://github.com/tolatolatop/fly-chess)

Repository: tolatolatop/fly-chess

**Purpose.** A browser chess opponent with a live neural-activity view.

**Biological substrate.** FlyWire v783; whole-brain LIF.

**Method.** Rust/WASM worker; engineered board encoding and a fixed, untrained linear move readout. Includes neuron disconnection controls and a Brian2 comparison.

**Evidence and limits.** Demonstrates an interface to chess; the opponent is weak and is not a trained chess reasoning system.

**Potential reuse.** Client-side neural inference, move-score inspection and interactive lesions.

#### 14. [Fly Craftax](https://github.com/liuzihe02/fly-craftax)

Repository: liuzihe02/fly-craftax

**Purpose.** Train a fly-derived controller in Craftax survival tasks.

**Biological substrate.** MaleCNS; approximately 146,000 non-VNC neurons.

**Method.** JAX LIF brain stays fixed; PPO trains a linear readout of descending-neuron activity. Pixel input, internal needs and discrete actions are engineered.

**Evidence and limits.** The experiment tracker reports more achievements after training, but no convincing survival improvement. Held-out black/static-image controls barely change behavior; the policy mostly alternates forward and interact. Published run artifacts are not bundled and the current random-key sequence differs from the reported run.

**Potential reuse.** An informative ablation study separating reward gains from actual use of vision.

#### 15. [Fly Dino / flyjump](https://github.com/cobanov/flyjump)

Repository: cobanov/flyjump

**Purpose.** Teach a small connectome-based controller to play Chrome Dino.

**Biological substrate.** MaleCNS; 80 selected cells.

**Method.** Eight game features enter a fixed signed recurrent circuit; cross-entropy optimization trains a 243-parameter action readout. The large anatomical display is context, not the executing network.

**Evidence and limits.** Reports survival on 99/100 held-out 180-second courses, with untrained and silenced controls failing. It has not established superiority over comparable arbitrary topology.

**Potential reuse.** Compact, inexpensive training loop with bounded-task evaluation.

#### 16. [NeuroCraft Fly](https://github.com/evnsnclr/neurocraft-fly-public)

Repository: evnsnclr/neurocraft-fly-public

**Purpose.** Demonstrate neural fly behavior inside Minecraft.

**Biological substrate.** MaleCNS; whole retained graph in documented local demo.

**Method.** Neural readouts select authored body programs for several interactions; the repository describes the local controller and shows recordings.

**Evidence and limits.** Public documentation and media, with runnable mod/companion source still pending. An earlier trained readout reportedly performed worse than direct control.

**Potential reuse.** Design documentation and demonstration reference; not currently a complete runnable starting point.

#### 17. [Flyfear](https://github.com/furkancak1r/flyfear)

Repository: furkancak1r/flyfear

**Purpose.** A horror game where a neural fly influences movement and scare events while the human finds an exit.

**Biological substrate.** MaleCNS; fixed whole retained brain.

**Method.** Godot environment plus neural sensory/motor interfaces. A separate reward-updated event-selection layer is pretrained on synthetic players and can adapt from player telemetry.

**Evidence and limits.** Adaptive game-direction experiment. Training the scare-event selector does not demonstrate biological fear or learning within the fixed brain.

**Potential reuse.** A way to use neural state as part of an adaptive human-facing game.

#### 18. [FLYT3 / FLYC4](https://github.com/seanphan/flyt3)

Repository: seanphan/flyt3

**Purpose.** Tic-tac-toe opponents, with additional aerial-fire and satellite-damage image classifiers.

**Biological substrate.** MaleCNS; fixed graph plus two alternative learning mechanisms.

**Method.** The main game trains a descending/motor readout using self-play REINFORCE; the model card also describes a KC-to-MBON dopamine-plasticity variant. Image tasks train small decoders over fixed circuit features.

**Evidence and limits.** Model card reports 62% and 74% wins versus random for the two game variants. Satellite validation accuracy is 60.8%, versus 85.7% for a pixel MLP. Despite the README title, the documented environment is nine-cell tic-tac-toe. These are author-reported results.

**Potential reuse.** Multiple learning formulations and a useful conventional image-classifier comparison.

#### 19. [Fly Swing](https://github.com/JHC56/fly-swing)

Repository: JHC56/fly-swing

**Purpose.** A fly swings on Spider-Man-like webs through a MuJoCo obstacle course.

**Biological substrate.** MaleCNS; escape subcircuit for control, whole CNS for separate visualization.

**Method.** Looming drives a measured giant-fiber circuit. An external nearest-neighbor memory chooses among web directions and can act before the reflex triggers.

**Evidence and limits.** The limitations section clarifies that the whole-CNS simulation only observes and is rendered offline. The controlling circuit is small; the memory and web are invented, and the physical body is a capsule.

**Potential reuse.** Hybrid reflex-plus-memory control and an example of checking what a whole-brain visualization actually controls.

#### 20. [Fly Blackjack / flybrain-starter](https://github.com/WilliamJones/fly-blackjack)

Repository: WilliamJones/fly-blackjack

**Purpose.** A progression from Dino and body control to odor conditioning, learned navigation and a shared blackjack table.

**Biological substrate.** MaleCNS; small motor circuit and extracted mushroom-body circuit.

**Method.** Blackjack situations/actions are encoded like odors; mushroom-body outputs vote on hit/stand/double. Modeled dopamine updates KC-to-MBON synapses, and the table persists the learned state.

**Evidence and limits.** After 30,000 hands the reported negative score improves and basic-strategy agreement reaches 52%, mainly by avoiding busts. Poker failed. Odor-conditioning controls support a role for the implemented plasticity, but shuffled KC-to-MBON wiring learns similarly.

**Potential reuse.** A compact associative-learning model, useful ablations and a persistent public interaction loop.

#### 21. [Fly-NAF](https://github.com/ArtyMend07/Fly-NAF)

Repository: ArtyMend07/Fly-NAF

**Purpose.** Make a fly model operate Five Nights at Freddy's.

**Biological substrate.** FlyWire v783; whole-brain LIF via Eon code.

**Method.** Screen changes drive modeled sensory inputs; escape and other neural readouts trigger doors, looking and monitoring. Accumulators, global gain and a 30-second look safeguard are engineered.

**Evidence and limits.** Untrained controller, with a reported best run reaching 4 AM on night two. Safeguards and preprocessing contribute to performance; no learned game strategy is claimed.

**Potential reuse.** Screen-capture-to-neuron and neuron-to-desktop-action adapters.

### Models, simulation engines and research

#### 22. [Eon fly-brain](https://github.com/eonsystemspbc/fly-brain)

Repository: eonsystemspbc/fly-brain

**Purpose.** Make the Shiu whole-brain model run across several simulation backends.

**Biological substrate.** FlyWire; v783 and legacy v630 support.

**Method.** Implements activation, silencing and spike recording with Brian2 and accelerated alternatives including PyTorch, CUDA-oriented paths, NEST and GeNN.

**Evidence and limits.** Simulation engine and backend comparison, not an embodied animal or autonomous game policy. Numerical agreement and biological validity are separate questions.

**Potential reuse.** A shared engine underlying several listed applications; reference implementations and benchmark machinery.

#### 46. [Shiu Drosophila Brain Model](https://github.com/philshiu/Drosophila_brain_model)

Repository: philshiu/Drosophila_brain_model

**Purpose.** Reference code for connectome-based predictions of sensorimotor neural responses.

**Biological substrate.** FlyWire v630 by default; v783 configuration supplied.

**Method.** Brian2 LIF neurons propagate activation through measured connectivity; users stimulate or silence named neurons and inspect spike times/rates. Includes paper/example notebooks.

**Evidence and limits.** Scientific reference implementation underlying many later demos. It models a selected level of neural physiology and does not provide a full body, sensory world or general learning system.

**Potential reuse.** The reference equations, intervention experiments and numerical baseline for downstream simulators.

#### 47. [Flybody](https://github.com/TuragaLab/flybody)

Repository: TuragaLab/flybody

**Purpose.** A MuJoCo fly body and environments for walking, flying and vision-guided control.

**Biological substrate.** Anatomically detailed body; no connectome required.

**Method.** Provides mechanics, actuators, imitation environments and reinforcement-learning training infrastructure; control policies can be learned without a reconstructed neural graph.

**Evidence and limits.** Published biomechanical/learning platform. Its trained body policies should not be mistaken for behavior obtained from a connectome alone.

**Potential reuse.** A realistic body, action space, environment examples and locomotion-training tools.

#### 48. [FlyGym / NeuroMechFly](https://github.com/NeLy-EPFL/flygym)

Repository: NeLy-EPFL/flygym

**Purpose.** An embodied sensorimotor research environment with vision, olfaction, contact and locomotion.

**Biological substrate.** Biomechanical model, simulated senses and controller interfaces.

**Method.** Combines a micro-CT-derived body, physics, compound-eye sampling, odor sensing and modular control. Users supply or connect neural controllers.

**Evidence and limits.** Published platform; the current 2.x API is a major rewrite, so older examples may need migration. It is not itself the new MaleCNS whole-brain model.

**Potential reuse.** Body/environment physics, sensory interfaces and locomotion components for genuine feedback loops.

#### 49. [Flyvis](https://github.com/TuragaLab/flyvis)

Repository: TuragaLab/flyvis

**Purpose.** Predict visual-neuron responses and investigate motion computation.

**Biological substrate.** Connectome-constrained fly visual system.

**Method.** PyTorch mechanistic networks are constrained by measured connectivity and optimized on visual tasks such as optic flow; pretrained models and analysis notebooks are supplied.

**Evidence and limits.** Official implementation of a published study comparing predicted activity and tuning with visual-system findings. Its evidence concerns a visual subsystem, not an entire behaviorally complete fly.

**Potential reuse.** Trained visual front ends and a stronger template for relating task optimization to biological measurements.

#### 50. [Train Your Fly](https://github.com/eudald-seeslab/train-your-fly)

Repository: eudald-seeslab/train-your-fly

**Purpose.** Package a connectome-constrained model for visual classification.

**Biological substrate.** FlyWire v783; compound-eye mapping and whole-graph message passing.

**Method.** Keeps topology fixed while training synaptic gains, optionally thresholds, and a Kenyon-cell linear readout. Uses a few tanh message-passing steps; neurons do not retain state between steps.

**Evidence and limits.** A trainable graph ML library, not a spiking brain emulation. The study experiments and randomized-network controls are in the separate companion repository.

**Potential reuse.** Reusable training/configuration interfaces and a measured retina-to-graph input mapping.

#### 51. [Connectome visual-computation study](https://github.com/eudald-seeslab/connectome)

Repository: eudald-seeslab/connectome

**Purpose.** Study color, shape and numerical discrimination under biological wiring constraints.

**Biological substrate.** FlyWire v783; companion to Train Your Fly.

**Method.** Trains the graph model and compares four rewiring ensembles with different constraints on degree, wiring amount and connection lengths.

**Evidence and limits.** The authors report an advantage when spatial wiring constraints are matched; less spatially constrained randomized networks can score better. This is a conditional efficiency finding, not a universal advantage for biological topology.

**Potential reuse.** Experimental randomizers, task data pipelines, activity/manifold inspection and figure reproduction.

#### 52. [WebGPU Fly](https://github.com/abgnydn/webgpu-fly)

Repository: abgnydn/webgpu-fly

**Purpose.** Run a browser experiment from neural stimulation through a body, with replayable actions.

**Biological substrate.** FlyWire brain plus separate MANC nerve-cord dataset; Flybody.

**Method.** WebGPU LIF outputs modulate a hand-written tripod gait; default kinematic assistance also writes body velocity. A modeled cross-dataset brain-to-cord bridge joins the two connectomes.

**Evidence and limits.** Useful browser integration, but the README reports slower-than-real-time neural simulation and limited calibration. The body behavior is materially assisted; this is not one intact measured brain-to-cord specimen.

**Potential reuse.** Client-side GPU runtime, MuJoCo/WASM integration and reproducible action replays.

#### 53. [NeuroFly](https://github.com/seven-monarchs/NeuroFly)

Repository: seven-monarchs/NeuroFly

**Purpose.** Combine a continuous brain simulation, physical walking and sensory feedback.

**Biological substrate.** FlyWire v783 LIF plus NeuroMechFly body; separate visual components.

**Method.** Brian2 runs the graph while a locomotor controller moves the body. The documented steering formula is dominated by explicit odor-gradient guidance, with a smaller descending-neuron bias.

**Evidence and limits.** Closed-loop engineering prototype. Navigation is not wholly produced by the connectome; a modeled pattern generator replaces missing VNC motor circuitry. Recordings and analysis plots are provided.

**Potential reuse.** Brain/body synchronization, feedback recording and a concrete integration example.

#### 54. [Fruit Fly Laboratory](https://github.com/vaibhavkedarisetti/fruit-fly-lab)

Repository: vaibhavkedarisetti/fruit-fly-lab

**Purpose.** An interactive laboratory for looming escape, feeding and neural lesions.

**Biological substrate.** FlyWire v783; whole-brain Shiu-style LIF.

**Method.** A modeled looming encoder directly stimulates LC4/LPLC2; activity reaches the giant fiber through measured wiring. A kinematic body and circuit inspector display the outcome.

**Evidence and limits.** Reports that cutting both visual pathways removes the modeled escape-neuron response. It does not simulate the entire retina-to-muscle chain: photoreceptor vision is disabled, and VNC/body mechanics and several physiological mechanisms are absent.

**Potential reuse.** Well-bounded circuit interventions, replay and explicit model-component attribution.

#### 55. [CHIMERA](https://github.com/caparison1234/chimera)

Repository: caparison1234/chimera

**Purpose.** A multilingual text-controlled digital creature with a MuJoCo body.

**Biological substrate.** Larval fly connectome; README describes a 1,373-cell model.

**Method.** Qwen or a rule-based fallback turns language into sensory channels; a larval LIF network produces signals mapped onto body actions and descriptive text.

**Evidence and limits.** Uses an older larval dataset, not the new adult MaleCNS release. Language interpretation is external. Connectome data are fetched separately, and no comparative behavioral validation is established by the README.

**Potential reuse.** Natural-language stimulus translation and a lightweight neural-to-physical-creature interface.

#### 56. [Connectome OS](https://github.com/ruvnet/Connectome-OS)

Repository: ruvnet/Connectome-OS

**Purpose.** A debugger for inspecting, perturbing and measuring simulated neural networks.

**Biological substrate.** Synthetic fly-like graphs and a filtered FlyWire graph.

**Method.** Rust event-driven LIF plus graph partitioning, activity observation and structural interventions. The named repository is a documentation front door; runtime code is on a linked RuVector research branch.

**Evidence and limits.** Alpha demonstrator. Whole-body integration and larger-scale architecture remain planned; the full-graph coherence calculation has documented performance limits. The external source branch is public.

**Potential reuse.** Runtime introspection, perturbation infrastructure and explicit performance/architecture notes.

#### 57. [FastFly](https://github.com/eonfathom/FastFly)

Repository: eonfathom/FastFly

**Purpose.** Accelerate large fly LIF simulations on NVIDIA GPUs.

**Biological substrate.** FlyWire v783.

**Method.** CUDA/CuPy implementations use sparse connections, reduced-precision weights and spike-driven propagation, with a web activity viewer.

**Evidence and limits.** Performance-oriented simulator targeting real-time operation. Citing an LIF paper does not independently validate this implementation; no task-learning result is documented in the README.

**Potential reuse.** GPU kernels, data conversion and real-time activity streaming infrastructure.

#### 58. [MaleCNS Apple MPS Model](https://github.com/seohyunjun/mps-malecns-model)

Repository: seohyunjun/mps-malecns-model

**Purpose.** Run a fly graph on Apple Silicon and train a simple grid-navigation readout.

**Biological substrate.** MaleCNS; PyTorch MPS LIF.

**Method.** The fixed model precomputes features for 25 positions; A2C trains an actor/critic over those cached features. Neural state resets per observation.

**Evidence and limits.** Reports 24/24 starts reaching one fixed goal after training, versus 8.3% before. This is a small fixed-grid check, without temporal neural memory, unseen-goal generalization or biological learning.

**Potential reuse.** Apple GPU data preparation, activity reports and an inexpensive decoder-learning example.

#### 59. [Drosophila Brain MLX](https://github.com/Kisame76/drosophila-brain-mlx)

Repository: Kisame76/drosophila-brain-mlx

**Purpose.** Speed up the Shiu model on Apple Silicon while checking numerical agreement.

**Biological substrate.** FlyWire reference model; additional MaleCNS packs.

**Method.** MLX/Metal implementations of fixed LIF dynamics, with multiple execution paths, a float64 reference and Brian2 comparisons; nothing is trained.

**Evidence and limits.** Reports approximately 0.29 wall seconds per biological second for a specified v630 workload on M4 Pro, versus 2.07 for Brian2. Documents floating-point spike-timing differences and shows sugar-response sensitivity to rewiring.

**Potential reuse.** A carefully scoped acceleration study with reference checks, benchmark caveats and biological-circuit controls.

#### 60. [AxonWeave](https://github.com/dhakalnirajan/axonweave)

Repository: dhakalnirajan/axonweave

**Purpose.** Make measured wiring usable inside ordinary PyTorch, Keras and NumPy models.

**Biological substrate.** MaleCNS; configurable sparse graph layer.

**Method.** Provisioning, explicit sign policies and optional trainable edge parameters preserve topology while allowing surrounding learned layers. Includes Rust extension boundaries.

**Evidence and limits.** Library foundation. Detailed neuron/receptor dynamics, delays, plasticity and certified accelerator benchmarks remain roadmap items; it is not a completed biological simulator.

**Potential reuse.** Reusable substrate packaging, framework adapters and model/provenance metadata.

#### 61. [Emergent Individuality fly-brain](https://github.com/erojasoficial-byte/fly-brain)

Repository: erojasoficial-byte/fly-brain

**Purpose.** Study whether two initially similar neural flies develop different activity and behavior over experience.

**Biological substrate.** FlyWire v783; embodied LIF with Hebbian updates.

**Method.** Combines neural plasticity, modeled senses, NeuroMechFly and an authored body-state controller. Computes custom integration/complexity proxies and includes run records and a preprint.

**Evidence and limits.** Reports divergent weights and behavior. Source inspection shows explicit behavior thresholds and direct sensory contributions, so whole behavior cannot be assigned solely to wiring. Its custom composite index is not evidence of consciousness.

**Potential reuse.** Longitudinal paired simulations, persistent plasticity and recorded-data analysis.

#### 62. [ConnectomeLens / Wired Different](https://github.com/dhruvin-sarkar/ConnectomeLens)

Repository: dhruvin-sarkar/ConnectomeLens

**Purpose.** Ask whether male wiring features identify cell types annotated as sex-related.

**Biological substrate.** MaleCNS; graph and anatomical features at cell-type resolution.

**Method.** A classifier uses connectivity, neuropil and transmitter features; comparisons include 500 randomized wirings, feature ablations and lineage-grouped validation.

**Evidence and limits.** Reports AUC-PR 0.759 versus 0.041 prevalence, but neuropil location alone reaches 0.722. A planned named-cell ranking check fails; proposed candidates need independent anatomical confirmation. Independent, not peer reviewed.

**Potential reuse.** A substantive graph-analysis project with strong controls, interpretable results and an interactive atlas.

### Desktop pets and interactive worlds

#### 23. [Desktop Fly](https://github.com/DenisSergeevitch/desktop-fly)

Repository: DenisSergeevitch/desktop-fly

**Purpose.** A desktop pet reacting to cursor motion, windows, heat and time of day.

**Biological substrate.** FlyWire; 668-cell circuit plus a MaleCNS brain-to-leg extension.

**Method.** Selected neural circuits drive authored body/leg dynamics. Uses a much larger soma atlas for display; a later MaleCNS extension adds brain-to-leg connections through a modeled cross-dataset interface.

**Evidence and limits.** Small-circuit interactive model, not all atlas neurons being simulated. The Windows port has additional native verification still pending.

**Potential reuse.** Desktop embodiment, sensor adapters, articulated movement and interactive stimulation.

#### 24. [Gnat](https://github.com/lubabs770/gnat)

Repository: lubabs770/gnat

**Purpose.** Port the desktop pet to Linux Hyprland/Wayland in Rust.

**Biological substrate.** FlyWire; 668-cell Desktop Fly circuit.

**Method.** Cursor, window, temperature and clock signals feed the neural model; procedural gait and body-state logic render the response.

**Evidence and limits.** A platform port and extension, not an independent reconstruction. Its body code includes explicit behavior states despite stronger wording elsewhere in the README.

**Potential reuse.** Linux overlay integration, efficient small-circuit runtime and multi-fly interaction.

#### 25. [Desktop Fly Linux](https://github.com/somsom10/desktop-fly-linux)

Repository: somsom10/desktop-fly-linux

**Purpose.** Provide a Python/GTK desktop fly for GNOME, X11 and Wayland, with sugar placement.

**Biological substrate.** FlyWire; 668-cell Desktop Fly circuit.

**Method.** Ports the original neural circuit and anatomical display; adds odor/feeding interactions through modeled encoders and procedural body control.

**Evidence and limits.** Small-circuit port. Desktop sensing is limited under some Wayland/XWayland configurations; a large brain visualization does not mean a full-brain simulation.

**Potential reuse.** Accessible Python desktop implementation and interactive food stimuli.

#### 26. [snedea/flybrain](https://github.com/snedea/flybrain)

Repository: snedea/flybrain

**Purpose.** A browser fly playground with food, touch, wind, light and temperature controls.

**Biological substrate.** FlyWire; large filtered graph.

**Method.** LIF simulation in a Web Worker, connected to a rendered world and neuron-activity viewer; derived from an earlier worm-simulation project.

**Evidence and limits.** Interactive prototype. The README does not provide an independent behavioral benchmark supporting its emergence claims.

**Potential reuse.** Whole-brain-scale browser UI and multimodal stimulus controls.

#### 27. [FlyWire Neuro](https://github.com/pusulamkendim/flywire-neuro)

Repository: pusulamkendim/flywire-neuro

**Purpose.** A local embodied fly laboratory with interactive sensory stimulation and recording.

**Biological substrate.** FlyWire; whole-brain LIF.

**Method.** Neural readouts select or modulate Flybody-derived motion clips/cached poses, with a browser world and compressed neural logs.

**Evidence and limits.** Only partly closed-loop; automatic contact and continuous sensory feedback remain under development. Display frame rate should not be confused with neural simulated-time speed.

**Potential reuse.** Stimulus panels, run recording and a practical bridge from neural activity to body motion.

#### 28. [Closed Loop Fly](https://github.com/ZeroXClem/closed-loop-fly)

Repository: ZeroXClem/closed-loop-fly

**Purpose.** Connect compound-eye vision, a large neural simulation and an airborne fly body.

**Biological substrate.** MaleCNS; WebGPU LIF plus a separate visual model.

**Method.** An upstream optic-lobe model feeds the MaleCNS graph; selected neural rates steer an engineered flight model. Walking-related DNa02 activity is used as a flight-steering proxy.

**Evidence and limits.** Follow-up analysis retracts an apparent visual/haltere benefit because it came from a decoder artifact. Correcting the artifact leaves substantial drift, so stable biologically grounded flight is not established.

**Potential reuse.** Closed-loop browser plumbing and a valuable example of diagnosing misleading ablation results.

#### 29. [Flyverse](https://github.com/tel-0s/flyverse-core)

Repository: tel-0s/flyverse-core

**Purpose.** A reusable neural controller and instrumented room for testing sensorimotor behavior.

**Biological substrate.** MaleCNS, FlyWire FAFB and BANC through one API.

**Method.** LIF model, modeled senses and named motor readouts; separates its default physiological assumptions from opt-in instruments, synthetic additions and training hooks.

**Evidence and limits.** Reports several reflex and direction-selectivity checks, but also persistent failures in goal-directed turning, small-object responses, compass dynamics and directed food search. The default configuration already contains physiological approximations.

**Potential reuse.** Control API, cross-connectome experiments, explicit assumptions and detailed deficit/assay ledgers.

#### 30. [NeuroTerrarium](https://github.com/5p00kyy/neuroterrarium)

Repository: 5p00kyy/neuroterrarium

**Purpose.** Build an inspectable terrarium and reproducible circuit-comparison instrument.

**Biological substrate.** 48-cell synthetic fixture; separate 51-body MaleCNS microcircuit.

**Method.** The synthetic network drives the body. A separate measured giant-fiber input circuit supports pulse tests, matched rewiring, lesions and replay, but never controls the body.

**Evidence and limits.** The biological circuit and rewired controls tie on the default pulse test. Synthetic readout benchmarks also show no topology advantage; removing recurrence can improve the tested task.

**Potential reuse.** Provenance-conscious experimental UI, controlled comparisons and clear separation of synthetic and biological data.

#### 31. [FLYBOARD](https://github.com/NullLabTests/flybrain)

Repository: NullLabTests/flybrain

**Purpose.** An arcade panel for stimulating taste, nociception, courtship-related and dopamine populations.

**Biological substrate.** MaleCNS; whole retained graph.

**Method.** Buttons inject current into named cells; CPU leaky-integrator dynamics produce activity displayed on the brain.

**Evidence and limits.** A neural stimulus visualizer with deliberately simplified dynamics. Button labels do not establish pleasure, pain experience or biological death, and there is no demonstrated learning task.

**Potential reuse.** Simple population-targeted stimulation and a clear live activity display.

#### 32. [Infinite Sugar](https://github.com/cnqso/infinite-sugar)

Repository: cnqso/infinite-sugar

**Purpose.** An interactive art terrarium with continuous stimulation of sweet-sensing neurons.

**Biological substrate.** FlyWire; whole-brain simulation.

**Method.** Neural activity modulates feeding, head and antennal motion; wing and foot motion also use supplied patterns.

**Evidence and limits.** Art/embodiment demonstration, not evidence of pleasure or autonomous learning. The README explicitly distinguishes activity-driven motion from patterned animation.

**Potential reuse.** A focused stimulus-to-body experience and anatomy/activity visualization.

### Language, art and other experiments

#### 33. [Fly Language Model (FLM)](https://github.com/nftechie/flm)

Repository: nftechie/flm

**Purpose.** Use connectome activity as an adapter to a pretrained language model.

**Biological substrate.** MaleCNS; fixed whole-graph numerical reservoir.

**Method.** Token embeddings drive a fixed graph; a trained 278,528-parameter readout changes the next-token scores of a frozen LFM2.5 language model. These graph states are not simulated action potentials.

**Evidence and limits.** Language competence comes from the pretrained model. The separately documented study found the matched direct-input adapter slightly better; no advantage from fly topology is established. A trained conversational adapter is not bundled.

**Potential reuse.** An explicit test of connectome features inside an otherwise conventional ML system.

#### 34. [Chat with a Fruit Fly Brain](https://github.com/lixiang1076/fly-brain)

Repository: lixiang1076/fly-brain

**Purpose.** Expose neural stimulation through conversational commands such as taste, walk and escape.

**Biological substrate.** FlyWire v783; whole-brain LIF.

**Method.** A language/command interface maps requests to neuron populations, runs the model and translates output rates into behavioral descriptions. Additional scripts implement modeled mushroom-body plasticity.

**Evidence and limits.** The conversation is an interface around a simulator. Text responses and programmed stimulus mappings do not demonstrate language understanding by the neural circuit; biological learning claims require separate validation.

**Potential reuse.** Human-readable stimulation commands, neuron atlas and accessible model interaction.

#### 35. [Fly / Wirehead](https://github.com/mattyhempstead/fly-wirehead)

Repository: mattyhempstead/fly-wirehead

**Purpose.** Show a simulated fly watching an endless feed of short videos.

**Biological substrate.** MaleCNS; whole retained graph.

**Method.** Video pixels stimulate the network; motor readouts animate a body. Video playback also injects artificial current into PAM11 dopamine cells, with an experimental plasticity rule.

**Evidence and limits.** The feed advances on a timer: the fly does not choose videos. Displayed dopamine-cell firing is not dopamine concentration, and preference or addiction has not been established.

**Potential reuse.** Video-to-neural streaming, state persistence and an audiovisual installation.

#### 36. [FlyScroll / Fruitfly Doomscroller](https://github.com/ranagwho/Fruitfly-Doomscroller)

Repository: ranagwho/Fruitfly-Doomscroller

**Purpose.** Make neural state decide when to scroll to another short video.

**Biological substrate.** MaleCNS; approximately 70k visual crop or full retained graph.

**Method.** Frames drive modeled photoreceptors. An engineered novelty/interest signal and depression of KC-to-novelty-MBON synapses cause scrolling after habituation or a timeout.

**Evidence and limits.** Unlike a timed feed, the proposed action depends on content-sensitive state. The novelty mapping and plasticity are project assumptions, with no demonstrated biological preference or addiction.

**Potential reuse.** Content-dependent media control and a comparison point for the timer-driven Wirehead installation.

#### 37. [Stonkfly](https://github.com/nftechie/stonkfly)

Repository: nftechie/stonkfly

**Purpose.** Use a fly circuit to propose cryptocurrency buy/sell/hold actions.

**Biological substrate.** MaleCNS; whole retained graph.

**Method.** Price charts stimulate modeled eyes; fixed neural readouts propose orders through Coinbase integration. Portfolio outcomes become artificial reinforcement for selected mushroom-body synapses.

**Evidence and limits.** Paper trading is the default; live integration requires credentials and opt-in. Profitable learning has not been demonstrated. Trading integration is an engineering result, not evidence of financial predictive ability.

**Potential reuse.** An external-action adapter with logged observations, neural state and candidate plasticity.

#### 38. [OpenFly](https://github.com/marketcalls/openfly)

Repository: marketcalls/openfly

**Purpose.** Test connectome features for timing an intraday NIFTY options strategy.

**Biological substrate.** MaleCNS; whole retained graph.

**Method.** Charts enter the neural model; a fitted readout estimates future movement relative to option pricing. An alternative arm updates selected KC-to-MBON connections through engineered dopamine rewards.

**Evidence and limits.** Reports paper-mode integration, not a profitable edge. Its evaluation protocol requires comparison with fixed-entry, random-entry, shuffled-label and no-trade controls on an untuned period.

**Potential reuse.** A task-specific prediction/readout experiment with explicit financial baselines.

#### 39. [Fly Lab](https://github.com/Apolotary/fly-lab)

Repository: Apolotary/fly-lab

**Purpose.** Use one or twelve simulated flies to influence Ableton music.

**Biological substrate.** Small measured fly motor circuit.

**Method.** The Dark mode learns 70 weights selecting among ten authored musical gestures from neural activity. Other modes map collisions or collective movement to notes and sound parameters.

**Evidence and limits.** Reports improvement on its authored preference heuristic, not independent musical-quality evaluation. Harmony, rhythm and gestures are supplied; the fly does not listen to audio or learn composition.

**Potential reuse.** Small-circuit sonification, human feedback and a local MIDI/Ableton bridge.

#### 40. [Faiku / Haiku](https://github.com/xyzzyapps/faiku)

Repository: xyzzyapps/faiku

**Purpose.** Train fly-inspired control of letter/kana ink trails and generate short poems.

**Biological substrate.** MaleCNS whole graph; optional eight-channel synthetic mushroom-body fallback.

**Method.** Glyph cues are encoded as odor-like channels; ink rewards update selected KC-to-MBON synapses and a motor map. Word generation uses a supplied vocabulary/readout.

**Evidence and limits.** Reports weight changes, but that does not establish handwriting competence or open-ended language generation. The fallback is an invented eight-channel controller, not a measured connectome.

**Potential reuse.** A creative output interface and a small plasticity experiment with clearly different full-graph and synthetic modes.

#### 41. [Fruitless](https://github.com/nicodunks/fruitless)

Repository: nicodunks/fruitless

**Purpose.** Test whether blocking mAL output changes courtship-related responses to male-associated input.

**Biological substrate.** MaleCNS; whole-brain simulation, recorded activity in browser.

**Method.** Paired intact/blocked simulations keep input and other parameters fixed, measuring a small set of P1-related candidate neurons across seeds and inhibitory settings.

**Evidence and limits.** Reports increased responses to male cues, while female-cue responses remain stronger. It does not demonstrate male preference or a gene edit. The displayed flight/mounting is illustrative choreography over recorded spikes.

**Potential reuse.** A bounded mechanistic perturbation study with explicit readout and visual limits.

#### 42. [Fly Odor ON/OFF](https://github.com/yukincom/fly-odor-onoff)

Repository: yukincom/fly-odor-onoff

**Purpose.** Investigate why olfactory neurons keep firing after an odor disappears.

**Biological substrate.** MaleCNS-derived model from Fly Brain Minecraft.

**Method.** Blocks selected recurrent inputs only during stimulus-off intervals and compares onset, offset and re-stimulation, including four DM1/VA2 projection neurons.

**Evidence and limits.** Across eight paired configurations, the targeted intervention silences those four cells after offset while preserving stimulus responses. This is a model-specific result, not a repair of all olfaction or a biological experiment.

**Potential reuse.** Focused debugging experiment with fixed cohorts, protocols, result files and reproducibility hashes.

#### 43. [Fruit Fly Fashion](https://github.com/jtc268/fruit-fly-fashion)

Repository: jtc268/fruit-fly-fashion

**Purpose.** Use neural responses to transform print designs for a six-shirt collection.

**Biological substrate.** MaleCNS; DOOMFLY simulation for offline design runs.

**Method.** Seed images drive the graph; spike vectors control geometric changes such as rotation, placement and scale while the original palette stays fixed. A browser painting tool uses derived material.

**Evidence and limits.** A connectome-mediated art workflow with manifests and recordings. The browser tool does not rerun the full graph, and source compositions and design mappings are authored.

**Potential reuse.** Traceable neural input/output for generative design and a finished product presentation.

#### 44. [Mindmeld with Fly](https://github.com/Decentricity/mindmeld-with-fly)

Repository: Decentricity/mindmeld-with-fly

**Purpose.** Feed live human EEG band powers into a fly-shaped network and visualize its response.

**Biological substrate.** MaleCNS; sparse numerical reservoir.

**Method.** Muse EEG delta-through-gamma features pass through a fixed seeded input projection into the reservoir; the UI compares human input bands with spectra of the computed activity.

**Evidence and limits.** Human-to-model signal coupling, not mind transfer or insect EEG. Reservoir dynamics and its frequency bands are numerical constructs.

**Potential reuse.** Live physiological-signal input, terminal visualization and paired signal logging.

#### 45. [Boltzmann Fly](https://github.com/jniimi/boltzmann-fly)

Repository: jniimi/boltzmann-fly

**Purpose.** Test a connectome-shaped energy-based world model on simulated consumer behavior and interventions.

**Biological substrate.** MaleCNS; mushroom-body connectivity mask.

**Method.** Symmetrizes the measured connection pattern into a Boltzmann-machine mask and learns connection magnitudes. Evaluates prediction, consistency and counterfactual parameter recovery.

**Evidence and limits.** One-seed study: prediction roughly matches the dense model, but one counterfactual parameter is worse and the consistency test fails its expected direction. Some rewired controls do better. This is not an emulated fly brain.

**Potential reuse.** A clear example of topology as an ML architectural constraint, with meaningful negative controls.

### Datasets and annotations

#### 63. [Male CNS release website](https://github.com/janelia-flyem/male-cns)

Repository: janelia-flyem/male-cns

**Purpose.** Build the release website and neuron-type comparison pages.

**Biological substrate.** Official MaleCNS release resources.

**Method.** MkDocs/Jinja pipeline combines metadata, images, network summaries and links to anatomical viewers.

**Evidence and limits.** Official resource/site source, not a simulation engine. Rebuilding all generated data can require backend credentials even though the public website is readable.

**Potential reuse.** Release documentation, dataset navigation and examples of presenting anatomical comparisons.

#### 64. [Male CNS Cell Type Explorer](https://github.com/reiserlab/celltype-explorer-drosophila-male-cns)

Repository: reiserlab/celltype-explorer-drosophila-male-cns

**Purpose.** A searchable catalog of neuron types, anatomy and connectivity.

**Biological substrate.** MaleCNS v1.0; 11,751 annotated cell types.

**Method.** Filters by type, side, region, neurotransmitter and dimorphism; type pages expose connectivity, region innervation and Neuroglancer views.

**Evidence and limits.** Data exploration site. It helps choose relevant cells but makes no executable behavioral-model claim.

**Potential reuse.** Find and inspect candidate sensory, interneuron and motor populations before modeling.

#### 65. [2025malecns supplemental data](https://github.com/flyconnectome/2025malecns)

Repository: flyconnectome/2025malecns

**Purpose.** Distribute derived data and analyses accompanying the MaleCNS research.

**Biological substrate.** MaleCNS and aligned FlyWire comparisons.

**Method.** Includes neuron/connection counting, sensory-to-motor flow, graph traversal layers, optic-column assignments and male/female mappings.

**Evidence and limits.** Official study supplements rather than a brain emulator. The repository name reflects earlier research chronology, not a different game model.

**Potential reuse.** Prepared biological annotations and pathways for choosing and interpreting circuits.

#### 66. [Male visual-system connectome analysis](https://github.com/reiserlab/male-drosophila-visual-system-connectome-code)

Repository: reiserlab/male-drosophila-visual-system-connectome-code

**Purpose.** Reproduce analyses and figures for the male fly visual-system connectome.

**Biological substrate.** Male optic-lobe dataset.

**Method.** Python notebooks/scripts, workflow configuration, cached results and neuPrint queries characterize visual neurons and their connections.

**Evidence and limits.** Scientific analysis code for a visual subsystem; not a trained general-purpose vision controller.

**Potential reuse.** Examples of extracting visual anatomy, connectivity and reproducible figures.

#### 67. [BANC Project](https://github.com/htem/BANC-project)

Repository: htem/BANC-project

**Purpose.** Provide the research code and data products for the unified female CNS study.

**Biological substrate.** Female brain-and-nerve-cord connectome.

**Method.** R/Python analyses cover distributed control, brain/cord pathways, annotations and paper figures.

**Evidence and limits.** A distinct specimen and dataset from both MaleCNS and the earlier brain-only FlyWire reconstruction. Published anatomical research, not a turnkey behavioral simulation.

**Potential reuse.** Female whole-CNS comparisons and analyses of control spanning brain and nerve cord.

#### 68. [FlyWire Annotations](https://github.com/flyconnectome/flywire_annotations)

Repository: flyconnectome/flywire_annotations

**Purpose.** Maintain systematic cell annotations and cross-connectome cell typing.

**Biological substrate.** FlyWire FAFB v783.

**Method.** Versioned tables, skeleton-related data, connectivity resources and code connect neuron IDs to cell types and metadata.

**Evidence and limits.** Annotations evolve after publication; releases should be pinned. The repository warns that its systematic annotations can differ from other annotation mixtures shown in Codex.

**Potential reuse.** Reliable neuron identities and labels for selecting inputs, outputs and comparison populations.

#### 69. [Drosophila Neurotransmitters](https://github.com/flyconnectome/drosophila_neurotransmitters)

Repository: flyconnectome/drosophila_neurotransmitters

**Purpose.** Collect experimentally supported neurotransmitter identities with citations.

**Biological substrate.** Literature-curated transmitter evidence across fly cell types.

**Method.** Version-controlled tables and validation code link cell types to transmitter evidence and reference sources.

**Evidence and limits.** Identity evidence does not fully determine the sign or strength of every modeled connection; postsynaptic receptors still matter.

**Potential reuse.** Ground-truth checks for assumptions that many simulations otherwise infer from predicted labels.

#### 70. [Optic Lobe Annotations](https://github.com/flyconnectome/ol_annotations)

Repository: flyconnectome/ol_annotations

**Purpose.** Align visual-system cell types between male and female reconstructions.

**Biological substrate.** Female FlyWire and male optic-lobe datasets.

**Method.** Matching tables and shared anatomical viewer scenes support direct comparison across different type names and datasets.

**Evidence and limits.** Most matches are one-to-one, but some are more complex; mappings are versioned and can be refined.

**Potential reuse.** Translate visual-cell identities when moving a circuit between connectomes.

### Analysis and visualization tools

#### 71. [Codex Connectome Data Explorer](https://github.com/murthylab/codex)

Repository: murthylab/codex

**Purpose.** A web application for searching and exploring neurons and connections.

**Biological substrate.** FlyWire connectome and annotations.

**Method.** Flask application with imported connectome data, search/exploration interfaces and analysis views.

**Evidence and limits.** A neuroscience data browser; it is unrelated to the OpenAI coding product with the same name and does not simulate brain dynamics.

**Potential reuse.** Interactive neuron lookup, connectivity inspection and a model for building circuit-exploration interfaces.

#### 72. [FlyBrainLab](https://github.com/FlyBrainLab/FlyBrainLab)

Repository: FlyBrainLab/FlyBrainLab

**Purpose.** An interactive environment connecting anatomical exploration to circuit execution.

**Biological substrate.** Multiple fly anatomical datasets and executable circuit models.

**Method.** Combines notebook interfaces, 3D visualization, circuit construction and simulation services.

**Evidence and limits.** A research platform whose individual circuits require modeling and validation; it does not supply a universally complete fly mind.

**Potential reuse.** A mature structure-to-function workflow and an ecosystem of circuit tools.

#### 73. [EOScircuits](https://github.com/FlyBrainLab/EOScircuits)

Repository: FlyBrainLab/EOScircuits

**Purpose.** Provide executable antenna, antennal-lobe and mushroom-body models.

**Biological substrate.** Fly-inspired early olfactory circuit models.

**Method.** Configurable modules connect odor transduction and published olfactory-circuit formulations within FlyBrainLab.

**Evidence and limits.** Specialized mechanistic models, not a whole MaleCNS reconstruction. Their assumptions differ from simply applying uniform LIF neurons to an anatomical graph.

**Potential reuse.** Olfactory input and circuit dynamics for projects whose smell pathways fail under simpler models.

#### 74. [NAVis](https://github.com/navis-org/navis)

Repository: navis-org/navis

**Purpose.** A general Python library for analyzing and visualizing neurons.

**Biological substrate.** Dataset-agnostic neuron morphology and connectivity.

**Method.** Handles skeletons, meshes and other representations; supports morphology comparisons such as NBLAST, geometry transformations and connectivity-related analysis.

**Evidence and limits.** Foundational analysis library rather than a neural simulator or application experiment.

**Potential reuse.** Import, inspect, transform, compare and visualize biological neurons.

#### 75. [fafbseg-py](https://github.com/navis-org/fafbseg-py)

Repository: navis-org/fafbseg-py

**Purpose.** Provide Python access to segmented neurons, connectivity and annotations.

**Biological substrate.** FlyWire and other FAFB segmentations.

**Method.** Maps positions/segments to IDs, retrieves or generates meshes and skeletons, queries connections and handles viewer links; integrates with NAVis.

**Evidence and limits.** Dataset access and preparation, not behavioral modeling. Authentication and version choices depend on the requested service/data.

**Potential reuse.** A practical Python bridge from public fly data to an analysis pipeline.

#### 76. [navis-flybrains](https://github.com/navis-org/navis-flybrains)

Repository: navis-org/navis-flybrains

**Purpose.** Align anatomical data from different specimens and imaging templates.

**Biological substrate.** Fly template brains and connectome coordinate spaces.

**Method.** Provides template metadata, meshes and registered transformations, with additional transform downloads.

**Evidence and limits.** Spatial registration does not itself establish cell identity or biological equivalence across individuals.

**Potential reuse.** Place neurons, meshes and circuit visualizations into a common coordinate system.

#### 77. [Connectome Interpreter](https://github.com/YijieYin/connectome_interpreter)

Repository: YijieYin/connectome_interpreter

**Purpose.** Turn connectivity into testable hypotheses about circuit function.

**Biological substrate.** Adult and larval connectomes.

**Method.** Effective multi-hop connectivity, path finding, differentiable models, activation maximization, saliency and fitting to experimental responses.

**Evidence and limits.** An analysis/modeling toolkit with tutorials; predicted pathways and responses remain dependent on model assumptions and data quality.

**Potential reuse.** Identify candidate routes, explain signals and design stimulation/lesion experiments.

#### 78. [Connectome Data Prep](https://github.com/YijieYin/connectome_data_prep)

Repository: YijieYin/connectome_data_prep

**Purpose.** Publish processed connectivity and the code used to prepare it.

**Biological substrate.** MaleCNS, BANC, FlyWire, hemibrain, nerve-cord and larval datasets.

**Method.** Sparse matrices, metadata tables, normalization variants and experimental-response datasets support Connectome Interpreter and other projects.

**Evidence and limits.** Convenient prepared data, but normalization, axon/dendrite filtering and release version must be understood before comparing results.

**Potential reuse.** Avoid repeating expensive raw-data preparation while retaining a traceable processing recipe.

#### 79. [CoCoA](https://github.com/flyconnectome/cocoa)

Repository: flyconnectome/cocoa

**Purpose.** Compare cell types and connectivity across connectomes in Python.

**Biological substrate.** FlyWire, hemibrain, MANC and MaleCNS.

**Method.** Dataset abstractions, matching and joint clustering organize connectivity-based comparisons.

**Evidence and limits.** Comparative anatomy toolkit. Dataset adapters have different availability and authentication requirements.

**Potential reuse.** Match candidate circuits and cell types across reconstructions.

#### 80. [Connecto](https://github.com/schlegelp/connecto)

Repository: schlegelp/connecto

**Purpose.** Unify queries across datasets with incompatible IDs, schemas and conventions.

**Biological substrate.** Multiple connectomes through neuPrint and CAVE backends.

**Method.** Normalizes edge-table shapes, coordinate units and side labels, while exposing backend capabilities and refusing unsupported queries.

**Evidence and limits.** A data-access abstraction, not a simulator; it cannot make unsupported backend features exist.

**Potential reuse.** Reduce integration work when an experiment must run on more than one connectome.

#### 81. [DROCAT](https://github.com/Swida-Alba/Drosophila-cross-dataset-connectome-analysis)

Repository: Swida-Alba/Drosophila-cross-dataset-connectome-analysis

**Purpose.** An end-user toolkit for paths, connectivity, morphology and cross-dataset comparison.

**Biological substrate.** neuPrint datasets, FAFB and BANC.

**Method.** Web UI and scripts combine type-based path finding, neurotransmitter-aware views, 3D morphology and EM-to-light-microscopy driver-line mapping.

**Evidence and limits.** Analysis application. Its installation/agent helper files are optional project tooling, not part of a neural-learning result.

**Potential reuse.** A broad graphical environment for exploring potential circuits without assembling many libraries manually.

#### 82. [BigClust 2](https://github.com/flyconnectome/bigclust2)

Repository: flyconnectome/bigclust2

**Purpose.** Interactively explore large neuron clusterings and refine annotations.

**Biological substrate.** Morphology/connectivity embeddings; example spans several connectomes.

**Method.** Links 2D embeddings, 3D neurons, clustering/feature tools and annotation export or backend updates.

**Evidence and limits.** Actively developed analysis GUI. Cluster similarity is a hypothesis about cell organization, not automatic proof of functional identity.

**Potential reuse.** Find related neurons, compare candidate cell types and inspect large feature spaces.

#### 83. [neuVid](https://github.com/connectome-neuprint/neuVid)

Repository: connectome-neuprint/neuVid

**Purpose.** Produce research-quality animated anatomical videos.

**Biological substrate.** Anatomy from neuPrint, Neuroglancer and skeleton files.

**Method.** JSON descriptions specify neurons, regions, synapses, camera moves and visibility; scripts generate Blender scenes and renders. A natural-language helper is optional.

**Evidence and limits.** Anatomical animation, not neural dynamics or behavior generation.

**Potential reuse.** Clear circuit explanations, fly-brain walkthroughs and presentation assets.

#### 84. [malecns (R)](https://github.com/natverse/malecns)

Repository: natverse/malecns

**Purpose.** Expose the male CNS dataset through the natverse ecosystem.

**Biological substrate.** MaleCNS.

**Method.** Convenience functions retrieve metadata, connectivity and meshes and support coordinate conversion; currently builds on related male-VNC tooling.

**Evidence and limits.** Experimental R data-access wrapper. Some operations require neuPrint or production-service credentials.

**Potential reuse.** Native R access to MaleCNS with anatomical analysis conveniences.

#### 85. [coconatfly](https://github.com/natverse/coconatfly)

Repository: natverse/coconatfly

**Purpose.** Offer a uniform R interface for comparative and integrative connectomics.

**Biological substrate.** Multiple adult fly connectomes.

**Method.** Wraps dataset-specific access and supports connectivity comparison and clustering across datasets.

**Evidence and limits.** In active use but explicitly experimental; interfaces can change.

**Potential reuse.** A higher-level R starting point for multi-connectome projects.

#### 86. [fafbseg (R)](https://github.com/natverse/fafbseg)

Repository: natverse/fafbseg

**Purpose.** Access and analyze segmented electron-microscopy data from R.

**Biological substrate.** FAFB/FlyWire segmentations and associated services.

**Method.** Provides lower-level FlyWire support, data-release access and integration with the natverse; underlies parts of coconatfly.

**Evidence and limits.** Data infrastructure. Live production access may need authentication and differs from working with fixed public releases.

**Potential reuse.** R workflows needing segmentation-level or lower-level FlyWire functionality.

#### 87. [neuprintr](https://github.com/natverse/neuprintr)

Repository: natverse/neuprintr

**Purpose.** Provide an R client for the neuPrint graph database service.

**Biological substrate.** Connectomes served by neuPrint.

**Method.** Queries neuron metadata, connectivity, synapse locations and skeletons, integrated with natverse analysis.

**Evidence and limits.** General service client, not a specific MaleCNS experiment.

**Potential reuse.** Programmatic R extraction of neurons and synaptic graphs.

#### 88. [bancr](https://github.com/natverse/bancr)

Repository: natverse/bancr

**Purpose.** Provide R access to BANC metadata, annotations and connectivity.

**Biological substrate.** Female BANC brain-and-nerve-cord connectome.

**Method.** Uses compiled public data for common queries and supports authenticated live-service access where needed.

**Evidence and limits.** Dataset interface; distinguish release-specific public tables from evolving live annotations.

**Potential reuse.** Analyze female brain-to-cord pathways and compare them with MaleCNS.

#### 89. [neuprint-python](https://github.com/connectome-neuprint/neuprint-python)

Repository: connectome-neuprint/neuprint-python

**Purpose.** Provide a Python client for connectome database queries.

**Biological substrate.** Connectomes served by neuPrint.

**Method.** Wraps neuPrint service access for extracting neuron, connection and related anatomical data into Python workflows.

**Evidence and limits.** Core data-access dependency used by many other entries, not an independent behavioral experiment.

**Potential reuse.** Direct Python access to the graph and metadata needed for circuit extraction.

#### 90. [CAVEclient](https://github.com/CAVEconnectome/CAVEclient)

Repository: CAVEconnectome/CAVEclient

**Purpose.** Provide Python access to annotation, segmentation and materialization services.

**Biological substrate.** Versioned connectomics datasets hosted through CAVE.

**Method.** Client interfaces handle changing segmentation identities, metadata, annotations and versioned data queries.

**Evidence and limits.** General connectomics infrastructure. Public materialization versions and live segmentation are different analysis targets.

**Potential reuse.** Version-aware data access and reproducible queries for FlyWire/BANC-style datasets.

#### 91. [FlyWire Network Analysis](https://github.com/murthylab/flywire-network-analysis)

Repository: murthylab/flywire-network-analysis

**Purpose.** Reproduce whole-brain graph-statistics research.

**Biological substrate.** FlyWire; paper analyses use v630.

**Method.** Python and MATLAB analyses examine degree distributions, motifs, reciprocity, paths, connectivity organization and related data products.

**Evidence and limits.** Structural network analysis, not a spiking simulation; some analyses have substantial memory/compute requirements.

**Potential reuse.** Baselines and graph descriptors for testing whether a proposed circuit or topology result is unusual.

### Tutorials

#### 92. [Fly Connectome Data Tutorial](https://github.com/sjcabs/fly_connectome_data_tutorial)

Repository: sjcabs/fly_connectome_data_tutorial

**Purpose.** Teach loading, querying, analyzing and visualizing fly connectomes.

**Biological substrate.** Major adult fly brain and nerve-cord datasets.

**Method.** Workshop notebooks/code in Python and R, curated inputs and guides to morphology, connectivity and viewer tools.

**Evidence and limits.** Educational resource. Dataset descriptions and tutorial-specific releases should be checked against current primary releases.

**Potential reuse.** A coherent onboarding path for a team new to connectomics.

#### 93. [FlyConnectome data-access tutorials](https://github.com/seung-lab/FlyConnectome)

Repository: seung-lab/FlyConnectome

**Purpose.** Teach access to electron microscopy, segmentations, meshes, annotations and connections.

**Biological substrate.** FlyWire.

**Method.** Notebooks demonstrate CAVE, cloud-volume access, point lookups and rendering; linked workshop material explains the workflow.

**Evidence and limits.** Data-access instruction, not simulation or learning. Large imagery is normally queried in subvolumes rather than downloaded in full.

**Potential reuse.** The route from neuron IDs to original anatomy and evidence.

#### 94. [2020 Hemibrain Examples](https://github.com/flyconnectome/2020hemibrain_examples)

Repository: flyconnectome/2020hemibrain_examples

**Purpose.** Demonstrate connectome analysis in R and Python.

**Biological substrate.** Hemibrain and selected FAFB reconstructions.

**Method.** Examples cover neuPrint queries, olfactory circuitry, morphology, axon/dendrite splits and network traversal.

**Evidence and limits.** Older educational examples; API and dataset versions may require adaptation.

**Potential reuse.** Small concrete recipes for understanding and extracting biological circuits.

### Related resource lists

#### 95. [Awesome Fruit Fly Connectome](https://github.com/watthem/awesome-fruit-fly-connectome)

Repository: watthem/awesome-fruit-fly-connectome

**Purpose.** A second curated map of datasets, papers, tools and community experiments.

**Biological substrate.** Resource index spanning several fly datasets.

**Method.** Organizes references by milestone, data access, simulation and application area.

**Evidence and limits.** An index rather than an executable project. Its outgoing links were not recursively expanded into this review.

**Potential reuse.** Broader bibliography and cross-checking for future research.

#### 96. [flyconnectome/tools](https://github.com/flyconnectome/tools)

Repository: flyconnectome/tools

**Purpose.** Explain which analysis library serves which purpose.

**Biological substrate.** R/Python neuroanatomy ecosystem.

**Method.** Overview of natverse, NAVis and companion packages, emphasizing morphological matching and coordinate transformations.

**Evidence and limits.** A tool directory rather than a new experiment; linked packages have their own documentation and scope.

**Potential reuse.** Choosing the appropriate library for anatomy, data access or cross-dataset alignment.


## Provenance and reproducibility notes

The repository audit records the original collection URL, retrieved content hashes, observed commits, inspected source files, and one-to-one coverage. The original technical audit pins, among other sources, the Shiu implementation at 91bdd1e7dcf193f3e7ca5a8933497fcef63b7960 and the MaleCNS supplementary repository at 67767d2233657983993ff6c2be48e836a935863c. Performance figures in the original collection remain authors' reports. The additional fly-brain-feeding audit pins commit 86c7d84fccb1269842c8520846fc006a79fb3487 and records the 15 locally rerun tests and the model outputs explicitly labeled above. No Hedgehog replication or population-throughput benchmark has been performed.

The Hedgehog follow-up pins the source workbook at SHA-256 41deeecbecbcc97d0c1336c4b1aaf009b3723b93c396086c0cc0ba1fb4866667 and supplies a reproducible extraction script and selected numerical tables. These are published observations and descriptive calculations, not outputs from a new biological model.

The report builder preserves the 96-entry source CSV. Written-report updates preserve the HTML companion and its previously embedded Markdown snapshot; a presentation rebuild requires an explicit request. The current written reports include the neuromodulation follow-up, Hedgehog data mapping, original critique, and broader search with dedicated critics. These critiques are literature/code assessments, not independent experimental replications. The alternative-experiment audit records separately inspected code and source-data hashes without enlarging the original catalog. External citations require internet access; the preserved HTML and its earlier embedded report remain usable offline.
