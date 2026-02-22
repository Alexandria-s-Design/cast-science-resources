# Lesson: Growing Meat Without the Animal

## Header Information

| Field | Value |
|-------|-------|
| **Lesson ID** | G09L3-L04 |
| **Grade** | 9th Grade — Level 3: Biotech |
| **Lesson Name** | Growing Meat Without the Animal |
| **Status** | Template |

---

## Platform

### Title
**Growing Meat Without the Animal — Optimizing Cultured Meat Bioreactor Systems from Cell to Steak**

### Overview
This lesson introduces students to predictive modeling and multi-parameter optimization in the context of cellular agriculture — one of the most ambitious bioengineering challenges of the 21st century. Biotech skill focus: Predictive modeling and optimization. Growing meat from cell cultures requires simultaneously optimizing biological, engineering, and economic parameters — a perfect application for computational modeling. Students investigate the driving question: Can we grow a steak in a lab that tastes, feels, and costs the same as one from a cow — and should we? Using the LEVER framework, students identify key components, establish cause-and-effect relationships, run simulations to test scenarios, and extend their understanding through research and engineering challenges.

### Cover Image
[A photorealistic, cinematic image of diverse 14-15 year old students in a cutting-edge cellular agriculture lab examining bioreactors with pink cell culture media visible, cultured meat tissue samples on plates nearby, with bioprocess monitoring screens showing growth curves, modern clean-room aesthetic with white and chrome]

### Grade
9th Grade — Level 3: Biotech

### NGSS Standard
**HS-LS1-2, HS-ETS1-3**: Develop and use a model to illustrate the hierarchical organization of interacting systems that provide specific functions within multicellular organisms; evaluate a solution to a complex real-world problem based on prioritized criteria and trade-offs.

### Learning Objectives
- Build an optimization model for cultured meat production that balances cell growth, nutrient efficiency, and product quality across a bioreactor system
- Analyze how bioreactor conditions (temperature, oxygen, nutrients) interact to determine cell proliferation rate, tissue quality, and production cost
- Optimize multiple competing parameters simultaneously to achieve viable commercial-scale cultured meat production
- Evaluate the trade-offs between production cost, texture quality, and environmental sustainability in cellular agriculture

### Component List (Starting Model: 10 Components)

| Component | Type | What It Represents |
|-----------|------|-------------------|
| Cell Growth Rate | Internal | The speed at which muscle satellite cells divide and increase in number within the bioreactor, measured in population doublings per day — determines production throughput |
| Nutrient Medium Concentration | External | The formulation and concentration of amino acids, glucose, vitamins, minerals, and growth factors in the liquid medium that feeds the growing cells — the primary input and cost driver |
| Bioreactor Temperature | External | The precisely controlled temperature of the culture environment, typically maintained at 37°C for mammalian cells — deviations of even 1-2°C can dramatically affect cell behavior |
| Oxygen Supply | External | The rate of dissolved oxygen delivery to cells throughout the bioreactor volume — critical because cells deep inside tissue structures can become oxygen-starved (hypoxic) without active perfusion |
| Waste Product Accumulation | Internal | The buildup of metabolic byproducts (ammonia, lactate, carbon dioxide) that cells produce as they grow and consume nutrients — these toxins inhibit further growth if not removed |
| Scaffold Structure | External | The engineered three-dimensional framework that guides cell organization into muscle-like tissue architecture — determines whether the final product has the fibrous texture of steak or the mush of a paste |
| Texture Quality | Internal | The sensory and structural properties of the final cultured meat product — fiber alignment, marbling, tenderness, and mouthfeel — compared to conventionally produced meat |
| Energy Input | External | The total energy required to maintain bioreactor conditions — heating, mixing, oxygenation, pumping, sterilization — which determines the environmental footprint and operational cost |
| Production Cost | Internal | The calculated cost per kilogram of final cultured meat product, incorporating nutrient medium, energy, labor, equipment depreciation, and quality control — must approach $10-20/kg for commercial viability |
| Scale Factor | Internal | The ratio of production volume to cost efficiency — larger bioreactors can be more cost-effective but face challenges in maintaining uniform conditions throughout the vessel |

### Research for Lesson
- Cellular Agriculture Fundamentals — reference materials and textbook resources
- The Bioreactor Engineering Challenge — reference materials and textbook resources
- The Growth Factor Cost Problem — reference materials and textbook resources
- Texture: The Final Frontier — reference materials and textbook resources

---

## Activity 1: LOCATE — Build Your System

### Text Editor

```
GROWING MEAT WITHOUT THE ANIMAL

Optimizing Cultured Meat Bioreactor Systems from Cell to Steak.
Can we grow a steak in a lab that tastes, feels, and costs the same as one from a cow — and should we?

That's not just a question — it's something you can MODEL.
And you're about to build exactly that.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1: CHOOSE YOUR COMPONENTS
• Look at the component panel on the RIGHT side of your screen
• Find the EXTERNAL components (things we can't control):
  ○ Click "Nutrient Medium Concentration" — the formulation and concentration of amino acids
  ○ Click "Bioreactor Temperature" — the precisely controlled temperature of the culture environment
  ○ Click "Oxygen Supply" — the rate of dissolved oxygen delivery to cells throughout the bioreactor volume — critical because cells deep inside tissue structures can become oxygen-starved (hypoxic) without active perfusion
  ○ Click "Scaffold Structure" — the engineered three-dimensional framework that guides cell organization into muscle-like tissue architecture — determines whether the final product has the fibrous texture of steak or the mush of a paste
  ○ Click "Energy Input" — the total energy required to maintain bioreactor conditions — heating
• Find the INTERNAL components (things that change because of other things):
  ○ Click "Cell Growth Rate" — the speed at which muscle satellite cells divide and increase in number within the bioreactor
  ○ Click "Waste Product Accumulation" — the buildup of metabolic byproducts (ammonia
  ○ Click "Texture Quality" — the sensory and structural properties of the final cultured meat product — fiber alignment
  ○ Click "Production Cost" — the calculated cost per kilogram of final cultured meat product
  ○ Click "Scale Factor" — the ratio of production volume to cost efficiency — larger bioreactors can be more cost-effective but face challenges in maintaining uniform conditions throughout the vessel

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
"Can we grow a steak in a lab that tastes, feels, and costs the same as one from a cow — and should we?

That's what we're going to figure out today. Not by reading about
it — by MODELING it. You're going to build a system that shows
exactly how this works.

Let's build our system. Look at the component panel on the right
side of your screen. You'll see two types of components:

EXTERNAL components — things that come from outside the system.
Inputs we can't directly control.

INTERNAL components — things that change BECAUSE of other things
in the system. They respond to the externals.

Click on 'Cell Growth Rate' — that's internal. The speed at which muscle satellite cells divide and increase in number within the bioreactor.
Click on 'Nutrient Medium Concentration' — that's external. The formulation and concentration of amino acids.
Click on 'Bioreactor Temperature' — that's external. The precisely controlled temperature of the culture environment.
Click on 'Oxygen Supply' — that's external. The rate of dissolved oxygen delivery to cells throughout the bioreactor volume — critical because cells deep inside tissue structures can become oxygen-starved (hypoxic) without active perfusion.
Click on 'Waste Product Accumulation' — that's internal. The buildup of metabolic byproducts (ammonia.
Click on 'Scaffold Structure' — that's external. The engineered three-dimensional framework that guides cell organization into muscle-like tissue architecture — determines whether the final product has the fibrous texture of steak or the mush of a paste.
Click on 'Texture Quality' — that's internal. The sensory and structural properties of the final cultured meat product — fiber alignment.
Click on 'Energy Input' — that's external. The total energy required to maintain bioreactor conditions — heating.
Click on 'Production Cost' — that's internal. The calculated cost per kilogram of final cultured meat product.
Click on 'Scale Factor' — that's internal. The ratio of production volume to cost efficiency — larger bioreactors can be more cost-effective but face challenges in maintaining uniform conditions throughout the vessel.

Now you need to SORT them. Which ones are external — things that
come from outside the system? Which ones are internal — things
that change because of what's happening inside?

Nutrient Medium Concentration, Bioreactor Temperature, Oxygen Supply, Scaffold Structure, and Energy Input are external components because they represent engineering parameters that bioprocess engineers directly control and set. Cell Growth Rate, Waste Product Accumulation, Texture Quality, Production Cost, and Scale Factor are internal components because they emerge as outcomes of the bioreactor system — they respond to the external inputs but cannot be directly set by the engineer.

Sort your components, then hit the PLUS button to add each one
to your model canvas.

You've got your pieces. But right now they're just sitting there,
not connected. In the next activity, we'll draw the invisible
lines that show how everything affects everything else.

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing 10 components sorted: Nutrient Medium Concentration, Bioreactor Temperature, Oxygen Supply, Scaffold Structure, Energy Input (External), Cell Growth Rate, Waste Product Accumulation, Texture Quality, Production Cost, Scale Factor (Internal)]

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
• Click on "Nutrient Medium Concentration" and drag an arrow to "Cell Growth Rate"
• Click on "Cell Growth Rate" and drag an arrow to "Waste Product Accumulation"
• Click on "Waste Product Accumulation" and drag an arrow to "Cell Growth Rate"
• Click on "Oxygen Supply" and drag an arrow to "Cell Growth Rate"
• Click on "Scaffold Structure" and drag an arrow to "Texture Quality"
• Click on "Nutrient Medium Concentration" and drag an arrow to "Production Cost"

STEP 3: SET POSITIVE OR NEGATIVE
• Look at the +/− toggle in the TOP LEFT corner
• For each connection, ask: "When this goes UP, does the other go UP or DOWN?"

  ○ Nutrient Medium Concentration → Cell Growth Rate = POSITIVE (+)
    Higher nutrient concentration provides more amino acids, glucose, and growth factors for cell metabolism and division, directly increasing the cell proliferation rate.

  ○ Cell Growth Rate → Waste Product Accumulation = POSITIVE (+)
    Faster-growing cells metabolize more nutrients per unit time, producing proportionally more waste products (ammonia, lactate) that accumulate in the medium.

  ○ Waste Product Accumulation → Cell Growth Rate = NEGATIVE (−)
    As metabolic waste accumulates, it creates an increasingly toxic environment that inhibits cell division — this is the primary negative feedback loop in bioreactor systems.

  ○ Oxygen Supply → Cell Growth Rate = POSITIVE (+)
    Adequate dissolved oxygen is essential for aerobic cellular metabolism; insufficient oxygen causes cells to switch to inefficient anaerobic pathways or die from hypoxia.

  ○ Scaffold Structure → Texture Quality = POSITIVE (+)
    Better scaffold design provides more appropriate physical cues for cell alignment, fiber formation, and tissue architecture, directly improving the textural properties of the final product.

  ○ Nutrient Medium Concentration → Production Cost = POSITIVE (+)
    Growth medium — especially growth factors — is the primary cost driver; higher concentration and more frequent replacement directly increase per-kilogram production costs.

STEP 4: CHECK YOUR MODEL
• You should have 6 arrows total
• 1 negative relationship(s), 5 positive relationship(s)
• This is your system model!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THINK ABOUT IT: Increasing Nutrient Medium Concentration boosts Cell Growth Rate but drives up Production Cost. Raising Bioreactor Temperature to exactly 37°C optimizes growth but increases Energy Input. Improving Scaffold Structure enhances Texture Quality but adds complexity and cost. And as Scale Factor increases, maintaining uniform Oxygen Supply and Waste Product removal becomes exponentially harder. How do you optimize everything simultaneously when improving one parameter often worsens another?
```

### Video Script

```
"Your pieces are on the board, but they're not talking to each
other yet. Time to draw the invisible lines — the relationships
that make this a SYSTEM, not just a pile of parts.

Click the 'Connect' icon in the top left corner. Now you're in
connection mode.

First connection: Click on 'Nutrient Medium Concentration' and drag an arrow
over to 'Cell Growth Rate.'

Here's the key question: When nutrient medium concentration goes UP, does
cell growth rate go UP or DOWN?

Higher nutrient concentration provides more amino acids, glucose, and growth factors for cell metabolism and division, directly increasing the cell proliferation rate.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Next connection: Click on 'Cell Growth Rate' and drag an arrow
over to 'Waste Product Accumulation.'

Here's the key question: When cell growth rate goes UP, does
waste product accumulation go UP or DOWN?

Faster-growing cells metabolize more nutrients per unit time, producing proportionally more waste products (ammonia, lactate) that accumulate in the medium.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Last connection: Click on 'Waste Product Accumulation' and drag an arrow
over to 'Cell Growth Rate.'

Here's the key question: When waste product accumulation goes UP, does
cell growth rate go UP or DOWN?

As metabolic waste accumulates, it creates an increasingly toxic environment that inhibits cell division — this is the primary negative feedback loop in bioreactor systems.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Final connection: Click on 'Oxygen Supply' and drag an arrow
over to 'Cell Growth Rate.'

Here's the key question: When oxygen supply goes UP, does
cell growth rate go UP or DOWN?

Adequate dissolved oxygen is essential for aerobic cellular metabolism; insufficient oxygen causes cells to switch to inefficient anaerobic pathways or die from hypoxia.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Final connection: Click on 'Scaffold Structure' and drag an arrow
over to 'Texture Quality.'

Here's the key question: When scaffold structure goes UP, does
texture quality go UP or DOWN?

Better scaffold design provides more appropriate physical cues for cell alignment, fiber formation, and tissue architecture, directly improving the textural properties of the final product.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Final connection: Click on 'Nutrient Medium Concentration' and drag an arrow
over to 'Production Cost.'

Here's the key question: When nutrient medium concentration goes UP, does
production cost go UP or DOWN?

Growth medium — especially growth factors — is the primary cost driver; higher concentration and more frequent replacement directly increase per-kilogram production costs.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Look at your model now. You've got 1 negative and 5
positive relationships. 6 arrows total.

Increasing Nutrient Medium Concentration boosts Cell Growth Rate but drives up Production Cost. Raising Bioreactor Temperature to exactly 37°C optimizes growth but increases Energy Input. Improving Scaffold Structure enhances Texture Quality but adds complexity and cost. And as Scale Factor increases, maintaining uniform Oxygen Supply and Waste Product removal becomes exponentially harder. How do you optimize everything simultaneously when improving one parameter often worsens another?

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing connected model with arrows: Nutrient Medium Concentration +→ Cell Growth Rate, Cell Growth Rate +→ Waste Product Accumulation, Waste Product Accumulation −→ Cell Growth Rate, Oxygen Supply +→ Cell Growth Rate, Scaffold Structure +→ Texture Quality, Nutrient Medium Concentration +→ Production Cost]

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
• When Nutrient Medium Concentration is HIGH, what happens to the internal components?

STEP 3: SCENARIO — LAB PROTOTYPE
• Small-scale, optimized conditions
• PREDICT FIRST: What do you predict Production Cost per kilogram will be at lab scale, and why?
• Resume the simulation and observe what happens
• Was your prediction correct?

STEP 4: SCENARIO — MAXIMUM GROWTH
• All inputs maximized for fastest cell division
• PREDICT FIRST: What do you predict happens to Waste Product Accumulation when Cell Growth Rate is maximized?
• Resume the simulation and observe what happens
• Was your prediction correct?

STEP 5: SCENARIO — COMMERCIAL SCALE-UP
• Large bioreactor, cost-minimized inputs
• PREDICT FIRST: Do you predict that scaling up 1000x will reduce per-kilogram cost, and what new problems emerge?
• Resume the simulation and observe what happens
• Was your prediction correct?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT DID YOU DISCOVER?
• The primary cost driver in cultured meat is the nutrient medium — particularly growth factors that currently cost thousands of dollars per gram and must be produced through recombinant protein technology
• Oxygen delivery is the critical scaling bottleneck — cells more than 200 micrometers from an oxygen source become hypoxic, limiting how thick cultured meat tissue can grow without vascularization
• Waste product accumulation creates a negative feedback loop — as cells grow and metabolize, they produce toxins that inhibit further growth, requiring continuous medium perfusion or replacement
• Texture quality requires both scaffold engineering and mechanical stimulation — without aligned fibers and exercised muscle cells, cultured meat lacks the sensory experience consumers expect from conventional meat

THE ANSWER: Growing meat without animals is technically possible but commercially challenging. The optimization problem is multidimensional: nutrient medium must be rich enough to support rapid cell growth but affordable enough for commercial viability; oxygen must reach every cell in a three-dimensional tissue but diffusion limits tissue thickness to about 200 micrometers; waste products must be removed continuously as they accumulate; and scaffold structures must guide cells into forming the aligned fibers that give meat its texture. The key insight is that this is fundamentally an engineering optimization problem — every parameter improvement in one dimension creates constraints in others. Computational modeling allows researchers to find the narrow operating window where all parameters are simultaneously viable, dramatically accelerating the path from lab prototype to commercial reality.
```

### Video Script

```
"You've built the machine. You've wired the connections. Now let's
flip the switch and see if your model matches reality.

Click the 'Play' button in the top left. Watch the graph panel —
you'll see lines representing each component as a percentage.

Let it run. Watch how the components interact at baseline levels.
Everything should be balanced, moving together.

First scenario: Lab Prototype. Small-scale, optimized conditions.
Watch the graph. What do you see happening?

Now let's push the system. Scenario two: Maximum Growth.
All inputs maximized for fastest cell division.

Before you run it — make a prediction. What do you predict happens to Waste Product Accumulation when Cell Growth Rate is maximized?

Resume the simulation and watch what happens. Did your prediction
match the model? If not, that's actually a GOOD thing — it means
you learned something unexpected.

One more scenario: Commercial Scale-Up. Large bioreactor, cost-minimized inputs.
Do you predict that scaling up 1000x will reduce per-kilogram cost, and what new problems emerge?

Here's what our model reveals: Growing meat without animals is technically possible but commercially challenging. The optimization problem is multidimensional: nutrient medium must be rich enough to support rapid cell growth but affordable enough for commercial viability; oxygen must reach every cell in a three-dimensional tissue but diffusion limits tissue thickness to about 200 micrometers; waste products must be removed continuously as they accumulate; and scaffold structures must guide cells into forming the aligned fibers that give meat its texture. The key insight is that this is fundamentally an engineering optimization problem — every parameter improvement in one dimension creates constraints in others. Computational modeling allows researchers to find the narrow operating window where all parameters are simultaneously viable, dramatically accelerating the path from lab prototype to commercial reality.

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
   • What happens if you turn OFF Nutrient Medium Concentration?
   • What happens if you turn OFF Bioreactor Temperature?
   • What happens if you turn OFF Oxygen Supply?
   • What happens if you turn OFF Scaffold Structure?
   • What happens if you turn OFF Energy Input?
   • What happens if you change multiple variables at once?
   • Can you find a combination where the system stays stable?

3. WHAT'S MISSING?
   Your model is simple. Real systems involve more. Think about:

   • Fat Cell Integration — The inclusion of adipocyte (fat) cells alongside muscle cells to create the marbling and flavor profile that makes meat taste rich — requiring different growth conditions from muscle cells
   • Mechanical Stimulation — The application of cyclic stretching or electrical pulses to cultured muscle cells, mimicking exercise to promote fiber alignment, protein production, and the textural properties of real muscle tissue
   • Serum-Free Medium Development — The replacement of fetal bovine serum (FBS) — an expensive, animal-derived, and ethically problematic component — with plant-derived or recombinant growth factors, which is essential for both cost reduction and consumer acceptance

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RESEARCH DIRECTIONS:

Don't just guess — find out! Here's what to look for:

📚 IN YOUR TEXTBOOK:
   • Cellular Agriculture Fundamentals — how does this connect to your model?
   • The Bioreactor Engineering Challenge — how does this connect to your model?

🔍 QUESTIONS TO INVESTIGATE:
   • How does your model reveal the multi-dimensional optimization challenge of cultured meat production?
   • Which parameter do you think is the most critical bottleneck for commercial viability, and what does your model suggest?
   • What trade-offs between Production Cost and Texture Quality did you discover, and which compromises are acceptable?
   • How would adding Fat Cell Integration change the bioreactor requirements and production complexity?

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

Fat Cell Integration. The inclusion of adipocyte (fat) cells alongside muscle cells to create the marbling and flavor profile that makes meat taste rich — requiring different growth conditions from muscle cells
How would you model that?

Mechanical Stimulation. The application of cyclic stretching or electrical pulses to cultured muscle cells, mimicking exercise to promote fiber alignment, protein production, and the textural properties of real muscle tissue
How would you model that?

Serum-Free Medium Development. The replacement of fetal bovine serum (FBS) — an expensive, animal-derived, and ethically problematic component — with plant-derived or recombinant growth factors, which is essential for both cost reduction and consumer acceptance
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

Bioprocess Engineers design and optimize bioreactor systems for cellular agriculture, biopharmaceutical production, and industrial biotechnology. They work for cultured meat companies (Upside Foods, GOOD Meat, Mosa Meat), biotech firms, and food technology startups, earning $80,000–$150,000/year. Tissue Engineers who specialize in edible scaffold design earn $90,000–$170,000/year.

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
Visual: Title slide with dramatic side-by-side of conventional slaughterhouse versus clean bioreactor lab
Say: "By 2050, the world needs to feed 10 billion people. Conventional livestock uses 77% of agricultural land but produces only 18% of calories. What if we could grow the same meat — same taste, same texture — without a single animal?"
Do: Show the land use statistic with a visual comparison. Ask students to react before introducing cultured meat.
Time: 2 min

SLIDE 2: LEARNING OBJECTIVES
Visual: Learning goals and cellular agriculture vocabulary
Say: "Today you're bioprocess engineers. Your job is to optimize a bioreactor that grows real beef from cells — and figure out how to make it affordable enough for everyone."
Do: Pre-teach bioreactor and scaffold. Show a 30-second time-lapse of cells growing in culture to establish the biological basis.
Time: 3 min

SLIDE 3: BIG QUESTION
Visual: Can we grow a steak in a lab that's affordable and delicious?
Say: "The first cultured beef burger cost $330,000 to produce in 2013. Today it's down to around $10-50 per burger. But conventional beef burgers cost $1. How do we close that gap — and what has to be sacrificed along the way?"
Do: Quick-write: Students list what they think makes cultured meat expensive. Compile class predictions on the board.
Time: 3 min

SLIDE 4: LEVER FRAMEWORK
Visual: LEVER steps with bioreactor optimization context
Say: "We're going to optimize ten interacting parameters simultaneously — cell biology, engineering, and economics all at once. Welcome to multi-parameter optimization."
Do: Preview LEVER steps. Emphasize that this model has five external (controllable) variables — the most of any model we've built.
Time: 2 min

SLIDE 5: ACTIVITY 1: COMPONENTS
Visual: Ten component cards spanning biology, engineering, and economics
Say: "Five of these ten components are controllable — you set them. The other five are responses. Identify them and think about why the controllable ones are the expensive ones."
Do: Guide sorting of external versus internal components. Note that four of five externals represent costs (nutrients, energy, temperature control, scaffolds) — this is why cultured meat is expensive.
Time: 8 min

SLIDE 6: ACTIVITY 2: CONNECTIONS
Visual: Complex web of bioreactor parameter interactions
Say: "Here's the optimization nightmare: making cells grow faster increases waste. Improving texture adds cost. Scaling up breaks oxygen delivery. Everything is connected to everything."
Do: Students map relationships, identifying trade-offs and constraints. Highlight the fundamental tension between quality, speed, and cost.
Time: 8 min

SLIDE 7: ACTIVITY 3: SIMULATION
Visual: Multi-parameter optimization dashboard with cost, quality, and growth metrics
Say: "Find the sweet spot. The bioreactor configuration where cells grow fast enough, meat tastes good enough, and the price is low enough. Spoiler: it's a very small target."
Do: Students predict outcomes, then run lab-scale, max-growth, and commercial-scale scenarios. Track the three-way trade-off between growth rate, texture quality, and production cost.
Time: 10 min

SLIDE 8: DISCOVERIES
Visual: Key optimization findings and real-world cost trajectories
Say: "The industry has already brought costs down 99.9% from $330,000 to about $10 per burger. Your model shows the same optimization principles the real companies are using."
Do: Connect model findings to the real cost trajectory of cultured meat. Discuss which remaining bottlenecks your model identified.
Time: 5 min

SLIDE 9: STEM CHALLENGE
Visual: Commercial-scale bioreactor design challenge
Say: "A startup just raised $50 million to build the world's first commercial cultured meat factory. Design their bioreactor."
Do: Groups design commercial bioreactor systems including vessel type, monitoring systems, waste management, and cost projections. Present engineering proposals.
Time: 12 min

```

### Teacher Guide

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TEACHER GUIDE: Growing Meat Without the Animal
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LESSON PURPOSE:
This lesson introduces students to predictive modeling and multi-parameter optimization in the context of cellular agriculture — one of the most ambitious bioengineering challenges of the 21st century. Biotech skill focus: Predictive modeling and optimization. Growing meat from cell cultures requires simultaneously optimizing biological, engineering, and economic parameters — a perfect application for computational modeling.

NGSS ALIGNMENT:
HS-LS1-2, HS-ETS1-3: Develop and use a model to illustrate the hierarchical organization of interacting systems that provide specific functions within multicellular organisms; evaluate a solution to a complex real-world problem based on prioritized criteria and trade-offs.

THREE-DIMENSIONAL LEARNING:
• Science Practice: Developing and Using Models / Constructing Explanations and Designing Solutions
  Students develop a computational bioreactor model and use it to design optimized solutions that balance competing production constraints.
• Disciplinary Core Idea: LS1.A Structure and Function / ETS1.C Optimizing the Design Solution
  Multicellular organisms have hierarchical organization; engineering optimization requires systematically testing and refining solutions against multiple criteria and constraints.
• Crosscutting Concept: Systems and System Models / Stability and Change
  Students model the bioreactor as a complex system where multiple interacting variables must be simultaneously optimized, and small changes in one parameter cascade through the entire system.

PACING GUIDE:
• Activity 1 (Locate): 8-10 minutes
• Activity 2 (Establish): 8-10 minutes
• Activity 3 (Visualize & Evaluate): 10-12 minutes
• Activity 4 (Revise & Extend): 10-15 minutes
• Total: 50-70 minutes (or split across 2 class periods)

PRE-LESSON PREP:
□ Test ModelIt access on student devices
□ Review vocabulary: Cellular Agriculture, Bioreactor, Scaffold, Growth Factor
□ Prepare Can we grow a steak in a lab that tastes, feels, and costs the same as one from a cow — and should we discussion hook
□ Have images or video ready for phenomenon introduction

LEVER FRAMEWORK:
• Locate: Students identify ten components spanning cell biology (Cell Growth Rate, Waste Product Accumulation), engineering (Bioreactor Temperature, Oxygen Supply, Scaffold Structure, Energy Input), medium chemistry (Nutrient Medium Concentration), and economics (Production Cost, Scale Factor, Texture Quality).
• Establish: Students determine that Nutrient Medium Concentration, Bioreactor Temperature, Oxygen Supply, Scaffold Structure, and Energy Input are the controllable inputs that drive Cell Growth Rate and Texture Quality — while Waste Product Accumulation acts as a growth inhibitor, and Production Cost and Scale Factor represent the economic constraints.
• Visualize: Students build a computational model connecting all ten components, visualizing how changing one parameter cascades through the system and affects multiple outputs simultaneously.
• Evaluate: Students run lab-scale, maximum-growth, and commercial-scale scenarios to discover that optimizing for one metric (speed, quality, or cost) often degrades the others — and search for the narrow window where all three are acceptable.
• Revise: Students add Fat Cell Integration, Mechanical Stimulation, or Serum-Free Medium Development to explore more realistic cultured meat production challenges.

BACKGROUND CONTENT:
• Cellular Agriculture Fundamentals:
  Cultured meat begins with a small biopsy of muscle stem cells (satellite cells) from a living animal — a painless procedure that yields enough cells to theoretically produce tons of meat. These cells are placed in nutrient-rich media inside bioreactors where they proliferate, differentiate into muscle fibers, and organize into tissue. The process mirrors what happens naturally in an animal's body: cells divide, consume nutrients, produce waste, and organize into structured tissues. The difference is that engineers must artificially provide everything the animal's body normally supplies — nutrients, oxygen, waste removal, structural support, growth signals, and mechanical stimulation. The current state of the art can produce small quantities of cultured meat that is safe to eat and reasonably similar to conventional meat, but at costs that are 10-40x higher than conventional production.

• The Bioreactor Engineering Challenge:
  Bioreactors for cultured meat must maintain mammalian cell culture conditions (37°C, pH 7.4, 20% dissolved oxygen, specific nutrient concentrations) while scaling to thousands of liters. The critical engineering challenge is mass transfer — getting oxygen and nutrients TO cells and waste products AWAY from cells throughout the entire volume. In a small flask, diffusion handles this naturally. In a 10,000-liter bioreactor, cells in the center can be centimeters from the nearest oxygen source, far beyond the ~200 micrometer diffusion limit for mammalian cells. Solutions include perfusion bioreactors (continuous medium flow), hollow-fiber systems (oxygen delivered through permeable tubes), and microcarrier cultures (cells growing on small beads suspended in circulating medium). Each approach has trade-offs in cost, scalability, and product quality.

• The Growth Factor Cost Problem:
  The single biggest cost barrier in cultured meat is the growth medium — specifically, the growth factors (signaling proteins like FGF2, TGF-beta, IGF-1, and transferrin) that instruct cells to proliferate and differentiate. In research labs, these are purchased at costs of $500-$50,000 per gram. Traditional cell culture uses fetal bovine serum (FBS) as a growth factor source, but FBS costs $300-500/liter, is derived from unborn calves (defeating the ethical purpose), and varies batch-to-batch. The industry is racing to develop serum-free, animal-free media using recombinant growth factors produced by engineered bacteria or yeast, edible plant-derived alternatives, or genetic engineering of the meat cells themselves to produce their own growth factors (autocrine signaling). Reducing medium cost from ~$400/liter to under $1/liter is necessary for commercial viability.

• Texture: The Final Frontier:
  The biggest quality challenge in cultured meat is texture. Ground meat products (burgers, nuggets, sausages) are relatively straightforward because they don't require organized tissue structure. But whole-cut products (steaks, chicken breasts, pork chops) require aligned muscle fibers, intramuscular fat marbling, connective tissue, and the complex architecture that gives meat its 'bite.' Achieving this requires three-dimensional scaffolds (made from plant proteins, alginate, or decellularized plant tissue), mechanical stimulation (cyclic stretching that mimics exercise), and co-culture of multiple cell types (muscle, fat, fibroblasts). Current prototypes achieve reasonable texture in thin products (<5mm thickness) but struggle with thick cuts where oxygen delivery and structural integrity become limiting factors.

COMMON MISCONCEPTIONS:
• "Lab-grown meat is 'fake' or 'artificial' meat"
  Reality: Cultured meat is real animal meat — it contains the same muscle cells, proteins, and fats as conventional meat because it IS animal cells. The only difference is where the cells grew: in a bioreactor instead of inside an animal. At the molecular level, a cultured beef cell is identical to a cell from a cow's muscle. Calling it 'fake' is like calling ice from a freezer 'fake ice' because it wasn't made by a glacier.
  Strategy: Ask: If you took a muscle cell from a cow and grew it in a dish, is it still a cow cell? If you grew a trillion of them, is it still beef? Where does 'real' end and 'fake' begin?

• "Cultured meat must be unhealthy because it's 'unnatural'"
  Reality: Cultured meat can be engineered to be HEALTHIER than conventional meat. Producers can control fat content, reduce saturated fat, add omega-3 fatty acids, eliminate antibiotics and growth hormones, and ensure zero pathogen contamination (no Salmonella, E. coli, or prions). The 'unnatural' criticism ignores that most modern food production — from cheese to bread to yogurt — involves controlled biological processes.
  Strategy: Comparison: Yogurt is made by adding bacteria to milk in controlled conditions. Cheese is made by adding enzymes and microbes. Beer is made by yeast in a bioreactor. These are all 'lab-grown' products that nobody considers 'fake.'

• "Cultured meat will be available and affordable within a few years"
  Reality: While progress has been extraordinary ($330,000/burger in 2013 to ~$10-50 today), achieving true commercial viability ($5-15/kg at millions of tons/year) requires solving several fundamental engineering challenges that the model reveals: growth factor cost reduction by 100-1000x, oxygen delivery at industrial scale, waste management for massive bioreactors, and texture engineering for whole-cut products. Most industry experts estimate 5-15 years for cost-competitive commodity products, though premium products may arrive sooner.
  Strategy: Model it: Even if you solve every other problem, growth factor cost alone makes cultured meat 3-5x more expensive than conventional beef. What breakthrough would change that equation?

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
Big Question: Can we grow a steak in a lab that tastes, feels, and costs the same as one from a cow — and should we?
Answer: Growing meat without animals is technically possible but commercially challenging. The optimization problem is multidimensional: nutrient medium must be rich enough to support rapid cell growth but affordable enough for commercial viability; oxygen must reach every cell in a three-dimensional tissue but diffusion limits tissue thickness to about 200 micrometers; waste products must be removed continuously as they accumulate; and scaffold structures must guide cells into forming the aligned fibers that give meat its texture. The key insight is that this is fundamentally an engineering optimization problem — every parameter improvement in one dimension creates constraints in others. Computational modeling allows researchers to find the narrow operating window where all parameters are simultaneously viable, dramatically accelerating the path from lab prototype to commercial reality.

Simulation Answers:
• Lab Prototype Scenario: At lab scale, all conditions can be precisely controlled. Cell Growth Rate is optimized because Oxygen Supply reaches every cell through diffusion, Waste Product Accumulation is managed through frequent medium changes, and Nutrient Medium Concentration is high. Texture Quality is moderate with basic scaffolds. However, Production Cost is astronomical — estimated at $100-400/kg due to expensive growth factors, intensive labor, and no economies of scale. Scale Factor is too small for commercial viability.
• Commercial Scale-Up Scenario: At 1000x scale, Production Cost per kilogram decreases due to economies of scale (Scale Factor effect), but new problems emerge. Oxygen Supply becomes the critical bottleneck — cells in the center of large bioreactors are oxygen-starved, reducing Cell Growth Rate in those regions. Waste Product Accumulation is harder to manage in large volumes. Texture Quality may decrease because scaffold structures are difficult to maintain uniformly at scale. The model reveals that the path to commercial viability requires solving the oxygen delivery and waste removal problems simultaneously.

Reflection Exemplars:
• Q: Which parameter is the most critical bottleneck for commercial viability?
  A: The model suggests that Nutrient Medium Concentration (specifically growth factor cost) is the primary economic bottleneck, while Oxygen Supply is the primary engineering bottleneck for scaling. At lab scale, cost dominates — growth medium accounts for 55-95% of production expense. At commercial scale, oxygen delivery becomes the limiting factor because cells more than 200 micrometers from an oxygen source become hypoxic. Solving both simultaneously is the key challenge: you need cheap medium AND effective oxygen delivery at scale.
• Q: What environmental trade-offs exist between cultured and conventional meat?
  A: The model shows that Energy Input is a significant component of Production Cost, and this energy largely comes from electricity for heating, mixing, and oxygenation. Cultured meat eliminates the massive land use, water use, and methane emissions of conventional livestock — but replaces them with industrial energy consumption. Whether cultured meat is environmentally superior depends on the energy source: if powered by renewable energy, the environmental savings are dramatic; if powered by fossil fuels, the advantage narrows. The model helps quantify this trade-off.

STEM CHALLENGE GUIDANCE:
Title: Design a Commercial-Scale Cultured Meat Bioreactor
Mission: Design a bioreactor system that can produce cultured meat at commercial scale ($15/kg) while maintaining texture quality comparable to conventional beef.
Scenario: A cellular agriculture startup has proven they can grow cultured beef at lab scale — but it costs $400/kg. They need to reduce costs by 96% while maintaining quality. Your engineering team has been hired to design the bioreactor system that bridges the gap between lab and commercial production.
Introduction: Present the challenge: A cellular agriculture startup has raised $50 million to build the world's first commercial-scale cultured meat factory. Your engineering team must design the bioreactor system — vessel type, capacity, monitoring, medium management, scaffold integration, and waste handling — that produces beef-quality cultured meat at $15/kg or less.

Key Concepts:
• Perfusion Bioreactor Design: Unlike batch reactors (where medium is added once and replaced periodically), perfusion bioreactors continuously flow fresh medium through the culture while removing spent medium and waste products. This maintains more stable growth conditions and supports higher cell densities — critical for commercial-scale production.
• Real-Time Bioprocess Monitoring: Commercial bioreactors use sensors for pH, dissolved oxygen, temperature, glucose, lactate, and cell density — feeding data to control systems that automatically adjust conditions. Advanced facilities use Raman spectroscopy for real-time medium composition analysis and machine learning for predictive process control.
• Techno-Economic Modeling: Before building a factory, engineers create techno-economic models that calculate production costs based on medium consumption, energy use, equipment depreciation, labor, quality control, and facility costs. These models identify which cost reductions have the greatest impact on per-kilogram price — guiding R&D investment priorities.

Evaluation Rubric:
• Expert (4): Design includes detailed bioreactor specification with justified vessel type, monitoring system, medium management strategy, scaffold integration plan, cost projection based on model data, and analysis of scaling challenges
• Proficient (3): Design includes bioreactor type selection, basic monitoring, and cost considerations linked to model findings
• Developing (2): Design covers basic bioreactor concepts but lacks specificity on monitoring, medium management, or cost analysis
• Beginning (1): Design is incomplete or does not connect engineering decisions to the bioreactor optimization model

DIFFERENTIATION:
Support (Struggling Learners):
  • Provide a simplified bioreactor diagram showing inputs (nutrients, oxygen, heat) and outputs (waste, product) with labeled flows
  • Use a cost breakdown template where students can estimate the contribution of each component to total production cost
  • Scaffold optimization thinking: 'If I increase ___, it improves ___ but worsens ___ because ___.'

Extensions (Advanced Learners):
  • Research the current state of the cultured meat industry — which companies are closest to commercial production and what are their remaining technical challenges?
  • Investigate how 3D bioprinting could be used to create structured cultured meat products with realistic marbling and fiber alignment
  • Compare the life cycle environmental analysis of cultured meat versus conventional beef, poultry, and plant-based meat alternatives

Cross-Curricular Connections:
  • Math: Build a techno-economic model calculating production cost per kilogram as a function of medium cost, bioreactor volume, cell density, and cycle time — determine the cost reduction needed for commercial viability
  • ELA: Research and write a consumer communication strategy explaining cultured meat technology to the public — addressing safety, ethics, and taste concerns
  • Economics/Business: Develop a business plan for a cultured meat startup including market analysis, pricing strategy, regulatory pathway, and competitive positioning against conventional and plant-based meat

CAST ALIGNMENT:
• Model the multi-parameter optimization challenge of scaling cultured meat production from lab to commercial viability
• Analyze trade-offs between cell growth rate, texture quality, oxygen delivery, and production cost in bioreactor systems
• Evaluate how scaling factor affects the balance between cost efficiency and product quality in cellular agriculture

CAST-Style Assessment Questions:
• Multiple Choice: A cultured meat company scales their bioreactor from 10 liters to 10,000 liters. Which problem is most likely to worsen at larger scale, based on your model?
• Constructed Response: Using your bioreactor optimization model, explain why cultured meat that tastes identical to conventional beef is so difficult to produce at affordable prices. Reference at least three model components and the trade-offs between them.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Activity Pack

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STUDENT ACTIVITY PACK: Growing Meat Without the Animal
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NAME: _________________________ DATE: _____________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRE-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. What do you think 'lab-grown meat' actually means — how do you grow meat without an animal?

   _________________________________________________________

   _________________________________________________________

2. Why do you think cultured meat currently costs hundreds of dollars per kilogram while conventional beef costs about $10/kg?

   _________________________________________________________

   _________________________________________________________

3. Draw a diagram of what you think a bioreactor for growing meat would look like and what conditions it would need to maintain.

   [DRAWING BOX]

4. What factors do you think determine whether cultured meat tastes and feels like real meat?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VOCABULARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Match the term to the definition:

___ Cellular Agriculture          
___ Bioreactor                    
___ Scaffold                      
___ Growth Factor                 

A. The production of animal products — meat, dairy, leather — directly from cell cultures rather than from whole animals, using techniques borrowed from tissue engineering and bioprocessing
B. A controlled vessel that maintains optimal conditions for cell growth — temperature, pH, oxygen, nutrients — while removing waste products and providing mechanical stimulation for tissue development at industrial scale
C. A three-dimensional structural framework (made from plant proteins, hydrogels, or decellularized tissue) that provides physical support for muscle cells to attach, align, and develop the fibrous texture characteristic of real meat
D. Signaling proteins (like FGF2, TGF-beta, and IGF-1) added to the nutrient medium that instruct cells to proliferate, differentiate into muscle fibers, or organize into tissue — the most expensive component of cultured meat production

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

SCENARIO: Lab Prototype
Settings: Small-scale, optimized conditions
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Maximum Growth
Settings: All inputs maximized for fastest cell division
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Commercial Scale-Up
Settings: Large bioreactor, cost-minimized inputs
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

1. How does your model reveal the multi-dimensional optimization challenge of cultured meat production?

   _________________________________________________________

   _________________________________________________________

2. Which parameter do you think is the most critical bottleneck for commercial viability, and what does your model suggest?

   _________________________________________________________

   _________________________________________________________

3. What trade-offs between Production Cost and Texture Quality did you discover, and which compromises are acceptable?

   _________________________________________________________

   _________________________________________________________

4. How would adding Fat Cell Integration change the bioreactor requirements and production complexity?

   _________________________________________________________

   _________________________________________________________

5. What are the environmental implications of cultured meat compared to conventional livestock farming according to your model's Energy Input data?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
POST-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Can we grow a steak in a lab that tastes, feels, and costs the same as one from a cow — and should we? Explain using evidence from your model:

   _________________________________________________________

   _________________________________________________________

   _________________________________________________________

2. Which NGSS dimensions did this lesson address?
   (Check all that apply)
   □ Science Practice: Developing and Using Models / Constructing Explanations and Designing Solutions
   □ Disciplinary Core Idea: LS1.A Structure and Function / ETS1.C Optimizing the Design Solution
   □ Crosscutting Concept: Systems and System Models / Stability and Change

3. What are the environmental implications of cultured meat compared to conventional livestock farming according to your model's Energy Input data?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEM CHALLENGE: Design a Commercial-Scale Cultured Meat Bioreactor
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MISSION: Design a bioreactor system that can produce cultured meat at commercial scale ($15/kg) while maintaining texture quality comparable to conventional beef.

SCENARIO: A cellular agriculture startup has proven they can grow cultured beef at lab scale — but it costs $400/kg. They need to reduce costs by 96% while maintaining quality. Your engineering team has been hired to design the bioreactor system that bridges the gap between lab and commercial production.

GUIDING QUESTIONS:
• What is the single biggest cost driver in your bioreactor system and how would you reduce it?
• How would you solve the oxygen delivery problem as you scale from milliliters to thousands of liters?
• What trade-offs between texture quality and production cost are acceptable for a commercial product?

DESIGN THINKING:
• What bioreactor configuration would you use — stirred tank, hollow fiber, perfusion, or a novel design?

  _________________________________________________________

• How would you monitor cell health and product quality in real time inside the bioreactor?

  _________________________________________________________

• What recycling or recovery systems would you include to reduce nutrient medium waste?

  _________________________________________________________

• How would you incorporate scaffold structures at commercial scale?

  _________________________________________________________


EVALUATION RUBRIC:
• Expert (4): Design includes detailed bioreactor specification with justified vessel type, monitoring system, medium management strategy, scaffold integration plan, cost projection based on model data, and analysis of scaling challenges
• Proficient (3): Design includes bioreactor type selection, basic monitoring, and cost considerations linked to model findings
• Developing (2): Design covers basic bioreactor concepts but lacks specificity on monitoring, medium management, or cost analysis
• Beginning (1): Design is incomplete or does not connect engineering decisions to the bioreactor optimization model

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Resources

| Resource | Link |
|----------|------|
| Activity Pack (DOCX) | [materials/grade-09/G09L3-L04/G09L3-L04-Student-Activity-Pack.docx] |
| Teacher Guide (DOCX) | [materials/grade-09/G09L3-L04/G09L3-L04-Teachers-Guide.docx] |
| PPT Presentation | [materials/grade-09/G09L3-L04/G09L3-L04-Student-Presentation.pptx] |
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