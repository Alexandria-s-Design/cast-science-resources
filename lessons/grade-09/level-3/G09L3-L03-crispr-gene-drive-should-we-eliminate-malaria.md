# Lesson: CRISPR Gene Drive: Should We Eliminate Malaria?

## Header Information

| Field | Value |
|-------|-------|
| **Lesson ID** | G09L3-L03 |
| **Grade** | 9th Grade — Level 3: Biotech |
| **Lesson Name** | CRISPR Gene Drive: Should We Eliminate Malaria? |
| **Status** | Template |

---

## Platform

### Title
**CRISPR Gene Drive: Should We Eliminate Malaria? — Systems Biology Modeling of Gene Drive Ecology and Ethics**

### Overview
This lesson introduces students to systems biology and synthetic design in the context of gene drive technology — arguably the most powerful and controversial application of CRISPR genetic engineering. Biotech skill focus: Systems biology and synthetic design. Gene drives have the theoretical capacity to alter or eliminate entire wild species, forcing us to confront questions at the intersection of molecular biology, ecology, evolution, and ethics. Students investigate the driving question: We have the technology to make mosquitoes extinct and end malaria forever — but should we? Using the LEVER framework, students identify key components, establish cause-and-effect relationships, run simulations to test scenarios, and extend their understanding through research and engineering challenges.

### Cover Image
[A photorealistic, cinematic image of diverse 14-15 year old students in an advanced genetics lab examining CRISPR gene drive diagrams on holographic displays, with a mosquito specimen under a high-powered microscope visible, dramatic green and gold lighting suggesting the tension between biotech power and ecological responsibility]

### Grade
9th Grade — Level 3: Biotech

### NGSS Standard
**HS-LS3-2, HS-LS4-5**: Make and defend a claim based on evidence that inheritable genetic variations may result from new genetic combinations through meiosis, viable errors occurring during replication, or mutations caused by environmental factors; evaluate the evidence supporting claims that changes in environmental conditions may result in increases in the number of individuals of some species, the emergence of new species over time, and the extinction of other species.

### Learning Objectives
- Build a systems biology model that traces gene drive propagation from molecular genetic mechanisms through mosquito populations to ecosystem-level consequences
- Analyze how gene drive efficiency, resistance evolution, and ecological dependencies interact across scales to determine system-wide outcomes
- Evaluate the trade-offs between eliminating malaria (saving hundreds of thousands of human lives) and the ecological risks of driving a species toward extinction
- Predict long-term unintended consequences of gene drive deployment using multi-generation simulation modeling

### Component List (Starting Model: 9 Components)

| Component | Type | What It Represents |
|-----------|------|-------------------|
| Gene Drive Efficiency | External | The percentage of offspring that inherit the gene drive construct rather than the wild-type gene — in theory 99%+ but reduced by drive resistance mutations, mating competition, and molecular failure rates |
| Mosquito Population | Internal | The total number of Anopheles mosquitoes in the target region, including both gene-drive-carrying individuals and wild-type individuals, which determines malaria transmission capacity |
| Malaria Transmission Rate | Internal | The number of new human malaria infections per mosquito per unit time, which decreases as gene-drive-carrying mosquitoes replace wild-type vectors or as the overall mosquito population declines |
| Wild-Type Gene Frequency | Internal | The proportion of natural, unmodified genes in the mosquito population — as the gene drive spreads, Wild-Type Gene Frequency decreases and the population shifts toward the engineered genotype |
| Ecological Dependence | Internal | The degree to which other species in the ecosystem depend on mosquitoes as a food source, pollinator, or ecological role — bats, birds, fish, and other organisms that would be affected by mosquito population collapse |
| Resistance Evolution | Internal | The rate at which natural selection produces mosquitoes with mutations that block the CRISPR gene drive mechanism — the molecular arms race between the engineered drive and natural genetic variation |
| Geographic Spread Rate | Internal | The speed at which gene-drive-carrying mosquitoes expand beyond the initial release area through natural dispersal, wind patterns, and human-mediated transport — gene drives cannot be geographically contained |
| Human Malaria Cases | Internal | The number of clinical malaria cases in the human population, which decreases as the gene drive reduces mosquito vectoring capacity but may rebound if resistance evolves or if other vector species fill the niche |
| Ecosystem Disruption Risk | Internal | The overall magnitude of ecological consequences from mosquito population decline — measured by food web stability, pollination changes, freshwater ecosystem impacts, and cascading species population shifts |

### Research for Lesson
- CRISPR Gene Drive Mechanism — reference materials and textbook resources
- Malaria: The Scale of the Problem — reference materials and textbook resources
- Ecological Risk Assessment — reference materials and textbook resources
- The Gene Drive Governance Challenge — reference materials and textbook resources

---

## Activity 1: LOCATE — Build Your System

### Text Editor

```
CRISPR GENE DRIVE: SHOULD WE ELIMINATE MALARIA?

Systems Biology Modeling of Gene Drive Ecology and Ethics.
We have the technology to make mosquitoes extinct and end malaria forever — but should we?

That's not just a question — it's something you can MODEL.
And you're about to build exactly that.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1: CHOOSE YOUR COMPONENTS
• Look at the component panel on the RIGHT side of your screen
• Find the EXTERNAL components (things we can't control):
  ○ Click "Gene Drive Efficiency" — the percentage of offspring that inherit the gene drive construct rather than the wild-type gene — in theory 99%+ but reduced by drive resistance mutations
• Find the INTERNAL components (things that change because of other things):
  ○ Click "Mosquito Population" — the total number of anopheles mosquitoes in the target region
  ○ Click "Malaria Transmission Rate" — the number of new human malaria infections per mosquito per unit time
  ○ Click "Wild-Type Gene Frequency" — the proportion of natural
  ○ Click "Ecological Dependence" — the degree to which other species in the ecosystem depend on mosquitoes as a food source
  ○ Click "Resistance Evolution" — the rate at which natural selection produces mosquitoes with mutations that block the crispr gene drive mechanism — the molecular arms race between the engineered drive and natural genetic variation
  ○ Click "Geographic Spread Rate" — the speed at which gene-drive-carrying mosquitoes expand beyond the initial release area through natural dispersal
  ○ Click "Human Malaria Cases" — the number of clinical malaria cases in the human population
  ○ Click "Ecosystem Disruption Risk" — the overall magnitude of ecological consequences from mosquito population decline — measured by food web stability

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
"We have the technology to make mosquitoes extinct and end malaria forever — but should we?

That's what we're going to figure out today. Not by reading about
it — by MODELING it. You're going to build a system that shows
exactly how this works.

Let's build our system. Look at the component panel on the right
side of your screen. You'll see two types of components:

EXTERNAL components — things that come from outside the system.
Inputs we can't directly control.

INTERNAL components — things that change BECAUSE of other things
in the system. They respond to the externals.

Click on 'Gene Drive Efficiency' — that's external. The percentage of offspring that inherit the gene drive construct rather than the wild-type gene — in theory 99%+ but reduced by drive resistance mutations.
Click on 'Mosquito Population' — that's internal. The total number of Anopheles mosquitoes in the target region.
Click on 'Malaria Transmission Rate' — that's internal. The number of new human malaria infections per mosquito per unit time.
Click on 'Wild-Type Gene Frequency' — that's internal. The proportion of natural.
Click on 'Ecological Dependence' — that's internal. The degree to which other species in the ecosystem depend on mosquitoes as a food source.
Click on 'Resistance Evolution' — that's internal. The rate at which natural selection produces mosquitoes with mutations that block the CRISPR gene drive mechanism — the molecular arms race between the engineered drive and natural genetic variation.
Click on 'Geographic Spread Rate' — that's internal. The speed at which gene-drive-carrying mosquitoes expand beyond the initial release area through natural dispersal.
Click on 'Human Malaria Cases' — that's internal. The number of clinical malaria cases in the human population.
Click on 'Ecosystem Disruption Risk' — that's internal. The overall magnitude of ecological consequences from mosquito population decline — measured by food web stability.

Now you need to SORT them. Which ones are external — things that
come from outside the system? Which ones are internal — things
that change because of what's happening inside?

Gene Drive Efficiency is the sole external component because it represents the only parameter that bioengineers directly control — the molecular design of the CRISPR construct determines how efficiently it converts wild-type alleles. All other eight components are internal responses of the biological and ecological system: Mosquito Population, Malaria Transmission Rate, Wild-Type Gene Frequency, Ecological Dependence, Resistance Evolution, Geographic Spread Rate, Human Malaria Cases, and Ecosystem Disruption Risk all emerge from the dynamic interactions between the engineered gene, the mosquito population, the malaria parasite, the ecosystem, and evolution.

Sort your components, then hit the PLUS button to add each one
to your model canvas.

You've got your pieces. But right now they're just sitting there,
not connected. In the next activity, we'll draw the invisible
lines that show how everything affects everything else.

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing 9 components sorted: Gene Drive Efficiency (External), Mosquito Population, Malaria Transmission Rate, Wild-Type Gene Frequency, Ecological Dependence, Resistance Evolution, Geographic Spread Rate, Human Malaria Cases, Ecosystem Disruption Risk (Internal)]

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
• Click on "Gene Drive Efficiency" and drag an arrow to "Wild-Type Gene Frequency"
• Click on "Wild-Type Gene Frequency" and drag an arrow to "Mosquito Population"
• Click on "Mosquito Population" and drag an arrow to "Malaria Transmission Rate"
• Click on "Mosquito Population" and drag an arrow to "Ecosystem Disruption Risk"
• Click on "Resistance Evolution" and drag an arrow to "Gene Drive Efficiency"

STEP 3: SET POSITIVE OR NEGATIVE
• Look at the +/− toggle in the TOP LEFT corner
• For each connection, ask: "When this goes UP, does the other go UP or DOWN?"

  ○ Gene Drive Efficiency → Wild-Type Gene Frequency = NEGATIVE (−)
    Higher Gene Drive Efficiency means more offspring inherit the drive construct instead of wild-type alleles, directly decreasing the frequency of natural genes in the population.

  ○ Wild-Type Gene Frequency → Mosquito Population = POSITIVE (+)
    As Wild-Type Gene Frequency drops (more mosquitoes carry the suppression drive), Mosquito Population declines because drive-carrying females have reduced fertility or the population is modified to prevent malaria transmission.

  ○ Mosquito Population → Malaria Transmission Rate = POSITIVE (+)
    Fewer mosquitoes means fewer opportunities for the Plasmodium parasite to be transmitted between human and mosquito hosts, directly reducing malaria transmission.

  ○ Mosquito Population → Ecosystem Disruption Risk = NEGATIVE (−)
    Declining Mosquito Population increases Ecosystem Disruption Risk as species that depend on mosquitoes for food lose a critical resource, triggering potential cascade effects through the food web.

  ○ Resistance Evolution → Gene Drive Efficiency = NEGATIVE (−)
    As Resistance Evolution increases in the mosquito population, the effective Gene Drive Efficiency decreases because resistant mosquitoes produce offspring that inherit wild-type alleles instead of the drive construct.

STEP 4: CHECK YOUR MODEL
• You should have 5 arrows total
• 3 negative relationship(s), 2 positive relationship(s)
• This is your system model!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THINK ABOUT IT: When Gene Drive Efficiency is set very high, the drive spreads rapidly through the Mosquito Population, causing Wild-Type Gene Frequency to plummet and Human Malaria Cases to drop dramatically. But Ecological Dependence means other species suffer as mosquitoes disappear, and the drive keeps spreading geographically because it cannot be recalled. Meanwhile, Resistance Evolution is working against the drive. Is there a setting where you save the most human lives with the least ecological damage — or is this an impossible trade-off?
```

### Video Script

```
"Your pieces are on the board, but they're not talking to each
other yet. Time to draw the invisible lines — the relationships
that make this a SYSTEM, not just a pile of parts.

Click the 'Connect' icon in the top left corner. Now you're in
connection mode.

First connection: Click on 'Gene Drive Efficiency' and drag an arrow
over to 'Wild-Type Gene Frequency.'

Here's the key question: When gene drive efficiency goes UP, does
wild-type gene frequency go UP or DOWN?

Higher Gene Drive Efficiency means more offspring inherit the drive construct instead of wild-type alleles, directly decreasing the frequency of natural genes in the population.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Next connection: Click on 'Wild-Type Gene Frequency' and drag an arrow
over to 'Mosquito Population.'

Here's the key question: When wild-type gene frequency goes UP, does
mosquito population go UP or DOWN?

As Wild-Type Gene Frequency drops (more mosquitoes carry the suppression drive), Mosquito Population declines because drive-carrying females have reduced fertility or the population is modified to prevent malaria transmission.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Last connection: Click on 'Mosquito Population' and drag an arrow
over to 'Malaria Transmission Rate.'

Here's the key question: When mosquito population goes UP, does
malaria transmission rate go UP or DOWN?

Fewer mosquitoes means fewer opportunities for the Plasmodium parasite to be transmitted between human and mosquito hosts, directly reducing malaria transmission.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Final connection: Click on 'Mosquito Population' and drag an arrow
over to 'Ecosystem Disruption Risk.'

Here's the key question: When mosquito population goes UP, does
ecosystem disruption risk go UP or DOWN?

Declining Mosquito Population increases Ecosystem Disruption Risk as species that depend on mosquitoes for food lose a critical resource, triggering potential cascade effects through the food web.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Final connection: Click on 'Resistance Evolution' and drag an arrow
over to 'Gene Drive Efficiency.'

Here's the key question: When resistance evolution goes UP, does
gene drive efficiency go UP or DOWN?

As Resistance Evolution increases in the mosquito population, the effective Gene Drive Efficiency decreases because resistant mosquitoes produce offspring that inherit wild-type alleles instead of the drive construct.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Look at your model now. You've got 3 negative and 2
positive relationships. 5 arrows total.

When Gene Drive Efficiency is set very high, the drive spreads rapidly through the Mosquito Population, causing Wild-Type Gene Frequency to plummet and Human Malaria Cases to drop dramatically. But Ecological Dependence means other species suffer as mosquitoes disappear, and the drive keeps spreading geographically because it cannot be recalled. Meanwhile, Resistance Evolution is working against the drive. Is there a setting where you save the most human lives with the least ecological damage — or is this an impossible trade-off?

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing connected model with arrows: Gene Drive Efficiency −→ Wild-Type Gene Frequency, Wild-Type Gene Frequency +→ Mosquito Population, Mosquito Population +→ Malaria Transmission Rate, Mosquito Population −→ Ecosystem Disruption Risk, Resistance Evolution −→ Gene Drive Efficiency]

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
• When Gene Drive Efficiency is HIGH, what happens to the internal components?

STEP 3: SCENARIO — MODERATE REGIONAL DEPLOYMENT
• 95% efficiency, single region release
• PREDICT FIRST: What do you predict happens to Wild-Type Gene Frequency over 20 mosquito generations with a 95% efficient gene drive?
• Resume the simulation and observe what happens
• Was your prediction correct?

STEP 4: SCENARIO — RESISTANCE RACE
• 85% efficiency, elevated resistance evolution
• PREDICT FIRST: Do you predict the gene drive will suppress the mosquito population before resistance mutations spread through the population?
• Resume the simulation and observe what happens
• Was your prediction correct?

STEP 5: SCENARIO — GLOBAL MAXIMUM RELEASE
• 99.5% efficiency, global spread
• PREDICT FIRST: What do you predict the ecosystem looks like 50 generations after a near-perfect gene drive is released globally?
• Resume the simulation and observe what happens
• Was your prediction correct?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT DID YOU DISCOVER?
• Gene drives can theoretically spread a modified gene to an entire wild population within 10-20 generations, far faster than any natural evolutionary process — but this speed also means mistakes cannot be undone
• Resistance evolution is nearly inevitable — natural genetic variation ensures that some mosquitoes will carry mutations blocking the CRISPR mechanism, and selection will amplify these resistant genotypes
• The ecological consequences of mosquito elimination are uncertain but potentially significant — mosquitoes serve as food for thousands of species and as pollinators in some ecosystems
• Gene drives cannot be geographically contained — once released, the engineered gene will spread wherever the target species exists, making deployment an irreversible global decision

THE ANSWER: CRISPR gene drives give us the power to eliminate malaria by engineering mosquitoes to either die before transmitting the disease or to become unable to carry the parasite. The technology works because gene drives bias inheritance — instead of the normal 50/50 chance, over 99% of offspring inherit the engineered gene, allowing it to sweep through wild populations in just a few generations. But this power comes with profound risks: gene drives cannot be recalled once released, resistance evolution may undermine the effort, and driving mosquitoes extinct could trigger unpredictable ecological cascades. Systems biology modeling reveals that this isn't a simple yes/no decision — it's a complex optimization problem balancing human lives saved against ecological disruption, with deep uncertainty about long-term consequences. This is perhaps the most consequential bioethics question of the 21st century.
```

### Video Script

```
"You've built the machine. You've wired the connections. Now let's
flip the switch and see if your model matches reality.

Click the 'Play' button in the top left. Watch the graph panel —
you'll see lines representing each component as a percentage.

Let it run. Watch how the components interact at baseline levels.
Everything should be balanced, moving together.

First scenario: Moderate Regional Deployment. 95% efficiency, single region release.
Watch the graph. What do you see happening?

Now let's push the system. Scenario two: Resistance Race.
85% efficiency, elevated resistance evolution.

Before you run it — make a prediction. Do you predict the gene drive will suppress the mosquito population before resistance mutations spread through the population?

Resume the simulation and watch what happens. Did your prediction
match the model? If not, that's actually a GOOD thing — it means
you learned something unexpected.

One more scenario: Global Maximum Release. 99.5% efficiency, global spread.
What do you predict the ecosystem looks like 50 generations after a near-perfect gene drive is released globally?

Here's what our model reveals: CRISPR gene drives give us the power to eliminate malaria by engineering mosquitoes to either die before transmitting the disease or to become unable to carry the parasite. The technology works because gene drives bias inheritance — instead of the normal 50/50 chance, over 99% of offspring inherit the engineered gene, allowing it to sweep through wild populations in just a few generations. But this power comes with profound risks: gene drives cannot be recalled once released, resistance evolution may undermine the effort, and driving mosquitoes extinct could trigger unpredictable ecological cascades. Systems biology modeling reveals that this isn't a simple yes/no decision — it's a complex optimization problem balancing human lives saved against ecological disruption, with deep uncertainty about long-term consequences. This is perhaps the most consequential bioethics question of the 21st century.

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
   • What happens if you turn OFF Gene Drive Efficiency?
   • What happens if you change multiple variables at once?
   • Can you find a combination where the system stays stable?

3. WHAT'S MISSING?
   Your model is simple. Real systems involve more. Think about:

   • Alternative Vector Species — Other mosquito species or biting insects that could potentially fill the ecological niche and become new malaria vectors if Anopheles mosquitoes are suppressed
   • Gene Drive Reversal Mechanism — An engineered 'daisy chain' or 'kill switch' system designed to halt or reverse gene drive spread — still theoretical and unproven in wild populations
   • Climate Change Interaction — The effect of changing temperature and precipitation patterns on mosquito range, breeding habitats, and gene drive spread dynamics — climate change is expanding malaria zones regardless of gene drive deployment

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RESEARCH DIRECTIONS:

Don't just guess — find out! Here's what to look for:

📚 IN YOUR TEXTBOOK:
   • CRISPR Gene Drive Mechanism — how does this connect to your model?
   • Malaria: The Scale of the Problem — how does this connect to your model?

🔍 QUESTIONS TO INVESTIGATE:
   • How does your systems biology model reveal the tension between saving human lives and protecting ecosystem stability?
   • Why is it important that gene drives cannot be geographically contained — what makes this different from other genetic engineering applications?
   • What role does Resistance Evolution play in determining whether the gene drive succeeds or fails, and how predictable is this outcome?
   • How would adding a Gene Drive Reversal Mechanism change your model's predictions and the governance conversation?

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

Alternative Vector Species. Other mosquito species or biting insects that could potentially fill the ecological niche and become new malaria vectors if Anopheles mosquitoes are suppressed
How would you model that?

Gene Drive Reversal Mechanism. An engineered 'daisy chain' or 'kill switch' system designed to halt or reverse gene drive spread — still theoretical and unproven in wild populations
How would you model that?

Climate Change Interaction. The effect of changing temperature and precipitation patterns on mosquito range, breeding habitats, and gene drive spread dynamics — climate change is expanding malaria zones regardless of gene drive deployment
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

Gene Drive Researchers and Conservation Geneticists work at the intersection of genetic engineering and ecology. They develop and evaluate gene drive technologies at institutions like the Target Malaria consortium, DARPA, and academic research labs, earning $80,000–$160,000/year. Bioethicists who evaluate the societal implications of these technologies earn $70,000–$140,000/year.

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
Visual: Title slide with split image — child with malaria on one side, thriving ecosystem on the other
Say: "A child dies of malaria every 60 seconds. We have the technology to stop it — by engineering mosquitoes to carry a self-spreading genetic modification that could wipe them out. But there's a catch: once we release it, we can never take it back."
Do: Start a 60-second timer. Tell students that by the time it ends, another child will have died from malaria. Let the silence speak.
Time: 2 min

SLIDE 2: LEARNING OBJECTIVES
Visual: Learning goals and gene drive vocabulary
Say: "Today you're going to model a technology that can rewrite the genetics of an entire wild species. And then you're going to decide whether we should use it."
Do: Pre-teach gene drive and CRISPR-Cas9. Show a simple animation of gene drive inheritance versus normal Mendelian inheritance.
Time: 3 min

SLIDE 3: BIG QUESTION
Visual: We can eliminate malaria forever — but should we?
Say: "If you could press a button that saves 600,000 lives a year but might permanently alter ecosystems in ways we can't predict — would you press it?"
Do: Anonymous poll: Press or don't press? Record the class results. Tell them the model will help them make a more informed decision.
Time: 3 min

SLIDE 4: LEVER FRAMEWORK
Visual: LEVER steps with systems biology context spanning molecules to ecosystems
Say: "We're building a systems biology model that connects a molecular event — CRISPR cutting DNA — to the extinction of a species and the potential collapse of ecosystems. That's four scales in one model."
Do: Preview LEVER steps. Map the four scales: molecular, population, human health, ecosystem. Emphasize that systems biology integrates all of them.
Time: 2 min

SLIDE 5: ACTIVITY 1: COMPONENTS
Visual: Nine component cards spanning molecular to ecosystem scales
Say: "Only ONE of these nine components is truly under human control — the efficiency of the gene drive we engineer. Everything else is biology responding to our intervention. What does that tell you about the risks?"
Do: Guide component sorting. Discuss why Gene Drive Efficiency is the only truly controllable variable. Map each component to its biological scale.
Time: 8 min

SLIDE 6: ACTIVITY 2: CONNECTIONS
Visual: Complex systems biology web connecting genes to ecosystems
Say: "Trace the cascade: A molecular edit in a mosquito embryo leads to the potential extinction of a species and the collapse of food webs. Map every connection."
Do: Students trace the full causal chain from Gene Drive Efficiency through population suppression to ecological cascade. Identify where Resistance Evolution acts as a brake on the system.
Time: 8 min

SLIDE 7: ACTIVITY 3: SIMULATION
Visual: Multi-generation population dynamics and ecological impact dashboards
Say: "Run these three scenarios and find out: Is there a gene drive setting that eliminates malaria without devastating the ecosystem? Or is that impossible?"
Do: Students predict outcomes for all three scenarios, then run simulations. Track Human Malaria Cases and Ecosystem Disruption Risk simultaneously to visualize the trade-off.
Time: 10 min

SLIDE 8: DISCOVERIES
Visual: Key systems biology findings and ethical dimensions
Say: "Your model just showed you what the world's top geneticists and ecologists are debating right now. There may not be a setting that gives us everything we want. So what do we do?"
Do: Revisit the opening poll. Has anyone changed their mind? Discuss what model evidence changed perspectives. Introduce the concept of irreversible decisions under uncertainty.
Time: 5 min

SLIDE 9: STEM CHALLENGE
Visual: Gene drive governance framework design challenge — UN simulation
Say: "The United Nations just appointed your team to design the rules for gene drive deployment. 600,000 lives hang in the balance — and so does the integrity of Earth's ecosystems. Design the framework."
Do: Groups design governance frameworks including evidence thresholds, decision-making authority, monitoring requirements, and reversal strategies. Present and debate.
Time: 12 min

```

### Teacher Guide

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TEACHER GUIDE: CRISPR Gene Drive: Should We Eliminate Malaria?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LESSON PURPOSE:
This lesson introduces students to systems biology and synthetic design in the context of gene drive technology — arguably the most powerful and controversial application of CRISPR genetic engineering. Biotech skill focus: Systems biology and synthetic design. Gene drives have the theoretical capacity to alter or eliminate entire wild species, forcing us to confront questions at the intersection of molecular biology, ecology, evolution, and ethics.

NGSS ALIGNMENT:
HS-LS3-2, HS-LS4-5: Make and defend a claim based on evidence that inheritable genetic variations may result from new genetic combinations through meiosis, viable errors occurring during replication, or mutations caused by environmental factors; evaluate the evidence supporting claims that changes in environmental conditions may result in increases in the number of individuals of some species, the emergence of new species over time, and the extinction of other species.

THREE-DIMENSIONAL LEARNING:
• Science Practice: Engaging in Argument from Evidence
  Students evaluate competing claims about gene drive deployment using systems biology model data, ecological evidence, and ethical reasoning to construct and defend evidence-based positions.
• Disciplinary Core Idea: LS3.B Variation of Traits / LS4.C Adaptation
  Genetic variation arises through mutation and is shaped by natural selection; gene drives exploit and override natural inheritance mechanisms, with evolutionary consequences for both target and non-target species.
• Crosscutting Concept: Cause and Effect / Systems and System Models
  Students trace causal chains from molecular CRISPR mechanisms through population genetics to ecosystem-level consequences, modeling the system across multiple scales and timescales.

PACING GUIDE:
• Activity 1 (Locate): 8-10 minutes
• Activity 2 (Establish): 8-10 minutes
• Activity 3 (Visualize & Evaluate): 10-12 minutes
• Activity 4 (Revise & Extend): 10-15 minutes
• Total: 50-70 minutes (or split across 2 class periods)

PRE-LESSON PREP:
□ Test ModelIt access on student devices
□ Review vocabulary: Gene Drive, CRISPR-Cas9, Ecological Cascade, Resistance Evolution
□ Prepare We have the technology to make mosquitoes extinct and end malaria forever — but should we discussion hook
□ Have images or video ready for phenomenon introduction

LEVER FRAMEWORK:
• Locate: Students identify nine components spanning molecular genetics (Gene Drive Efficiency, Wild-Type Gene Frequency), population biology (Mosquito Population, Resistance Evolution, Geographic Spread Rate), human health (Malaria Transmission Rate, Human Malaria Cases), and ecology (Ecological Dependence, Ecosystem Disruption Risk).
• Establish: Students determine that Gene Drive Efficiency drives the decline in Wild-Type Gene Frequency, which suppresses Mosquito Population, reducing Malaria Transmission Rate and Human Malaria Cases — while simultaneously increasing Ecosystem Disruption Risk through Ecological Dependence, with Resistance Evolution working to counteract the drive.
• Visualize: Students build a systems biology model connecting molecular gene drive mechanics to population-level dynamics to ecosystem-scale consequences, visualizing the multi-generational spread and its cascading effects.
• Evaluate: Students run moderate, high-resistance, and maximum-efficiency scenarios to map the outcome space — identifying parameter regions where malaria is eliminated, where resistance halts the drive, and where ecological cascades become severe.
• Revise: Students add Alternative Vector Species, Gene Drive Reversal Mechanism, or Climate Change Interaction to explore more realistic and nuanced scenarios.

BACKGROUND CONTENT:
• CRISPR Gene Drive Mechanism:
  A CRISPR gene drive works by encoding the Cas9 protein and a guide RNA within the modified gene itself. When a gene-drive-carrying mosquito mates with a wild-type mosquito, the Cas9 protein cuts the wild-type copy of the gene on the partner chromosome. The cell's DNA repair machinery then uses the gene drive copy as a template, converting the heterozygous cell to homozygous for the drive. This means that instead of inheriting the modified gene 50% of the time (Mendelian), offspring inherit it 99%+ of the time. Over multiple generations, the drive spreads exponentially through the population. Two strategies exist: population suppression drives (carrying genes that reduce female fertility, crashing the population) and population modification drives (carrying genes that make mosquitoes unable to transmit the malaria parasite while maintaining population size).

• Malaria: The Scale of the Problem:
  Malaria kills approximately 600,000 people per year — a child dies every minute. Over 95% of malaria deaths occur in sub-Saharan Africa, and 80% of victims are children under 5. The disease is caused by Plasmodium parasites transmitted by female Anopheles mosquitoes. Despite billions of dollars invested in bed nets, insecticides, and antimalarial drugs, malaria has proven extraordinarily difficult to control because the parasite has evolved resistance to every drug we've developed, and the mosquito has evolved resistance to every insecticide. Gene drives offer a fundamentally different approach — instead of trying to outpace evolution with new chemicals, they co-opt evolution itself to spread the desired trait through the vector population.

• Ecological Risk Assessment:
  The ecological consequences of driving Anopheles mosquitoes extinct are genuinely uncertain. Mosquitoes serve as food for bats, birds, dragonflies, frogs, fish, and spiders. Mosquito larvae are a significant food source in freshwater ecosystems. Some mosquito species pollinate plants (primarily in Arctic regions). However, ecologists are divided on whether mosquitoes are a 'keystone species' whose removal would trigger cascading extinctions, or a replaceable food source whose ecological niche would be filled by other insects. The honest scientific answer is: we don't know. Models can simulate potential cascades, but the complexity of real ecosystems means our predictions carry substantial uncertainty — and the consequences of being wrong are irreversible.

• The Gene Drive Governance Challenge:
  Gene drives present an unprecedented governance challenge because they are inherently transboundary — mosquitoes don't respect national borders. A gene drive released in one country will inevitably spread to neighboring countries and potentially the entire species range. This means the decision to deploy affects every nation in the species' range, yet there is no international body with the authority to make or enforce such decisions. The Convention on Biological Diversity has debated gene drive moratoriums; the African Union has studied the issue extensively; the Target Malaria consortium conducts community engagement in Burkina Faso, Mali, and Uganda. The core ethical tension: children are dying NOW from malaria, but deploying an irreversible technology based on uncertain ecological models risks unforeseen consequences that could last forever. Who decides — and on what evidence basis?

COMMON MISCONCEPTIONS:
• "Gene drives are like GMO crops — contained and controllable"
  Reality: Gene drives are fundamentally different from GMO crops in one critical way: they are designed to spread. GMO crops contain modifications that follow normal Mendelian inheritance and stay in cultivated populations. Gene drives override Mendelian genetics and actively propagate through wild populations across generations and geographic boundaries. There is currently no proven technology to recall a gene drive once released.
  Strategy: Analogy: A GMO crop is like painting your own house a new color. A gene drive is like releasing a paint that automatically repaints every house in the neighborhood — and you can't undo it.

• "If we eliminate mosquitoes, nothing bad will happen because they're just pests"
  Reality: Mosquitoes play multiple ecological roles beyond being human pests. They are a primary food source for bats, birds, dragonflies, fish, and frogs. Mosquito larvae are a major component of freshwater food webs. Some mosquito species are pollinators. While individual ecological roles might be filled by other species, the cascading effects of removing an entire taxon from global ecosystems are genuinely unpredictable. Ecologists are genuinely divided on this question.
  Strategy: Challenge: Name 5 species that eat mosquitoes. Now imagine those species losing a significant food source. What happens to THEIR populations? And what eats THEM?

• "CRISPR is perfectly precise and gene drives will work exactly as designed"
  Reality: CRISPR is remarkably precise but not perfect. Off-target cuts occur, resistance mutations evolve, and molecular mechanisms can fail in ways not predicted by laboratory experiments. The model's Resistance Evolution component captures this reality — natural selection is relentless and creative. Every gene drive experiment in laboratory mosquito populations has observed resistance evolution within 10-25 generations. The question is whether the drive suppresses the population before resistance spreads, not whether resistance will emerge at all.
  Strategy: Show: In lab experiments, CRISPR gene drives reached only 60-80% of the wild mosquito population before resistance plateaued the effect. What does that mean for malaria elimination?

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
Big Question: We have the technology to make mosquitoes extinct and end malaria forever — but should we?
Answer: CRISPR gene drives give us the power to eliminate malaria by engineering mosquitoes to either die before transmitting the disease or to become unable to carry the parasite. The technology works because gene drives bias inheritance — instead of the normal 50/50 chance, over 99% of offspring inherit the engineered gene, allowing it to sweep through wild populations in just a few generations. But this power comes with profound risks: gene drives cannot be recalled once released, resistance evolution may undermine the effort, and driving mosquitoes extinct could trigger unpredictable ecological cascades. Systems biology modeling reveals that this isn't a simple yes/no decision — it's a complex optimization problem balancing human lives saved against ecological disruption, with deep uncertainty about long-term consequences. This is perhaps the most consequential bioethics question of the 21st century.

Simulation Answers:
• Moderate Regional Deployment Scenario: With 95% Gene Drive Efficiency in a single region, Wild-Type Gene Frequency drops rapidly over the first 5-10 generations as the drive spreads through the local Mosquito Population. Human Malaria Cases decline substantially. However, Resistance Evolution begins to accumulate, and by generation 15-20, resistant mosquitoes represent a growing fraction of the population, slowing the drive's progress. Ecosystem Disruption Risk increases moderately as mosquito populations decline. Geographic Spread Rate carries the drive beyond the initial release region.
• Global Maximum Release Scenario: With 99.5% efficiency and global release, the gene drive overwhelms resistance evolution in most populations, driving Wild-Type Gene Frequency toward zero across the species range. Human Malaria Cases plummet toward elimination. However, Ecosystem Disruption Risk escalates dramatically as mosquito populations crash globally — triggering food web disruptions in freshwater and terrestrial ecosystems. The model reveals that complete malaria elimination comes at the cost of significant ecological uncertainty, and the change is irreversible.

Reflection Exemplars:
• Q: Why can't gene drives be geographically contained?
  A: Gene drives spread through reproduction, and mosquitoes do not respect political borders. Once a gene-drive-carrying mosquito mates with a wild-type mosquito from a neighboring region, the drive enters that population and begins spreading there too. The Geographic Spread Rate in the model shows that containment is impossible because mosquitoes naturally disperse through flight and human transport. This means a release decision in one country is effectively a decision for every country in the species' range — making it an inherently global action.
• Q: How should we handle the ethical trade-off between human lives and ecological risk?
  A: The model reveals that there is no setting that maximizes human health benefits while eliminating ecological risk. Every scenario that significantly reduces Human Malaria Cases also increases Ecosystem Disruption Risk. This forces a genuine ethical trade-off: 600,000 real human deaths per year versus uncertain but potentially significant ecological consequences. The uncertainty itself is a key factor — we know with certainty that malaria kills, but we don't know with certainty what ecosystem consequences would follow mosquito suppression. How we weigh certain harm against uncertain risk is a values question, not a purely scientific one.

STEM CHALLENGE GUIDANCE:
Title: Design a Gene Drive Governance Framework
Mission: Design a comprehensive governance framework that determines when, where, and how gene drive technology should be deployed — balancing human health benefits against ecological risks using systems biology evidence.
Scenario: The United Nations has convened a special panel on gene drive technology. Malaria kills 600,000 people per year, mostly children under 5 in sub-Saharan Africa. Gene drive technology could potentially eliminate the disease. But the technology is irreversible once deployed and could have unpredictable ecological consequences. Your team has been appointed to design the governance framework that will determine global policy on gene drive deployment.
Introduction: Present the challenge: The United Nations has convened a special panel on CRISPR gene drive technology for malaria elimination. Your team will design the governance framework that determines global policy — including evidence requirements, decision-making authority, monitoring systems, and reversal strategies. The stakes could not be higher.

Key Concepts:
• Risk-Benefit Analysis Under Uncertainty: Gene drive decisions involve comparing known, quantifiable benefits (malaria deaths prevented) against uncertain, difficult-to-quantify risks (ecological cascade effects). Governance frameworks must establish how much uncertainty is acceptable before deployment and what monitoring evidence would trigger intervention.
• Stakeholder Analysis: Gene drive deployment affects different communities differently. Sub-Saharan African nations bear the burden of malaria but may also depend on mosquito-linked ecosystems. Scientific institutions control the technology. Environmental organizations advocate for ecological caution. A governance framework must determine whose voices count and how conflicts are resolved.
• Precautionary Principle vs. Proactionary Principle: The precautionary principle argues that technologies with irreversible consequences should not be deployed until proven safe. The proactionary principle argues that inaction also has consequences — every year of delay means 600,000 more deaths. Gene drive governance must navigate between these philosophies with explicit criteria for action thresholds.

Evaluation Rubric:
• Expert (4): Framework includes explicit evidence thresholds, inclusive stakeholder process, multi-scale monitoring systems, reversal contingencies, and nuanced treatment of the certainty-uncertainty trade-off, supported by systems biology model evidence
• Proficient (3): Framework addresses evidence requirements, decision authority, and monitoring, with reasoning connected to model findings
• Developing (2): Framework covers basic governance elements but lacks specificity on evidence thresholds or stakeholder inclusion
• Beginning (1): Framework is incomplete or does not connect governance decisions to the systems biology model evidence

DIFFERENTIATION:
Support (Struggling Learners):
  • Provide a simplified gene drive inheritance diagram comparing normal 50/50 Mendelian inheritance to 99%+ gene drive inheritance
  • Use a food web template pre-populated with mosquitoes so students can trace ecological cascades from mosquito population decline
  • Scaffold ethical reasoning: 'The benefit is ___ (quantified as ___). The risk is ___ (uncertain because ___). I recommend ___ because ___.'

Extensions (Advanced Learners):
  • Research the Target Malaria project in Burkina Faso — how is the consortium engaging local communities in gene drive governance decisions?
  • Investigate 'daisy chain' gene drives — self-limiting drives designed to spread through a local population but not persist indefinitely — and model how they change the risk-benefit calculus
  • Compare gene drive mosquito suppression to other malaria control strategies (bed nets, insecticides, vaccines) in terms of cost-effectiveness, scalability, and reversibility

Cross-Curricular Connections:
  • Math: Calculate gene drive spread rates using Hardy-Weinberg equilibrium models modified for non-Mendelian inheritance and compare predicted versus simulated allele frequencies
  • ELA: Write a position paper for the UN panel arguing for or against gene drive deployment, using systems biology model evidence and ethical reasoning frameworks
  • Social Studies/Ethics: Analyze the colonial history of malaria research in Africa and debate who should have authority over gene drive decisions that primarily affect African communities

CAST ALIGNMENT:
• Model gene drive propagation from molecular CRISPR mechanisms through mosquito population genetics to ecosystem-scale ecological consequences
• Analyze the trade-offs between malaria elimination and ecological disruption using multi-generation systems biology simulations
• Evaluate the role of resistance evolution in determining gene drive outcomes and the implications for technology deployment decisions

CAST-Style Assessment Questions:
• Multiple Choice: A gene drive with 95% efficiency is released in a mosquito population. After 15 generations, Wild-Type Gene Frequency begins to increase instead of decrease. Based on your model, what is the most likely explanation?
• Constructed Response: Using your systems biology model, construct an argument for OR against deploying a CRISPR gene drive to eliminate malaria. You must address at least two benefits, two risks, and the role of uncertainty in your recommendation. Reference specific model components and simulation results.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Activity Pack

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STUDENT ACTIVITY PACK: CRISPR Gene Drive: Should We Eliminate Malaria?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NAME: _________________________ DATE: _____________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRE-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. What do you know about CRISPR and how it is used to edit genes?

   _________________________________________________________

   _________________________________________________________

2. Malaria kills about 600,000 people per year — mostly children. If we could eliminate the disease by making mosquitoes extinct, should we?

   _________________________________________________________

   _________________________________________________________

3. Draw a food web that includes mosquitoes — what other species would be affected if mosquitoes disappeared?

   [DRAWING BOX]

4. What does it mean for a gene to 'drive' through a population, and how is this different from normal inheritance?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VOCABULARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Match the term to the definition:

___ Gene Drive                    
___ CRISPR-Cas9                   
___ Ecological Cascade            
___ Resistance Evolution          

A. A genetic engineering technology that biases inheritance to spread a modified gene through a population at rates far exceeding normal Mendelian genetics — from 50% inheritance to over 99% — capable of altering or eliminating entire wild species within a few generations
B. A molecular tool adapted from bacterial immune systems that allows precise cutting and editing of DNA at specific locations — the 'molecular scissors' that make gene drives technically possible by cutting the wild-type gene and forcing the cell to copy the drive sequence
C. A chain reaction through an ecosystem where the removal or addition of one species triggers population changes in multiple other species — predators, prey, competitors, pollinators, and decomposers — that ripple through the entire food web
D. The inevitable process by which natural selection favors organisms that develop genetic resistance to the gene drive — mutations that prevent CRISPR from cutting the target site, potentially rendering the drive ineffective before the goal is achieved

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

SCENARIO: Moderate Regional Deployment
Settings: 95% efficiency, single region release
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Resistance Race
Settings: 85% efficiency, elevated resistance evolution
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Global Maximum Release
Settings: 99.5% efficiency, global spread
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

1. How does your systems biology model reveal the tension between saving human lives and protecting ecosystem stability?

   _________________________________________________________

   _________________________________________________________

2. Why is it important that gene drives cannot be geographically contained — what makes this different from other genetic engineering applications?

   _________________________________________________________

   _________________________________________________________

3. What role does Resistance Evolution play in determining whether the gene drive succeeds or fails, and how predictable is this outcome?

   _________________________________________________________

   _________________________________________________________

4. How would adding a Gene Drive Reversal Mechanism change your model's predictions and the governance conversation?

   _________________________________________________________

   _________________________________________________________

5. What are the ethical implications of a technology that makes irreversible changes to wild species — who has the right to make that decision?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
POST-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. We have the technology to make mosquitoes extinct and end malaria forever — but should we? Explain using evidence from your model:

   _________________________________________________________

   _________________________________________________________

   _________________________________________________________

2. Which NGSS dimensions did this lesson address?
   (Check all that apply)
   □ Science Practice: Engaging in Argument from Evidence
   □ Disciplinary Core Idea: LS3.B Variation of Traits / LS4.C Adaptation
   □ Crosscutting Concept: Cause and Effect / Systems and System Models

3. What are the ethical implications of a technology that makes irreversible changes to wild species — who has the right to make that decision?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEM CHALLENGE: Design a Gene Drive Governance Framework
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MISSION: Design a comprehensive governance framework that determines when, where, and how gene drive technology should be deployed — balancing human health benefits against ecological risks using systems biology evidence.

SCENARIO: The United Nations has convened a special panel on gene drive technology. Malaria kills 600,000 people per year, mostly children under 5 in sub-Saharan Africa. Gene drive technology could potentially eliminate the disease. But the technology is irreversible once deployed and could have unpredictable ecological consequences. Your team has been appointed to design the governance framework that will determine global policy on gene drive deployment.

GUIDING QUESTIONS:
• What evidence threshold should be required before approving gene drive deployment?
• Who should have the authority to decide whether to release a gene drive — and should affected communities have veto power?
• What monitoring systems would you require to detect unintended ecological consequences?

DESIGN THINKING:
• How would you design a 'kill switch' or recall mechanism for the gene drive if unintended consequences are detected?

  _________________________________________________________

• What international agreements would need to exist before a gene drive that crosses national borders is released?

  _________________________________________________________

• How do you weigh 600,000 human deaths per year against uncertain ecological risks that may or may not materialize?

  _________________________________________________________

• What role should the communities most affected by malaria play in the decision-making process?

  _________________________________________________________


EVALUATION RUBRIC:
• Expert (4): Framework includes explicit evidence thresholds, inclusive stakeholder process, multi-scale monitoring systems, reversal contingencies, and nuanced treatment of the certainty-uncertainty trade-off, supported by systems biology model evidence
• Proficient (3): Framework addresses evidence requirements, decision authority, and monitoring, with reasoning connected to model findings
• Developing (2): Framework covers basic governance elements but lacks specificity on evidence thresholds or stakeholder inclusion
• Beginning (1): Framework is incomplete or does not connect governance decisions to the systems biology model evidence

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Resources

| Resource | Link |
|----------|------|
| Activity Pack (DOCX) | [materials/grade-09/G09L3-L03/G09L3-L03-Student-Activity-Pack.docx] |
| Teacher Guide (DOCX) | [materials/grade-09/G09L3-L03/G09L3-L03-Teachers-Guide.docx] |
| PPT Presentation | [materials/grade-09/G09L3-L03/G09L3-L03-Student-Presentation.pptx] |
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