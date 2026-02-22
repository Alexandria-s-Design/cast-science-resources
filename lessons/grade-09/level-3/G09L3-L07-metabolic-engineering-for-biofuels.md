# Lesson: Metabolic Engineering for Biofuels

## Header Information

| Field | Value |
|-------|-------|
| **Lesson ID** | G09L3-L07 |
| **Grade** | 9th Grade — Level 3: Biotech |
| **Lesson Name** | Metabolic Engineering for Biofuels |
| **Status** | Template |

---

## Platform

### Title
**Metabolic Engineering for Biofuels — Pathway Optimization and Flux Balancing in Microbial Fuel Production**

### Overview
This lesson introduces students to metabolic engineering — the systematic design and optimization of cellular metabolic pathways for industrial production. Biotech skill focus: Pathway flux balancing and multi-variable optimization. The global energy crisis demands alternatives to fossil fuels, and engineered microorganisms represent one of the most promising routes to sustainable liquid fuels. Students investigate the driving question: We burn 100 million barrels of oil every day. Can we engineer microbes to brew fuel instead of drilling for it — and can we make it economically competitive? Using the LEVER framework, students identify key components, establish cause-and-effect relationships, run simulations to test scenarios, and extend their understanding through research and engineering challenges.

### Cover Image
[A photorealistic, cinematic image of diverse 14-15 year old students in an advanced biotech fermentation lab examining bioreactor vessels with fluorescent-green cultures, metabolic pathway diagrams and flux analysis charts on screens, warm industrial lighting with steel and glass equipment]

### Grade
9th Grade — Level 3: Biotech

### NGSS Standard
**HS-LS1-5, HS-ETS1-3**: Use a model to illustrate how photosynthesis transforms light energy into stored chemical energy; optimize the design of a solution to a complex real-world problem by considering trade-offs among criteria and constraints.

### Learning Objectives
- Build a metabolic engineering model that traces carbon flux from substrate input through engineered enzymatic pathways to biofuel product output
- Analyze how substrate concentration, enzyme kinetics, cofactor recycling, and metabolic burden interact to determine overall pathway efficiency
- Optimize pathway flux and fermentation conditions to maximize product yield while maintaining cell viability and growth
- Evaluate the economic and environmental trade-offs between fossil fuel extraction and engineered biofuel production

### Component List (Starting Model: 9 Components)

| Component | Type | What It Represents |
|-----------|------|-------------------|
| Substrate Concentration | External | The amount of fermentable carbon source (glucose, xylose, glycerol, or lignocellulosic hydrolysate) available to the engineered microbe — the raw material input that feeds the entire metabolic pathway |
| Enzyme Activity | Internal | The catalytic efficiency of the key engineered pathway enzymes, determined by protein expression level, folding efficiency, and kinetic parameters (kcat and Km) — the molecular machines that perform each conversion step |
| Pathway Flux | Internal | The overall rate of carbon flow through the engineered biofuel pathway from substrate to product, measured in mmol per gram dry cell weight per hour — limited by the slowest enzymatic step (the bottleneck) |
| Cofactor Availability | Internal | The intracellular pool of essential cofactors (NADH, NADPH, ATP, CoA) available to support pathway enzyme reactions — cofactor imbalance is one of the most common reasons engineered pathways fail in practice |
| Metabolic Burden | Internal | The total resource cost the cell pays for expressing the engineered pathway — measured as the fraction of cellular protein synthesis, ATP production, and precursor metabolites diverted from native functions to foreign pathway enzymes |
| Cell Growth Rate | Internal | The doubling time of the engineered microbial population during fermentation — faster growth increases total bioreactor productivity but competes with product formation for cellular resources |
| Product Yield | Internal | The mass of biofuel produced per mass of substrate consumed — expressed as a percentage of the theoretical maximum yield, which is set by the stoichiometry of the biochemical conversion |
| Byproduct Accumulation | Internal | The buildup of unwanted metabolic side products (acetate, lactate, ethanol in non-ethanol pathways, organic acids) that divert carbon away from the desired product and can inhibit cell growth at high concentrations |
| Fermentation Efficiency | Internal | The overall process performance integrating Product Yield, volumetric productivity (grams per liter per hour), and final titer — the composite metric that determines whether the biofuel is economically competitive with petroleum |

### Research for Lesson
- The Energy Challenge and Biofuels — reference materials and textbook resources
- Metabolic Pathway Design — reference materials and textbook resources
- The Metabolic Burden Problem — reference materials and textbook resources
- From Laboratory to Industrial Scale — reference materials and textbook resources

---

## Activity 1: LOCATE — Build Your System

### Text Editor

```
METABOLIC ENGINEERING FOR BIOFUELS

Pathway Optimization and Flux Balancing in Microbial Fuel Production.
We burn 100 million barrels of oil every day. Can we engineer microbes to brew fuel instead of drilling for it — and can we make it economically competitive?

That's not just a question — it's something you can MODEL.
And you're about to build exactly that.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1: CHOOSE YOUR COMPONENTS
• Look at the component panel on the RIGHT side of your screen
• Find the EXTERNAL components (things we can't control):
  ○ Click "Substrate Concentration" — the amount of fermentable carbon source (glucose
• Find the INTERNAL components (things that change because of other things):
  ○ Click "Enzyme Activity" — the catalytic efficiency of the key engineered pathway enzymes
  ○ Click "Pathway Flux" — the overall rate of carbon flow through the engineered biofuel pathway from substrate to product
  ○ Click "Cofactor Availability" — the intracellular pool of essential cofactors (nadh
  ○ Click "Metabolic Burden" — the total resource cost the cell pays for expressing the engineered pathway — measured as the fraction of cellular protein synthesis
  ○ Click "Cell Growth Rate" — the doubling time of the engineered microbial population during fermentation — faster growth increases total bioreactor productivity but competes with product formation for cellular resources
  ○ Click "Product Yield" — the mass of biofuel produced per mass of substrate consumed — expressed as a percentage of the theoretical maximum yield
  ○ Click "Byproduct Accumulation" — the buildup of unwanted metabolic side products (acetate
  ○ Click "Fermentation Efficiency" — the overall process performance integrating product yield

STEP 2: ADD TO YOUR MODEL
• Click the PLUS (+) button to add each component to your picture
• You should now see 9 components on your canvas

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
"We burn 100 million barrels of oil every day. Can we engineer microbes to brew fuel instead of drilling for it — and can we make it economically competitive?

That's what we're going to figure out today. Not by reading about
it — by MODELING it. You're going to build a system that shows
exactly how this works.

Let's build our system. Look at the component panel on the right
side of your screen. You'll see two types of components:

EXTERNAL components — things that come from outside the system.
Inputs we can't directly control.

INTERNAL components — things that change BECAUSE of other things
in the system. They respond to the externals.

Click on 'Substrate Concentration' — that's external. The amount of fermentable carbon source (glucose.
Click on 'Enzyme Activity' — that's internal. The catalytic efficiency of the key engineered pathway enzymes.
Click on 'Pathway Flux' — that's internal. The overall rate of carbon flow through the engineered biofuel pathway from substrate to product.
Click on 'Cofactor Availability' — that's internal. The intracellular pool of essential cofactors (NADH.
Click on 'Metabolic Burden' — that's internal. The total resource cost the cell pays for expressing the engineered pathway — measured as the fraction of cellular protein synthesis.
Click on 'Cell Growth Rate' — that's internal. The doubling time of the engineered microbial population during fermentation — faster growth increases total bioreactor productivity but competes with product formation for cellular resources.
Click on 'Product Yield' — that's internal. The mass of biofuel produced per mass of substrate consumed — expressed as a percentage of the theoretical maximum yield.
Click on 'Byproduct Accumulation' — that's internal. The buildup of unwanted metabolic side products (acetate.
Click on 'Fermentation Efficiency' — that's internal. The overall process performance integrating Product Yield.

Now you need to SORT them. Which ones are external — things that
come from outside the system? Which ones are internal — things
that change because of what's happening inside?

Substrate Concentration is the primary external component because it represents the amount of carbon feedstock supplied to the fermentation — a process parameter fully under the engineer's control. All other eight components are internal: Enzyme Activity is partially controllable through genetic engineering but ultimately constrained by the cell's protein synthesis capacity and Metabolic Burden. Pathway Flux, Cofactor Availability, Cell Growth Rate, Product Yield, Byproduct Accumulation, and Fermentation Efficiency are emergent properties of the biological system responding to substrate input and genetic modifications.

Sort your components, then hit the PLUS button to add each one
to your model canvas.

You've got your pieces. But right now they're just sitting there,
not connected. In the next activity, we'll draw the invisible
lines that show how everything affects everything else.

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing 9 components sorted: Substrate Concentration (External), Enzyme Activity, Pathway Flux, Cofactor Availability, Metabolic Burden, Cell Growth Rate, Product Yield, Byproduct Accumulation, Fermentation Efficiency (Internal)]

### Graph
[Empty graph panel — no simulation yet]

---

## Activity 2: ESTABLISH — Connect the Relationships

### Text Editor

```
TIME TO DRAW THE INVISIBLE LINES

Those 9 components don't just sit there — they AFFECT each other.
When one changes, others change too. Let's map those connections.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1: OPEN CONNECTION MODE
• Click the "Connect" icon in the TOP LEFT corner of your screen
• Your cursor is now ready to draw relationship arrows

STEP 2: DRAW YOUR RELATIONSHIPS
• Click on "Substrate Concentration" and drag an arrow to "Pathway Flux"
• Click on "Enzyme Activity" and drag an arrow to "Pathway Flux"
• Click on "Enzyme Activity" and drag an arrow to "Metabolic Burden"
• Click on "Metabolic Burden" and drag an arrow to "Cell Growth Rate"
• Click on "Pathway Flux" and drag an arrow to "Cofactor Availability"
• Click on "Pathway Flux" and drag an arrow to "Product Yield"

STEP 3: SET POSITIVE OR NEGATIVE
• Look at the +/− toggle in the TOP LEFT corner
• For each connection, ask: "When this goes UP, does the other go UP or DOWN?"

  ○ Substrate Concentration → Pathway Flux = POSITIVE (+)
    Higher substrate concentration provides more carbon molecules to enter the engineered pathway, increasing flux through the first enzymatic step up to the enzyme's saturation point.

  ○ Enzyme Activity → Pathway Flux = POSITIVE (+)
    More active pathway enzymes process intermediates faster, increasing the overall flux of carbon through the pathway toward the desired biofuel product.

  ○ Enzyme Activity → Metabolic Burden = POSITIVE (+)
    Higher enzyme expression diverts more cellular resources (ribosomes, amino acids, ATP) from growth to foreign protein production, increasing the fitness cost on the cell.

  ○ Metabolic Burden → Cell Growth Rate = NEGATIVE (−)
    Greater metabolic burden slows cell division by depleting resources needed for DNA replication, membrane synthesis, and essential protein production.

  ○ Pathway Flux → Cofactor Availability = NEGATIVE (−)
    Faster pathway flux consumes cofactors (NADH, NADPH, ATP) more rapidly, depleting intracellular pools and potentially stalling the pathway and other essential cellular processes.

  ○ Pathway Flux → Product Yield = POSITIVE (+)
    Higher pathway flux directs more carbon atoms toward the desired biofuel product rather than allowing them to be diverted to competing metabolic routes or byproducts.

STEP 4: CHECK YOUR MODEL
• You should have 6 arrows total
• 2 negative relationship(s), 4 positive relationship(s)
• This is your system model!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THINK ABOUT IT: Here's the central paradox of metabolic engineering: you want the cell to be a biofuel factory, but the cell wants to be a cell. Every enzyme you add to the biofuel pathway steals resources (ribosomes, ATP, amino acids) from the cell's own growth and maintenance — that's Metabolic Burden. Push the pathway too hard and Cell Growth Rate crashes, meaning fewer cells producing less total product. But push too gently and Product Yield is low because the cell diverts carbon to Byproduct Accumulation and biomass instead. Meanwhile, Cofactor Availability can collapse if the pathway consumes NADH or ATP faster than the cell regenerates them. How do you balance a factory that doesn't want to be a factory?
```

### Video Script

```
"Your pieces are on the board, but they're not talking to each
other yet. Time to draw the invisible lines — the relationships
that make this a SYSTEM, not just a pile of parts.

Click the 'Connect' icon in the top left corner. Now you're in
connection mode.

First connection: Click on 'Substrate Concentration' and drag an arrow
over to 'Pathway Flux.'

Here's the key question: When substrate concentration goes UP, does
pathway flux go UP or DOWN?

Higher substrate concentration provides more carbon molecules to enter the engineered pathway, increasing flux through the first enzymatic step up to the enzyme's saturation point.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Next connection: Click on 'Enzyme Activity' and drag an arrow
over to 'Pathway Flux.'

Here's the key question: When enzyme activity goes UP, does
pathway flux go UP or DOWN?

More active pathway enzymes process intermediates faster, increasing the overall flux of carbon through the pathway toward the desired biofuel product.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Last connection: Click on 'Enzyme Activity' and drag an arrow
over to 'Metabolic Burden.'

Here's the key question: When enzyme activity goes UP, does
metabolic burden go UP or DOWN?

Higher enzyme expression diverts more cellular resources (ribosomes, amino acids, ATP) from growth to foreign protein production, increasing the fitness cost on the cell.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Final connection: Click on 'Metabolic Burden' and drag an arrow
over to 'Cell Growth Rate.'

Here's the key question: When metabolic burden goes UP, does
cell growth rate go UP or DOWN?

Greater metabolic burden slows cell division by depleting resources needed for DNA replication, membrane synthesis, and essential protein production.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Final connection: Click on 'Pathway Flux' and drag an arrow
over to 'Cofactor Availability.'

Here's the key question: When pathway flux goes UP, does
cofactor availability go UP or DOWN?

Faster pathway flux consumes cofactors (NADH, NADPH, ATP) more rapidly, depleting intracellular pools and potentially stalling the pathway and other essential cellular processes.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Final connection: Click on 'Pathway Flux' and drag an arrow
over to 'Product Yield.'

Here's the key question: When pathway flux goes UP, does
product yield go UP or DOWN?

Higher pathway flux directs more carbon atoms toward the desired biofuel product rather than allowing them to be diverted to competing metabolic routes or byproducts.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Look at your model now. You've got 2 negative and 4
positive relationships. 6 arrows total.

Here's the central paradox of metabolic engineering: you want the cell to be a biofuel factory, but the cell wants to be a cell. Every enzyme you add to the biofuel pathway steals resources (ribosomes, ATP, amino acids) from the cell's own growth and maintenance — that's Metabolic Burden. Push the pathway too hard and Cell Growth Rate crashes, meaning fewer cells producing less total product. But push too gently and Product Yield is low because the cell diverts carbon to Byproduct Accumulation and biomass instead. Meanwhile, Cofactor Availability can collapse if the pathway consumes NADH or ATP faster than the cell regenerates them. How do you balance a factory that doesn't want to be a factory?

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing connected model with arrows: Substrate Concentration +→ Pathway Flux, Enzyme Activity +→ Pathway Flux, Enzyme Activity +→ Metabolic Burden, Metabolic Burden −→ Cell Growth Rate, Pathway Flux −→ Cofactor Availability, Pathway Flux +→ Product Yield]

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

STEP 3: SCENARIO — BASELINE FERMENTATION
• Standard substrate, moderate enzyme expression
• PREDICT FIRST: What do you predict the ratio of Product Yield to Byproduct Accumulation will be without pathway optimization?
• Resume the simulation and observe what happens
• Was your prediction correct?

STEP 4: SCENARIO — MAXIMUM EXPRESSION
• All pathway enzymes at maximum expression
• PREDICT FIRST: What do you predict happens to Cell Growth Rate when every ribosome in the cell is making pathway enzymes instead of growth-essential proteins?
• Resume the simulation and observe what happens
• Was your prediction correct?

STEP 5: SCENARIO — BALANCED OPTIMIZATION
• Tuned expression with cofactor engineering
• PREDICT FIRST: Do you predict that reducing enzyme expression from maximum can actually INCREASE total Fermentation Efficiency?
• Resume the simulation and observe what happens
• Was your prediction correct?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT DID YOU DISCOVER?
• Maximum enzyme expression does NOT produce maximum product yield — excessive Metabolic Burden crashes Cell Growth Rate, resulting in fewer cells and lower total productivity than a moderately-expressed pathway
• Cofactor imbalance is a silent killer of engineered pathways — a pathway that looks perfect on paper fails in practice because it consumes NADH faster than the cell can regenerate it from central metabolism
• Byproduct accumulation is both a carbon sink and a toxin — acetate and organic acid byproducts divert 15-40% of substrate carbon while simultaneously inhibiting cell growth at concentrations above 5-10 g/L
• The economic breakeven for microbial biofuel production requires achieving at least 85% of theoretical maximum yield at titers above 50 g/L — most laboratory strains achieve 30-60% of maximum yield at 10-20 g/L, highlighting the engineering gap

THE ANSWER: Engineering microbes to produce biofuels is a metabolic tug-of-war between what the engineer wants (maximum fuel production) and what the cell needs (growth, maintenance, and survival). The nine components of this model capture the fundamental trade-offs: Substrate Concentration feeds carbon into the system, but Enzyme Activity must be precisely balanced to maintain Pathway Flux without overwhelming the cell with Metabolic Burden. Cofactor Availability acts as a hidden constraint — if the pathway drains NAD+, NADPH, or ATP faster than the cell regenerates them, flux stalls regardless of enzyme levels. Cell Growth Rate competes directly with Product Yield for the same carbon and energy. Byproduct Accumulation represents both lost carbon and metabolic toxicity. Fermentation Efficiency — the composite metric that determines commercial viability — requires simultaneously optimizing all eight upstream components. This is why metabolic engineering is sometimes called 'the art of compromise' — the best biofuel strain is never the one with the most enzyme, but the one with the most balanced metabolism.
```

### Video Script

```
"You've built the machine. You've wired the connections. Now let's
flip the switch and see if your model matches reality.

Click the 'Play' button in the top left. Watch the graph panel —
you'll see lines representing each component as a percentage.

Let it run. Watch how the components interact at baseline levels.
Everything should be balanced, moving together.

First scenario: Baseline Fermentation. Standard substrate, moderate enzyme expression.
Watch the graph. What do you see happening?

Now let's push the system. Scenario two: Maximum Expression.
All pathway enzymes at maximum expression.

Before you run it — make a prediction. What do you predict happens to Cell Growth Rate when every ribosome in the cell is making pathway enzymes instead of growth-essential proteins?

Resume the simulation and watch what happens. Did your prediction
match the model? If not, that's actually a GOOD thing — it means
you learned something unexpected.

One more scenario: Balanced Optimization. Tuned expression with cofactor engineering.
Do you predict that reducing enzyme expression from maximum can actually INCREASE total Fermentation Efficiency?

Here's what our model reveals: Engineering microbes to produce biofuels is a metabolic tug-of-war between what the engineer wants (maximum fuel production) and what the cell needs (growth, maintenance, and survival). The nine components of this model capture the fundamental trade-offs: Substrate Concentration feeds carbon into the system, but Enzyme Activity must be precisely balanced to maintain Pathway Flux without overwhelming the cell with Metabolic Burden. Cofactor Availability acts as a hidden constraint — if the pathway drains NAD+, NADPH, or ATP faster than the cell regenerates them, flux stalls regardless of enzyme levels. Cell Growth Rate competes directly with Product Yield for the same carbon and energy. Byproduct Accumulation represents both lost carbon and metabolic toxicity. Fermentation Efficiency — the composite metric that determines commercial viability — requires simultaneously optimizing all eight upstream components. This is why metabolic engineering is sometimes called 'the art of compromise' — the best biofuel strain is never the one with the most enzyme, but the one with the most balanced metabolism.

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
   • What happens if you change multiple variables at once?
   • Can you find a combination where the system stays stable?

3. WHAT'S MISSING?
   Your model is simple. Real systems involve more. Think about:

   • Product Toxicity Threshold — The concentration of biofuel product at which it begins to damage the producing cell's membrane and proteins — ethanol tolerance in yeast is 12-15% while butanol kills most bacteria above 2%, making product toxicity one of the most critical limitations in biofuel fermentation
   • Feedstock Flexibility — The range of carbon substrates the engineered organism can utilize — strains that can co-ferment glucose AND xylose from lignocellulosic biomass access 40% more available carbon than glucose-only strains, dramatically improving process economics
   • Genetic Stability Index — The probability that the engineered production pathway maintains full function over extended fermentation runs — cells under high Metabolic Burden face selective pressure to mutate and inactivate costly pathway enzymes, causing production to decline over time

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RESEARCH DIRECTIONS:

Don't just guess — find out! Here's what to look for:

📚 IN YOUR TEXTBOOK:
   • The Energy Challenge and Biofuels — how does this connect to your model?
   • Metabolic Pathway Design — how does this connect to your model?

🔍 QUESTIONS TO INVESTIGATE:
   • How does your model demonstrate the fundamental trade-off between Cell Growth Rate and Product Yield — and why can't you simply maximize both?
   • Why is Cofactor Availability often called the 'silent killer' of engineered metabolic pathways?
   • What did you learn about the relationship between Enzyme Activity levels and Metabolic Burden — why doesn't 'more enzyme' always mean 'more product'?
   • How would adding Product Toxicity Threshold change your optimization strategy for Fermentation Efficiency?

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

Your model has 9 components. Real systems involve
way more. Think about...

Product Toxicity Threshold. The concentration of biofuel product at which it begins to damage the producing cell's membrane and proteins — ethanol tolerance in yeast is 12-15% while butanol kills most bacteria above 2%, making product toxicity one of the most critical limitations in biofuel fermentation
How would you model that?

Feedstock Flexibility. The range of carbon substrates the engineered organism can utilize — strains that can co-ferment glucose AND xylose from lignocellulosic biomass access 40% more available carbon than glucose-only strains, dramatically improving process economics
How would you model that?

Genetic Stability Index. The probability that the engineered production pathway maintains full function over extended fermentation runs — cells under high Metabolic Burden face selective pressure to mutate and inactivate costly pathway enzymes, causing production to decline over time
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

Metabolic Engineers design and optimize microbial production pathways for fuels, chemicals, and pharmaceuticals. They work for biotech companies (Amyris, Ginkgo Bioworks, LanzaTech, Genomatica), renewable energy startups, and national laboratories, earning $90,000-$175,000/year. Fermentation Scientists who scale up lab strains to industrial production earn $80,000-$150,000/year.

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
Visual: Title slide with dramatic imagery of bioreactors alongside petroleum refineries
Say: "We burn 100 million barrels of oil every day. What if, instead of drilling it out of the ground, we could brew it in a vat — using engineered microbes that convert sugar into fuel? That's metabolic engineering."
Do: Display the scale comparison: barrels of oil consumed daily versus current biofuel production. Let the gap sink in.
Time: 2 min

SLIDE 2: LEARNING OBJECTIVES
Visual: Learning goals and metabolic engineering vocabulary
Say: "Today you're metabolic engineers. You're going to design a microbial fuel factory — and discover why the biggest challenge isn't the chemistry, it's the biology."
Do: Pre-teach metabolic flux and cofactor recycling. Use the analogy: a factory assembly line where every worker needs specific tools (cofactors) to do their job.
Time: 3 min

SLIDE 3: BIG QUESTION
Visual: Can engineered microbes replace petroleum?
Say: "Yeast has been converting sugar to ethanol for 10,000 years — that's beer and wine. But ethanol is a lousy fuel. What if we could redirect that metabolism to make jet fuel, diesel, or gasoline — drop-in replacements?"
Do: Think-pair-share: Why is ethanol a poor fuel compared to gasoline? (Energy density, water miscibility, corrosion.) What properties would an ideal biofuel have?
Time: 3 min

SLIDE 4: LEVER FRAMEWORK
Visual: LEVER steps with metabolic engineering context
Say: "We're going to trace carbon from a sugar molecule all the way through an engineered metabolic pathway to a fuel molecule. Every step has constraints, trade-offs, and potential failure points."
Do: Preview LEVER steps. Emphasize: this model captures the fundamental tension between making the cell a factory and keeping the cell alive.
Time: 2 min

SLIDE 5: ACTIVITY 1: COMPONENTS
Visual: Nine component cards spanning molecular, cellular, and process scales
Say: "Only ONE of these nine components is something the engineer fully controls from outside. The rest are biological responses. Which one?"
Do: Guide identification of Substrate Concentration as the primary external input. Discuss how Enzyme Activity is partially controllable through genetic engineering but constrained by Metabolic Burden.
Time: 8 min

SLIDE 6: ACTIVITY 2: CONNECTIONS
Visual: Metabolic flux map from substrate through pathway to product with competing drains
Say: "Here's the problem: every carbon atom that enters the cell has three possible fates — it becomes fuel (what you want), biomass (what the cell wants), or byproduct (what neither of you wants). Trace the competition."
Do: Students map carbon flow from Substrate through Pathway Flux to the three-way split: Product Yield, Cell Growth Rate (biomass), and Byproduct Accumulation. Identify Cofactor Availability as the hidden constraint.
Time: 8 min

SLIDE 7: ACTIVITY 3: SIMULATION
Visual: Fermentation performance dashboards comparing three scenarios
Say: "Run scenario 2 first — maximum enzyme expression. Watch what happens. Then figure out why 'more enzyme' made things WORSE. Then design the fix."
Do: Students predict, then simulate. The counter-intuitive result — maximum expression crashes growth and total production — drives the key insight about Metabolic Burden. Challenge them to find the optimal balance.
Time: 10 min

SLIDE 8: DISCOVERIES
Visual: Key metabolic engineering insights and industrial benchmark data
Say: "You just discovered the first law of metabolic engineering: the cell is not a beaker. It's a living system with its own agenda, and you have to negotiate with it, not dictate to it."
Do: Connect findings to real industrial data. Show the gap between lab yields and commercial targets. Discuss what it takes to close that gap.
Time: 5 min

SLIDE 9: STEM CHALLENGE
Visual: Biofuel strain and process design challenge
Say: "A startup just gave your team $50 million. Design the strain, the pathway, and the fermentation process that makes jet fuel at $0.60 per liter. Can you compete with petroleum?"
Do: Groups design complete biofuel production systems: host organism selection, pathway engineering strategy, fermentation process, and economic analysis. Present and defend designs.
Time: 12 min

```

### Teacher Guide

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TEACHER GUIDE: Metabolic Engineering for Biofuels
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LESSON PURPOSE:
This lesson introduces students to metabolic engineering — the systematic design and optimization of cellular metabolic pathways for industrial production. Biotech skill focus: Pathway flux balancing and multi-variable optimization. The global energy crisis demands alternatives to fossil fuels, and engineered microorganisms represent one of the most promising routes to sustainable liquid fuels.

NGSS ALIGNMENT:
HS-LS1-5, HS-ETS1-3: Use a model to illustrate how photosynthesis transforms light energy into stored chemical energy; optimize the design of a solution to a complex real-world problem by considering trade-offs among criteria and constraints.

THREE-DIMENSIONAL LEARNING:
• Science Practice: Developing and Using Models / Using Mathematics and Computational Thinking
  Students develop a metabolic flux model integrating enzyme kinetics, cofactor balance, and growth-production trade-offs, using quantitative analysis to optimize pathway performance.
• Disciplinary Core Idea: LS1.C Organization for Matter and Energy Flow / ETS1.C Optimizing the Design Solution
  Matter and energy flow through metabolic pathways following conservation laws; engineering design requires iterative optimization of multiple competing criteria and constraints.
• Crosscutting Concept: Energy and Matter / Stability and Change
  Students trace carbon and energy flow from substrate through metabolic pathways to product, analyzing how perturbations in one pathway component cascade through the system to affect overall stability and output.

PACING GUIDE:
• Activity 1 (Locate): 8-10 minutes
• Activity 2 (Establish): 8-10 minutes
• Activity 3 (Visualize & Evaluate): 10-12 minutes
• Activity 4 (Revise & Extend): 10-15 minutes
• Total: 50-70 minutes (or split across 2 class periods)

PRE-LESSON PREP:
□ Test ModelIt access on student devices
□ Review vocabulary: Metabolic Flux, Cofactor Recycling, Metabolic Burden, Fermentation Titer
□ Prepare We burn 100 million barrels of oil every day. Can we engineer microbes to brew fuel instead of drilling for it — and can we make it economically competitive discussion hook
□ Have images or video ready for phenomenon introduction

LEVER FRAMEWORK:
• Locate: Students identify nine components spanning substrate input (Substrate Concentration), enzyme-level function (Enzyme Activity), pathway-level dynamics (Pathway Flux, Cofactor Availability), cell-level constraints (Metabolic Burden, Cell Growth Rate), and process-level outcomes (Product Yield, Byproduct Accumulation, Fermentation Efficiency).
• Establish: Students determine that Substrate Concentration is the primary external input, while Enzyme Activity, Pathway Flux, Cofactor Availability, Metabolic Burden, Cell Growth Rate, Product Yield, Byproduct Accumulation, and Fermentation Efficiency emerge as interconnected internal responses — recognizing that Enzyme Activity is partially controllable through genetic engineering but ultimately constrained by cellular resources.
• Visualize: Students build a metabolic flux model connecting substrate input through enzymatic conversion steps to product output, visualizing how carbon flows partition between desired product, biomass, and unwanted byproducts.
• Evaluate: Students run baseline, maximum-expression, and balanced-optimization scenarios to discover that maximum enzyme expression does not produce maximum Fermentation Efficiency due to Metabolic Burden effects.
• Revise: Students add Product Toxicity Threshold, Feedstock Flexibility, or Genetic Stability Index to explore more realistic industrial constraints on microbial biofuel production.

BACKGROUND CONTENT:
• The Energy Challenge and Biofuels:
  Global civilization consumes approximately 100 million barrels of crude oil per day — roughly 15.9 billion liters. Transportation fuels (gasoline, diesel, jet fuel) account for about 60% of this consumption. First-generation biofuels (corn ethanol, biodiesel from vegetable oil) have demonstrated the concept of biological fuel production but face fundamental limitations: they compete with food production for agricultural land, their energy return on investment (EROI) is marginal (1.3:1 for corn ethanol versus 15:1 for conventional oil), and ethanol has only 67% the energy density of gasoline. Advanced biofuels — produced by engineered microorganisms from non-food feedstocks like agricultural waste, forestry residues, or CO2 — could overcome these limitations if metabolic engineering can close the gap between laboratory yields and commercial requirements.

• Metabolic Pathway Design:
  Engineering a microbial biofuel pathway involves three fundamental challenges. First, pathway selection: choosing the biochemical route from substrate to product. For example, fatty acid-derived biodiesel requires a pathway from glucose through acetyl-CoA to fatty acid synthesis to ester formation — a 12+ enzyme cascade. Butanol production through the Clostridial ABE pathway requires 7 enzymes. Each route has a different theoretical maximum yield set by biochemical stoichiometry and thermodynamics. Second, enzyme balancing: each enzyme in the pathway must be expressed at the right level. Too little of the bottleneck enzyme limits flux; too much of any enzyme wastes cellular resources. Third, cofactor engineering: most biosynthetic pathways consume reducing equivalents (NADH or NADPH) and ATP. If the pathway drains these cofactors faster than central metabolism regenerates them, flux stalls regardless of enzyme levels.

• The Metabolic Burden Problem:
  Every protein a cell makes costs resources: ribosomes to translate the mRNA, amino acids to build the protein, ATP to fold it, and chaperones to maintain it. When metabolic engineers introduce 5-15 foreign enzymes at high expression levels, the total protein production burden can consume 20-40% of the cell's biosynthetic capacity. This 'metabolic burden' manifests as slower growth, reduced stress tolerance, and paradoxically lower product yield because the cell cannot maintain healthy metabolism while running the production pathway at full capacity. The solution is dynamic pathway regulation — genetic circuits that sense the cell's metabolic state and adjust enzyme expression in real time, similar to how natural metabolic regulation works. Strategies include growth-coupled production (linking product formation to essential metabolic pathways so cells cannot grow without producing), quorum sensing-based induction (delaying pathway activation until cell density is high), and stress-responsive promoters.

• From Laboratory to Industrial Scale:
  The gap between laboratory biofuel production and commercial viability is measured in three metrics: yield (grams of product per gram of substrate — must be above 85% of theoretical maximum), titer (final product concentration — must exceed 50 g/L for economical downstream processing), and productivity (grams per liter per hour — determines bioreactor capital costs). Most laboratory strains achieve 30-60% of theoretical yield at titers of 10-20 g/L, well below commercial requirements. Scale-up introduces additional challenges: oxygen transfer limitations in large bioreactors (which can be 200,000+ liters), contamination risks during multi-day fermentations, the cost of sterilizing and cooling large volumes, and genetic stability over hundreds of generations. Companies like Amyris, LanzaTech, and Genomatica have spent over a decade and billions of dollars bridging this gap for specific products.

COMMON MISCONCEPTIONS:
• "More enzyme expression always means more product"
  Reality: This is the most common and most dangerous misconception in metabolic engineering. The model clearly demonstrates that increasing Enzyme Activity beyond a critical threshold DECREASES total product output because Metabolic Burden crashes Cell Growth Rate. Fewer, sicker cells produce less total product than a moderate number of healthy cells expressing enzymes at balanced levels. The relationship between enzyme expression and product yield is a curve with a peak — and the peak is almost never at maximum expression.
  Strategy: Model it: Increase Enzyme Activity from moderate to maximum and watch Cell Growth Rate, total cell count, and cumulative Product Yield. The total yield curve rises, peaks, then falls — maximum enzyme is past the peak.

• "Biofuels are automatically carbon-neutral because they come from plants"
  Reality: The carbon accounting for biofuels is far more complex than 'plants absorb CO2, we burn biofuel, CO2 goes back to plants.' A full life cycle analysis must include: fossil energy used to grow and harvest the feedstock (tractors, fertilizer from natural gas, irrigation), energy to transport biomass to the biorefinery, energy to pretreat and sterilize the feedstock, energy for fermentation (aeration, cooling, mixing), energy for product separation and purification, and land use change emissions (clearing forest for agriculture releases stored carbon). When all these are counted, corn ethanol reduces greenhouse gas emissions by only 20-40% compared to gasoline — far from carbon-neutral.
  Strategy: Calculate: If making 1 gallon of biofuel requires 0.7 gallons-equivalent of fossil energy input, what's the net energy gain? What if we could reduce that fossil input to 0.3 gallons?

• "We can just scale up the lab strain and it will work in a big fermenter"
  Reality: Scale-up from a laboratory flask (milliliters) to an industrial bioreactor (hundreds of thousands of liters) changes almost everything about the microbial environment. Oxygen transfer becomes limited because bubbles can't reach all cells in a thick broth. Temperature gradients develop because heat from metabolism can't be removed fast enough. Mixing creates shear forces that damage cells. pH varies across the vessel. Contamination risk increases with longer fermentation times. And genetic instability means the production pathway mutates and degrades over hundreds of generations. The model's Fermentation Efficiency captures these scale-up losses, which typically reduce performance by 30-50% compared to laboratory results.
  Strategy: Analogy: A recipe that works perfectly in your kitchen doesn't automatically scale to a restaurant serving 1,000 people. What changes when you multiply everything by 1,000?

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
Big Question: We burn 100 million barrels of oil every day. Can we engineer microbes to brew fuel instead of drilling for it — and can we make it economically competitive?
Answer: Engineering microbes to produce biofuels is a metabolic tug-of-war between what the engineer wants (maximum fuel production) and what the cell needs (growth, maintenance, and survival). The nine components of this model capture the fundamental trade-offs: Substrate Concentration feeds carbon into the system, but Enzyme Activity must be precisely balanced to maintain Pathway Flux without overwhelming the cell with Metabolic Burden. Cofactor Availability acts as a hidden constraint — if the pathway drains NAD+, NADPH, or ATP faster than the cell regenerates them, flux stalls regardless of enzyme levels. Cell Growth Rate competes directly with Product Yield for the same carbon and energy. Byproduct Accumulation represents both lost carbon and metabolic toxicity. Fermentation Efficiency — the composite metric that determines commercial viability — requires simultaneously optimizing all eight upstream components. This is why metabolic engineering is sometimes called 'the art of compromise' — the best biofuel strain is never the one with the most enzyme, but the one with the most balanced metabolism.

Simulation Answers:
• Baseline Fermentation Scenario: With standard substrate and moderate enzyme expression, the engineered strain shows a workable but suboptimal balance. Pathway Flux is moderate — limited by the lowest-expressed enzyme (the bottleneck). Cofactor Availability remains adequate because the pathway isn't consuming cofactors faster than central metabolism regenerates them. Cell Growth Rate is near wild-type levels because Metabolic Burden is low. However, Product Yield is only 30-40% of theoretical maximum because significant carbon is diverted to Byproduct Accumulation (acetate, CO2) and biomass. Fermentation Efficiency is below commercial thresholds.
• Balanced Optimization Scenario: With tuned enzyme expression and cofactor engineering, the results are counter-intuitive: LOWER enzyme expression at certain steps can produce HIGHER total product. By reducing the expression of non-bottleneck enzymes, Metabolic Burden decreases significantly while Pathway Flux drops only marginally (because the bottleneck enzyme, not the reduced ones, was limiting flux). Cell Growth Rate recovers, producing more total biomass and therefore more total enzyme and more total product. Cofactor engineering (adding a heterologous NADH regeneration pathway) prevents cofactor depletion. The result: 60-75% of theoretical yield with adequate titer, approaching commercial viability.

Reflection Exemplars:
• Q: Why doesn't maximum enzyme expression produce maximum product yield?
  A: The model reveals that enzyme expression and product yield have a non-linear, non-monotonic relationship mediated by Metabolic Burden. At moderate expression levels, increasing enzyme activity increases Pathway Flux and Product Yield. But above a threshold, the cellular resources consumed by foreign protein production (Metabolic Burden) begin to crash Cell Growth Rate. Fewer cells, each growing slower and under metabolic stress, actually produce LESS total product than a moderately-expressing, healthy population. This is why metabolic engineers often use weak or tunable promoters rather than maximum-strength ones — the art is finding the expression sweet spot.
• Q: How does Cofactor Availability act as a hidden constraint?
  A: Cofactors like NADH and NADPH are required by many pathway enzymes but are present in limited intracellular pools. The model shows that when Pathway Flux is high, these cofactors are consumed faster than central metabolism regenerates them. The result is a metabolic traffic jam: enzymes have substrate available but cannot catalyze reactions without their required cofactor, so flux drops despite adequate enzyme levels. This is why cofactor engineering (adding heterologous cofactor regeneration pathways) is often more effective at increasing Product Yield than simply adding more pathway enzyme.

STEM CHALLENGE GUIDANCE:
Title: Design a Next-Generation Biofuel Production Strain
Mission: Design an engineered microbial strain and fermentation process that produces advanced biofuel at commercially competitive yields, titers, and productivities.
Scenario: A renewable energy startup has secured $50 million in venture capital to develop a microbial biofuel that can replace jet fuel. Current petroleum-based jet fuel costs $0.60 per liter to produce. Your metabolic engineering team must design a microbial strain and fermentation process that produces a drop-in jet fuel replacement at competitive cost — which means achieving high Product Yield, high titer (above 50 g/L), and high volumetric productivity (above 1 g/L/hr).
Introduction: Present the challenge: A renewable energy startup needs your metabolic engineering team to design a microbial strain and process that produces drop-in jet fuel replacement at commercially competitive cost ($0.60/liter). Current petroleum-based jet fuel sets the price target. Your design must specify the host organism, pathway, fermentation strategy, and economic projections.

Key Concepts:
• Host Organism Selection: Different chassis organisms offer different advantages: E. coli (fast growth, well-characterized genetics, limited solvent tolerance), S. cerevisiae (ethanol tolerance up to 15%, GRAS status, eukaryotic protein folding), Clostridium (natural butanol producer, anaerobic, difficult genetics), and cyanobacteria (photosynthetic — can use CO2 directly, but slow growth). The choice of host determines the engineering strategy and process constraints.
• Dynamic Pathway Regulation: Rather than expressing pathway enzymes at a constant level, dynamic regulation uses biosensors and genetic circuits to adjust expression based on the cell's metabolic state. For example: induce pathway enzymes only after cells reach high density (quorum sensing), reduce expression when cofactor pools drop below a threshold (metabolite-responsive promoters), or link production to essential metabolism so cells cannot grow without producing (growth-coupled design).
• Techno-Economic Analysis: Commercial biofuel viability depends on three numbers: yield (determines substrate cost per unit product), titer (determines downstream processing cost — distillation and purification below 50 g/L is prohibitively expensive), and productivity (determines bioreactor capital cost per unit product). A complete techno-economic analysis also includes substrate sourcing, utility costs (steam, cooling, aeration), labor, and waste treatment.

Evaluation Rubric:
• Expert (4): Design includes justified host selection, balanced pathway with cofactor strategy, dynamic regulation plan, fermentation process design, techno-economic projections, and evidence from model simulations
• Proficient (3): Design includes host organism, pathway engineering approach, and fermentation strategy with reasoning connected to model trade-offs
• Developing (2): Design covers basic pathway engineering but lacks detail on cofactor balance, metabolic burden management, or economic feasibility
• Beginning (1): Design is incomplete or does not connect engineering decisions to the metabolic model's trade-offs

DIFFERENTIATION:
Support (Struggling Learners):
  • Provide a visual metabolic map showing carbon flow from glucose through central metabolism to the biofuel product, with branch points and competing pathways highlighted
  • Use a cofactor balance sheet template: 'Pathway step ___ consumes ___ NADH. Total NADH consumed per cycle: ___. NADH regenerated by central metabolism: ___. Balance: ___'
  • Scaffold the growth-production trade-off: 'If 100 carbon atoms enter the cell, ___ go to biomass, ___ go to product, and ___ go to byproducts. To increase product, I need to redirect carbon FROM ___'

Extensions (Advanced Learners):
  • Research how LanzaTech engineers bacteria to convert industrial waste gases (CO and CO2) directly into ethanol and jet fuel — how does gas fermentation differ from sugar fermentation?
  • Investigate the concept of 'consolidated bioprocessing' (CBP) where a single organism both breaks down cellulose AND ferments the sugars — why is this the 'holy grail' of biofuel production?
  • Compare the energy return on investment (EROI) of corn ethanol (1.3:1), cellulosic ethanol (5:1), petroleum (15:1), and solar electricity (10:1) — what does this tell you about the true sustainability of different energy sources?

Cross-Curricular Connections:
  • Math: Calculate theoretical maximum yield using stoichiometric equations: C6H12O6 to 2 C2H5OH + 2 CO2 gives 51% mass yield — then compare to actual fermentation yields and calculate the 'yield gap' as a percentage
  • ELA: Write an investor pitch for a biofuel startup that explains the metabolic engineering strategy in non-technical language while honestly addressing the yield-titer-productivity challenges
  • Environmental Science: Conduct a life cycle assessment comparing the greenhouse gas emissions of petroleum jet fuel versus microbial biofuel from three feedstocks: corn sugar, agricultural waste, and captured CO2

CAST ALIGNMENT:
• Model metabolic flux from substrate through engineered enzymatic pathways to biofuel product, identifying rate-limiting steps and cofactor constraints
• Optimize the balance between enzyme expression level, metabolic burden, and cell growth to maximize overall fermentation efficiency
• Evaluate the economic feasibility of microbial biofuel production by analyzing the gap between laboratory yields and commercially competitive targets

CAST-Style Assessment Questions:
• Multiple Choice: An engineered E. coli strain producing butanol shows high Enzyme Activity but Fermentation Efficiency is declining over a 48-hour fermentation. Based on your model, which factor is most likely responsible?
• Constructed Response: Using your metabolic engineering model, explain why doubling the expression of every enzyme in a biofuel pathway does NOT double the Product Yield. Reference at least three model components and describe the trade-offs involved.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Activity Pack

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STUDENT ACTIVITY PACK: Metabolic Engineering for Biofuels
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NAME: _________________________ DATE: _____________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRE-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. What do you think happens inside a yeast cell when it ferments sugar into alcohol — and how is that related to making fuel?

   _________________________________________________________

   _________________________________________________________

2. Why do you think we can't just grow corn and turn it all into ethanol to replace gasoline?

   _________________________________________________________

   _________________________________________________________

3. Draw a diagram showing how you think a cell converts sugar into a useful chemical product — where does the carbon go?

   [DRAWING BOX]

4. What does 'metabolic engineering' mean to you and how might it differ from genetic engineering?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VOCABULARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Match the term to the definition:

___ Metabolic Flux                
___ Cofactor Recycling            
___ Metabolic Burden              
___ Fermentation Titer            

A. The rate at which metabolites flow through a biochemical pathway — measured in moles per gram of cells per hour — which determines how efficiently an organism converts substrate into desired product versus biomass or byproducts
B. The regeneration of essential helper molecules (NAD+/NADH, NADP+/NADPH, ATP/ADP, CoA) that enzymes require to catalyze reactions — if cofactors are consumed faster than they are recycled, the entire pathway stalls regardless of enzyme activity
C. The fitness cost imposed on a cell by expressing engineered pathway enzymes — diverting cellular resources (ribosomes, amino acids, ATP) from growth and maintenance to foreign protein production, which can slow growth or kill the cell
D. The final concentration of desired product (e.g., ethanol, butanol, fatty acid esters) achieved in the fermentation broth at the end of a production run — the key economic metric that determines whether a biofuel process is commercially viable

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

SCENARIO: Baseline Fermentation
Settings: Standard substrate, moderate enzyme expression
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Maximum Expression
Settings: All pathway enzymes at maximum expression
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Balanced Optimization
Settings: Tuned expression with cofactor engineering
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

1. How does your model demonstrate the fundamental trade-off between Cell Growth Rate and Product Yield — and why can't you simply maximize both?

   _________________________________________________________

   _________________________________________________________

2. Why is Cofactor Availability often called the 'silent killer' of engineered metabolic pathways?

   _________________________________________________________

   _________________________________________________________

3. What did you learn about the relationship between Enzyme Activity levels and Metabolic Burden — why doesn't 'more enzyme' always mean 'more product'?

   _________________________________________________________

   _________________________________________________________

4. How would adding Product Toxicity Threshold change your optimization strategy for Fermentation Efficiency?

   _________________________________________________________

   _________________________________________________________

5. What are the environmental justice implications of siting large biofuel fermentation facilities — who benefits and who bears the costs?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
POST-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. We burn 100 million barrels of oil every day. Can we engineer microbes to brew fuel instead of drilling for it — and can we make it economically competitive? Explain using evidence from your model:

   _________________________________________________________

   _________________________________________________________

   _________________________________________________________

2. Which NGSS dimensions did this lesson address?
   (Check all that apply)
   □ Science Practice: Developing and Using Models / Using Mathematics and Computational Thinking
   □ Disciplinary Core Idea: LS1.C Organization for Matter and Energy Flow / ETS1.C Optimizing the Design Solution
   □ Crosscutting Concept: Energy and Matter / Stability and Change

3. What are the environmental justice implications of siting large biofuel fermentation facilities — who benefits and who bears the costs?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEM CHALLENGE: Design a Next-Generation Biofuel Production Strain
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MISSION: Design an engineered microbial strain and fermentation process that produces advanced biofuel at commercially competitive yields, titers, and productivities.

SCENARIO: A renewable energy startup has secured $50 million in venture capital to develop a microbial biofuel that can replace jet fuel. Current petroleum-based jet fuel costs $0.60 per liter to produce. Your metabolic engineering team must design a microbial strain and fermentation process that produces a drop-in jet fuel replacement at competitive cost — which means achieving high Product Yield, high titer (above 50 g/L), and high volumetric productivity (above 1 g/L/hr).

GUIDING QUESTIONS:
• Which host organism (E. coli, yeast, Clostridium, cyanobacteria) would you choose as your chassis and why?
• How would you balance Enzyme Activity levels across the pathway to avoid the Metabolic Burden trap?
• What cofactor engineering strategy would you use to prevent NADH/NADPH imbalance from stalling the pathway?

DESIGN THINKING:
• Would you use a batch, fed-batch, or continuous fermentation process — and how does this choice affect Substrate Concentration management?

  _________________________________________________________

• How would you engineer the strain to tolerate high product concentrations that are typically toxic to the cell?

  _________________________________________________________

• What genetic stability strategies would you implement to prevent the production pathway from mutating out during long fermentations?

  _________________________________________________________

• How does the carbon footprint of your biofuel compare to petroleum when you account for substrate production, fermentation energy, and downstream processing?

  _________________________________________________________


EVALUATION RUBRIC:
• Expert (4): Design includes justified host selection, balanced pathway with cofactor strategy, dynamic regulation plan, fermentation process design, techno-economic projections, and evidence from model simulations
• Proficient (3): Design includes host organism, pathway engineering approach, and fermentation strategy with reasoning connected to model trade-offs
• Developing (2): Design covers basic pathway engineering but lacks detail on cofactor balance, metabolic burden management, or economic feasibility
• Beginning (1): Design is incomplete or does not connect engineering decisions to the metabolic model's trade-offs

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Resources

| Resource | Link |
|----------|------|
| Activity Pack (DOCX) | [materials/grade-09/G09L3-L07/G09L3-L07-Student-Activity-Pack.docx] |
| Teacher Guide (DOCX) | [materials/grade-09/G09L3-L07/G09L3-L07-Teachers-Guide.docx] |
| PPT Presentation | [materials/grade-09/G09L3-L07/G09L3-L07-Student-Presentation.pptx] |
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