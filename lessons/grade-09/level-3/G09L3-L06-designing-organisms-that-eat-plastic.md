# Lesson: Designing Organisms That Eat Plastic

## Header Information

| Field | Value |
|-------|-------|
| **Lesson ID** | G09L3-L06 |
| **Grade** | 9th Grade — Level 3: Biotech |
| **Lesson Name** | Designing Organisms That Eat Plastic |
| **Status** | Template |

---

## Platform

### Title
**Designing Organisms That Eat Plastic — Synthetic Biology and Metabolic Engineering for Environmental Remediation**

### Overview
This lesson introduces students to synthetic biology and metabolic engineering in the context of plastic bioremediation — one of the most exciting applications of engineered organisms. Biotech skill focus: Synthetic design and systems biology. The discovery of natural plastic-degrading enzymes opened a new frontier in environmental biotechnology, but translating laboratory breakthroughs to real-world solutions requires systems-level synthetic design. Students investigate the driving question: 8 million tons of plastic enter the ocean every year. Can we engineer a living organism that breaks it down? Using the LEVER framework, students identify key components, establish cause-and-effect relationships, run simulations to test scenarios, and extend their understanding through research and engineering challenges.

### Cover Image
[A photorealistic, cinematic image of diverse 14-15 year old students in an advanced synthetic biology lab examining engineered bacterial colonies on plates next to degrading plastic samples, with DNA design software and metabolic pathway diagrams on screens, green and blue laboratory lighting]

### Grade
9th Grade — Level 3: Biotech

### NGSS Standard
**HS-LS1-5, HS-ETS1-2**: Use a model to illustrate how photosynthesis transforms light energy into stored chemical energy; design a solution to a complex real-world problem by breaking it down into smaller, more manageable problems.

### Learning Objectives
- Build a synthetic biology model that integrates enzyme engineering, metabolic pathway design, and organism behavior for environmental plastic degradation
- Analyze how enzyme activity, substrate concentration, metabolic efficiency, and environmental conditions interact in an engineered biodegradation system
- Optimize organism design parameters to maximize plastic degradation rate while minimizing toxic byproduct generation and ecological risk
- Evaluate the trade-offs between degradation speed, organism containment, and environmental safety in synthetic biology applications

### Component List (Starting Model: 10 Components)

| Component | Type | What It Represents |
|-----------|------|-------------------|
| Enzyme Activity Level | Internal | The catalytic efficiency of the engineered plastic-degrading enzyme (PETase or engineered variants), measured by turnover rate — how many plastic molecules each enzyme molecule processes per second |
| Substrate Concentration | External | The amount of plastic material available for degradation in the environment — determined by plastic waste density, surface area exposure, and the physical form of the plastic (film, fiber, particle, microplastic) |
| Metabolic Pathway Efficiency | Internal | The completeness and efficiency of the engineered metabolic pathway that converts plastic breakdown products (terephthalic acid, ethylene glycol) into energy and biomass rather than accumulating toxic intermediates |
| Byproduct Toxicity | Internal | The harmful effects of intermediate chemical compounds produced during plastic degradation — incomplete breakdown can generate compounds more toxic than the original plastic |
| Organism Growth Rate | Internal | The proliferation speed of the engineered organism in environmental conditions, which determines how quickly the degradation capacity scales up in a contaminated site |
| Environmental Temperature | External | The ambient temperature of the degradation environment, which critically affects enzyme activity (PETase is most active at 30-65°C) and organism survival |
| pH Tolerance | Internal | The engineered organism's ability to function across a range of environmental pH conditions — ocean water (pH 8.1), soil (pH 4-9), and landfill leachate (pH 5-9) present different challenges |
| Oxygen Requirements | External | The amount of dissolved oxygen the engineered organism needs for aerobic metabolism and enzyme function — determines whether the system works in oxygen-rich surface environments or oxygen-poor deep ocean/landfill conditions |
| Degradation Rate | Internal | The overall speed at which plastic is broken down into harmless products in the environment, measured in grams per liter per day — the key performance metric for the engineered system |
| Containment Level | External | The degree of biological containment engineered into the organism — kill switches, auxotrophies (dependence on lab-supplied nutrients), or geographic barriers that prevent uncontrolled spread into natural ecosystems |

### Research for Lesson
- The Plastic Pollution Crisis — reference materials and textbook resources
- The PETase Discovery — reference materials and textbook resources
- Metabolic Engineering for Complete Degradation — reference materials and textbook resources
- The Containment Challenge — reference materials and textbook resources

---

## Activity 1: LOCATE — Build Your System

### Text Editor

```
DESIGNING ORGANISMS THAT EAT PLASTIC

Synthetic Biology and Metabolic Engineering for Environmental Remediation.
8 million tons of plastic enter the ocean every year. Can we engineer a living organism that breaks it down?

That's not just a question — it's something you can MODEL.
And you're about to build exactly that.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1: CHOOSE YOUR COMPONENTS
• Look at the component panel on the RIGHT side of your screen
• Find the EXTERNAL components (things we can't control):
  ○ Click "Substrate Concentration" — the amount of plastic material available for degradation in the environment — determined by plastic waste density
  ○ Click "Environmental Temperature" — the ambient temperature of the degradation environment
  ○ Click "Oxygen Requirements" — the amount of dissolved oxygen the engineered organism needs for aerobic metabolism and enzyme function — determines whether the system works in oxygen-rich surface environments or oxygen-poor deep ocean/landfill conditions
  ○ Click "Containment Level" — the degree of biological containment engineered into the organism — kill switches
• Find the INTERNAL components (things that change because of other things):
  ○ Click "Enzyme Activity Level" — the catalytic efficiency of the engineered plastic-degrading enzyme (petase or engineered variants)
  ○ Click "Metabolic Pathway Efficiency" — the completeness and efficiency of the engineered metabolic pathway that converts plastic breakdown products (terephthalic acid
  ○ Click "Byproduct Toxicity" — the harmful effects of intermediate chemical compounds produced during plastic degradation — incomplete breakdown can generate compounds more toxic than the original plastic
  ○ Click "Organism Growth Rate" — the proliferation speed of the engineered organism in environmental conditions
  ○ Click "pH Tolerance" — the engineered organism's ability to function across a range of environmental ph conditions — ocean water (ph 8
  ○ Click "Degradation Rate" — the overall speed at which plastic is broken down into harmless products in the environment

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
"8 million tons of plastic enter the ocean every year. Can we engineer a living organism that breaks it down?

That's what we're going to figure out today. Not by reading about
it — by MODELING it. You're going to build a system that shows
exactly how this works.

Let's build our system. Look at the component panel on the right
side of your screen. You'll see two types of components:

EXTERNAL components — things that come from outside the system.
Inputs we can't directly control.

INTERNAL components — things that change BECAUSE of other things
in the system. They respond to the externals.

Click on 'Enzyme Activity Level' — that's internal. The catalytic efficiency of the engineered plastic-degrading enzyme (PETase or engineered variants).
Click on 'Substrate Concentration' — that's external. The amount of plastic material available for degradation in the environment — determined by plastic waste density.
Click on 'Metabolic Pathway Efficiency' — that's internal. The completeness and efficiency of the engineered metabolic pathway that converts plastic breakdown products (terephthalic acid.
Click on 'Byproduct Toxicity' — that's internal. The harmful effects of intermediate chemical compounds produced during plastic degradation — incomplete breakdown can generate compounds more toxic than the original plastic.
Click on 'Organism Growth Rate' — that's internal. The proliferation speed of the engineered organism in environmental conditions.
Click on 'Environmental Temperature' — that's external. The ambient temperature of the degradation environment.
Click on 'pH Tolerance' — that's internal. The engineered organism's ability to function across a range of environmental pH conditions — ocean water (pH 8.
Click on 'Oxygen Requirements' — that's external. The amount of dissolved oxygen the engineered organism needs for aerobic metabolism and enzyme function — determines whether the system works in oxygen-rich surface environments or oxygen-poor deep ocean/landfill conditions.
Click on 'Degradation Rate' — that's internal. The overall speed at which plastic is broken down into harmless products in the environment.
Click on 'Containment Level' — that's external. The degree of biological containment engineered into the organism — kill switches.

Now you need to SORT them. Which ones are external — things that
come from outside the system? Which ones are internal — things
that change because of what's happening inside?

Substrate Concentration, Environmental Temperature, Oxygen Requirements, and Containment Level are external components because they represent conditions that engineers select through deployment decisions (where and how the organism is used) and genetic design choices (containment features). Scaffold Structure is also external as an engineered design parameter. Enzyme Activity Level, Metabolic Pathway Efficiency, Byproduct Toxicity, Organism Growth Rate, pH Tolerance, and Degradation Rate are internal components because they emerge from the organism's biology interacting with environmental conditions — they are consequences of the design, not directly settable parameters.

Sort your components, then hit the PLUS button to add each one
to your model canvas.

You've got your pieces. But right now they're just sitting there,
not connected. In the next activity, we'll draw the invisible
lines that show how everything affects everything else.

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing 10 components sorted: Substrate Concentration, Environmental Temperature, Oxygen Requirements, Containment Level (External), Enzyme Activity Level, Metabolic Pathway Efficiency, Byproduct Toxicity, Organism Growth Rate, pH Tolerance, Degradation Rate (Internal)]

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
• Click on "Substrate Concentration" and drag an arrow to "Degradation Rate"
• Click on "Enzyme Activity Level" and drag an arrow to "Degradation Rate"
• Click on "Environmental Temperature" and drag an arrow to "Enzyme Activity Level"
• Click on "Metabolic Pathway Efficiency" and drag an arrow to "Byproduct Toxicity"
• Click on "Organism Growth Rate" and drag an arrow to "Degradation Rate"
• Click on "Containment Level" and drag an arrow to "Organism Growth Rate"

STEP 3: SET POSITIVE OR NEGATIVE
• Look at the +/− toggle in the TOP LEFT corner
• For each connection, ask: "When this goes UP, does the other go UP or DOWN?"

  ○ Substrate Concentration → Degradation Rate = POSITIVE (+)
    Higher plastic substrate concentration provides more material for the engineered enzyme to process, increasing the overall Degradation Rate up to the enzyme's saturation point.

  ○ Enzyme Activity Level → Degradation Rate = POSITIVE (+)
    More efficient enzymes process more plastic molecules per second, directly increasing the rate at which plastic substrate is converted to breakdown products.

  ○ Environmental Temperature → Enzyme Activity Level = NEGATIVE (−)
    Enzyme activity increases with temperature up to the optimum (30-65°C for most PETase variants) then drops sharply as the enzyme denatures — critical for ocean deployment where temperatures are far below optimum.

  ○ Metabolic Pathway Efficiency → Byproduct Toxicity = NEGATIVE (−)
    More efficient metabolic pathways convert plastic breakdown products completely to harmless end products (CO2, biomass), reducing the accumulation of toxic intermediate compounds.

  ○ Organism Growth Rate → Degradation Rate = POSITIVE (+)
    Faster organism proliferation increases the total enzyme concentration in the environment, amplifying the system-wide Degradation Rate as the microbial population expands.

  ○ Containment Level → Organism Growth Rate = NEGATIVE (−)
    Stronger containment features (kill switches, auxotrophies) impose metabolic costs on the organism and limit its ability to proliferate freely, reducing the population density achievable in the environment.

STEP 4: CHECK YOUR MODEL
• You should have 6 arrows total
• 3 negative relationship(s), 4 positive relationship(s)
• This is your system model!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THINK ABOUT IT: Engineering an organism that eats plastic sounds like a perfect solution — until you consider the complications. Higher Enzyme Activity Level increases Degradation Rate, but it also increases Byproduct Toxicity if the Metabolic Pathway Efficiency isn't high enough to completely process the breakdown products. The organism needs to grow in real-world conditions (variable Environmental Temperature, pH, and Oxygen), not just a controlled lab. And there's the containment paradox: you WANT the organism to spread to where the plastic is, but you DON'T want an engineered organism spreading uncontrollably through natural ecosystems. How do you balance effectiveness with safety?
```

### Video Script

```
"Your pieces are on the board, but they're not talking to each
other yet. Time to draw the invisible lines — the relationships
that make this a SYSTEM, not just a pile of parts.

Click the 'Connect' icon in the top left corner. Now you're in
connection mode.

First connection: Click on 'Substrate Concentration' and drag an arrow
over to 'Degradation Rate.'

Here's the key question: When substrate concentration goes UP, does
degradation rate go UP or DOWN?

Higher plastic substrate concentration provides more material for the engineered enzyme to process, increasing the overall Degradation Rate up to the enzyme's saturation point.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Next connection: Click on 'Enzyme Activity Level' and drag an arrow
over to 'Degradation Rate.'

Here's the key question: When enzyme activity level goes UP, does
degradation rate go UP or DOWN?

More efficient enzymes process more plastic molecules per second, directly increasing the rate at which plastic substrate is converted to breakdown products.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Last connection: Click on 'Environmental Temperature' and drag an arrow
over to 'Enzyme Activity Level.'

Here's the key question: When environmental temperature goes UP, does
enzyme activity level go UP or DOWN?

Enzyme activity increases with temperature up to the optimum (30-65°C for most PETase variants) then drops sharply as the enzyme denatures — critical for ocean deployment where temperatures are far below optimum.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Final connection: Click on 'Metabolic Pathway Efficiency' and drag an arrow
over to 'Byproduct Toxicity.'

Here's the key question: When metabolic pathway efficiency goes UP, does
byproduct toxicity go UP or DOWN?

More efficient metabolic pathways convert plastic breakdown products completely to harmless end products (CO2, biomass), reducing the accumulation of toxic intermediate compounds.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Final connection: Click on 'Organism Growth Rate' and drag an arrow
over to 'Degradation Rate.'

Here's the key question: When organism growth rate goes UP, does
degradation rate go UP or DOWN?

Faster organism proliferation increases the total enzyme concentration in the environment, amplifying the system-wide Degradation Rate as the microbial population expands.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Final connection: Click on 'Containment Level' and drag an arrow
over to 'Organism Growth Rate.'

Here's the key question: When containment level goes UP, does
organism growth rate go UP or DOWN?

Stronger containment features (kill switches, auxotrophies) impose metabolic costs on the organism and limit its ability to proliferate freely, reducing the population density achievable in the environment.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Look at your model now. You've got 3 negative and 4
positive relationships. 6 arrows total.

Engineering an organism that eats plastic sounds like a perfect solution — until you consider the complications. Higher Enzyme Activity Level increases Degradation Rate, but it also increases Byproduct Toxicity if the Metabolic Pathway Efficiency isn't high enough to completely process the breakdown products. The organism needs to grow in real-world conditions (variable Environmental Temperature, pH, and Oxygen), not just a controlled lab. And there's the containment paradox: you WANT the organism to spread to where the plastic is, but you DON'T want an engineered organism spreading uncontrollably through natural ecosystems. How do you balance effectiveness with safety?

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing connected model with arrows: Substrate Concentration +→ Degradation Rate, Enzyme Activity Level +→ Degradation Rate, Environmental Temperature −→ Enzyme Activity Level, Metabolic Pathway Efficiency −→ Byproduct Toxicity, Organism Growth Rate +→ Degradation Rate, Containment Level −→ Organism Growth Rate]

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
• When Substrate Concentration is HIGH, what happens to the internal components?

STEP 3: SCENARIO — CONTROLLED LAB
• Ideal conditions, maximum containment
• PREDICT FIRST: What Degradation Rate do you predict under perfect laboratory conditions with unlimited resources?
• Resume the simulation and observe what happens
• Was your prediction correct?

STEP 4: SCENARIO — OCEAN DEPLOYMENT
• Real ocean conditions, reduced containment
• PREDICT FIRST: How much do you predict real-world ocean conditions reduce Degradation Rate compared to lab performance?
• Resume the simulation and observe what happens
• Was your prediction correct?

STEP 5: SCENARIO — OPTIMIZED FIELD RELEASE
• Balanced performance and safety
• PREDICT FIRST: What do you predict is the maximum achievable Degradation Rate that maintains acceptable Containment Level and Byproduct Toxicity?
• Resume the simulation and observe what happens
• Was your prediction correct?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT DID YOU DISCOVER?
• The gap between laboratory enzyme performance and real-world degradation is enormous — enzymes optimized for lab conditions lose 80-95% of their activity in environmental conditions (cold ocean water, variable pH, limited oxygen)
• Incomplete plastic breakdown can generate toxic intermediates — optimizing enzyme activity without optimizing the complete metabolic pathway can make the pollution problem WORSE by converting plastic into soluble toxins
• The containment-effectiveness paradox is a fundamental challenge — organisms need to spread to where plastic accumulates, but uncontrolled spread of engineered organisms poses ecological risks we cannot fully predict
• Temperature is the critical limiting factor — most plastic-degrading enzymes have evolved or been engineered for warm conditions (30-65°C), but ocean temperatures average 15°C and much plastic accumulates in cold deep-sea environments

THE ANSWER: Engineering organisms to eat plastic is technically achievable but far more complex than it initially appears. The discovery of PETase in Ideonella sakaiensis proved that biology CAN break down synthetic polymers. But the real challenges are environmental: cold ocean temperatures drastically slow enzyme activity; incomplete degradation generates toxic byproducts worse than the original plastic; and deploying self-replicating engineered organisms into open environments creates containment risks we cannot fully assess. Synthetic biology modeling allows researchers to optimize all ten parameters simultaneously — engineering enzymes for cold-tolerance, designing complete metabolic pathways that leave no toxic intermediates, and building biological containment systems that limit environmental spread while maintaining degradation capacity. This is systems-level synthetic design at its most challenging.
```

### Video Script

```
"You've built the machine. You've wired the connections. Now let's
flip the switch and see if your model matches reality.

Click the 'Play' button in the top left. Watch the graph panel —
you'll see lines representing each component as a percentage.

Let it run. Watch how the components interact at baseline levels.
Everything should be balanced, moving together.

First scenario: Controlled Lab. Ideal conditions, maximum containment.
Watch the graph. What do you see happening?

Now let's push the system. Scenario two: Ocean Deployment.
Real ocean conditions, reduced containment.

Before you run it — make a prediction. How much do you predict real-world ocean conditions reduce Degradation Rate compared to lab performance?

Resume the simulation and watch what happens. Did your prediction
match the model? If not, that's actually a GOOD thing — it means
you learned something unexpected.

One more scenario: Optimized Field Release. Balanced performance and safety.
What do you predict is the maximum achievable Degradation Rate that maintains acceptable Containment Level and Byproduct Toxicity?

Here's what our model reveals: Engineering organisms to eat plastic is technically achievable but far more complex than it initially appears. The discovery of PETase in Ideonella sakaiensis proved that biology CAN break down synthetic polymers. But the real challenges are environmental: cold ocean temperatures drastically slow enzyme activity; incomplete degradation generates toxic byproducts worse than the original plastic; and deploying self-replicating engineered organisms into open environments creates containment risks we cannot fully assess. Synthetic biology modeling allows researchers to optimize all ten parameters simultaneously — engineering enzymes for cold-tolerance, designing complete metabolic pathways that leave no toxic intermediates, and building biological containment systems that limit environmental spread while maintaining degradation capacity. This is systems-level synthetic design at its most challenging.

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
   • What happens if you turn OFF Substrate Concentration?
   • What happens if you turn OFF Environmental Temperature?
   • What happens if you turn OFF Oxygen Requirements?
   • What happens if you turn OFF Containment Level?
   • What happens if you change multiple variables at once?
   • Can you find a combination where the system stays stable?

3. WHAT'S MISSING?
   Your model is simple. Real systems involve more. Think about:

   • Biofilm Formation Capacity — The engineered organism's ability to form biofilms on plastic surfaces, which concentrates enzyme activity at the substrate interface and dramatically improves degradation efficiency compared to free-floating organisms
   • Horizontal Gene Transfer Risk — The probability that the engineered genes transfer from the designed organism to wild microbes through natural DNA exchange mechanisms — a containment breach that could create unintended environmental consequences
   • Multi-Plastic Capability — The breadth of plastic types the engineered organism can degrade — PET, polyethylene, polypropylene, polystyrene, and nylon all require different enzymes, and a single organism that handles multiple types would be far more practically useful

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RESEARCH DIRECTIONS:

Don't just guess — find out! Here's what to look for:

📚 IN YOUR TEXTBOOK:
   • The Plastic Pollution Crisis — how does this connect to your model?
   • The PETase Discovery — how does this connect to your model?

🔍 QUESTIONS TO INVESTIGATE:
   • How does your model reveal the gap between laboratory enzyme performance and real-world environmental degradation?
   • What is the containment-effectiveness paradox, and how does your model help navigate it?
   • Why is Metabolic Pathway Efficiency critical for preventing the cure from being worse than the disease?
   • How would adding Biofilm Formation Capacity change the organism's environmental performance?

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

Biofilm Formation Capacity. The engineered organism's ability to form biofilms on plastic surfaces, which concentrates enzyme activity at the substrate interface and dramatically improves degradation efficiency compared to free-floating organisms
How would you model that?

Horizontal Gene Transfer Risk. The probability that the engineered genes transfer from the designed organism to wild microbes through natural DNA exchange mechanisms — a containment breach that could create unintended environmental consequences
How would you model that?

Multi-Plastic Capability. The breadth of plastic types the engineered organism can degrade — PET, polyethylene, polypropylene, polystyrene, and nylon all require different enzymes, and a single organism that handles multiple types would be far more practically useful
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

Synthetic Biologists design and engineer organisms with novel capabilities for applications in medicine, energy, materials, and environmental remediation. They work for biotech companies (Ginkgo Bioworks, Zymergen), environmental engineering firms, and academic research labs, earning $85,000–$170,000/year. Bioremediation Engineers who deploy biological cleanup systems earn $75,000–$140,000/year.

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
Visual: Title slide with dramatic ocean plastic pollution imagery alongside molecular enzyme structures
Say: "Every minute, a garbage truck's worth of plastic enters the ocean. We can't clean it up fast enough with machines. But what if we could engineer a living organism that eats it?"
Do: Show the scale of ocean plastic pollution with a visual comparison. Ask: Why can't we just scoop it all out?
Time: 2 min

SLIDE 2: LEARNING OBJECTIVES
Visual: Learning goals and synthetic biology vocabulary
Say: "Today you're synthetic biologists. Your job is to design a living organism from scratch — one that can do something no natural organism has ever done: break down plastic."
Do: Pre-teach synthetic biology and metabolic engineering. Show the Ideonella sakaiensis discovery story as a 1-minute intro.
Time: 3 min

SLIDE 3: BIG QUESTION
Visual: Can we engineer life to clean up our plastic mess?
Say: "Plastic has only existed for about 70 years. No organism evolved to eat it because it never existed in nature before. But in 2016, scientists found a bacterium in a recycling plant that had EVOLVED to eat PET plastic. What if we could make it better?"
Do: Think-pair-share: Students brainstorm what you'd need to engineer into an organism to make it eat plastic effectively in the ocean. Compile ideas.
Time: 3 min

SLIDE 4: LEVER FRAMEWORK
Visual: LEVER steps with synthetic design context
Say: "We're going to design an organism from the enzyme level up — like programming a biological machine with ten interacting parts. This is synthetic biology in action."
Do: Preview LEVER steps. Emphasize the multi-scale design challenge: molecular (enzymes) → cellular (metabolism) → organism (growth) → environmental (deployment).
Time: 2 min

SLIDE 5: ACTIVITY 1: COMPONENTS
Visual: Ten component cards spanning enzyme, organism, environment, and safety scales
Say: "Four of these ten components are environmental conditions you can choose where to deploy. One is a safety feature you engineer in. Five are biological responses. Sort them."
Do: Guide sorting of external versus internal components. Discuss the containment paradox: you want the organism to spread to plastic but NOT spread everywhere else.
Time: 8 min

SLIDE 6: ACTIVITY 2: CONNECTIONS
Visual: Metabolic pathway from plastic polymer to harmless end products with safety constraints
Say: "Here's the trap: if you optimize the enzyme to chew up plastic faster but the metabolic pathway can't keep up, you convert solid plastic into dissolved toxins. The cure becomes worse than the disease."
Do: Students trace the complete degradation pathway. Identify where incomplete degradation produces toxic intermediates. Map the containment-effectiveness trade-off.
Time: 8 min

SLIDE 7: ACTIVITY 3: SIMULATION
Visual: Performance comparison across lab, ocean, and optimized scenarios
Say: "Run your organism in the lab, then drop it in the ocean. Watch what happens to performance. Then try to redesign it for real-world conditions."
Do: Students predict lab-to-field performance drop, then verify with simulations. Challenge: find the design that works in real ocean conditions while maintaining containment.
Time: 10 min

SLIDE 8: DISCOVERIES
Visual: Key synthetic biology findings and real-world design constraints
Say: "You just learned the first rule of synthetic biology: what works in the lab almost never works in the real world without major redesign. But the gap is shrinking — and your generation might close it."
Do: Connect model findings to the real FAST-PETase breakthrough. Discuss remaining challenges and timelines for real-world deployment.
Time: 5 min

SLIDE 9: STEM CHALLENGE
Visual: Ocean plastic cleanup biological system design challenge
Say: "You have $100 million and the world's best synthetic biology tools. Design the organism — or organism system — that cleans up the Great Pacific Garbage Patch. Go."
Do: Groups design complete biological cleanup systems including organism design, deployment strategy, containment plan, and monitoring system. Present proposals.
Time: 12 min

```

### Teacher Guide

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TEACHER GUIDE: Designing Organisms That Eat Plastic
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LESSON PURPOSE:
This lesson introduces students to synthetic biology and metabolic engineering in the context of plastic bioremediation — one of the most exciting applications of engineered organisms. Biotech skill focus: Synthetic design and systems biology. The discovery of natural plastic-degrading enzymes opened a new frontier in environmental biotechnology, but translating laboratory breakthroughs to real-world solutions requires systems-level synthetic design.

NGSS ALIGNMENT:
HS-LS1-5, HS-ETS1-2: Use a model to illustrate how photosynthesis transforms light energy into stored chemical energy; design a solution to a complex real-world problem by breaking it down into smaller, more manageable problems.

THREE-DIMENSIONAL LEARNING:
• Science Practice: Developing and Using Models / Designing Solutions
  Students develop a synthetic biology model integrating enzyme kinetics, metabolic engineering, and environmental conditions to design an optimized biodegradation system.
• Disciplinary Core Idea: LS1.C Organization for Matter and Energy Flow / ETS1.B Developing Possible Solutions
  Organisms use energy from chemical reactions to build complex molecules and drive cellular processes; engineering solutions require breaking complex problems into manageable sub-problems.
• Crosscutting Concept: Energy and Matter / Systems and System Models
  Students trace matter and energy flow through the engineered metabolic pathway from plastic polymer to harmless end products, modeling the system across molecular, organism, and environmental scales.

PACING GUIDE:
• Activity 1 (Locate): 8-10 minutes
• Activity 2 (Establish): 8-10 minutes
• Activity 3 (Visualize & Evaluate): 10-12 minutes
• Activity 4 (Revise & Extend): 10-15 minutes
• Total: 50-70 minutes (or split across 2 class periods)

PRE-LESSON PREP:
□ Test ModelIt access on student devices
□ Review vocabulary: Synthetic Biology, Metabolic Engineering, PETase, Bioremediation
□ Prepare 8 million tons of plastic enter the ocean every year. Can we engineer a living organism that breaks it down discussion hook
□ Have images or video ready for phenomenon introduction

LEVER FRAMEWORK:
• Locate: Students identify ten components spanning enzyme biochemistry (Enzyme Activity Level), metabolic engineering (Metabolic Pathway Efficiency, Byproduct Toxicity), organism biology (Organism Growth Rate, pH Tolerance), environmental conditions (Substrate Concentration, Environmental Temperature, Oxygen Requirements), and biosafety (Degradation Rate, Containment Level).
• Establish: Students determine that Substrate Concentration, Environmental Temperature, Oxygen Requirements, Scaffold Structure, and Containment Level are the controllable inputs — while Enzyme Activity Level, Metabolic Pathway Efficiency, Byproduct Toxicity, Organism Growth Rate, pH Tolerance, and Degradation Rate emerge as biological responses to the environmental conditions and genetic engineering decisions.
• Visualize: Students build a synthetic biology model connecting enzyme performance to metabolic pathway function to organism-level environmental degradation, visualizing how lab-optimized parameters translate (or fail to translate) to real-world performance.
• Evaluate: Students run controlled-lab, ocean-deployment, and optimized-field-release scenarios to quantify the performance gap between laboratory and environmental conditions and find the design specifications that balance effectiveness with safety.
• Revise: Students add Biofilm Formation Capacity, Horizontal Gene Transfer Risk, or Multi-Plastic Capability to explore more sophisticated and realistic synthetic biology designs.

BACKGROUND CONTENT:
• The Plastic Pollution Crisis:
  Humans have produced approximately 8.3 billion metric tons of plastic since 1950. Of this, only 9% has been recycled, 12% incinerated, and 79% accumulated in landfills or the natural environment. An estimated 8 million tons enter the oceans annually. The Great Pacific Garbage Patch alone contains 80,000 tons across 1.6 million square kilometers. Conventional plastics are synthetic polymers — long chains of repeating chemical units — that no organism evolved to degrade because they didn't exist in nature until the 20th century. PET (polyethylene terephthalate — drink bottles), polyethylene (bags, packaging), polypropylene (food containers), and polystyrene (foam) each have different chemical structures requiring different degradation enzymes. The environmental persistence of these materials ranges from hundreds to thousands of years.

• The PETase Discovery:
  In 2016, researchers at the Kyoto Institute of Technology discovered Ideonella sakaiensis — a bacterium from a Japanese recycling plant that had evolved the ability to break down PET plastic using a novel enzyme called PETase. This was the first confirmed example of a naturally evolved enzyme capable of degrading a synthetic polymer. PETase works by hydrolyzing the ester bonds in PET, producing terephthalic acid and ethylene glycol as breakdown products. A second enzyme, MHETase, completes the degradation of an intermediate compound. However, natural PETase is slow — it takes weeks to significantly degrade a thin plastic film at the enzyme's optimal temperature of 30°C. Protein engineering has created 'supercharged' PETase variants (like FAST-PETase, developed at UT Austin in 2022) that work 5-10x faster and at higher temperatures, but significant challenges remain for real-world deployment.

• Metabolic Engineering for Complete Degradation:
  Breaking PET into terephthalic acid and ethylene glycol is only the first step — the organism must then metabolize these products completely, or they accumulate as pollutants. Complete degradation requires engineering a multi-enzyme metabolic pathway: PETase breaks PET into MHET, MHETase converts MHET to terephthalic acid and ethylene glycol, additional enzymes convert terephthalic acid through protocatechuate to central metabolism (TCA cycle), and ethylene glycol is oxidized to glycolate and enters central metabolism. If any step in this pathway is inefficient, intermediate compounds accumulate — and some of these intermediates (particularly oxidized ethylene glycol derivatives) are more toxic than the original plastic. This is the critical lesson: optimizing one enzyme without optimizing the complete pathway can make the pollution problem worse.

• The Containment Challenge:
  Releasing engineered organisms into the environment is the most controversial aspect of synthetic biology. Containment strategies include: (1) Auxotrophies — engineering the organism to require a synthetic amino acid or nutrient not found in nature, so it dies without laboratory supplementation; (2) Kill switches — genetic circuits that kill the organism in response to environmental signals (temperature change, absence of an inducer chemical); (3) Genetic firewalls — recoding the organism's genetic code so its genes cannot function if transferred to wild microbes; (4) Physical containment — deploying organisms in enclosed bioreactor systems rather than as free-living environmental releases. Each strategy has limitations: kill switches can be mutated, auxotrophies can be bypassed by horizontal gene transfer, and physical containment limits deployment scale. The field of biosafety engineering is dedicated to making containment robust enough for real-world deployment.

COMMON MISCONCEPTIONS:
• "We can just release bacteria into the ocean and the plastic problem is solved"
  Reality: Releasing engineered organisms into the ocean faces enormous challenges the model reveals: cold temperatures slow enzyme activity by 80-95%, nutrient-poor ocean water limits organism growth, UV radiation damages DNA, and the organisms must somehow find and attach to widely dispersed plastic particles. Additionally, the sheer scale of ocean plastic (80,000+ tons in the Pacific alone) would require organism populations of astronomical size. Bioremediation is a tool that complements other approaches — it's not a magic bullet.
  Strategy: Scale it: If each bacterium degrades 1 microgram of plastic per day, how many bacteria would you need to clean up 80,000 tons? (Answer: ~8 × 10^16 — about 80 quadrillion bacteria.)

• "Engineered organisms are inherently dangerous and should never be released"
  Reality: Risk assessment of engineered organisms must be evidence-based, not fear-based. Billions of engineered bacteria are already used safely in industrial fermentation (producing insulin, enzymes, vitamins). The key is containment engineering — multiple redundant safety systems that prevent the organism from surviving outside its intended deployment context. The model's Containment Level component shows that well-designed safety features can dramatically reduce environmental risk while maintaining useful function.
  Strategy: Compare: We release billions of engineered yeast cells into the environment every time we bake bread or brew beer. What's different about releasing an engineered bacterium into the ocean?

• "Plastic is just a chemistry problem — biology is too slow"
  Reality: While chemical recycling can process plastic faster than biological degradation, it requires high temperatures, harsh chemicals, and centralized infrastructure. Biology offers something chemistry cannot: self-replication and self-deployment. An engineered organism can reproduce, spread to plastic-contaminated sites, and adapt to local conditions — potentially providing continuous, self-sustaining cleanup in remote locations where chemical processing infrastructure doesn't exist.
  Strategy: Think about it: Would you rather build a chemical recycling plant on every beach in the world, or deploy an organism that goes where the plastic is?

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
Big Question: 8 million tons of plastic enter the ocean every year. Can we engineer a living organism that breaks it down?
Answer: Engineering organisms to eat plastic is technically achievable but far more complex than it initially appears. The discovery of PETase in Ideonella sakaiensis proved that biology CAN break down synthetic polymers. But the real challenges are environmental: cold ocean temperatures drastically slow enzyme activity; incomplete degradation generates toxic byproducts worse than the original plastic; and deploying self-replicating engineered organisms into open environments creates containment risks we cannot fully assess. Synthetic biology modeling allows researchers to optimize all ten parameters simultaneously — engineering enzymes for cold-tolerance, designing complete metabolic pathways that leave no toxic intermediates, and building biological containment systems that limit environmental spread while maintaining degradation capacity. This is systems-level synthetic design at its most challenging.

Simulation Answers:
• Controlled Lab Scenario: Under ideal laboratory conditions (37°C, optimal pH, high oxygen, high substrate concentration), the engineered organism shows impressive performance. Enzyme Activity Level is high, Metabolic Pathway Efficiency processes breakdown products efficiently, and Byproduct Toxicity remains low. Degradation Rate peaks at the system's theoretical maximum. However, Containment Level is maximum — the organism is fully contained in a bioreactor. This represents the best-case benchmark but not a realistic deployment scenario.
• Ocean Deployment Scenario: When deployed in real ocean conditions (15°C average, pH 8.1, limited oxygen in deeper waters), performance drops dramatically. Enzyme Activity Level decreases by 80-95% because PETase variants are optimized for warm temperatures. Organism Growth Rate is slow in cold, nutrient-poor ocean water. Degradation Rate is a fraction of lab performance. The model starkly reveals why laboratory breakthroughs don't automatically translate to environmental solutions — the gap between lab and field is the central challenge of environmental synthetic biology.

Reflection Exemplars:
• Q: What is the containment-effectiveness paradox?
  A: The model reveals a fundamental tension: containment features (kill switches, nutrient dependencies) reduce the organism's environmental fitness, limiting its ability to grow and degrade plastic in the real world. But WITHOUT containment, an engineered organism could spread uncontrollably, potentially disrupting natural ecosystems in ways we cannot predict. You want the organism to be GOOD ENOUGH at surviving to do its job, but NOT SO GOOD that it outcompetes natural organisms. Finding this balance is the core design challenge of environmental synthetic biology.
• Q: Why can optimizing enzyme activity make the pollution problem worse?
  A: If Enzyme Activity Level is increased without proportionally improving Metabolic Pathway Efficiency, the enzyme breaks plastic into intermediate compounds faster than the cell can metabolize them. These intermediates — particularly oxidized ethylene glycol derivatives and partially hydrolyzed PET oligomers — can be more soluble, mobile, and toxic than the original solid plastic. The model shows that optimizing one step without optimizing the entire pathway converts visible plastic pollution into invisible chemical pollution — potentially worse for marine ecosystems.

STEM CHALLENGE GUIDANCE:
Title: Design a Plastic-Eating Organism for Ocean Cleanup
Mission: Design an engineered biological system that degrades ocean plastic waste at meaningful rates while maintaining rigorous biosafety containment.
Scenario: An environmental biotech company has received a $100 million grant to develop a biological plastic cleanup system for the Great Pacific Garbage Patch. Current mechanical cleanup methods remove only a fraction of the 80,000 tons of plastic accumulated there. Your synthetic biology team must design an organism-based system that can degrade plastic at scale in open ocean conditions while meeting regulatory biosafety requirements.
Introduction: Present the challenge: An environmental biotech company has received a $100 million grant to develop biological plastic cleanup for the Great Pacific Garbage Patch. Mechanical cleanup removes only a fraction of the 80,000 tons accumulated there. Your synthetic biology team must design an organism-based system that degrades plastic at meaningful rates in open ocean conditions while meeting regulatory biosafety requirements.

Key Concepts:
• Chassis Organism Selection: The 'chassis' is the base organism into which new genetic capabilities are engineered. Options include E. coli (well-characterized, easy to engineer, but poor ocean survivor), Vibrio species (native ocean bacteria, salt-tolerant, but less engineering toolkit), and marine fungi (can attach to plastic surfaces, produce diverse enzymes, but slower growing). The choice of chassis determines the environmental performance envelope.
• Genetic Circuit Design: Kill switches, auxotrophies, and containment features are implemented as genetic circuits — DNA-encoded logic gates that respond to environmental signals. A well-designed kill switch might activate cell death when the organism drifts away from the deployment zone (sensing temperature, salinity, or a specific chemical signal from the deployment platform).
• Deployment Platform Engineering: Rather than releasing free-living organisms, some designs use floating platforms or enclosed mesh systems that concentrate organisms near plastic accumulations while providing physical containment. These platforms can also supply nutrients, maintain temperature, and collect degradation byproducts for processing.

Evaluation Rubric:
• Expert (4): Design includes justified chassis selection, complete metabolic pathway, multi-layer containment strategy, deployment platform, monitoring plan, and analysis of environmental risks, supported by model-derived performance predictions
• Proficient (3): Design includes organism engineering, containment strategy, and deployment approach with reasoning connected to model findings
• Developing (2): Design covers basic organism engineering but lacks detail on containment, deployment logistics, or environmental risk assessment
• Beginning (1): Design is incomplete or does not connect organism engineering decisions to the synthetic biology model

DIFFERENTIATION:
Support (Struggling Learners):
  • Provide a simplified metabolic pathway diagram showing PET → MHET → TPA + EG → central metabolism, with toxic intermediates highlighted
  • Use a lab-vs-field performance comparison template where students can predict and then verify the performance gap for each parameter
  • Scaffold synthetic design: 'My organism needs to ___ (function) in ___ (environment), so I will engineer ___ (genetic feature) because ___.'

Extensions (Advanced Learners):
  • Research the FAST-PETase enzyme developed at UT Austin — what engineering modifications made it faster and more thermostable than natural PETase?
  • Investigate the emerging field of plastic-eating fungi (like Pestalotiopsis microspora) and compare fungal versus bacterial approaches to bioremediation
  • Design a closed-loop system where the engineered organism not only degrades plastic but converts the breakdown products into useful chemicals (upcycling) — like converting PET into vanillin (vanilla flavoring)

Cross-Curricular Connections:
  • Math: Calculate enzyme kinetics using Michaelis-Menten equations to predict Degradation Rate as a function of Substrate Concentration and Enzyme Activity Level
  • ELA: Write a regulatory submission document arguing for FDA/EPA approval of an engineered organism for environmental release, addressing safety, efficacy, and containment evidence
  • Environmental Science: Conduct a life cycle analysis comparing biological plastic remediation to mechanical cleanup, chemical recycling, and landfill disposal in terms of energy use, cost, and environmental impact

CAST ALIGNMENT:
• Model the synthetic biology design process from enzyme engineering through metabolic pathway construction to organism-level environmental performance
• Analyze the trade-offs between degradation rate, byproduct toxicity, and containment safety in engineered bioremediation systems
• Evaluate how environmental conditions (temperature, pH, oxygen) limit the translation of laboratory enzyme performance to real-world applications

CAST-Style Assessment Questions:
• Multiple Choice: An engineered plastic-eating bacterium shows excellent degradation in the lab at 37°C but is deployed in ocean water at 15°C. Based on your model, what is the most likely outcome?
• Constructed Response: Using your synthetic biology model, explain why simply engineering a faster enzyme does not solve the ocean plastic problem. Discuss at least three other model components that must be optimized simultaneously and the trade-offs between them.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Activity Pack

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STUDENT ACTIVITY PACK: Designing Organisms That Eat Plastic
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NAME: _________________________ DATE: _____________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRE-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Do you think any living organism can naturally break down plastic — and if not, why not?

   _________________________________________________________

   _________________________________________________________

2. What would you need to change about a bacterium to make it capable of eating plastic?

   _________________________________________________________

   _________________________________________________________

3. Draw a diagram showing how you imagine an engineered plastic-eating organism would work at the molecular level.

   [DRAWING BOX]

4. What risks might come from releasing genetically engineered organisms into the ocean?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VOCABULARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Match the term to the definition:

___ Synthetic Biology             
___ Metabolic Engineering         
___ PETase                        
___ Bioremediation                

A. The engineering discipline that designs and constructs new biological systems — or redesigns existing ones — for useful purposes, using standardized genetic parts (promoters, genes, terminators) assembled like engineering components
B. The targeted modification of an organism's metabolic pathways to enhance production of desired compounds or enable new biochemical capabilities — such as breaking down synthetic polymers that no natural organism evolved to degrade
C. A naturally occurring enzyme discovered in the bacterium Ideonella sakaiensis that can break down PET plastic (polyethylene terephthalate) — the first known enzyme capable of degrading a synthetic polymer, now being engineered for enhanced activity
D. The use of living organisms — bacteria, fungi, plants, or engineered microbes — to clean up environmental pollutants, including oil spills, heavy metals, pesticides, and increasingly, plastic waste

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

SCENARIO: Controlled Lab
Settings: Ideal conditions, maximum containment
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Ocean Deployment
Settings: Real ocean conditions, reduced containment
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Optimized Field Release
Settings: Balanced performance and safety
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

1. How does your model reveal the gap between laboratory enzyme performance and real-world environmental degradation?

   _________________________________________________________

   _________________________________________________________

2. What is the containment-effectiveness paradox, and how does your model help navigate it?

   _________________________________________________________

   _________________________________________________________

3. Why is Metabolic Pathway Efficiency critical for preventing the cure from being worse than the disease?

   _________________________________________________________

   _________________________________________________________

4. How would adding Biofilm Formation Capacity change the organism's environmental performance?

   _________________________________________________________

   _________________________________________________________

5. What ethical responsibilities do synthetic biologists have when designing organisms intended for environmental release?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
POST-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. 8 million tons of plastic enter the ocean every year. Can we engineer a living organism that breaks it down? Explain using evidence from your model:

   _________________________________________________________

   _________________________________________________________

   _________________________________________________________

2. Which NGSS dimensions did this lesson address?
   (Check all that apply)
   □ Science Practice: Developing and Using Models / Designing Solutions
   □ Disciplinary Core Idea: LS1.C Organization for Matter and Energy Flow / ETS1.B Developing Possible Solutions
   □ Crosscutting Concept: Energy and Matter / Systems and System Models

3. What ethical responsibilities do synthetic biologists have when designing organisms intended for environmental release?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEM CHALLENGE: Design a Plastic-Eating Organism for Ocean Cleanup
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MISSION: Design an engineered biological system that degrades ocean plastic waste at meaningful rates while maintaining rigorous biosafety containment.

SCENARIO: An environmental biotech company has received a $100 million grant to develop a biological plastic cleanup system for the Great Pacific Garbage Patch. Current mechanical cleanup methods remove only a fraction of the 80,000 tons of plastic accumulated there. Your synthetic biology team must design an organism-based system that can degrade plastic at scale in open ocean conditions while meeting regulatory biosafety requirements.

GUIDING QUESTIONS:
• What organism chassis would you use as your starting platform — bacteria, fungi, algae — and why?
• How would you engineer the organism to function in cold, salty, low-oxygen ocean conditions?
• What containment strategy would you use to prevent uncontrolled environmental spread?

DESIGN THINKING:
• Would you deploy free-living organisms or attach them to floating degradation platforms?

  _________________________________________________________

• How would you handle the toxic byproducts generated during plastic breakdown?

  _________________________________________________________

• What genetic kill switches or auxotrophies would you engineer for containment?

  _________________________________________________________

• How would you monitor organism spread and degradation progress in the open ocean?

  _________________________________________________________


EVALUATION RUBRIC:
• Expert (4): Design includes justified chassis selection, complete metabolic pathway, multi-layer containment strategy, deployment platform, monitoring plan, and analysis of environmental risks, supported by model-derived performance predictions
• Proficient (3): Design includes organism engineering, containment strategy, and deployment approach with reasoning connected to model findings
• Developing (2): Design covers basic organism engineering but lacks detail on containment, deployment logistics, or environmental risk assessment
• Beginning (1): Design is incomplete or does not connect organism engineering decisions to the synthetic biology model

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Resources

| Resource | Link |
|----------|------|
| Activity Pack (DOCX) | [materials/grade-09/G09L3-L06/G09L3-L06-Student-Activity-Pack.docx] |
| Teacher Guide (DOCX) | [materials/grade-09/G09L3-L06/G09L3-L06-Teachers-Guide.docx] |
| PPT Presentation | [materials/grade-09/G09L3-L06/G09L3-L06-Student-Presentation.pptx] |
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