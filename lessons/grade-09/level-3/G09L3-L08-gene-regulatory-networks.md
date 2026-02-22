# Lesson: Gene Regulatory Networks

## Header Information

| Field | Value |
|-------|-------|
| **Lesson ID** | G09L3-L08 |
| **Grade** | 9th Grade — Level 3: Biotech |
| **Lesson Name** | Gene Regulatory Networks |
| **Status** | Template |

---

## Platform

### Title
**Gene Regulatory Networks — From Transcription Factor to Phenotype — Modeling the Logic of Gene Expression**

### Overview
This lesson introduces students to gene regulatory networks — the molecular logic circuits that control which genes are expressed in every cell. Biotech skill focus: Network dynamics and feedback circuit analysis. Understanding gene regulation is fundamental to both basic biology (how does a fertilized egg become a complete organism?) and biotechnology (how do we engineer cells to produce desired proteins or behaviors?). Students investigate the driving question: Your body has 20,000 genes but every cell only uses a fraction of them. Who decides which genes turn on, which stay off, and when — and what happens when that decision-making system breaks? Using the LEVER framework, students identify key components, establish cause-and-effect relationships, run simulations to test scenarios, and extend their understanding through research and engineering challenges.

### Cover Image
[A photorealistic, cinematic image of diverse 14-15 year old students in an advanced molecular biology lab examining gene regulatory network diagrams on holographic displays, with fluorescent-labeled gene expression experiments visible under UV illumination, dramatic blue and violet laboratory lighting]

### Grade
9th Grade — Level 3: Biotech

### NGSS Standard
**HS-LS3-1, HS-LS1-4**: Ask questions to clarify relationships about the role of DNA and chromosomes in coding the instructions for characteristic traits passed from parents to offspring; use a model to illustrate the role of cellular division in producing and maintaining complex organisms.

### Learning Objectives
- Build a gene regulatory network model that traces signal flow from transcription factor binding through mRNA production and protein synthesis to emergent cellular behavior
- Analyze how promoter binding affinity, transcription and translation rates, and degradation kinetics interact to determine steady-state protein levels
- Optimize regulatory network parameters to achieve desired gene expression patterns — including switches, oscillators, and dose-response curves
- Evaluate how disruptions in regulatory network components lead to disease states including cancer, developmental disorders, and autoimmune conditions

### Component List (Starting Model: 10 Components)

| Component | Type | What It Represents |
|-----------|------|-------------------|
| Transcription Factor Concentration | External | The intracellular abundance of the regulatory protein that initiates the gene expression cascade — determined by the transcription factor's own production rate, degradation rate, and any upstream signals that regulate its activity |
| Promoter Binding Affinity | Internal | The strength of the molecular interaction between the transcription factor and its target promoter DNA sequence — determined by the complementarity of protein-DNA surfaces, measured in nanomolar dissociation constant (Kd) |
| mRNA Transcription Rate | Internal | The speed at which RNA polymerase synthesizes messenger RNA from the target gene template — dependent on Transcription Factor Concentration, Promoter Binding Affinity, and the availability of RNA polymerase and nucleotide precursors |
| mRNA Degradation Rate | Internal | The speed at which cellular ribonucleases break down messenger RNA molecules — mRNA half-lives range from 2 minutes (bacteria) to hours (mammalian cells), and degradation rate is a critical determinant of steady-state mRNA levels |
| Ribosome Availability | Internal | The fraction of the cell's ribosome pool that is free to translate the target mRNA — in rapidly growing cells, up to 80% of ribosomes may already be occupied translating other essential proteins, limiting translational capacity |
| Protein Translation Rate | Internal | The speed at which ribosomes synthesize the target protein from the mRNA template — dependent on mRNA stability, Ribosome Availability, codon usage efficiency, amino acid supply, and translation initiation signal strength |
| Protein Degradation Rate | Internal | The speed at which the target protein is broken down by cellular proteases (proteasome, autophagy) — protein half-lives range from minutes (cell cycle regulators) to days (structural proteins), and degradation is a key control point for rapid responses |
| Feedback Signal Strength | Internal | The intensity of the regulatory signal sent from the protein product back to influence its own transcription — in negative feedback, the protein represses its own gene; in positive feedback, the protein activates its own gene, creating fundamentally different dynamic behaviors |
| Epigenetic Modification | External | The degree of chromatin accessibility at the target gene locus — determined by DNA methylation, histone modifications, and chromatin remodeling enzyme activity, which set the baseline potential for gene activation regardless of transcription factor presence |
| Regulatory Network Stability | Internal | The overall robustness of the gene expression output to perturbations in any individual component — a well-designed regulatory network maintains consistent output despite molecular noise, environmental fluctuations, and stochastic variation in component levels |

### Research for Lesson
- The Central Dogma and Its Regulation — reference materials and textbook resources
- Feedback Loops: The Logic of Biological Circuits — reference materials and textbook resources
- Epigenetic Regulation: Above the Genome — reference materials and textbook resources
- Gene Regulatory Networks and Disease — reference materials and textbook resources

---

## Activity 1: LOCATE — Build Your System

### Text Editor

```
GENE REGULATORY NETWORKS

From Transcription Factor to Phenotype — Modeling the Logic of Gene Expression.
Your body has 20,000 genes but every cell only uses a fraction of them. Who decides which genes turn on, which stay off, and when — and what happens when that decision-making system breaks?

That's not just a question — it's something you can MODEL.
And you're about to build exactly that.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1: CHOOSE YOUR COMPONENTS
• Look at the component panel on the RIGHT side of your screen
• Find the EXTERNAL components (things we can't control):
  ○ Click "Transcription Factor Concentration" — the intracellular abundance of the regulatory protein that initiates the gene expression cascade — determined by the transcription factor's own production rate
  ○ Click "Epigenetic Modification" — the degree of chromatin accessibility at the target gene locus — determined by dna methylation
• Find the INTERNAL components (things that change because of other things):
  ○ Click "Promoter Binding Affinity" — the strength of the molecular interaction between the transcription factor and its target promoter dna sequence — determined by the complementarity of protein-dna surfaces
  ○ Click "mRNA Transcription Rate" — the speed at which rna polymerase synthesizes messenger rna from the target gene template — dependent on transcription factor concentration
  ○ Click "mRNA Degradation Rate" — the speed at which cellular ribonucleases break down messenger rna molecules — mrna half-lives range from 2 minutes (bacteria) to hours (mammalian cells)
  ○ Click "Ribosome Availability" — the fraction of the cell's ribosome pool that is free to translate the target mrna — in rapidly growing cells
  ○ Click "Protein Translation Rate" — the speed at which ribosomes synthesize the target protein from the mrna template — dependent on mrna stability
  ○ Click "Protein Degradation Rate" — the speed at which the target protein is broken down by cellular proteases (proteasome
  ○ Click "Feedback Signal Strength" — the intensity of the regulatory signal sent from the protein product back to influence its own transcription — in negative feedback
  ○ Click "Regulatory Network Stability" — the overall robustness of the gene expression output to perturbations in any individual component — a well-designed regulatory network maintains consistent output despite molecular noise

STEP 2: ADD TO YOUR MODEL
• Click the PLUS (+) button to add each component to your picture
• You should now see 10 components on your canvas

STEP 3: SORT YOUR COMPONENTS
• Sort your components into EXTERNAL and INTERNAL
• EXTERNAL = things we can't control (inputs from outside the system)
• INTERNAL = things that change because of other things in the system
• Your teacher will show you how this works in the video

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

You now have the basic pieces of your system.
But pieces alone don't explain anything — next, we connect them.
```

### Video Script

```
"Your body has 20,000 genes but every cell only uses a fraction of them. Who decides which genes turn on, which stay off, and when — and what happens when that decision-making system breaks?

That's what we're going to figure out today. Not by reading about
it — by MODELING it. You're going to build a system that shows
exactly how this works.

Let's build our system. Look at the component panel on the right
side of your screen. You'll see two types of components:

EXTERNAL components — things that come from outside the system.
Inputs we can't directly control.

INTERNAL components — things that change BECAUSE of other things
in the system. They respond to the externals.

Click on 'Transcription Factor Concentration' — that's external. The intracellular abundance of the regulatory protein that initiates the gene expression cascade — determined by the transcription factor's own production rate.
Click on 'Promoter Binding Affinity' — that's internal. The strength of the molecular interaction between the transcription factor and its target promoter DNA sequence — determined by the complementarity of protein-DNA surfaces.
Click on 'mRNA Transcription Rate' — that's internal. The speed at which RNA polymerase synthesizes messenger RNA from the target gene template — dependent on Transcription Factor Concentration.
Click on 'mRNA Degradation Rate' — that's internal. The speed at which cellular ribonucleases break down messenger RNA molecules — mRNA half-lives range from 2 minutes (bacteria) to hours (mammalian cells).
Click on 'Ribosome Availability' — that's internal. The fraction of the cell's ribosome pool that is free to translate the target mRNA — in rapidly growing cells.
Click on 'Protein Translation Rate' — that's internal. The speed at which ribosomes synthesize the target protein from the mRNA template — dependent on mRNA stability.
Click on 'Protein Degradation Rate' — that's internal. The speed at which the target protein is broken down by cellular proteases (proteasome.
Click on 'Feedback Signal Strength' — that's internal. The intensity of the regulatory signal sent from the protein product back to influence its own transcription — in negative feedback.
Click on 'Epigenetic Modification' — that's external. The degree of chromatin accessibility at the target gene locus — determined by DNA methylation.
Click on 'Regulatory Network Stability' — that's internal. The overall robustness of the gene expression output to perturbations in any individual component — a well-designed regulatory network maintains consistent output despite molecular noise.

Now you need to SORT them. Which ones are external — things that
come from outside the system? Which ones are internal — things
that change because of what's happening inside?

Transcription Factor Concentration and Epigenetic Modification are the two external/upstream components. Transcription Factor Concentration represents the regulatory signal arriving at the gene — determined by upstream signaling pathways, cellular environment, and developmental context, not by the target gene itself. Epigenetic Modification represents the chromatin accessibility state of the target locus, established during development and cell differentiation. All other eight components are internal: Promoter Binding Affinity, mRNA Transcription Rate, mRNA Degradation Rate, Ribosome Availability, Protein Translation Rate, Protein Degradation Rate, Feedback Signal Strength, and Regulatory Network Stability emerge from the molecular interactions between components.

Sort your components, then hit the PLUS button to add each one
to your model canvas.

You've got your pieces. But right now they're just sitting there,
not connected. In the next activity, we'll draw the invisible
lines that show how everything affects everything else.

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing 10 components sorted: Transcription Factor Concentration, Epigenetic Modification (External), Promoter Binding Affinity, mRNA Transcription Rate, mRNA Degradation Rate, Ribosome Availability, Protein Translation Rate, Protein Degradation Rate, Feedback Signal Strength, Regulatory Network Stability (Internal)]

### Graph
[Empty graph panel — no simulation yet]

---

## Activity 2: ESTABLISH — Connect the Relationships

### Text Editor

```
TIME TO DRAW THE INVISIBLE LINES

Those 10 components don't just sit there — they AFFECT each other.
When one changes, others change too. Let's map those connections.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1: OPEN CONNECTION MODE
• Click the "Connect" icon in the TOP LEFT corner of your screen
• Your cursor is now ready to draw relationship arrows

STEP 2: DRAW YOUR RELATIONSHIPS
• Click on "Transcription Factor Concentration" and drag an arrow to "mRNA Transcription Rate"
• Click on "Promoter Binding Affinity" and drag an arrow to "mRNA Transcription Rate"
• Click on "mRNA Degradation Rate" and drag an arrow to "Protein Translation Rate"
• Click on "Ribosome Availability" and drag an arrow to "Protein Translation Rate"
• Click on "Protein Degradation Rate" and drag an arrow to "Feedback Signal Strength"
• Click on "Epigenetic Modification" and drag an arrow to "mRNA Transcription Rate"

STEP 3: SET POSITIVE OR NEGATIVE
• Look at the +/− toggle in the TOP LEFT corner
• For each connection, ask: "When this goes UP, does the other go UP or DOWN?"

  ○ Transcription Factor Concentration → mRNA Transcription Rate = POSITIVE (+)
    Higher Transcription Factor Concentration increases the probability of promoter occupancy, recruiting more RNA polymerase molecules to the gene and increasing the rate of mRNA synthesis.

  ○ Promoter Binding Affinity → mRNA Transcription Rate = POSITIVE (+)
    Stronger Promoter Binding Affinity means each transcription factor molecule stays bound longer and recruits RNA polymerase more effectively, amplifying the transcriptional response at any given transcription factor concentration.

  ○ mRNA Degradation Rate → Protein Translation Rate = NEGATIVE (−)
    Faster mRNA degradation reduces the steady-state pool of translatable mRNA molecules, meaning fewer templates are available for ribosomes to produce protein, reducing the overall translation output.

  ○ Ribosome Availability → Protein Translation Rate = POSITIVE (+)
    More available ribosomes means more mRNA molecules can be simultaneously translated, increasing the rate of protein production from the available mRNA pool.

  ○ Protein Degradation Rate → Feedback Signal Strength = NEGATIVE (−)
    Faster protein degradation reduces the steady-state protein pool available to generate feedback signals, weakening the feedback loop and reducing the circuit's ability to self-regulate.

  ○ Epigenetic Modification → mRNA Transcription Rate = NEGATIVE (−)
    Repressive epigenetic marks (DNA methylation, H3K27 trimethylation) compact chromatin structure and block transcription factor access to the promoter, reducing mRNA Transcription Rate to near zero regardless of Transcription Factor Concentration.

STEP 4: CHECK YOUR MODEL
• You should have 6 arrows total
• 3 negative relationship(s), 3 positive relationship(s)
• This is your system model!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THINK ABOUT IT: Gene expression is not a simple on-off switch — it's a multi-layer cascade with degradation at every level. Even when Transcription Factor Concentration is high and Promoter Binding Affinity is strong, the resulting mRNA is constantly being destroyed by mRNA Degradation Rate. Any mRNA that survives must compete for limited Ribosome Availability to be translated into protein. The protein itself is constantly being degraded by Protein Degradation Rate. And the Feedback Signal Strength from the protein product loops back to change Transcription Factor Concentration or Promoter Binding Affinity — creating dynamic circuits that can oscillate, switch, or maintain precise steady states. Meanwhile, Epigenetic Modification acts as a master dimmer switch — if the chromatin is closed, nothing else matters. How does the cell maintain precise protein levels when every step is subject to production AND destruction simultaneously?
```

### Video Script

```
"Your pieces are on the board, but they're not talking to each
other yet. Time to draw the invisible lines — the relationships
that make this a SYSTEM, not just a pile of parts.

Click the 'Connect' icon in the top left corner. Now you're in
connection mode.

First connection: Click on 'Transcription Factor Concentration' and drag an arrow
over to 'mRNA Transcription Rate.'

Here's the key question: When transcription factor concentration goes UP, does
mrna transcription rate go UP or DOWN?

Higher Transcription Factor Concentration increases the probability of promoter occupancy, recruiting more RNA polymerase molecules to the gene and increasing the rate of mRNA synthesis.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Next connection: Click on 'Promoter Binding Affinity' and drag an arrow
over to 'mRNA Transcription Rate.'

Here's the key question: When promoter binding affinity goes UP, does
mrna transcription rate go UP or DOWN?

Stronger Promoter Binding Affinity means each transcription factor molecule stays bound longer and recruits RNA polymerase more effectively, amplifying the transcriptional response at any given transcription factor concentration.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Last connection: Click on 'mRNA Degradation Rate' and drag an arrow
over to 'Protein Translation Rate.'

Here's the key question: When mrna degradation rate goes UP, does
protein translation rate go UP or DOWN?

Faster mRNA degradation reduces the steady-state pool of translatable mRNA molecules, meaning fewer templates are available for ribosomes to produce protein, reducing the overall translation output.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Final connection: Click on 'Ribosome Availability' and drag an arrow
over to 'Protein Translation Rate.'

Here's the key question: When ribosome availability goes UP, does
protein translation rate go UP or DOWN?

More available ribosomes means more mRNA molecules can be simultaneously translated, increasing the rate of protein production from the available mRNA pool.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Final connection: Click on 'Protein Degradation Rate' and drag an arrow
over to 'Feedback Signal Strength.'

Here's the key question: When protein degradation rate goes UP, does
feedback signal strength go UP or DOWN?

Faster protein degradation reduces the steady-state protein pool available to generate feedback signals, weakening the feedback loop and reducing the circuit's ability to self-regulate.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Final connection: Click on 'Epigenetic Modification' and drag an arrow
over to 'mRNA Transcription Rate.'

Here's the key question: When epigenetic modification goes UP, does
mrna transcription rate go UP or DOWN?

Repressive epigenetic marks (DNA methylation, H3K27 trimethylation) compact chromatin structure and block transcription factor access to the promoter, reducing mRNA Transcription Rate to near zero regardless of Transcription Factor Concentration.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Look at your model now. You've got 3 negative and 3
positive relationships. 6 arrows total.

Gene expression is not a simple on-off switch — it's a multi-layer cascade with degradation at every level. Even when Transcription Factor Concentration is high and Promoter Binding Affinity is strong, the resulting mRNA is constantly being destroyed by mRNA Degradation Rate. Any mRNA that survives must compete for limited Ribosome Availability to be translated into protein. The protein itself is constantly being degraded by Protein Degradation Rate. And the Feedback Signal Strength from the protein product loops back to change Transcription Factor Concentration or Promoter Binding Affinity — creating dynamic circuits that can oscillate, switch, or maintain precise steady states. Meanwhile, Epigenetic Modification acts as a master dimmer switch — if the chromatin is closed, nothing else matters. How does the cell maintain precise protein levels when every step is subject to production AND destruction simultaneously?

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing connected model with arrows: Transcription Factor Concentration +→ mRNA Transcription Rate, Promoter Binding Affinity +→ mRNA Transcription Rate, mRNA Degradation Rate −→ Protein Translation Rate, Ribosome Availability +→ Protein Translation Rate, Protein Degradation Rate −→ Feedback Signal Strength, Epigenetic Modification −→ mRNA Transcription Rate]

---

## Activity 3: VISUALIZE & EVALUATE — Run Your Model

### Text Editor

```
TIME TO SEE YOUR SYSTEM IN ACTION

You built it. You connected it. Now let's see if it actually WORKS
like the real world.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1: RUN THE SIMULATION
• Click the "Play" button in the TOP LEFT corner
• Watch the graph panel — you'll see percentage lines for each component

STEP 2: OBSERVE THE BASELINE
• Let it run for about 30 time steps
• Notice how the lines relate to each other
• When Transcription Factor Concentration is HIGH, what happens to the internal components?

STEP 3: SCENARIO — STEADY-STATE EXPRESSION
• Moderate transcription factor, open chromatin, negative feedback
• PREDICT FIRST: What do you predict determines the final protein level — the production rates or the degradation rates?
• Resume the simulation and observe what happens
• Was your prediction correct?

STEP 4: SCENARIO — POSITIVE FEEDBACK SWITCH
• Strong positive autoregulation
• PREDICT FIRST: What do you predict happens when a protein activates its own gene — does expression stabilize at a higher level or does something more interesting happen?
• Resume the simulation and observe what happens
• Was your prediction correct?

STEP 5: SCENARIO — EPIGENETIC SILENCING
• Closed chromatin, high transcription factor
• PREDICT FIRST: Do you predict that a high concentration of Transcription Factor can overcome epigenetic silencing of the target gene?
• Resume the simulation and observe what happens
• Was your prediction correct?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT DID YOU DISCOVER?
• Steady-state protein levels are determined by the RATIO of production to degradation at every level — doubling transcription rate doubles mRNA only if mRNA Degradation Rate stays constant, and doubling mRNA doubles protein only if Ribosome Availability and Protein Degradation Rate remain unchanged
• Positive feedback loops create bistable switches — the network flips between two stable states (high expression and low expression) with a sharp threshold, explaining how genetically identical cells can adopt completely different fates during development
• Epigenetic modifications act as a master override — when chromatin is closed by DNA methylation or repressive histone marks, no amount of Transcription Factor Concentration can activate the gene, explaining why a liver cell and a neuron have identical DNA but completely different gene expression profiles
• Negative feedback loops create stability and noise reduction — the protein represses its own gene, creating a self-correcting circuit that maintains consistent output despite random fluctuations in any individual component

THE ANSWER: Your genome is not a simple blueprint — it's a dynamic regulatory network where 20,000 genes are controlled by thousands of transcription factors, each binding to specific promoter sequences with specific affinities, producing mRNA that is simultaneously being synthesized and degraded, translated by ribosomes that are a limited shared resource, producing proteins that are themselves being actively destroyed — and many of these proteins feed back to regulate their own genes and others. The ten components of this model capture the core logic: Transcription Factor Concentration and Promoter Binding Affinity determine how fast mRNA is made, mRNA and Protein Degradation Rates determine how fast molecules are destroyed, the balance creates steady-state levels, Feedback Signal Strength creates dynamic circuits (switches, oscillators, homeostats), and Epigenetic Modification sets the master accessibility of the entire locus. When this regulatory logic breaks — a transcription factor mutates, a feedback loop is disrupted, an epigenetic mark is lost — the consequence is disease: uncontrolled cell division (cancer), failed cell differentiation (developmental disorders), or misdirected immune responses (autoimmunity).
```

### Video Script

```
"You've built the machine. You've wired the connections. Now let's
flip the switch and see if your model matches reality.

Click the 'Play' button in the top left. Watch the graph panel —
you'll see lines representing each component as a percentage.

Let it run. Watch how the components interact at baseline levels.
Everything should be balanced, moving together.

First scenario: Steady-State Expression. Moderate transcription factor, open chromatin, negative feedback.
Watch the graph. What do you see happening?

Now let's push the system. Scenario two: Positive Feedback Switch.
Strong positive autoregulation.

Before you run it — make a prediction. What do you predict happens when a protein activates its own gene — does expression stabilize at a higher level or does something more interesting happen?

Resume the simulation and watch what happens. Did your prediction
match the model? If not, that's actually a GOOD thing — it means
you learned something unexpected.

One more scenario: Epigenetic Silencing. Closed chromatin, high transcription factor.
Do you predict that a high concentration of Transcription Factor can overcome epigenetic silencing of the target gene?

Here's what our model reveals: Your genome is not a simple blueprint — it's a dynamic regulatory network where 20,000 genes are controlled by thousands of transcription factors, each binding to specific promoter sequences with specific affinities, producing mRNA that is simultaneously being synthesized and degraded, translated by ribosomes that are a limited shared resource, producing proteins that are themselves being actively destroyed — and many of these proteins feed back to regulate their own genes and others. The ten components of this model capture the core logic: Transcription Factor Concentration and Promoter Binding Affinity determine how fast mRNA is made, mRNA and Protein Degradation Rates determine how fast molecules are destroyed, the balance creates steady-state levels, Feedback Signal Strength creates dynamic circuits (switches, oscillators, homeostats), and Epigenetic Modification sets the master accessibility of the entire locus. When this regulatory logic breaks — a transcription factor mutates, a feedback loop is disrupted, an epigenetic mark is lost — the consequence is disease: uncontrolled cell division (cancer), failed cell differentiation (developmental disorders), or misdirected immune responses (autoimmunity).

You just used a computational model to explain a real-world
phenomenon. That's what scientists do every day.

Now it's your turn to ModelIt!"
```

### Graph
[Screenshot showing simulation graph with scenario results — baseline vs. experimental conditions]

---

## Activity 4: REVISE & EXTEND — Play, Research, Expand

### Text Editor

```
YOUR MODEL WORKS — BUT IT'S NOT COMPLETE

You built a system model. It explains the basics. But real
systems involve WAY more factors.

Time to play, explore, and make your model BETTER.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PLAY TIME CHALLENGES:

1. TELL THE STORY
   • Run your simulation
   • Pretend you're a scientist presenting your findings
   • Explain what's happening and WHY to your partner

2. BREAK THE SYSTEM
   • What happens if you turn OFF Transcription Factor Concentration?
   • What happens if you turn OFF Epigenetic Modification?
   • What happens if you change multiple variables at once?
   • Can you find a combination where the system stays stable?

3. WHAT'S MISSING?
   Your model is simple. Real systems involve more. Think about:

   • MicroRNA Regulation — Small non-coding RNA molecules (18-25 nucleotides) that bind to complementary sequences in mRNA and either block translation or trigger mRNA degradation — adding a powerful post-transcriptional layer of gene regulation that affects over 60% of human genes
   • Chromatin Remodeling Activity — The activity of ATP-dependent chromatin remodeling complexes (SWI/SNF, ISWI, CHD, INO80) that physically reposition nucleosomes to expose or hide gene promoters — the molecular machines that execute epigenetic decisions about gene accessibility
   • Stochastic Noise Level — The inherent randomness in gene expression caused by the probabilistic nature of molecular interactions — when key regulatory molecules are present in low copy numbers (10-100 per cell), random fluctuations can cause genetically identical cells to express genes at dramatically different levels

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RESEARCH DIRECTIONS:

Don't just guess — find out! Here's what to look for:

📚 IN YOUR TEXTBOOK:
   • The Central Dogma and Its Regulation — how does this connect to your model?
   • Feedback Loops: The Logic of Biological Circuits — how does this connect to your model?

🔍 QUESTIONS TO INVESTIGATE:
   • How does your model demonstrate that gene expression is not a simple on-off switch but a dynamic balance of production and degradation at every level?
   • What is the functional difference between negative feedback and positive feedback in gene regulatory circuits — and what happens to Regulatory Network Stability in each case?
   • Why does Epigenetic Modification act as a master override that can silence a gene regardless of Transcription Factor Concentration?
   • How would adding Stochastic Noise Level to your model change predictions about cell-to-cell variation in gene expression?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ADD TO YOUR MODEL:
   • Pick ONE new component from your research
   • Decide: Is it INTERNAL or EXTERNAL?
   • Add it to your model (Plus button)
   • Connect it with relationships (+/−)
   • Run the simulation — does it work like you expected?

What story does your NEW model tell?
```

### Video Script

```
"Your model works. It showed us how the key components interact
and why things happen the way they do. But you and I both know
this isn't the whole story.

Real systems are way more complicated. So now it's time to PLAY,
QUESTION, and EXPAND.

First — tell the story. Run your simulation and pretend you're
a scientist presenting your findings at a conference. Explain
what's happening and WHY to someone next to you. If you can
explain it, you understand it.

Second — break the system. Change the variables. Turn things
on and off. What combinations create extreme results? What
keeps things stable? This is where real insight happens.

Third — and this is the big one — ask what's MISSING.

Your model has 10 components. Real systems involve
way more. Think about...

MicroRNA Regulation. Small non-coding RNA molecules (18-25 nucleotides) that bind to complementary sequences in mRNA and either block translation or trigger mRNA degradation — adding a powerful post-transcriptional layer of gene regulation that affects over 60% of human genes
How would you model that?

Chromatin Remodeling Activity. The activity of ATP-dependent chromatin remodeling complexes (SWI/SNF, ISWI, CHD, INO80) that physically reposition nucleosomes to expose or hide gene promoters — the molecular machines that execute epigenetic decisions about gene accessibility
How would you model that?

Stochastic Noise Level. The inherent randomness in gene expression caused by the probabilistic nature of molecular interactions — when key regulatory molecules are present in low copy numbers (10-100 per cell), random fluctuations can cause genetically identical cells to express genes at dramatically different levels
How would you model that?

Here's your mission: Research ONE new factor. Find out how it
actually works in the real world. Then add it to your model.

Is it internal or external? Click the plus button to add it.
Draw the connections. Set positive or negative. Run the simulation.

Does your new model match reality better than before?

This is how real scientists work. Start simple. Test it. Add
complexity. Test again. Your model is never 'done' — it's
always getting better.

What story will YOUR expanded model tell?

Now it's your turn to ModelIt!"
```

### Activity Network
[Screenshot showing expanded model with 1-2 additional components added by student]

---

## Fun Fact (Career Connection)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔬 CAREER CONNECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Systems Biologists and Synthetic Biologists design and analyze gene regulatory networks for applications in medicine, biosensing, and biomanufacturing. They work for biotech companies (Ginkgo Bioworks, Twist Bioscience), pharmaceutical companies, academic research labs, and government agencies, earning $85,000-$180,000/year. Bioinformaticians who computationally model gene regulatory networks earn $80,000-$160,000/year.

These professionals build models just like the one you made
today — understanding cause-and-effect relationships to solve
real-world problems. Your simple model? That's step one toward
this career.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## TPT Materials

### PowerPoint Slides

```
SLIDE 1: COVER
Visual: Title slide with dramatic visualization of a gene regulatory network — nodes and edges with activation/repression arrows
Say: "You have 20,000 genes. A brain cell uses about 8,000 of them. A skin cell uses a different 8,000. Same DNA, completely different cells. Who decides?"
Do: Display an image comparing cell types from the same organism. Ask: If they have the same DNA, why are they different? What controls which genes are active?
Time: 2 min

SLIDE 2: LEARNING OBJECTIVES
Visual: Learning goals with gene regulation vocabulary
Say: "Today you're building the control system that runs every cell in your body. Transcription factors are the decision-makers, feedback loops are the logic circuits, and epigenetics is the master switch."
Do: Pre-teach transcription factor and feedback loop. Use the analogy: a transcription factor is like a key for a specific lock on a gene — no key, gene stays closed.
Time: 3 min

SLIDE 3: BIG QUESTION
Visual: How does the same genome produce 200+ different cell types?
Say: "Here's the paradox: your liver cells and neurons have identical DNA. But a liver cell makes albumin and a neuron makes dopamine. Something BESIDES DNA is deciding which genes to use. What is it?"
Do: Think-pair-share: Students brainstorm mechanisms that could make the same DNA produce different cell types. Collect ideas — they'll verify these against the model.
Time: 3 min

SLIDE 4: LEVER FRAMEWORK
Visual: LEVER steps with gene regulation context
Say: "We're modeling the entire pipeline from a regulatory signal arriving at a gene to the final protein product — and the feedback loops that make this pipeline intelligent."
Do: Preview LEVER steps. Emphasize that gene expression is not a one-way street — the output feeds back to change the input, creating circuits with logic.
Time: 2 min

SLIDE 5: ACTIVITY 1: COMPONENTS
Visual: Ten component cards spanning signal, transcription, translation, degradation, feedback, and epigenetic levels
Say: "Ten components. Two are upstream inputs that set the stage. Eight are dynamic responses. But here's the twist — some of those responses loop BACK to become inputs through feedback."
Do: Guide sorting of external (Transcription Factor Concentration, Epigenetic Modification) versus internal components. Discuss how Feedback Signal Strength blurs the line between input and output.
Time: 8 min

SLIDE 6: ACTIVITY 2: CONNECTIONS
Visual: Gene expression cascade diagram with production and degradation arrows at every level, plus feedback loops
Say: "At every level — mRNA and protein — there's a race between production and destruction. Steady-state levels depend on the ratio. And the feedback loops make this cascade self-aware."
Do: Students trace the cascade: TF binds promoter, mRNA is made AND destroyed, surviving mRNA is translated AND protein is destroyed, protein feeds back. Map positive versus negative feedback consequences.
Time: 8 min

SLIDE 7: ACTIVITY 3: SIMULATION
Visual: Gene expression dynamics showing steady state, bistable switching, and epigenetic silencing
Say: "Run all three scenarios. In scenario 1, the gene reaches a stable level. In scenario 2, it switches to an entirely different behavior — same components, different circuit architecture. In scenario 3, nothing works at all. Why?"
Do: Students predict, then simulate each scenario. The positive feedback switch is the key discovery — understanding how the same parts create qualitatively different behaviors depending on circuit wiring.
Time: 10 min

SLIDE 8: DISCOVERIES
Visual: Key regulatory network insights with medical implications
Say: "You just modeled the logic that controls every cell in your body. When this logic breaks — when a feedback loop fails or an epigenetic mark is lost — the result is disease. Cancer, developmental disorders, autoimmunity — they're all regulatory network failures."
Do: Connect each scenario to a disease mechanism. Positive feedback stuck ON = cancer (constitutively active oncogene). Epigenetic silencing of tumor suppressor = cancer. Feedback loop disrupted = autoimmune disease.
Time: 5 min

SLIDE 9: STEM CHALLENGE
Visual: Synthetic gene circuit biosensor design challenge
Say: "A water agency needs a cheap biosensor for lead contamination. Design a living gene circuit — using the regulatory components you just modeled — that detects lead in water and glows green. This is real synthetic biology."
Do: Groups design synthetic gene circuits: sensor element (metal-responsive TF), circuit logic (feedback for sensitivity), output (fluorescent protein), and calibration strategy. Present designs.
Time: 12 min

```

### Teacher Guide

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TEACHER GUIDE: Gene Regulatory Networks
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LESSON PURPOSE:
This lesson introduces students to gene regulatory networks — the molecular logic circuits that control which genes are expressed in every cell. Biotech skill focus: Network dynamics and feedback circuit analysis. Understanding gene regulation is fundamental to both basic biology (how does a fertilized egg become a complete organism?) and biotechnology (how do we engineer cells to produce desired proteins or behaviors?).

NGSS ALIGNMENT:
HS-LS3-1, HS-LS1-4: Ask questions to clarify relationships about the role of DNA and chromosomes in coding the instructions for characteristic traits passed from parents to offspring; use a model to illustrate the role of cellular division in producing and maintaining complex organisms.

THREE-DIMENSIONAL LEARNING:
• Science Practice: Developing and Using Models / Asking Questions and Defining Problems
  Students develop a multi-scale gene regulatory model that connects molecular interactions (transcription factor-DNA binding) to cellular outcomes (protein levels, cell fate), asking questions about how regulatory logic creates emergent biological behavior.
• Disciplinary Core Idea: LS3.A Inheritance of Traits / LS1.A Structure and Function
  DNA contains instructions for protein production regulated by transcription factors and epigenetic modifications; cellular function emerges from the coordinated expression of gene regulatory networks.
• Crosscutting Concept: Cause and Effect / Systems and System Models
  Students trace causal chains from transcription factor binding through mRNA and protein dynamics to cellular phenotype, analyzing the gene regulatory network as a complex system with emergent properties including switches, oscillators, and stability.

PACING GUIDE:
• Activity 1 (Locate): 8-10 minutes
• Activity 2 (Establish): 8-10 minutes
• Activity 3 (Visualize & Evaluate): 10-12 minutes
• Activity 4 (Revise & Extend): 10-15 minutes
• Total: 50-70 minutes (or split across 2 class periods)

PRE-LESSON PREP:
□ Test ModelIt access on student devices
□ Review vocabulary: Transcription Factor, Promoter Binding Affinity, Feedback Loop, Epigenetic Modification
□ Prepare Your body has 20,000 genes but every cell only uses a fraction of them. Who decides which genes turn on, which stay off, and when — and what happens when that decision-making system breaks discussion hook
□ Have images or video ready for phenomenon introduction

LEVER FRAMEWORK:
• Locate: Students identify ten components spanning signal input (Transcription Factor Concentration), molecular interaction (Promoter Binding Affinity), mRNA dynamics (Transcription Rate, Degradation Rate), translation dynamics (Ribosome Availability, Translation Rate), protein dynamics (Degradation Rate), regulatory feedback (Feedback Signal Strength), epigenetic context (Epigenetic Modification), and system-level outcome (Regulatory Network Stability).
• Establish: Students determine that Transcription Factor Concentration and Epigenetic Modification are the primary external/upstream inputs — one representing the signal and the other representing chromatin accessibility — while all other components emerge as dynamic responses to these inputs and to each other through production-degradation balances and feedback loops.
• Visualize: Students build a gene regulatory network model connecting signal input through the transcription-translation cascade to protein output, with feedback loops that create dynamic behaviors (steady state, switching, or oscillation) depending on circuit architecture.
• Evaluate: Students run steady-state, positive-feedback-switch, and epigenetic-silencing scenarios to discover how the same molecular components create fundamentally different behaviors depending on feedback structure and chromatin state.
• Revise: Students add MicroRNA Regulation, Chromatin Remodeling Activity, or Stochastic Noise Level to explore post-transcriptional regulation, chromatin dynamics, and the role of molecular noise in cell fate decisions.

BACKGROUND CONTENT:
• The Central Dogma and Its Regulation:
  The flow of genetic information from DNA to RNA to protein — the central dogma of molecular biology — is regulated at every step. Transcriptional regulation (which genes are copied into mRNA) is controlled by transcription factors that bind to promoter and enhancer regions of DNA, either recruiting or blocking RNA polymerase. Post-transcriptional regulation controls mRNA processing (splicing, capping, polyadenylation), mRNA stability (degradation by ribonucleases and microRNAs), and mRNA localization. Translational regulation controls how efficiently ribosomes convert mRNA into protein, influenced by initiation factor availability, codon usage, and ribosome density. Post-translational regulation controls protein folding, modification (phosphorylation, ubiquitination, glycosylation), localization, and degradation. Each regulatory layer adds complexity but also adds control points that the cell — or the engineer — can exploit.

• Feedback Loops: The Logic of Biological Circuits:
  Gene regulatory networks use feedback loops to create sophisticated dynamic behaviors from simple molecular interactions. Negative feedback occurs when a gene's protein product represses its own transcription — this creates a self-correcting homeostatic circuit that maintains stable protein levels despite perturbations. If protein level rises above the setpoint, increased repression reduces transcription; if it falls below, reduced repression increases transcription. Positive feedback occurs when a gene's protein product activates its own transcription — this creates a bistable switch with two stable states (high expression or low expression) and a sharp threshold for switching between them. Positive feedback is how cells make irreversible fate decisions during development: once a master regulator crosses the threshold and activates its own gene, the cell locks into a new identity. Combined negative and positive feedback creates oscillators — circuits that rhythmically pulse gene expression, underlying circadian clocks, cell cycle progression, and somite segmentation in embryonic development.

• Epigenetic Regulation: Above the Genome:
  Epigenetic modifications add a layer of gene regulation that operates above the DNA sequence level — modifying gene accessibility without changing the genetic code. DNA methylation adds methyl groups to cytosine bases in CpG dinucleotides, which recruits repressive protein complexes that condense chromatin and silence gene expression. Histone modifications — acetylation (generally activating), methylation (activating or repressing depending on position), phosphorylation, and ubiquitination — alter the physical structure of chromatin, determining whether DNA is accessible to transcription factors and RNA polymerase. These modifications are maintained through cell division by dedicated maintenance enzymes, allowing a liver cell and a neuron to maintain their distinct gene expression profiles through hundreds of cell divisions despite having identical DNA. Epigenetic dysregulation is increasingly recognized as a driver of cancer (global hypomethylation and focal hypermethylation of tumor suppressor genes), aging, and developmental disorders.

• Gene Regulatory Networks and Disease:
  Many diseases result from disruptions in gene regulatory networks rather than mutations in the protein-coding genes themselves. Cancer frequently involves mutations in transcription factors (p53, MYC, RB) that disrupt the regulatory circuits controlling cell division — a single mutation in the p53 gene disrupts the network that senses DNA damage, arrests the cell cycle, and triggers apoptosis, removing a critical safety brake on cell proliferation. Developmental disorders like holoprosencephaly result from mutations in the Sonic Hedgehog (SHH) signaling pathway's regulatory elements — the gene itself is intact, but the regulatory network that controls where and when it's expressed is disrupted. Autoimmune diseases involve dysregulation of the transcription factor FOXP3, which controls regulatory T-cell differentiation — without proper FOXP3 expression, the immune system attacks the body's own tissues. Understanding gene regulatory network architecture is therefore essential for understanding disease mechanisms and designing therapeutic interventions.

COMMON MISCONCEPTIONS:
• "Genes are either 'on' or 'off' like a light switch"
  Reality: While some gene regulatory circuits DO behave as switches (positive feedback bistable systems), most gene expression is graded — genes can be expressed at any level from barely detectable to maximum capacity. The model demonstrates that steady-state expression is determined by the balance of production and degradation rates at every level, producing a continuous range of output levels. Even 'switch-like' genes have intermediate states during transitions. The light switch analogy is especially misleading because it implies gene regulation is simple — in reality, a single gene can be regulated by dozens of transcription factors, each binding with different affinity, creating a complex dose-response landscape.
  Strategy: Model it: Gradually increase Transcription Factor Concentration from zero to maximum and graph the protein output. Is the response a step function (switch) or a graded curve? Now add positive feedback and repeat — how does the curve change?

• "DNA methylation permanently silences genes forever"
  Reality: While DNA methylation is relatively stable and heritable through cell division, it is NOT permanent or irreversible. Cells express TET enzymes (TET1, TET2, TET3) that actively demethylate DNA, and passive demethylation occurs when maintenance methyltransferases fail to copy methylation patterns during DNA replication. During embryonic development, there are two waves of global demethylation (in the early embryo and in primordial germ cells) where most methylation marks are erased and re-established. In cancer, aberrant demethylation of silenced oncogenes and aberrant methylation of active tumor suppressors both contribute to disease. Epigenetic therapy drugs (5-azacytidine, decitabine) work by blocking DNA methyltransferases, demonstrating that methylation is reversible.
  Strategy: Ask: If DNA methylation were truly permanent, how would a fertilized egg (one cell type with one methylation pattern) give rise to 200+ cell types, each with different methylation patterns?

• "More transcription factor always means more gene expression"
  Reality: The relationship between Transcription Factor Concentration and gene expression is NOT linear — it follows a sigmoidal (S-shaped) saturation curve. At low TF concentrations, promoter occupancy is minimal and expression is low. At intermediate concentrations, small changes in TF produce large changes in expression (the sensitive range). At high concentrations, the promoter is fully occupied and adding more TF has no effect (saturation). Furthermore, if Epigenetic Modification has closed the chromatin, no amount of TF will activate the gene. And in circuits with negative feedback, increasing TF concentration is partially counteracted by the feedback loop, producing a smaller net increase in expression than expected.
  Strategy: Experiment: In the simulation, increase Transcription Factor Concentration from 10% to 90% and record the protein output at each step. Plot the data — is the relationship linear, logarithmic, or sigmoidal? Where is the steepest part of the curve?

FACILITATION TIPS:
• Activity 1: Let students explore the interface. Don't over-explain.
  Let them discover. Circulate and support, don't lecture.
• Activity 2: Ask "When this goes up, what happens to that?" to
  guide positive/negative relationship decisions. Let students debate.
• Activity 3: Give time for students to "break" the model — turn
  things on/off and observe. This is where real insight happens.
• Activity 4: Don't give answers. Ask questions. Let curiosity drive
  the research. Celebrate when students' additions don't work as
  expected — that's authentic science.

ANSWER KEY:
Big Question: Your body has 20,000 genes but every cell only uses a fraction of them. Who decides which genes turn on, which stay off, and when — and what happens when that decision-making system breaks?
Answer: Your genome is not a simple blueprint — it's a dynamic regulatory network where 20,000 genes are controlled by thousands of transcription factors, each binding to specific promoter sequences with specific affinities, producing mRNA that is simultaneously being synthesized and degraded, translated by ribosomes that are a limited shared resource, producing proteins that are themselves being actively destroyed — and many of these proteins feed back to regulate their own genes and others. The ten components of this model capture the core logic: Transcription Factor Concentration and Promoter Binding Affinity determine how fast mRNA is made, mRNA and Protein Degradation Rates determine how fast molecules are destroyed, the balance creates steady-state levels, Feedback Signal Strength creates dynamic circuits (switches, oscillators, homeostats), and Epigenetic Modification sets the master accessibility of the entire locus. When this regulatory logic breaks — a transcription factor mutates, a feedback loop is disrupted, an epigenetic mark is lost — the consequence is disease: uncontrolled cell division (cancer), failed cell differentiation (developmental disorders), or misdirected immune responses (autoimmunity).

Simulation Answers:
• Steady-State Expression Scenario: With moderate Transcription Factor Concentration, open chromatin (low repressive Epigenetic Modification), and negative Feedback Signal Strength, the gene expression cascade reaches a predictable steady state. mRNA Transcription Rate produces mRNA at a constant rate; mRNA Degradation Rate destroys it at a proportional rate; the balance determines steady-state mRNA level. Similarly, Protein Translation Rate produces protein while Protein Degradation Rate removes it. The negative feedback loop stabilizes the system: if protein rises above the setpoint, it represses its own transcription, reducing mRNA production and bringing protein back down. The result is remarkably stable protein output despite fluctuations in individual components.
• Epigenetic Silencing Scenario: When Epigenetic Modification is set to repressive (closed chromatin), the result is dramatic: mRNA Transcription Rate drops to near-zero regardless of Transcription Factor Concentration. Even with high TF levels and strong Promoter Binding Affinity, the gene is physically inaccessible because nucleosomes block the promoter and DNA methylation prevents TF binding. Existing mRNA and protein are degraded without replacement, and steady-state levels approach zero. This demonstrates why Epigenetic Modification acts as a master override — it controls gene accessibility at a level above transcription factor regulation, explaining how cell identity is maintained through division.

Reflection Exemplars:
• Q: How does the production-degradation balance determine steady-state levels?
  A: The model reveals a fundamental principle: steady-state molecule levels are determined not by production alone, but by the RATIO of production to degradation. Doubling mRNA Transcription Rate doubles steady-state mRNA only if mRNA Degradation Rate is unchanged. If the cell simultaneously increases mRNA Degradation Rate (which often happens as a compensatory response), the steady-state mRNA level may not change at all. This is why cells can respond quickly to signals — they don't need to 'turn off' mRNA production; they simply increase degradation rate. It also explains why protein half-lives matter so much: a protein with a 2-minute half-life can be eliminated 50x faster than one with a 2-hour half-life, enabling rapid regulatory responses.
• Q: What makes positive feedback create a bistable switch?
  A: Positive feedback creates bistability because the protein product activates its own transcription, creating a self-reinforcing loop. Below a critical threshold of Transcription Factor Concentration, the positive feedback is too weak to sustain itself and expression remains low. Above the threshold, positive feedback amplifies expression rapidly until it saturates at a high stable state. Between these states, the system is unstable — it must commit to one or the other. This creates a binary decision: ON or OFF, with a sharp transition. This is exactly how cells make irreversible fate decisions during development — once a master regulator crosses the threshold and activates its own expression, the cell locks into its new identity permanently.

STEM CHALLENGE GUIDANCE:
Title: Design a Synthetic Gene Circuit for Biosensing
Mission: Design a synthetic gene regulatory circuit that detects an environmental signal (toxin, pathogen, pollutant) and produces a visible output (fluorescent protein, color change, electronic signal) for use as a living biosensor.
Scenario: A water quality monitoring agency needs a low-cost, deployable biosensor that can detect heavy metal contamination (lead, arsenic, mercury) in drinking water supplies across rural communities where laboratory testing is unavailable. Your synthetic biology team must design a gene regulatory circuit that senses the presence of heavy metals and produces a visible fluorescent signal proportional to contamination level. The biosensor must be sensitive, specific, and stable.
Introduction: Present the challenge: A water quality monitoring agency needs a low-cost, deployable living biosensor that detects heavy metal contamination in drinking water. Your synthetic biology team will design a gene regulatory circuit that senses lead or arsenic in water and produces a fluorescent signal proportional to contamination level — using the exact regulatory components you modeled in class.

Key Concepts:
• Biosensor Circuit Design: A living biosensor has three modules: (1) Sensor — a metal-responsive transcription factor (like PbrR for lead or ArsR for arsenic) that changes conformation when it binds the target metal, altering its DNA-binding properties; (2) Processor — the regulatory circuit that converts the sensor signal into an amplified, dose-proportional output, potentially using feedback loops to improve sensitivity; (3) Reporter — the output gene (GFP, luciferase, or a chromogenic enzyme like LacZ) whose expression level is proportional to metal concentration.
• Signal Amplification and Noise Filtering: Raw biosensor signals are weak and noisy because transcription factor-metal binding is stochastic at low concentrations. Positive feedback can amplify weak signals but also amplifies noise. Negative feedback reduces noise but also reduces sensitivity. The optimal circuit uses a combination: positive feedback for signal amplification with a downstream negative feedback filter to suppress false positives. This is a fundamental engineering trade-off between sensitivity and specificity.
• Calibration and Quantitation: For a biosensor to be useful, fluorescence intensity must map to a specific metal concentration. This requires: a dose-response calibration curve (fluorescence vs. metal concentration), knowledge of the circuit's dynamic range (minimum and maximum detectable concentrations), understanding of environmental interferences (pH, temperature, other metals that might cross-react), and a standardized measurement protocol that accounts for cell number, growth phase, and measurement timing.

Evaluation Rubric:
• Expert (4): Circuit design includes justified sensor element, signal processing logic with feedback architecture, output reporter, calibration strategy, biocontainment plan, and analysis of sensitivity-specificity trade-offs supported by model predictions
• Proficient (3): Circuit design includes sensor, processor, and reporter modules with reasoning connected to regulatory network model principles
• Developing (2): Circuit design covers basic sensor-reporter connection but lacks signal processing logic, calibration strategy, or analysis of noise and specificity
• Beginning (1): Circuit design is incomplete or does not connect to gene regulatory network principles from the model

DIFFERENTIATION:
Support (Struggling Learners):
  • Provide a visual template showing the three biosensor modules (Sensor, Processor, Reporter) with empty boxes for students to fill in component choices and connections
  • Use a simplified feedback diagram: 'Signal IN -> [Sensor TF] -> [Promoter] -> [mRNA] -> [Protein/Reporter] -> Signal OUT. Where would you add feedback? What kind? Why?'
  • Scaffold dose-response thinking: 'At 0 ppb lead, the sensor produces ___. At 15 ppb (EPA action level), the sensor produces ___. At 100 ppb, the sensor produces ___. Is this response linear, switch-like, or something else?'

Extensions (Advanced Learners):
  • Research the iGEM (International Genetically Engineered Machine) competition — find a team that built a biosensor and analyze their gene regulatory circuit design using the components from your model
  • Investigate how CRISPR-based gene regulatory tools (CRISPRi and CRISPRa) allow programmable activation or repression of any gene — how does this change the design space for synthetic gene circuits?
  • Compare the gene regulatory networks controlling pluripotency in stem cells (OCT4, SOX2, NANOG) with the networks controlling differentiation — what circuit architecture keeps stem cells in their undifferentiated state?

Cross-Curricular Connections:
  • Math: Model the steady-state mRNA concentration using the equation [mRNA]ss = Transcription Rate / Degradation Rate, then calculate how changing each parameter by 2-fold affects the steady state — verify predictions with the simulation
  • ELA: Write a patient-accessible explanation of how a gene regulatory network malfunction leads to cancer — specifically, how a mutation in the p53 transcription factor disables the DNA damage feedback loop, using language a high school student's parent would understand
  • Computer Science: Compare gene regulatory network logic (AND gates, OR gates, NOT gates, feedback loops) to digital electronic circuit logic — are biological circuits fundamentally similar to computer circuits, or fundamentally different?

CAST ALIGNMENT:
• Model the multi-step cascade from transcription factor binding through mRNA production, translation, and protein degradation to final steady-state protein levels
• Analyze how positive and negative feedback loops create fundamentally different regulatory behaviors — bistable switches versus homeostatic stability
• Evaluate how epigenetic modifications override transcriptional regulation to create and maintain cell identity during development

CAST-Style Assessment Questions:
• Multiple Choice: A mutation increases the mRNA Degradation Rate of a tumor suppressor gene by 5-fold while leaving Transcription Rate unchanged. Based on your model, what is the most likely consequence for steady-state protein level and cell behavior?
• Constructed Response: Using your gene regulatory network model, explain how two genetically identical cells can have completely different gene expression profiles and become different cell types. Reference at least three model components — including Epigenetic Modification and Feedback Signal Strength — in your explanation.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Activity Pack

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STUDENT ACTIVITY PACK: Gene Regulatory Networks
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NAME: _________________________ DATE: _____________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRE-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. If every cell in your body has the same DNA, why is a brain cell so different from a skin cell?

   _________________________________________________________

   _________________________________________________________

2. What do you think controls which genes are turned on or off in a particular cell at a particular time?

   _________________________________________________________

   _________________________________________________________

3. Draw a diagram showing how you think a cell 'reads' a gene and makes the protein it codes for — include as many steps as you can.

   [DRAWING BOX]

4. What do you think happens when a gene that should be turned off gets stuck in the 'on' position?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VOCABULARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Match the term to the definition:

___ Transcription Factor          
___ Promoter Binding Affinity     
___ Feedback Loop                 
___ Epigenetic Modification       

A. A protein that binds to specific DNA sequences (promoter and enhancer regions) to increase or decrease the transcription rate of a target gene — the molecular decision-makers that control which genes are expressed in a given cell at a given time
B. The strength of the physical interaction between a transcription factor protein and its DNA binding site — measured by the dissociation constant (Kd), where lower Kd means tighter binding and stronger transcriptional activation or repression
C. A regulatory circuit where the output of a gene expression pathway feeds back to influence its own input — negative feedback creates stable, self-correcting systems while positive feedback creates bistable switches that lock cells into distinct states
D. Chemical modifications to DNA (methylation) or histone proteins (acetylation, methylation, phosphorylation) that alter gene expression without changing the DNA sequence — these modifications can be inherited through cell division and represent a layer of gene regulation above the genetic code

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MODEL PLANNING SPACE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Before you build in ModelIt, sort your components here:

EXTERNAL (can't control):
_______________ _______________ _______________

INTERNAL (changes based on other things):
_______________ _______________ _______________

Draw arrows showing relationships. Label each + or −.

[MODEL SKETCH BOX]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SIMULATION OBSERVATIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SCENARIO: Steady-State Expression
Settings: Moderate transcription factor, open chromatin, negative feedback
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Positive Feedback Switch
Settings: Strong positive autoregulation
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Epigenetic Silencing
Settings: Closed chromatin, high transcription factor
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

The KEY discovery from my simulation is:

_________________________________________________________

_________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RESEARCH & EXTEND
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NEW COMPONENT I want to add: _____________________________

Is it EXTERNAL or INTERNAL? (circle one)

What does it connect to? _________________________________

Is the relationship POSITIVE or NEGATIVE? _________________

Why? ____________________________________________________

_________________________________________________________

After adding it, my simulation showed:

_________________________________________________________

_________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REFLECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. How does your model demonstrate that gene expression is not a simple on-off switch but a dynamic balance of production and degradation at every level?

   _________________________________________________________

   _________________________________________________________

2. What is the functional difference between negative feedback and positive feedback in gene regulatory circuits — and what happens to Regulatory Network Stability in each case?

   _________________________________________________________

   _________________________________________________________

3. Why does Epigenetic Modification act as a master override that can silence a gene regardless of Transcription Factor Concentration?

   _________________________________________________________

   _________________________________________________________

4. How would adding Stochastic Noise Level to your model change predictions about cell-to-cell variation in gene expression?

   _________________________________________________________

   _________________________________________________________

5. What are the medical implications when gene regulatory networks malfunction — and how does your model help explain diseases like cancer?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
POST-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Your body has 20,000 genes but every cell only uses a fraction of them. Who decides which genes turn on, which stay off, and when — and what happens when that decision-making system breaks? Explain using evidence from your model:

   _________________________________________________________

   _________________________________________________________

   _________________________________________________________

2. Which NGSS dimensions did this lesson address?
   (Check all that apply)
   □ Science Practice: Developing and Using Models / Asking Questions and Defining Problems
   □ Disciplinary Core Idea: LS3.A Inheritance of Traits / LS1.A Structure and Function
   □ Crosscutting Concept: Cause and Effect / Systems and System Models

3. What are the medical implications when gene regulatory networks malfunction — and how does your model help explain diseases like cancer?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEM CHALLENGE: Design a Synthetic Gene Circuit for Biosensing
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MISSION: Design a synthetic gene regulatory circuit that detects an environmental signal (toxin, pathogen, pollutant) and produces a visible output (fluorescent protein, color change, electronic signal) for use as a living biosensor.

SCENARIO: A water quality monitoring agency needs a low-cost, deployable biosensor that can detect heavy metal contamination (lead, arsenic, mercury) in drinking water supplies across rural communities where laboratory testing is unavailable. Your synthetic biology team must design a gene regulatory circuit that senses the presence of heavy metals and produces a visible fluorescent signal proportional to contamination level. The biosensor must be sensitive, specific, and stable.

GUIDING QUESTIONS:
• What natural metal-responsive transcription factor would you use as your sensor element, and what Promoter Binding Affinity characteristics would you need?
• How would you engineer the circuit to produce a signal proportional to contamination level rather than a simple on/off response?
• What Feedback Signal Strength and type (positive or negative) would you include to improve sensitivity and reduce noise?

DESIGN THINKING:
• How would you ensure the biosensor remains functional in variable environmental conditions (temperature, pH, salinity)?

  _________________________________________________________

• What output signal would be most practical for field deployment — fluorescence, color change, or electronic signal — and why?

  _________________________________________________________

• How would you calibrate the biosensor so that fluorescence intensity can be converted to a quantitative contamination reading?

  _________________________________________________________

• What biocontainment strategy would you use to prevent the engineered bacteria from escaping into the water supply being tested?

  _________________________________________________________


EVALUATION RUBRIC:
• Expert (4): Circuit design includes justified sensor element, signal processing logic with feedback architecture, output reporter, calibration strategy, biocontainment plan, and analysis of sensitivity-specificity trade-offs supported by model predictions
• Proficient (3): Circuit design includes sensor, processor, and reporter modules with reasoning connected to regulatory network model principles
• Developing (2): Circuit design covers basic sensor-reporter connection but lacks signal processing logic, calibration strategy, or analysis of noise and specificity
• Beginning (1): Circuit design is incomplete or does not connect to gene regulatory network principles from the model

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Resources

| Resource | Link |
|----------|------|
| Activity Pack (DOCX) | [materials/grade-09/G09L3-L08/G09L3-L08-Student-Activity-Pack.docx] |
| Teacher Guide (DOCX) | [materials/grade-09/G09L3-L08/G09L3-L08-Teachers-Guide.docx] |
| PPT Presentation | [materials/grade-09/G09L3-L08/G09L3-L08-Student-Presentation.pptx] |
| Platform Link | [ModelIt lesson link] |

---

## Lesson Metadata

| Field | Value |
|-------|-------|
| Created | February 2026 |
| Author | Alexandria's Design |
| Template Version | 1.0 |
| Platform | ModelIt (formerly Cell Collective) |
| Estimated Time | 50-70 minutes |
| Can Split Across | 2 class periods |