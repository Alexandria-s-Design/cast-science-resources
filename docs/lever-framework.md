# LEVER Framework

## A Pedagogical Framework for Systems Thinking in the Age of Disruptive Technology

**Version:** 1.0
**Created:** February 2026
**Purpose:** Integrate Boolean modeling, NGSS standards, and 4th Industrial Revolution skills through ModelIt

---

## Overview

The LEVER Framework is a pedagogical approach designed to teach systems thinking through computational modeling. It provides a structured pathway for students to investigate scientific phenomena using Boolean logic while developing skills essential for the Fourth Industrial Revolution.

**LEVER** stands for:

| Letter | Component | Core Question |
|--------|-----------|---------------|
| **L** | **Locate the System** | What is the phenomenon? What are its boundaries? |
| **E** | **Establish Relationships** | How do parts connect and influence each other? |
| **V** | **Visualize & Model** | What does the system look like in action? |
| **E** | **Evaluate Outcomes** | What do the results tell us? What patterns emerge? |
| **R** | **Revise & Extend** | How can we improve our understanding? |

---

## The LEVER Phases in Detail

### L — Locate the System

**Definition:** Identify the phenomenon, define system boundaries, and recognize the components (nodes) that matter.

**Student Actions:**
- Observe a real-world phenomenon
- Ask: "What are the parts of this system?"
- Distinguish internal vs. external components
- Identify what's IN the system vs. what INFLUENCES it from outside

**NGSS Alignment:**
- SEP: Asking Questions and Defining Problems
- CCC: Systems and System Models (defining boundaries)

**ModelIt Application:**
- Students identify nodes to place on the canvas
- Distinguish between internal components and external inputs

**Example (Grade 5 - Ecosystems):**
> *Phenomenon: A pond ecosystem is changing*
> - Internal: Fish, algae, insects, bacteria
> - External: Sunlight, temperature, human activity

---

### E — Establish Relationships

**Definition:** Determine how components influence each other using Boolean logic (activates/inhibits, ON/OFF).

**Student Actions:**
- Ask: "What turns ON when this is ON?"
- Ask: "What turns OFF when this is ON?"
- Draw arrows showing positive (+) and negative (-) relationships
- Create truth tables for simple interactions

**NGSS Alignment:**
- SEP: Developing and Using Models
- CCC: Cause and Effect

**ModelIt Application:**
- Students draw connection arrows between nodes
- Assign relationship types (activation = green, inhibition = red)
- Define Boolean logic rules (AND, OR, NOT)

**Boolean Logic for Students:**

| Relationship | Meaning | Real Example |
|--------------|---------|--------------|
| A → B (activates) | When A is ON, B turns ON | Sunlight → Photosynthesis |
| A ⊣ B (inhibits) | When A is ON, B turns OFF | Predator → Prey population |
| A AND B → C | Both must be ON for C | Water AND Sunlight → Plant growth |
| A OR B → C | Either can turn C ON | Rain OR Irrigation → Soil moisture |

---

### V — Visualize & Model

**Definition:** Build and run computational models to see system behavior over time.

**Student Actions:**
- Construct the model in ModelIt/Cell Collective
- Set initial conditions (which components start ON or OFF?)
- Run simulations
- Watch the system evolve

**NGSS Alignment:**
- SEP: Using Mathematics and Computational Thinking
- SEP: Developing and Using Models
- CCC: Patterns

**ModelIt Application:**
- Students build their Boolean network on canvas
- Set initial states for all components
- Run simulation and observe Activity Graph
- Generate multiple scenarios (What if sunlight is OFF?)

**Graph Literacy Skills:**
- X-axis = Time steps (iterations)
- Y-axis = Activity level (% ON)
- Rising line = Component becoming active
- Falling line = Component deactivating
- Oscillation = System cycling
- Flat line = Stable state (attractor)

---

### E — Evaluate Outcomes

**Definition:** Analyze simulation results, identify patterns, and test predictions against evidence.

**Student Actions:**
- Interpret the Activity Graph output
- Identify stable states (attractors) - where does the system "settle"?
- Compare predictions to simulation results
- Ask: "Does this match what happens in nature?"
- Gather evidence to support or refute the model

**NGSS Alignment:**
- SEP: Analyzing and Interpreting Data
- SEP: Constructing Explanations
- CCC: Stability and Change

**ModelIt Application:**
- Students analyze dose-response curves
- Identify feedback loops (positive and negative)
- Compare model behavior to real-world data
- Document what the model explains and what it doesn't

**Key Evaluation Questions:**
1. What patterns do you see in the graph?
2. Does the system reach a stable state or keep changing?
3. Which component has the most influence?
4. What happens when you change the initial conditions?

---

### R — Revise & Extend

**Definition:** Iterate on the model based on new information, extend to new phenomena, and transfer learning.

**Student Actions:**
- Add new components based on research/evidence
- Modify relationships based on evaluation
- Test "what if" scenarios
- Apply the same systems thinking to new phenomena
- Communicate findings to peers

**NGSS Alignment:**
- SEP: Engaging in Argument from Evidence
- SEP: Obtaining, Evaluating, and Communicating Information
- CCC: Systems and System Models (refinement)

**ModelIt Application:**
- Students add nodes to increase model complexity
- Adjust Boolean rules based on evidence
- Run new simulations with modifications
- Present models to class for peer review
- Export/share models for collaboration

**Extension Prompts:**
- "What component is missing from your model?"
- "How would climate change affect this system?"
- "Can you apply this same logic to a different ecosystem?"

---

## LEVER + NGSS Three-Dimensional Alignment

| LEVER Phase | Science & Engineering Practices | Crosscutting Concepts | Disciplinary Core Ideas |
|-------------|--------------------------------|----------------------|------------------------|
| **Locate** | Asking Questions, Defining Problems | Systems & System Models | Domain-specific (Life, Earth, Physical) |
| **Establish** | Developing & Using Models | Cause & Effect | Structure & Function |
| **Visualize** | Computational Thinking, Modeling | Patterns | Energy & Matter |
| **Evaluate** | Analyzing Data, Constructing Explanations | Stability & Change | Domain-specific |
| **Revise** | Argument from Evidence, Communicating | Scale, Proportion, Quantity | Engineering Design |

---

## LEVER + Boolean Modeling

### Why Boolean Models?

Boolean models are ideal for K-12 education because they:

1. **Require no advanced math** — Only ON/OFF logic
2. **Mirror real scientific practice** — Used by researchers in systems biology
3. **Develop computational thinking** — Same logic that powers computers and AI
4. **Visualize cause and effect** — Students see how changes propagate
5. **Scale with complexity** — Start simple, add depth as understanding grows

### Boolean Model Components

| Component | Definition | Example |
|-----------|------------|---------|
| **Node** | A component in the system | "Sunlight", "Plant Growth", "Predator" |
| **State** | ON (1) or OFF (0) | Sunlight = ON, Rain = OFF |
| **Edge** | Connection between nodes | Sunlight → Photosynthesis |
| **Activation** | Positive influence | A turns B ON |
| **Inhibition** | Negative influence | A turns B OFF |
| **Logic Gate** | Rule for combining inputs | AND, OR, NOT |
| **Attractor** | Stable end state | System settles into equilibrium |

### Reading Boolean Graphs

When students run simulations in ModelIt, they see Activity Graphs showing:

- **Time (X-axis):** Steps in the simulation
- **Activity (Y-axis):** Percentage likelihood of being ON (0-100%)
- **Lines:** Each component's behavior over time

**Interpreting Patterns:**

| Pattern | Meaning | Scientific Interpretation |
|---------|---------|--------------------------|
| Line rises to 100% | Component fully activates | Process is triggered |
| Line falls to 0% | Component fully deactivates | Process is inhibited |
| Line oscillates | System cycles | Predator-prey dynamics |
| Lines converge | System reaches stability | Equilibrium state |
| Chaotic movement | Sensitive system | Small changes = big effects |

---

## LEVER + AI Literacy

### Teaching Students to Work WITH AI

The LEVER framework prepares students for an AI-integrated world by teaching them how AI systems actually work.

| LEVER Phase | AI Connection | Student Learning |
|-------------|---------------|------------------|
| **Locate** | AI identifies patterns in data | Students learn AI needs defined problems |
| **Establish** | AI uses logic and rules | Students understand AI "thinks" in IF-THEN logic |
| **Visualize** | AI generates predictions/simulations | Students see AI as a modeling tool |
| **Evaluate** | AI can be wrong; needs validation | Students learn to verify AI outputs |
| **Revise** | AI improves with feedback | Students understand iterative learning |

### Key AI Literacy Outcomes

1. **AI is a tool, not magic** — It follows logical rules (like Boolean models)
2. **AI needs good inputs** — Garbage in, garbage out
3. **AI can be biased** — Models reflect the data and assumptions we give them
4. **Humans evaluate AI** — Critical thinking is essential
5. **AI + Humans > Either alone** — Collaboration amplifies capability

### Classroom AI Integration with LEVER

| Phase | AI Tool Usage |
|-------|---------------|
| **Locate** | Use AI to research phenomenon, find data sources |
| **Establish** | Use AI to suggest possible relationships to investigate |
| **Visualize** | Use AI to help interpret complex model outputs |
| **Evaluate** | Use AI to find contradicting evidence, check reasoning |
| **Revise** | Use AI to suggest extensions, generate "what if" scenarios |

---

## LEVER + Fourth Industrial Revolution (4IR)

### The Educational Imperative

The Fourth Industrial Revolution is characterized by technologies that blur the lines between physical, digital, and biological systems. Students need frameworks that help them understand and navigate this convergence.

### Disruptive Technologies Mapped to LEVER

| Technology | LEVER Application | Systems Thinking Connection |
|------------|-------------------|----------------------------|
| **Artificial Intelligence** | AI as modeling partner | Neural networks as Boolean-like logic |
| **Biotechnology/CRISPR** | Gene regulatory networks | Boolean models of gene expression |
| **Internet of Things (IoT)** | Sensor networks as systems | Data inputs as external components |
| **Robotics/Automation** | Decision trees, logic gates | Boolean control systems |
| **Blockchain** | Distributed trust networks | System states and verification |
| **Augmented Reality** | Immersive system visualization | 3D model exploration |
| **Quantum Computing** | Complex system states | Superposition as "both ON and OFF" |
| **Synthetic Biology** | Engineering living systems | Designing Boolean circuits in cells |

### Education 4.0 Competencies Through LEVER

| 4IR Competency | LEVER Development |
|----------------|-------------------|
| **Computational Thinking** | Boolean logic, algorithmic reasoning |
| **Systems Thinking** | Core framework purpose |
| **Critical Reasoning** | Evaluate phase — questioning outputs |
| **Collaboration** | Revise phase — peer model review |
| **Adaptability** | Iterative modeling, handling uncertainty |
| **Data Literacy** | Graph interpretation, pattern recognition |
| **Digital Citizenship** | Ethical modeling, responsible AI use |

---

## LEVER Across Grade Bands

### PreK-2: Foundation Level

| Phase | Simplified Language | Activity Example |
|-------|---------------------|------------------|
| **L** | "What are the parts?" | Name parts of a plant |
| **E** | "What helps what?" | Sun helps plant grow |
| **V** | "Let's pretend and see" | Act out plant growing |
| **E** | "What happened?" | Describe what they observed |
| **R** | "What else could happen?" | Add water to the story |

**Sample PreK Activity:** Boolean Coloring Sheets
- Color the sun ON (yellow) or OFF (gray)
- Color the plant based on whether sun is ON or OFF
- Simple cause-and-effect visualization

### Grades 3-5: Developing Level

| Phase | Student Language | ModelIt Integration |
|-------|------------------|---------------------|
| **L** | "What's in the system?" | Identify 3-5 nodes |
| **E** | "What turns on what?" | Draw simple connections |
| **V** | "Build and run the model" | Use ModelIt interface |
| **E** | "Read the graph" | Interpret basic outputs |
| **R** | "Add more to the model" | Expand to 5-8 nodes |

### Grades 6-8: Proficient Level

| Phase | Student Language | ModelIt Integration |
|-------|------------------|---------------------|
| **L** | "Define system boundaries" | Internal vs. external components |
| **E** | "Establish Boolean logic" | AND/OR/NOT relationships |
| **V** | "Simulate scenarios" | Multiple initial conditions |
| **E** | "Analyze attractors" | Identify stable states |
| **R** | "Validate with evidence" | Compare to real data |

### Grades 9-12: Advanced Level

| Phase | Student Language | ModelIt Integration |
|-------|------------------|---------------------|
| **L** | "Model complex phenomena" | 10+ node systems |
| **E** | "Design regulatory networks" | Feedback loops, cascades |
| **V** | "Run sensitivity analysis" | Dose-response curves |
| **E** | "Compare model types" | Boolean vs. ODE discussion |
| **R** | "Publish and defend" | Scientific communication |

---

## LEVER vs. Other Frameworks

| Framework | Focus | LEVER Advantage |
|-----------|-------|-----------------|
| **5E Model** | General inquiry | LEVER adds computational modeling explicitly |
| **NGSS Storylines** | Phenomenon-driven | LEVER adds systems thinking structure |
| **Project-Based Learning** | Project-driven | LEVER provides specific cognitive scaffolding |
| **CER (Claim-Evidence-Reasoning)** | Argumentation | LEVER includes modeling before claiming |
| **Traditional Labs** | Hands-on experimentation | LEVER adds computational simulation layer |

### LEVER's Unique Value Proposition

1. **Memorable acronym** — Easy for teachers and students to recall
2. **Action-oriented** — Each letter is a verb (doing science)
3. **Computationally explicit** — Built for digital modeling tools
4. **Scalable** — Works PreK through graduate school
5. **Future-proof** — Designed for 4IR technologies
6. **NGSS-native** — Maps directly to three dimensions
7. **Biotech-ready** — Prepares students for life sciences careers

---

## Implementation Guide

### Getting Started with LEVER + ModelIt

**Week 1-2: Introduction**
- Introduce Boolean logic with unplugged activities
- Simple ON/OFF sorting games
- Basic cause-effect mapping on paper

**Week 3-4: First Model**
- Guide students through a simple 3-4 node model
- Teacher demonstrates ModelIt interface
- Students practice interpreting graphs

**Week 5-6: Student-Led Modeling**
- Students choose phenomena to investigate
- Build models independently or in pairs
- Peer review and iteration

**Week 7+: Advanced Applications**
- Connect to curriculum content
- Integrate with CAST preparation
- Cross-disciplinary applications

### Teacher Preparation

1. **Complete ModelIt tutorial** (available at cellcollective.org)
2. **Review NGSS Performance Expectations** for target grade
3. **Identify phenomena** that lend themselves to Boolean modeling
4. **Practice reading Activity Graphs** before teaching students
5. **Prepare scaffolded worksheets** for each LEVER phase

### Assessment Strategies

| LEVER Phase | Assessment Method |
|-------------|-------------------|
| **Locate** | System boundary diagram, component list |
| **Establish** | Relationship map, truth table |
| **Visualize** | Model screenshot, simulation recording |
| **Evaluate** | Graph interpretation worksheet, written analysis |
| **Revise** | Before/after model comparison, reflection |

---

## CAST Alignment

The LEVER framework directly supports California Science Test (CAST) preparation by:

1. **Developing three-dimensional proficiency** — SEPs, DCIs, and CCCs integrated
2. **Building graph literacy** — Essential for CAST item types
3. **Practicing systems analysis** — Core CAST competency
4. **Engaging with phenomena** — Mirrors CAST assessment design
5. **Constructing explanations** — Key CAST constructed response skill

### High-Alignment Performance Expectations

**Grade 5:**
- 5-LS2-1: Matter cycling in ecosystems
- 5-ESS2-1: Earth systems interactions
- 5-ESS3-1: Community resource protection
- 5-PS1-2: Conservation of matter

**Grade 8:**
- MS-LS2-3: Matter/energy flow in ecosystems
- MS-ESS2-6: Atmospheric/oceanic circulation
- MS-ESS3-4: Population impacts on Earth systems
- MS-LS2-1: Resource availability & populations

---

## Resources

### Official Documentation
- [Cell Collective Platform](https://cellcollective.org/)
- [NGSS Standards](https://www.nextgenscience.org/)
- [CAST Information](https://www.cde.ca.gov/ta/tg/ca/caasppscience.asp)

### Research Foundation
- Kauffman, S.A. (1969). Boolean networks and genetic regulatory networks
- NGSS Lead States. (2013). Next Generation Science Standards
- World Economic Forum. Education 4.0 Framework

---

## Contact

**Developed by:** Alexandria's Design
**For:** ModelIt K12 Platform
**Repository:** [cast-science-resources](https://github.com/Alexandria-s-Design/cast-science-resources)

---

*LEVER Framework v1.0 — Empowering students to think in systems, model with logic, and prepare for the future.*
