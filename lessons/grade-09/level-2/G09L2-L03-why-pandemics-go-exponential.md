# Lesson: Why Pandemics Go Exponential

## Header Information

| Field | Value |
|-------|-------|
| **Lesson ID** | G09L2-L03 |
| **Grade** | 9th Grade — Level 2: Advanced |
| **Lesson Name** | Why Pandemics Go Exponential |
| **Status** | Template |

---

## Platform

### Title
**Why Pandemics Go Exponential — The Math Behind How One Infection Becomes a Global Crisis**

### Overview
This lesson uses a coupled compartment model (SIR dynamics) to explore how infectious diseases spread through populations. The model demonstrates coupled system dynamics — the flow between Susceptible, Infected, and Recovered compartments depends on the state of multiple compartments simultaneously. Students will explore exponential growth in the early epidemic phase, the natural balancing feedback as susceptible populations deplete, and how interventions (quarantine and vaccination) modify the system's behavior. The lesson connects mathematical reasoning (R₀, herd immunity threshold) with public health decision-making. Students investigate the driving question: How does one person's infection become a global pandemic in weeks? Using the LEVER framework, students identify key components, establish cause-and-effect relationships, run simulations to test scenarios, and extend their understanding through research and engineering challenges.

### Cover Image
[A photorealistic, cinematic visualization of a network of connected people with infection spreading through connections shown as glowing pathways, transitioning from green (healthy) to red (infected) to blue (recovered), dark background with dramatic lighting]

### Grade
9th Grade — Level 2: Advanced

### NGSS Standard
**HS-LS2-6, HS-ETS1-4**: Evaluate claims, evidence, and reasoning that the complex interactions in ecosystems maintain relatively consistent numbers and types of organisms in stable conditions, but changing conditions may result in a new ecosystem. Use a computer simulation to model the impact of proposed solutions to a complex real-world problem with numerous criteria and constraints, including the analysis of system interactions and component interactions.

### Learning Objectives
- Model SIR (Susceptible-Infected-Recovered) disease dynamics using a coupled compartment system
- Explain how contact rate and transmission rate drive exponential growth in the early stages of an outbreak
- Analyze how interventions (vaccination, quarantine) create balancing feedback that counteracts exponential spread
- Predict the effects of different intervention timing on total infections and peak hospital burden
- Evaluate the trade-offs between early aggressive intervention and delayed response

### Component List (Starting Model: 7 Components)

| Component | Type | What It Represents |
|-----------|------|-------------------|
| Susceptible Population | Internal | The number of people who have not yet been infected and have no immunity — decreases as people get infected or vaccinated |
| Infected Population | Internal | The number of people currently infectious and capable of spreading the disease — increases with new infections and decreases with recovery |
| Recovered Population | Internal | The number of people who have recovered and gained immunity — increases as infected people recover and are removed from the transmission chain |
| Contact Rate | External | The average number of close contacts per person per day — affected by social behavior, population density, and public health measures |
| Transmission Rate | Internal | The probability that a contact between an infected and susceptible person results in transmission — determined by pathogen biology and hygiene practices |
| Vaccination Rate | External | The number of susceptible people vaccinated per day, moving them directly from Susceptible to Recovered without going through infection |
| Quarantine Effectiveness | External | How effectively quarantine measures reduce the Contact Rate — ranging from 0% (no quarantine) to near 100% (complete isolation) |

### Research for Lesson
- The SIR Model — reference materials and textbook resources
- R-naught and Exponential Growth — reference materials and textbook resources
- Herd Immunity and Natural Balancing Feedback — reference materials and textbook resources
- Interventions: Changing the System — reference materials and textbook resources
- Beyond Basic SIR — reference materials and textbook resources

---

## Activity 1: LOCATE — Build Your System

### Text Editor

```
WHY PANDEMICS GO EXPONENTIAL

The Math Behind How One Infection Becomes a Global Crisis.
How does one person's infection become a global pandemic in weeks?

That's not just a question — it's something you can MODEL.
And you're about to build exactly that.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1: CHOOSE YOUR COMPONENTS
• Look at the component panel on the RIGHT side of your screen
• Find the EXTERNAL components (things we can't control):
  ○ Click "Contact Rate" — the average number of close contacts per person per day — affected by social behavior
  ○ Click "Vaccination Rate" — the number of susceptible people vaccinated per day
  ○ Click "Quarantine Effectiveness" — how effectively quarantine measures reduce the contact rate — ranging from 0% (no quarantine) to near 100% (complete isolation)
• Find the INTERNAL components (things that change because of other things):
  ○ Click "Susceptible Population" — the number of people who have not yet been infected and have no immunity — decreases as people get infected or vaccinated
  ○ Click "Infected Population" — the number of people currently infectious and capable of spreading the disease — increases with new infections and decreases with recovery
  ○ Click "Recovered Population" — the number of people who have recovered and gained immunity — increases as infected people recover and are removed from the transmission chain
  ○ Click "Transmission Rate" — the probability that a contact between an infected and susceptible person results in transmission — determined by pathogen biology and hygiene practices

STEP 2: ADD TO YOUR MODEL
• Click the PLUS (+) button to add each component to your picture
• You should now see 7 components on your canvas

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
"How does one person's infection become a global pandemic in weeks?

That's what we're going to figure out today. Not by reading about
it — by MODELING it. You're going to build a system that shows
exactly how this works.

Let's build our system. Look at the component panel on the right
side of your screen. You'll see two types of components:

EXTERNAL components — things that come from outside the system.
Inputs we can't directly control.

INTERNAL components — things that change BECAUSE of other things
in the system. They respond to the externals.

Click on 'Susceptible Population' — that's internal. The number of people who have not yet been infected and have no immunity — decreases as people get infected or vaccinated.
Click on 'Infected Population' — that's internal. The number of people currently infectious and capable of spreading the disease — increases with new infections and decreases with recovery.
Click on 'Recovered Population' — that's internal. The number of people who have recovered and gained immunity — increases as infected people recover and are removed from the transmission chain.
Click on 'Contact Rate' — that's external. The average number of close contacts per person per day — affected by social behavior.
Click on 'Transmission Rate' — that's internal. The probability that a contact between an infected and susceptible person results in transmission — determined by pathogen biology and hygiene practices.
Click on 'Vaccination Rate' — that's external. The number of susceptible people vaccinated per day.
Click on 'Quarantine Effectiveness' — that's external. How effectively quarantine measures reduce the Contact Rate — ranging from 0% (no quarantine) to near 100% (complete isolation).

Now you need to SORT them. Which ones are external — things that
come from outside the system? Which ones are internal — things
that change because of what's happening inside?

Contact Rate, Vaccination Rate, and Quarantine Effectiveness are external components because they represent human decisions and interventions — we can choose to implement quarantine, vaccinate at a certain rate, or modify social behavior. Susceptible Population, Infected Population, and Recovered Population are internal because they are determined by the coupled flows between compartments. Transmission Rate is internal because it is determined by pathogen biology, not human choice (though hygiene can modify it). The key insight is that the three compartments are coupled — the flow from S to I depends on both S and I simultaneously, which is what creates exponential dynamics.

Sort your components, then hit the PLUS button to add each one
to your model canvas.

You've got your pieces. But right now they're just sitting there,
not connected. In the next activity, we'll draw the invisible
lines that show how everything affects everything else.

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing 7 components sorted: Contact Rate, Vaccination Rate, Quarantine Effectiveness (External), Susceptible Population, Infected Population, Recovered Population, Transmission Rate (Internal)]

### Graph
[Empty graph panel — no simulation yet]

---

## Activity 2: ESTABLISH — Connect the Relationships

### Text Editor

```
TIME TO DRAW THE INVISIBLE LINES

Those 7 components don't just sit there — they AFFECT each other.
When one changes, others change too. Let's map those connections.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1: OPEN CONNECTION MODE
• Click the "Connect" icon in the TOP LEFT corner of your screen
• Your cursor is now ready to draw relationship arrows

STEP 2: DRAW YOUR RELATIONSHIPS
• Click on "Contact Rate" and drag an arrow to "Infected Population"
• Click on "Susceptible Population" and drag an arrow to "Infected Population"
• Click on "Infected Population" and drag an arrow to "Susceptible Population"
• Click on "Infected Population" and drag an arrow to "Recovered Population"
• Click on "Vaccination Rate" and drag an arrow to "Susceptible Population"
• Click on "Quarantine Effectiveness" and drag an arrow to "Contact Rate"
• Click on "Transmission Rate" and drag an arrow to "Infected Population"

STEP 3: SET POSITIVE OR NEGATIVE
• Look at the +/− toggle in the TOP LEFT corner
• For each connection, ask: "When this goes UP, does the other go UP or DOWN?"

  ○ Contact Rate → Infected Population = POSITIVE (+)
    Higher Contact Rate means each infected person encounters more susceptible people per day, increasing the rate of new infections. This is the primary target of quarantine interventions.

  ○ Susceptible Population → Infected Population = POSITIVE (+)
    A larger Susceptible Population provides more potential targets for infection. As S decreases (through infection or vaccination), the rate of new infections naturally slows — this is the balancing feedback that eventually ends epidemics.

  ○ Infected Population → Susceptible Population = NEGATIVE (−)
    More Infected individuals deplete the Susceptible population faster, as susceptible people become infected. This coupling means the flow rate depends on BOTH compartments simultaneously.

  ○ Infected Population → Recovered Population = POSITIVE (+)
    More Infected individuals means more people recovering over time, increasing the Recovered population and building herd immunity.

  ○ Vaccination Rate → Susceptible Population = NEGATIVE (−)
    Vaccination moves people directly from Susceptible to Recovered, reducing the susceptible pool without requiring infection. This is the most efficient path to herd immunity.

  ○ Quarantine Effectiveness → Contact Rate = NEGATIVE (−)
    Higher Quarantine Effectiveness reduces the effective Contact Rate, lowering R₀ and slowing transmission. This intervention modifies the system's behavior without changing the pathogen itself.

  ○ Transmission Rate → Infected Population = POSITIVE (+)
    Higher Transmission Rate means each contact is more likely to result in infection, increasing the flow from S to I and driving higher R₀.

STEP 4: CHECK YOUR MODEL
• You should have 7 arrows total
• 3 negative relationship(s), 4 positive relationship(s)
• This is your system model!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THINK ABOUT IT: In the early stages of a pandemic, every infected person contacts many susceptible people. But as more people get infected and recover, there are fewer susceptible people to infect. How does this natural depletion of the susceptible population create a balancing feedback loop — and why isn't that enough to prevent catastrophe?
```

### Video Script

```
"Your pieces are on the board, but they're not talking to each
other yet. Time to draw the invisible lines — the relationships
that make this a SYSTEM, not just a pile of parts.

Click the 'Connect' icon in the top left corner. Now you're in
connection mode.

First connection: Click on 'Contact Rate' and drag an arrow
over to 'Infected Population.'

Here's the key question: When contact rate goes UP, does
infected population go UP or DOWN?

Higher Contact Rate means each infected person encounters more susceptible people per day, increasing the rate of new infections. This is the primary target of quarantine interventions.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Next connection: Click on 'Susceptible Population' and drag an arrow
over to 'Infected Population.'

Here's the key question: When susceptible population goes UP, does
infected population go UP or DOWN?

A larger Susceptible Population provides more potential targets for infection. As S decreases (through infection or vaccination), the rate of new infections naturally slows — this is the balancing feedback that eventually ends epidemics.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Last connection: Click on 'Infected Population' and drag an arrow
over to 'Susceptible Population.'

Here's the key question: When infected population goes UP, does
susceptible population go UP or DOWN?

More Infected individuals deplete the Susceptible population faster, as susceptible people become infected. This coupling means the flow rate depends on BOTH compartments simultaneously.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Final connection: Click on 'Infected Population' and drag an arrow
over to 'Recovered Population.'

Here's the key question: When infected population goes UP, does
recovered population go UP or DOWN?

More Infected individuals means more people recovering over time, increasing the Recovered population and building herd immunity.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Final connection: Click on 'Vaccination Rate' and drag an arrow
over to 'Susceptible Population.'

Here's the key question: When vaccination rate goes UP, does
susceptible population go UP or DOWN?

Vaccination moves people directly from Susceptible to Recovered, reducing the susceptible pool without requiring infection. This is the most efficient path to herd immunity.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Final connection: Click on 'Quarantine Effectiveness' and drag an arrow
over to 'Contact Rate.'

Here's the key question: When quarantine effectiveness goes UP, does
contact rate go UP or DOWN?

Higher Quarantine Effectiveness reduces the effective Contact Rate, lowering R₀ and slowing transmission. This intervention modifies the system's behavior without changing the pathogen itself.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Final connection: Click on 'Transmission Rate' and drag an arrow
over to 'Infected Population.'

Here's the key question: When transmission rate goes UP, does
infected population go UP or DOWN?

Higher Transmission Rate means each contact is more likely to result in infection, increasing the flow from S to I and driving higher R₀.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Look at your model now. You've got 3 negative and 4
positive relationships. 7 arrows total.

In the early stages of a pandemic, every infected person contacts many susceptible people. But as more people get infected and recover, there are fewer susceptible people to infect. How does this natural depletion of the susceptible population create a balancing feedback loop — and why isn't that enough to prevent catastrophe?

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing connected model with arrows: Contact Rate +→ Infected Population, Susceptible Population +→ Infected Population, Infected Population −→ Susceptible Population, Infected Population +→ Recovered Population, Vaccination Rate −→ Susceptible Population, Quarantine Effectiveness −→ Contact Rate, Transmission Rate +→ Infected Population]

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
• When Contact Rate is HIGH, what happens to the internal components?

STEP 3: SCENARIO — UNCONTROLLED EPIDEMIC
• High contact rate, no interventions
• PREDICT FIRST: What do you predict the shape of the Infected Population curve will look like over time? Will it keep growing forever, or will it peak and decline? Why?
• Resume the simulation and observe what happens
• Was your prediction correct?

STEP 4: SCENARIO — EARLY VS. LATE INTERVENTION
• Quarantine at 1% infected vs. 10% infected
• PREDICT FIRST: Do you predict that the TIMING of quarantine matters more than its strength? What will be the difference in total infections between early and late intervention?
• Resume the simulation and observe what happens
• Was your prediction correct?

STEP 5: SCENARIO — VACCINATION EFFECT
• Moderate vaccination rate throughout epidemic
• PREDICT FIRST: How do you predict vaccination changes the herd immunity threshold? At what percentage of vaccinated population will the epidemic stop growing?
• Resume the simulation and observe what happens
• Was your prediction correct?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT DID YOU DISCOVER?
• Pandemics grow exponentially because every infected person creates multiple new infections — each of whom creates multiple more
• The SIR model shows that epidemics naturally peak and decline as the susceptible population is depleted, but the damage before the peak can be catastrophic
• Timing of intervention matters enormously: the same quarantine implemented at 1% vs. 10% infection can reduce total infections by 50% or more
• Vaccination creates a shortcut from Susceptible to Recovered, building immunity without the disease — reducing both the peak and total infections
• R₀ determines epidemic dynamics: above 1, the epidemic grows; below 1, it shrinks. Every intervention aims to push R₀ below 1
• The three compartments (S, I, R) are coupled — changes in one directly affect the flows to and from the others

THE ANSWER: One infection becomes a pandemic through exponential growth: if each infected person infects 2-3 others (R₀ of 2-3), one case becomes 3, then 9, then 27, then 81. Within 20 generations of transmission (which can take just weeks), millions are infected. The SIR model shows this happens because the Susceptible population is large and the transmission chain grows proportionally. Interventions work by reducing R₀ below 1 — through quarantine (reducing contact rate), vaccination (reducing susceptible population), or both. The critical insight is that timing matters enormously: early intervention prevents far more infections than the same intervention applied later.
```

### Video Script

```
"You've built the machine. You've wired the connections. Now let's
flip the switch and see if your model matches reality.

Click the 'Play' button in the top left. Watch the graph panel —
you'll see lines representing each component as a percentage.

Let it run. Watch how the components interact at baseline levels.
Everything should be balanced, moving together.

First scenario: Uncontrolled Epidemic. High contact rate, no interventions.
Watch the graph. What do you see happening?

Now let's push the system. Scenario two: Early vs. Late Intervention.
Quarantine at 1% infected vs. 10% infected.

Before you run it — make a prediction. Do you predict that the TIMING of quarantine matters more than its strength? What will be the difference in total infections between early and late intervention?

Resume the simulation and watch what happens. Did your prediction
match the model? If not, that's actually a GOOD thing — it means
you learned something unexpected.

One more scenario: Vaccination Effect. Moderate vaccination rate throughout epidemic.
How do you predict vaccination changes the herd immunity threshold? At what percentage of vaccinated population will the epidemic stop growing?

Here's what our model reveals: One infection becomes a pandemic through exponential growth: if each infected person infects 2-3 others (R₀ of 2-3), one case becomes 3, then 9, then 27, then 81. Within 20 generations of transmission (which can take just weeks), millions are infected. The SIR model shows this happens because the Susceptible population is large and the transmission chain grows proportionally. Interventions work by reducing R₀ below 1 — through quarantine (reducing contact rate), vaccination (reducing susceptible population), or both. The critical insight is that timing matters enormously: early intervention prevents far more infections than the same intervention applied later.

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
   • What happens if you turn OFF Contact Rate?
   • What happens if you turn OFF Vaccination Rate?
   • What happens if you turn OFF Quarantine Effectiveness?
   • What happens if you change multiple variables at once?
   • Can you find a combination where the system stays stable?

3. WHAT'S MISSING?
   Your model is simple. Real systems involve more. Think about:

   • Hospital Capacity — The maximum number of patients the healthcare system can treat simultaneously — when exceeded, mortality increases dramatically
   • Asymptomatic Transmission Rate — The percentage of infected people who show no symptoms but can still transmit the disease, making detection and isolation much harder
   • Reinfection Rate — The rate at which recovered individuals lose immunity and become susceptible again, turning the SIR model into an SIRS model with no permanent recovery

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RESEARCH DIRECTIONS:

Don't just guess — find out! Here's what to look for:

📚 IN YOUR TEXTBOOK:
   • The SIR Model — how does this connect to your model?
   • R-naught and Exponential Growth — how does this connect to your model?

🔍 QUESTIONS TO INVESTIGATE:
   • Why does the epidemic curve naturally peak and decline even without intervention? What does this tell you about the SIR model's built-in balancing feedback?
   • Your model shows that the same quarantine implemented at 1% infection vs. 10% produces dramatically different outcomes. Why does timing matter so much in exponential systems?
   • How does vaccination change the dynamics compared to quarantine? Which intervention affects which component of the SIR model?
   • What real-world factors make pandemic modeling more complicated than the basic SIR model?

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

Your model has 7 components. Real systems involve
way more. Think about...

Hospital Capacity. The maximum number of patients the healthcare system can treat simultaneously — when exceeded, mortality increases dramatically
How would you model that?

Asymptomatic Transmission Rate. The percentage of infected people who show no symptoms but can still transmit the disease, making detection and isolation much harder
How would you model that?

Reinfection Rate. The rate at which recovered individuals lose immunity and become susceptible again, turning the SIR model into an SIRS model with no permanent recovery
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

Epidemiologists and Public Health Modelers study disease transmission patterns and design intervention strategies. They work at the CDC, WHO, state health departments, and academic research centers, earning $75,000–$150,000/year. During the COVID-19 pandemic, their models directly informed decisions affecting billions of people.

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
Visual: Network visualization of infection spreading through connected people
Say: "In December 2019, a single person in Wuhan, China had a cough. Three months later, the entire world was in lockdown. How did ONE infection become a GLOBAL pandemic?"
Do: Show a visualization of COVID-19's global spread over time. Let students react. Ask: 'What mathematical pattern could explain something spreading this fast?'
Time: 3 min

SLIDE 2: LEARNING OBJECTIVES
Visual: Learning goals, SIR diagram, and vocabulary
Say: "Today we're building the exact type of model that scientists used to predict COVID-19's spread and to design the interventions that saved millions of lives."
Do: Introduce the SIR framework visually. Pre-teach R₀ with a concrete example: 'If one person infects 3 others, and each of those infects 3 more, how many are infected after 10 rounds?' Let students calculate (59,049).
Time: 4 min

SLIDE 3: BIG QUESTION
Visual: How does one person's infection become a global pandemic in weeks?
Say: "The answer is exponential growth. And the terrifying thing about exponential growth is that it's almost impossible for human brains to intuit. Let me show you why."
Do: Classic doubling problem: 'If a pond has lily pads that double daily and the pond is full on day 30, when was it half full?' (Day 29.) 'When was it 1% full?' (Day 23.) This illustrates why exponential problems seem manageable until they're catastrophic.
Time: 4 min

SLIDE 4: LEVER FRAMEWORK
Visual: LEVER steps with SIR compartment overview
Say: "We're building a coupled compartment model — three population groups connected by flows that depend on each other. This is the most sophisticated model type we've built."
Do: Draw S, I, and R boxes on the board with arrows. Ask: 'What determines how fast people move from S to I? What determines how fast they move from I to R?' Build intuition for the coupled dynamics.
Time: 3 min

SLIDE 5: ACTIVITY 1: COMPONENTS
Visual: Seven component cards with compartment and control sorting
Say: "We have three populations that people flow between, plus external controls that modify the flows. Sort them — but think carefully about which are internal dynamics and which are human decisions."
Do: Guide component sorting. Key insight: Susceptible, Infected, and Recovered are coupled internal compartments. Contact Rate, Vaccination Rate, and Quarantine Effectiveness are external because humans control them. Transmission Rate is internal (determined by pathogen biology).
Time: 8 min

SLIDE 6: ACTIVITY 2: CONNECTIONS
Visual: Coupled compartment flow diagram with intervention points
Say: "Map the flows between compartments. The critical question: why does the flow from S to I depend on BOTH the number of Susceptible AND the number of Infected people?"
Do: Students map coupled flows. Emphasize: new infections require BOTH a susceptible person AND an infected person to make contact. This coupling is why the SIR model is more complex than a simple linear system. Identify where each intervention (quarantine, vaccination) modifies the system.
Time: 10 min

SLIDE 7: ACTIVITY 3: SIMULATION
Visual: Epidemic curve comparisons: uncontrolled, early quarantine, late quarantine, vaccination
Say: "Four scenarios. Uncontrolled epidemic, early quarantine at 1%, late quarantine at 10%, and vaccination. Predict FIRST, then run. The timing comparison will surprise you."
Do: Students predict outcomes before running each scenario. Key revelation: the same quarantine at 1% vs. 10% can reduce total infections by half or more. Have students calculate: if the epidemic doubles every 3 days, how many more people are infected in the 2 weeks between 1% and 10%? This quantifies the cost of delay.
Time: 12 min

SLIDE 8: DISCOVERIES
Visual: Key findings with real-world COVID-19 comparisons
Say: "Your model just showed you what every epidemiologist tried to tell the world in March 2020: in exponential systems, acting one week early saves more lives than acting one month late with ten times the resources."
Do: Connect model findings to real COVID-19 data. Compare countries that locked down early vs. late. Discuss: 'Why is it so hard for leaders to act early, when the numbers still look small?' This is the core challenge of exponential thinking.
Time: 5 min

SLIDE 9: STEM CHALLENGE
Visual: Pandemic response decision tool design challenge
Say: "Build a tool that helps health officials make the hardest decision in public health: when to act. Your tool needs to show what happens if they act NOW versus if they wait."
Do: Groups design decision support tools using model data. Key requirement: the tool must show the 'cost of waiting' clearly. Groups present and peer-evaluate on usability, accuracy, and decision-support value.
Time: 12 min

```

### Teacher Guide

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TEACHER GUIDE: Why Pandemics Go Exponential
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LESSON PURPOSE:
This lesson uses a coupled compartment model (SIR dynamics) to explore how infectious diseases spread through populations. The model demonstrates coupled system dynamics — the flow between Susceptible, Infected, and Recovered compartments depends on the state of multiple compartments simultaneously. Students will explore exponential growth in the early epidemic phase, the natural balancing feedback as susceptible populations deplete, and how interventions (quarantine and vaccination) modify the system's behavior. The lesson connects mathematical reasoning (R₀, herd immunity threshold) with public health decision-making.

NGSS ALIGNMENT:
HS-LS2-6, HS-ETS1-4: Evaluate claims, evidence, and reasoning that the complex interactions in ecosystems maintain relatively consistent numbers and types of organisms in stable conditions, but changing conditions may result in a new ecosystem. Use a computer simulation to model the impact of proposed solutions to a complex real-world problem with numerous criteria and constraints, including the analysis of system interactions and component interactions.

THREE-DIMENSIONAL LEARNING:
• Science Practice: Using Mathematics and Computational Thinking
  Students use the SIR compartmental model to quantitatively analyze disease transmission dynamics, calculate R₀, and predict the effects of interventions on epidemic trajectories.
• Disciplinary Core Idea: LS2.C Ecosystem Dynamics / ETS1.B Developing Solutions
  Complex interactions in populations (disease transmission) can maintain or disrupt stability. Students use computational models to evaluate intervention strategies for a complex real-world problem.
• Crosscutting Concept: Systems and System Models
  Students model populations as interconnected compartments where flows between compartments depend on the state of multiple components, demonstrating coupled system dynamics.

PACING GUIDE:
• Activity 1 (Locate): 8-10 minutes
• Activity 2 (Establish): 8-10 minutes
• Activity 3 (Visualize & Evaluate): 10-12 minutes
• Activity 4 (Revise & Extend): 10-15 minutes
• Total: 50-70 minutes (or split across 2 class periods)

PRE-LESSON PREP:
□ Test ModelIt access on student devices
□ Review vocabulary: SIR Model, R-naught (R₀), Exponential Growth, Herd Immunity Threshold, Flattening the Curve, Coupled Compartments
□ Prepare How does one person's infection become a global pandemic in weeks discussion hook
□ Have images or video ready for phenomenon introduction

LEVER FRAMEWORK:
• Locate: Students identify seven components across three types: three internal compartment variables (Susceptible, Infected, Recovered), one internal rate (Transmission Rate), and three external controls (Contact Rate, Vaccination Rate, Quarantine Effectiveness). Students recognize that the three compartments are coupled — changes in one directly affect flows to the others.
• Establish: Students map the coupled flows: Susceptible → Infected (driven by contact between S and I) and Infected → Recovered (driven by recovery time). They identify the reinforcing loop in early epidemic (more I → more new infections) and the natural balancing loop (more R → fewer S → fewer new infections). They determine how each external control modifies these flows.
• Visualize: Students build a coupled compartment model showing how Contact Rate and Transmission Rate drive the flow from Susceptible to Infected, how recovery drives the flow from Infected to Recovered, and how Vaccination Rate and Quarantine Effectiveness modify these dynamics. The model must demonstrate exponential growth, natural peak, and decline.
• Evaluate: Students run uncontrolled, early intervention, late intervention, and vaccination scenarios. They quantify the difference in total infections and peak infected population between early and late quarantine, discovering that timing is often more important than intensity in exponential systems.
• Revise: Students extend the model with Hospital Capacity (threshold effect on mortality), Asymptomatic Transmission Rate, or Reinfection Rate to explore how real-world complexity changes the basic SIR dynamics.

BACKGROUND CONTENT:
• The SIR Model:
  The SIR model is one of the foundational tools in epidemiology. It divides a population into three compartments: Susceptible (S) — people who can be infected; Infected (I) — people who are currently infectious; and Recovered (R) — people who have recovered and are immune. People flow from S to I when infected, and from I to R when they recover. The rate of flow from S to I depends on the product of S, I, and the transmission rate — making it a coupled system where both compartments affect the flow simultaneously. This coupling is what creates exponential growth: more infected people create more opportunities for transmission.

• R-naught and Exponential Growth:
  R₀ (R-naught) is the basic reproduction number: the average number of new infections caused by one infected person in a fully susceptible population. If R₀ > 1, each infected person creates more than one new infection, and the epidemic grows exponentially. If R₀ < 1, the epidemic dies out. For context: measles has R₀ ≈ 12-18, COVID-19 original strain ≈ 2.5-3, seasonal flu ≈ 1.3. The exponential nature means that early in an epidemic, the infected population doubles at regular intervals. With R₀ = 3, one case becomes approximately 59,000 cases in just 10 generations of transmission.

• Herd Immunity and Natural Balancing Feedback:
  The SIR model contains a natural balancing feedback loop: as people get infected and recover, the susceptible population shrinks. With fewer susceptible people available, each infected person has fewer potential targets, and the effective reproduction number drops below 1. This is herd immunity — when enough people are immune that sustained transmission is impossible. The threshold is calculated as 1 - (1/R₀). For R₀ = 3, that's 67% immune. However, reaching herd immunity through natural infection means 67% of the population gets sick — with potentially catastrophic consequences.

• Interventions: Changing the System:
  Public health interventions work by modifying specific parameters of the SIR model. Quarantine reduces the Contact Rate, directly lowering R₀. Vaccination moves people from Susceptible to Recovered without going through Infected, reducing the susceptible pool and lowering the effective R₀. The critical insight is that intervention TIMING dramatically affects outcomes. In an exponential system, acting one week earlier can prevent more infections than acting one month later with greater intensity. This is because exponential growth means the infected population during that week of delay may double or triple, creating a vastly larger base for subsequent transmission.

• Beyond Basic SIR:
  Real epidemics are more complex than the basic SIR model. Asymptomatic transmission means some infected people spread disease without knowing they're sick. Waning immunity can turn the model into SIRS (where Recovered people become Susceptible again). Heterogeneous mixing means some people have many more contacts than others. Hospital capacity introduces a threshold effect: below capacity, mortality is manageable; above capacity, mortality spikes because patients can't receive care. Despite these complexities, the basic SIR model captures the essential dynamics that make pandemics so dangerous and interventions so time-sensitive.

COMMON MISCONCEPTIONS:
• "Pandemics grow at the same rate throughout"
  Reality: Pandemics do NOT grow at a constant rate. They grow exponentially at first (when the susceptible pool is large), reach a peak, then decline as the susceptible population is depleted. The epidemic curve is bell-shaped, not linear. The model shows this clearly: the growth rate depends on the SIZE of both the Susceptible and Infected populations, which change over time.
  Strategy: Draw a bell curve and ask: 'Why doesn't the epidemic keep growing forever? What resource runs out?' Answer: susceptible people. As more people get infected and recover, there are fewer people left to infect.

• "Quarantine and vaccination do the same thing"
  Reality: Quarantine and vaccination work on DIFFERENT components of the SIR model. Quarantine reduces the Contact Rate — it doesn't change who's susceptible, but it reduces how often susceptible and infected people interact. Vaccination reduces the Susceptible Population — it moves people directly to Recovered without infection. Quarantine is temporary and must be maintained; vaccination is permanent (for that individual). Both reduce R₀, but through entirely different mechanisms.
  Strategy: Draw the SIR diagram. Show where quarantine acts (the arrow between S and I, reducing contact) vs. where vaccination acts (moving people from S to R directly). They modify different parts of the system.

• "Herd immunity means nobody gets sick"
  Reality: Herd immunity doesn't mean zero infections — it means sustained TRANSMISSION stops. Once enough people are immune, each infected person infects fewer than one new person on average, and chains of transmission die out. But individuals can still get infected; they just don't spark chain reactions. Herd immunity protects the POPULATION, not every individual.
  Strategy: Analogy: Fire breaks in a forest don't prevent all trees from burning, but they prevent a small fire from becoming a wildfire by removing enough fuel (susceptible trees) to stop the fire from spreading indefinitely.

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
Big Question: How does one person's infection become a global pandemic in weeks?
Answer: One infection becomes a pandemic through exponential growth: if each infected person infects 2-3 others (R₀ of 2-3), one case becomes 3, then 9, then 27, then 81. Within 20 generations of transmission (which can take just weeks), millions are infected. The SIR model shows this happens because the Susceptible population is large and the transmission chain grows proportionally. Interventions work by reducing R₀ below 1 — through quarantine (reducing contact rate), vaccination (reducing susceptible population), or both. The critical insight is that timing matters enormously: early intervention prevents far more infections than the same intervention applied later.

Simulation Answers:
• Uncontrolled Epidemic Scenario: Without intervention, the epidemic follows a classic bell curve. Infected Population grows exponentially as the large Susceptible Population provides abundant targets. The curve peaks when enough people have been infected and recovered that the Susceptible pool is depleted below the herd immunity threshold. The epidemic then declines naturally. However, the peak is extremely high — potentially overwhelming healthcare systems — and the total infected population reaches 60-80% before the epidemic ends.
• Early vs. Late Quarantine Comparison: Quarantine at 1% infection dramatically reduces both the peak Infected Population and total infections. Because the intervention is applied when exponential growth is still in its early stages, it prevents the massive amplification that occurs in the following weeks. The same quarantine at 10% infection has much less impact because the base of active infections is already 10x larger, and exponential growth has already generated enormous momentum. The model demonstrates that in exponential systems, early action is exponentially more effective than delayed action.
• Vaccination Scenario: Vaccination steadily reduces the Susceptible Population, moving people to Recovered without illness. This has two effects: it directly prevents those individuals from getting sick, and it reduces the pool of susceptible contacts available to infected people, lowering the effective R₀. When enough people are vaccinated to cross the herd immunity threshold, the epidemic cannot sustain transmission and collapses. Vaccination combined with early quarantine produces the best outcome.

Reflection Exemplars:
• Q: Why does timing matter so much in exponential systems?
  A: In exponential growth, the infected population doubles at regular intervals. Intervening when there are 1,000 cases prevents the doubling to 2,000, then 4,000, then 8,000. Waiting until there are 10,000 cases means the same intervention must prevent 20,000, then 40,000, then 80,000 new cases from a much larger base. The same action applied one week earlier in an exponential system can prevent more total infections than applying it later with much greater intensity. This is why public health experts emphasize speed over perfection in pandemic response.
• Q: How does the SIR model's natural balancing feedback eventually end an epidemic?
  A: The natural balancing feedback works through depletion: as people get infected and recover, they move from Susceptible to Recovered. Each recovery reduces the pool of people who can be infected. When the Susceptible population drops below the herd immunity threshold, each infected person infects fewer than one new person on average (R < 1), and the epidemic declines. However, this 'natural' end comes at enormous cost — it requires 60-80% of the population to be infected first. Vaccination achieves the same herd immunity without the disease, which is why it's the most important public health tool in the model.

STEM CHALLENGE GUIDANCE:
Title: Design a Pandemic Response Decision Tool
Mission: Using your SIR model data, design a decision support tool that helps public health officials determine WHEN and HOW AGGRESSIVELY to implement interventions during an outbreak, showing the cost of delayed action.
Scenario: A county health department needs a tool that shows, in real time, where they are on the epidemic curve and what different intervention strategies would achieve. Your team will build this tool using your model data, emphasizing the critical importance of intervention timing.
Introduction: Present the challenge: A county health department needs a real-time decision support tool for pandemic response. The tool must show where the epidemic currently stands (which phase of the SIR curve), project outcomes under different intervention strategies, and clearly communicate the cost of delayed action. Your model data is the foundation — translate it into a tool that saves lives by helping officials act faster.

Key Concepts:
• Coupled Compartment Dynamics: The SIR model's compartments are coupled because the flow between them depends on the state of multiple compartments simultaneously. New infections require both a susceptible person and an infected person, making the transmission rate proportional to S × I. This coupling is what produces exponential growth when S is large.
• Exponential Growth and Intervention Timing: In exponential systems, the current size of the problem determines the rate of growth. Acting when the problem is small prevents vastly more damage than acting when it's large, because every doubling period that passes without intervention doubles the total burden.
• Herd Immunity as System Threshold: Herd immunity is the threshold where the effective R drops below 1 and the epidemic cannot sustain transmission. It can be reached through infection (costly) or vaccination (efficient). The threshold value depends on R₀: more transmissible diseases require higher immunity levels to stop.

Evaluation Rubric:
• Expert (4): Tool clearly shows current epidemic phase, projects multiple intervention scenarios with timing comparisons, communicates the cost of delay quantitatively, and helps officials make evidence-based decisions under uncertainty
• Proficient (3): Tool accurately represents SIR dynamics, shows intervention comparisons, and communicates urgency of early action
• Developing (2): Tool shows some epidemic curve concepts but lacks clear intervention timing comparisons or decision-support features
• Beginning (1): Tool is incomplete or does not accurately represent SIR dynamics or intervention effects

DIFFERENTIATION:
Support (Struggling Learners):
  • Provide pre-drawn SIR compartment diagrams with labeled arrows that students can annotate
  • Use a physical demonstration: pass a ball (infection) around a circle of students, removing students who 'recover' to show how the susceptible pool shrinks
  • Sentence frames: 'When [intervention] is implemented at [timing], R₀ changes from ___ to ___ because ___'
  • Scaffolded epidemic curve templates where students plot predictions before running simulations

Extensions (Advanced Learners):
  • Research COVID-19 R₀ values for different variants and model how increased transmissibility changes epidemic outcomes
  • Extend the model to SEIR (adding an Exposed compartment with incubation period) and compare dynamics to basic SIR
  • Analyze real-world data comparing countries with early vs. late pandemic responses and validate against model predictions
  • Model the emergence of vaccine-resistant variants by adding a reinfection pathway from R back to S

Cross-Curricular Connections:
  • Math: Derive the herd immunity threshold formula (1 - 1/R₀) and calculate thresholds for diseases with different R₀ values. Create exponential growth projections for the first 30 days of an uncontrolled epidemic.
  • ELA: Write a crisis communication press release for a health department announcing pandemic interventions, using model evidence to justify the timing and intensity of the response.
  • Social Studies: Research how socioeconomic factors (housing density, healthcare access, essential worker status) create unequal pandemic impacts and analyze whose R₀ is effectively higher.

CAST ALIGNMENT:
• Model disease spread using the SIR compartmental framework with coupled dynamics
• Calculate and interpret R₀ as the key determinant of epidemic growth or decline
• Analyze the impact of intervention timing on total infections and peak burden
• Evaluate trade-offs between different pandemic response strategies using model evidence

CAST-Style Assessment Questions:
• Multiple Choice: During an epidemic with R₀ = 3, approximately what percentage of the population must be immune (through infection or vaccination) to achieve herd immunity and stop sustained transmission?
• Constructed Response: Using the SIR model, explain why a quarantine implemented when 1% of the population is infected produces dramatically different outcomes than the same quarantine at 10% infection. Include in your explanation the role of exponential growth, the coupling between compartments, and the concept of R₀.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Activity Pack

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STUDENT ACTIVITY PACK: Why Pandemics Go Exponential
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NAME: _________________________ DATE: _____________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRE-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. What do you remember about the COVID-19 pandemic? What measures were taken to slow the spread?

   _________________________________________________________

   _________________________________________________________

2. Why do you think some diseases spread faster than others?

   _________________________________________________________

   _________________________________________________________

3. What does 'exponential growth' mean, and why is it relevant to pandemics?

   _________________________________________________________

   _________________________________________________________

4. Draw what you think the number of infections looks like over time during an uncontrolled epidemic.

   [DRAWING BOX]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VOCABULARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Match the term to the definition:

___ SIR Model                     
___ R-naught (R₀)                 
___ Exponential Growth            
___ Herd Immunity Threshold       
___ Flattening the Curve          
___ Coupled Compartments          

A. A compartmental model dividing a population into Susceptible, Infected, and Recovered groups — individuals flow between compartments based on transmission and recovery rates
B. The basic reproduction number — the average number of new infections caused by one infected person in a fully susceptible population. If R₀ > 1, the epidemic grows; if R₀ < 1, it shrinks
C. Growth where the rate of increase is proportional to the current amount — the larger the infected population, the faster it grows, creating a J-shaped curve
D. The proportion of the population that must be immune to stop sustained transmission — calculated as 1 - (1/R₀)
E. Interventions that reduce R₀ below 1, slowing the rate of new infections so healthcare systems are not overwhelmed
F. A model structure where populations in different 'compartments' (S, I, R) are linked by flows that depend on the state of multiple compartments simultaneously

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

SCENARIO: Uncontrolled Epidemic
Settings: High contact rate, no interventions
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Early vs. Late Intervention
Settings: Quarantine at 1% infected vs. 10% infected
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Vaccination Effect
Settings: Moderate vaccination rate throughout epidemic
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

1. Why does the epidemic curve naturally peak and decline even without intervention? What does this tell you about the SIR model's built-in balancing feedback?

   _________________________________________________________

   _________________________________________________________

2. Your model shows that the same quarantine implemented at 1% infection vs. 10% produces dramatically different outcomes. Why does timing matter so much in exponential systems?

   _________________________________________________________

   _________________________________________________________

3. How does vaccination change the dynamics compared to quarantine? Which intervention affects which component of the SIR model?

   _________________________________________________________

   _________________________________________________________

4. What real-world factors make pandemic modeling more complicated than the basic SIR model?

   _________________________________________________________

   _________________________________________________________

5. If you were a public health official during the early days of an outbreak, what would you need to know to make good decisions?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
POST-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. How does one person's infection become a global pandemic in weeks? Explain using evidence from your model:

   _________________________________________________________

   _________________________________________________________

   _________________________________________________________

2. Which NGSS dimensions did this lesson address?
   (Check all that apply)
   □ Science Practice: Using Mathematics and Computational Thinking
   □ Disciplinary Core Idea: LS2.C Ecosystem Dynamics / ETS1.B Developing Solutions
   □ Crosscutting Concept: Systems and System Models

3. If you were a public health official during the early days of an outbreak, what would you need to know to make good decisions?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEM CHALLENGE: Design a Pandemic Response Decision Tool
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MISSION: Using your SIR model data, design a decision support tool that helps public health officials determine WHEN and HOW AGGRESSIVELY to implement interventions during an outbreak, showing the cost of delayed action.

SCENARIO: A county health department needs a tool that shows, in real time, where they are on the epidemic curve and what different intervention strategies would achieve. Your team will build this tool using your model data, emphasizing the critical importance of intervention timing.

GUIDING QUESTIONS:
• What is the single most important metric a health official needs to see during an outbreak?
• How can your tool show the 'cost of waiting' — the difference between acting now vs. acting later?
• What trade-offs must health officials consider when deciding intervention timing and intensity?

DESIGN THINKING:
• How will your tool visualize the SIR compartments in real time as the epidemic progresses?

  _________________________________________________________

• How will you show the projected outcomes of different intervention strategies side by side?

  _________________________________________________________

• How will you communicate uncertainty — the fact that early in an epidemic, we don't know exact R₀ values?

  _________________________________________________________

• How will you help officials weigh health outcomes against economic and social costs of interventions?

  _________________________________________________________


EVALUATION RUBRIC:
• Expert (4): Tool clearly shows current epidemic phase, projects multiple intervention scenarios with timing comparisons, communicates the cost of delay quantitatively, and helps officials make evidence-based decisions under uncertainty
• Proficient (3): Tool accurately represents SIR dynamics, shows intervention comparisons, and communicates urgency of early action
• Developing (2): Tool shows some epidemic curve concepts but lacks clear intervention timing comparisons or decision-support features
• Beginning (1): Tool is incomplete or does not accurately represent SIR dynamics or intervention effects

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Resources

| Resource | Link |
|----------|------|
| Activity Pack (DOCX) | [materials/grade-09/G09L2-L03/G09L2-L03-Student-Activity-Pack.docx] |
| Teacher Guide (DOCX) | [materials/grade-09/G09L2-L03/G09L2-L03-Teachers-Guide.docx] |
| PPT Presentation | [materials/grade-09/G09L2-L03/G09L2-L03-Student-Presentation.pptx] |
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