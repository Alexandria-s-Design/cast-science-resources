#!/usr/bin/env python3
"""Complete lesson data for G07-L01 through G07-L10 (Grade 7 ModelIt! Lessons)"""

L01 = {
    "id": "G07-L01",
    "title": "Blood Moon: When the Sky Turns Red",
    "subtitle": "The Cosmic Dance of Earth, Moon, and Sun",
    "ngss": "MS-ESS1-1, MS-ESS1-2",
    "ngss_desc": "Develop and use a model of the Earth-Sun-Moon system to describe the cyclic patterns of lunar phases, eclipses of the Sun and Moon, and seasons. Develop and use a model to describe the role of gravity in the motions within galaxies and the solar system.",
    "big_question": "Why does the Moon change shape every night and sometimes turn blood red?",
    "objectives": [
        "Model how the Moon's orbital position determines the phase we see from Earth",
        "Explain why lunar eclipses turn the Moon red instead of making it disappear",
        "Predict when eclipses occur based on the alignment of Earth, Moon, and Sun",
        "Describe how gravity keeps the Earth-Moon-Sun system in constant motion"
    ],
    "vocabulary": [
        ("Lunar Eclipse", "When Earth passes between the Sun and Moon, casting its shadow on the Moon's surface"),
        ("Orbital Period", "The time it takes for one object to complete a full orbit around another — the Moon's is about 29.5 days"),
        ("Penumbra", "The lighter, outer part of a shadow where only some light is blocked"),
        ("Revolution", "One complete orbit of an object around another, like the Moon around Earth")
    ],
    "components": [
        ("Sun Angle", "The angle of sunlight hitting the Earth-Moon system, which changes as Earth orbits", True),
        ("Moon Position", "Where the Moon is in its 29.5-day orbit around Earth at any given time", True),
        ("Earth's Shadow", "The cone of darkness cast by Earth into space, away from the Sun", False),
        ("Visible Moon Phase", "How much of the Moon's surface appears lit when viewed from Earth", False)
    ],
    "think_about_it": "When the Moon's position moves directly behind Earth (relative to the Sun), what happens to Earth's shadow and the visible Moon phase?",
    "scenarios": [
        ("Full Moon Night", "Set Moon Position to opposite side of Earth from Sun and observe"),
        ("Lunar Eclipse", "Align Moon Position directly behind Earth's shadow and observe"),
        ("New Moon", "Set Moon Position between Earth and Sun and observe visibility")
    ],
    "sim_scenarios": [
        ("Full Moon", "Moon on opposite side of Earth from Sun, not in shadow", "What do you predict the Visible Moon Phase will be when the Moon is fully facing the Sun?"),
        ("Lunar Eclipse", "Moon passes through Earth's Shadow directly", "What do you predict happens to the Moon's appearance when it enters Earth's shadow?"),
        ("New Moon", "Moon between Earth and Sun", "Why do you predict we can't see the Moon during this phase?")
    ],
    "discoveries": [
        "The Moon doesn't produce its own light — it reflects sunlight, so its appearance depends on position",
        "Lunar eclipses turn the Moon red because Earth's atmosphere bends red light into the shadow",
        "Eclipses don't happen every month because the Moon's orbit is tilted 5 degrees relative to Earth's",
        "Gravity is the invisible force that keeps the Moon orbiting Earth and Earth orbiting the Sun"
    ],
    "answer": "The Moon appears to change shape because we see different amounts of its sunlit side as it orbits Earth. During a lunar eclipse, Earth blocks direct sunlight but our atmosphere bends red wavelengths into the shadow — painting the Moon blood red!",
    "stem_title": "Design a Moon Phase Predictor",
    "stem_mission": "Design a physical or digital tool that can predict the Moon's phase and eclipse events for any date, using your understanding of orbital mechanics.",
    "stem_scenario": "A local planetarium needs a hands-on exhibit that helps visitors understand why the Moon changes shape and when the next eclipse will occur. Your team has been hired to build the prototype.",
    "stem_questions": [
        "How can you represent the Moon's orbit to accurately show phases?",
        "What determines whether a full moon is a normal full moon or an eclipse?",
        "How would your predictor account for the Moon's tilted orbit?"
    ],
    "stem_design_qs": [
        "What materials will you use to represent Earth, Moon, and Sun?",
        "How will you show the Moon's orbital tilt and why eclipses are rare?",
        "How will your exhibit demonstrate why the Moon turns red during eclipses?",
        "How can visitors interact with your model to explore different phases?"
    ],
    "career": "Planetary Scientists and Astronomers study celestial mechanics and predict eclipses, tides, and orbital events. They work at NASA, observatories, and universities, earning $70,000–$130,000/year.",
    "images": {
        "cover": ("cover-blood-moon.png", "A dramatic blood-red lunar eclipse in a dark starry sky, the Moon glowing deep crimson with Earth's shadow visible, cinematic astrophotography"),
        "landscape": ("landscape-moon.png", "7th grade students outside at night using telescopes to observe the Moon, excited expressions, a large bright Moon visible in the sky"),
        "modeling": ("modeling-moon.png", "A diverse group of 7th grade students working on laptops building a digital model of the Earth-Moon-Sun system, classroom with space posters on walls"),
        "discussion": ("discussion-moon.png", "A teacher pointing at a large diagram of lunar phases on a smartboard while 7th grade students raise hands and discuss, bright modern classroom"),
        "stem": ("stem-moon-model.png", "7th grade students building a physical 3D model of the Earth-Moon-Sun system using styrofoam balls and a lamp, collaborative group work")
    },
    "pre_assessment": [
        "Why do you think the Moon appears to change shape throughout the month?",
        "Have you ever seen a lunar eclipse? What did it look like?",
        "Draw what you think causes the Moon to look different each night.",
        "Does the Moon make its own light? How do we see it?"
    ],
    "extend_components": [
        ("Tidal Force", "The gravitational pull of the Moon that creates ocean tides on Earth"),
        ("Orbital Tilt", "The 5-degree tilt of the Moon's orbit that determines when eclipses can occur"),
        ("Solar Eclipse", "When the Moon passes between Earth and Sun, blocking sunlight")
    ],
    "reflections": [
        "Why don't we get a lunar eclipse every single month?",
        "How does your model show that the Moon doesn't produce its own light?",
        "What would happen to the Moon's phases if the Moon orbited faster?",
        "How are lunar eclipses and solar eclipses different in your model?",
        "Why is gravity essential for the patterns we observe in the sky?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a computational model of the Earth-Sun-Moon system to explain lunar phases and eclipses."),
        ("Disciplinary Core Idea", "ESS1.A/B The Universe and the Solar System", "Patterns of the apparent motion of the Sun, Moon, and stars can be observed, described, predicted, and explained with models."),
        ("Crosscutting Concept", "Patterns", "Students identify the cyclic patterns of lunar phases and the conditions required for eclipses to occur.")
    ],
    "cast_items": [
        "Use a model to describe cyclic patterns of lunar phases",
        "Explain the role of gravity in the Earth-Moon-Sun system",
        "Predict when and why eclipses occur based on orbital mechanics"
    ],
    "cast_questions": [
        ("Multiple Choice:", "During a lunar eclipse, the Moon appears red instead of disappearing completely. Which best explains this observation?"),
        ("Constructed Response:", "Using a model of the Earth-Sun-Moon system, explain why we see different Moon phases throughout a month and why eclipses don't happen every month.")
    ],
    "background_intro": "The Earth-Moon-Sun system creates some of the most dramatic natural phenomena visible from Earth — lunar phases, eclipses, and tides. Understanding these patterns requires modeling how gravity, orbital mechanics, and light interact across vast distances.",
    "background_sections": [
        ("Lunar Phases", "The Moon completes one orbit around Earth every 29.5 days. As it orbits, the angle between Sun, Moon, and Earth changes, illuminating different portions of the Moon's surface. The Moon doesn't produce light — it reflects sunlight. New moon occurs when the Moon is between Earth and Sun, and full moon when Earth is between Sun and Moon."),
        ("Lunar Eclipses", "A lunar eclipse occurs when Earth passes directly between the Sun and Moon, casting its shadow on the Moon. The Moon turns red because Earth's atmosphere refracts red wavelengths of sunlight into the shadow. Eclipses don't happen monthly because the Moon's orbit is tilted 5.1 degrees relative to Earth's orbital plane."),
        ("Gravity and Orbits", "Gravity is the attractive force between all objects with mass. The Moon orbits Earth because gravity provides the centripetal force for orbital motion. The same force creates tides — the Moon's gravity pulls on Earth's oceans, creating bulges on opposite sides of the planet."),
        ("Scale and Distance", "The Moon is about 384,400 km from Earth. Light from the Sun takes about 8 minutes to reach Earth and an additional 1.3 seconds to reach the Moon. The Moon's diameter is about 1/4 of Earth's, making accurate physical models challenging to build.")
    ],
    "lever_L": "Students identify Sun angle, Moon position, Earth's shadow, and visible Moon phase as key components of the lunar phase system.",
    "lever_E": "Students determine that Moon position and Sun angle together determine Earth's shadow and visible phase through positive and negative relationships.",
    "lever_V": "Students build a model showing how the Moon's orbital position creates predictable phase patterns.",
    "lever_Ev": "Students run full moon, eclipse, and new moon scenarios to test their model's predictions against real observations.",
    "lever_R": "Students add tidal force or orbital tilt to explore more complex Earth-Moon interactions.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with dramatic blood moon imagery", "say": "Have you ever looked up and seen the Moon turn red? It's not magic — it's science.", "do": "Show a time-lapse video of a lunar eclipse if available.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we're building a model of something that's mystified humans for thousands of years.", "do": "Have students read objectives. Pre-teach 'revolution' vs. 'rotation.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why does the Moon change shape and turn red?", "say": "Right now, the Moon is out there orbiting us. But WHY does it look different every night?", "do": "Quick poll: Who has seen a blood moon? What did they think was happening?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll build a model of the Earth-Moon-Sun system to answer this.", "do": "Preview each LEVER step. Emphasize that this is a SYSTEM with interacting parts.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for moon phase model", "say": "What are the key players in this cosmic dance?", "do": "Guide sorting of external vs. internal components.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows between components", "say": "When the Moon moves to a certain position, what happens to what we see?", "do": "Help students identify how position determines visibility.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and results", "say": "Let's create a full moon, then an eclipse, then a new moon!", "do": "Students predict first, then run simulations. Compare phases.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings from model", "say": "So WHY does the Moon turn red instead of disappearing during an eclipse?", "do": "Lead discussion about atmosphere bending light. Connect to sunsets.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Moon phase predictor design challenge", "say": "Now you're building something a planetarium would actually use!", "do": "Groups design Moon phase predictors.", "time": "12 min"}
    ],
    "sort_reasoning": "Sun Angle and Moon Position are external because they are determined by orbital mechanics — we can't control where the Sun's light comes from or where the Moon is in its orbit. Earth's Shadow and Visible Moon Phase are internal because they change as a direct result of the positions of these celestial bodies.",
    "relationships": [
        ("Sun Angle to Visible Moon Phase", "POSITIVE (+)", "When the Sun's angle allows more direct light to hit the Moon's Earth-facing side, we see more of the Moon illuminated (fuller phases)."),
        ("Moon Position to Earth's Shadow", "POSITIVE (+)", "When the Moon's position moves into alignment behind Earth, it enters Earth's shadow, creating eclipse conditions."),
        ("Earth's Shadow to Visible Moon Phase", "NEGATIVE (-)", "When Earth's shadow covers the Moon (eclipse), the visible illuminated phase decreases dramatically — the Moon darkens or turns red.")
    ],
    "sim_answers": [
        ("Full Moon Scenario", "When Moon Position is on the opposite side of Earth from the Sun, Visible Moon Phase is at maximum. We see the Moon's entire sunlit face. Earth's Shadow is minimal because the Moon is not aligned with the shadow."),
        ("Lunar Eclipse Scenario", "When Moon Position aligns exactly behind Earth relative to the Sun, Earth's Shadow engulfs the Moon. Visible Moon Phase drops significantly, and the Moon turns red because Earth's atmosphere bends red light into the shadow zone.")
    ],
    "reflection_exemplars": [
        ("Why don't we get an eclipse every month?", "The Moon's orbit is tilted about 5 degrees relative to Earth's orbit around the Sun. Most months, the Moon passes above or below Earth's shadow. Eclipses only happen when the Moon crosses the plane of Earth's orbit at exactly the right time — about 2-4 times per year."),
        ("Why does the Moon turn red?", "Earth's atmosphere acts like a lens, bending sunlight around our planet. Blue and green wavelengths scatter away (same reason our sky is blue), but red wavelengths bend enough to reach the Moon inside the shadow. It's essentially projecting all of Earth's sunsets onto the Moon simultaneously.")
    ],
    "stem_intro": "Present the challenge: A planetarium needs a hands-on exhibit teaching visitors about Moon phases and eclipses. Your team will design and build a working prototype that demonstrates the Earth-Moon-Sun system.",
    "stem_concepts": [
        ("Orbital Mechanics", "The Moon orbits Earth due to gravity, completing one revolution every 29.5 days. The geometry of this orbit determines what we see from Earth's surface."),
        ("Light and Shadow", "The Moon has no light of its own — it reflects sunlight. The amount we see depends on the Moon's position relative to Earth and Sun."),
        ("Atmospheric Refraction", "Earth's atmosphere bends light waves, especially red wavelengths. During eclipses, this bending creates the blood-red color instead of total darkness.")
    ],
    "stem_eval": [
        ("Expert (4)", "Model accurately demonstrates all major Moon phases, shows eclipse mechanics, and explains the red color phenomenon"),
        ("Proficient (3)", "Model shows major Moon phases and explains why eclipses occur"),
        ("Developing (2)", "Model shows some phases but doesn't clearly demonstrate eclipse mechanics"),
        ("Beginning (1)", "Model is incomplete or doesn't accurately represent the Earth-Moon-Sun relationship")
    ],
    "support": [
        "Provide a printed Moon phase diagram with positions labeled for reference",
        "Use a flashlight and tennis balls to physically demonstrate Sun-Moon-Earth alignment",
        "Sentence frames: 'When the Moon is at this position, we see __ because __'"
    ],
    "extensions": [
        "Research the difference between lunar and solar eclipses and model both",
        "Calculate how many full moons occur in one year using the 29.5-day orbital period",
        "Investigate how the Moon's gravity creates tides and add tidal force to the model"
    ],
    "cross_curr": [
        ("Math", "Calculate the Moon's orbital period and predict future eclipse dates using astronomical data"),
        ("ELA", "Research and write about how ancient cultures explained lunar eclipses through mythology"),
        ("Art", "Create a scale poster showing the Earth-Moon-Sun system with accurate proportions")
    ],
    "misconceptions": [
        ("The Moon makes its own light", "The Moon has no light source — it reflects sunlight. What we call moonlight is actually reflected sunlight. The Moon's brightness depends entirely on its position relative to the Sun.", "Shine a flashlight on a ball in a dark room. Ask: Is the ball producing light or reflecting it?"),
        ("Earth's shadow causes Moon phases", "Moon phases are caused by the ANGLE at which we see the Moon's sunlit side, not by Earth's shadow. Earth's shadow only affects the Moon during the rare event of a lunar eclipse.", "Use a ball and flashlight. Show that turning the ball creates phases without any shadow from a third object."),
        ("The Moon changes shape", "The Moon doesn't physically change — it's always a sphere. What changes is how much of its sunlit side we can see from Earth as it orbits. We're seeing different ANGLES, not different shapes.", "Hold a ball under a light and walk around it. Notice you see different amounts of the lit side.")
    ]
}

L02 = {
    "id": "G07-L02",
    "title": "Your Inner Fish",
    "subtitle": "Why You Share Bones with a 375-Million-Year-Old Fish",
    "ngss": "MS-LS4-1, MS-LS4-2",
    "ngss_desc": "Analyze and interpret data for patterns in the fossil record that document the existence, diversity, extinction, and change of life forms throughout the history of life on Earth. Apply scientific ideas to construct an explanation for the anatomical similarities and differences among modern organisms and between modern and fossil organisms to infer evolutionary relationships.",
    "big_question": "Why do humans have the same bones as a fish that lived 375 million years ago?",
    "objectives": [
        "Analyze fossil evidence showing how species have changed over millions of years",
        "Model how environmental change drives species diversification and extinction",
        "Identify homologous structures as evidence of common ancestry",
        "Explain how the fossil record supports the theory of evolution"
    ],
    "vocabulary": [
        ("Fossil Record", "The collection of all known fossils arranged chronologically, showing the history of life on Earth"),
        ("Homologous Structure", "Body parts in different species that share the same basic structure because they evolved from a common ancestor"),
        ("Common Ancestor", "An ancient organism from which two or more different species evolved over time"),
        ("Transitional Fossil", "A fossil that shows features of both an ancestral group and a descendant group")
    ],
    "components": [
        ("Environmental Change Rate", "How quickly an environment changes — temperature, habitat loss, food availability", True),
        ("Time (Millions of Years)", "The geological timescale over which evolution occurs", True),
        ("Anatomical Similarity", "How much structural resemblance exists between different species' body plans", False),
        ("Species Diversity", "The number of different species that exist in an ecosystem at any given time", False)
    ],
    "think_about_it": "When environmental change rate increases dramatically, what happens to species diversity? Does it always go up, or can it crash?",
    "scenarios": [
        ("Stable Environment", "Set Environmental Change Rate low and observe Species Diversity over time"),
        ("Mass Extinction Event", "Lock Environmental Change Rate to maximum and observe the cascade"),
        ("Gradual Adaptation", "Set moderate change and track Anatomical Similarity over millions of years")
    ],
    "sim_scenarios": [
        ("Stable Environment", "Low environmental change, long time period", "What do you predict happens to Species Diversity when the environment stays stable for millions of years?"),
        ("Mass Extinction", "Environmental Change Rate at maximum", "What do you predict will happen to Species Diversity during rapid environmental change?"),
        ("Gradual Change", "Moderate change over a long time period", "How do you predict Anatomical Similarity between related species changes over millions of years?")
    ],
    "discoveries": [
        "Species that can't adapt to environmental change go extinct — creating gaps in the fossil record",
        "Homologous structures prove that very different-looking animals evolved from common ancestors",
        "Mass extinction events reduce diversity temporarily but open ecological niches for new species",
        "The fossil record shows a clear pattern: simple organisms came first, complexity increased over time"
    ],
    "answer": "Humans share bones with ancient fish because we evolved from the same common ancestor. The fossil Tiktaalik (375 million years old) shows the transition from fins to limbs. Our arm bones — humerus, radius, ulna — are the SAME bones, modified over millions of years through evolution!",
    "stem_title": "Build an Evolutionary Evidence Wall",
    "stem_mission": "Create a visual display showing evidence for evolution from the fossil record, including homologous structures and transitional fossils, for a natural history museum.",
    "stem_scenario": "A natural history museum needs a new exhibit showing how scientists use fossils and anatomy to trace evolutionary relationships. Your team will design the exhibit using evidence from your model.",
    "stem_questions": [
        "What fossil evidence most clearly shows evolutionary relationships?",
        "How do you visually show homologous structures across different species?",
        "What story does your evidence wall tell about the history of life?"
    ],
    "stem_design_qs": [
        "Which transitional fossils will you feature and why?",
        "How will you show homologous structures between fish, reptiles, and mammals?",
        "How will you represent the timeline of evolution visually?",
        "What interactive elements will help visitors understand the evidence?"
    ],
    "career": "Paleontologists excavate and study fossils to understand the history of life on Earth. They work for museums, universities, and geological surveys, earning $55,000–$110,000/year.",
    "images": {
        "cover": ("cover-inner-fish.png", "A dramatic split image showing a fossilized Tiktaalik skeleton on one side and a modern human arm skeleton on the other, highlighting the same bone structure, museum lighting"),
        "landscape": ("landscape-fossils.png", "7th grade students examining real fossils and casts in a natural history museum or science lab, using magnifying glasses, excited expressions"),
        "modeling": ("modeling-evolution.png", "A diverse group of 7th grade students working on laptops building a digital evolutionary model, classroom with fossil posters and evolution timelines on walls"),
        "discussion": ("discussion-fossils.png", "A teacher holding up fossil casts while leading an animated discussion with 7th grade students about evolutionary evidence, students engaged"),
        "stem": ("stem-evidence-wall.png", "7th grade students creating a large poster display showing evolutionary evidence with diagrams of homologous structures and fossil timelines")
    },
    "pre_assessment": [
        "What is a fossil and how do you think they form?",
        "Why do you think your arm has the same bones as a whale's flipper?",
        "Draw what you think a transitional fossil between a fish and a land animal might look like.",
        "How do scientists figure out which animals are related to each other?"
    ],
    "extend_components": [
        ("Mutation Rate", "How quickly random genetic changes occur in populations, creating variation"),
        ("Geographic Isolation", "When populations are separated by physical barriers, preventing gene flow"),
        ("Ecological Niche Availability", "The number of open habitats and food sources available for new species")
    ],
    "reflections": [
        "How does finding the same bone structure in fish, frogs, birds, and humans support evolution?",
        "Why are transitional fossils like Tiktaalik so important to scientists?",
        "What would happen to the fossil record if a massive asteroid hit Earth today?",
        "How is your model similar to and different from real evolution?",
        "If evolution is real, why do we still have fish?"
    ],
    "dimensions": [
        ("Science Practice", "Analyzing and Interpreting Data", "Students analyze patterns in fossil evidence and anatomical data to construct explanations of evolutionary relationships."),
        ("Disciplinary Core Idea", "LS4.A Evidence of Common Ancestry and Diversity", "The fossil record documents the existence, diversity, extinction, and change of many life forms throughout history."),
        ("Crosscutting Concept", "Patterns", "Students identify patterns of anatomical similarity across species and through geological time as evidence of common ancestry.")
    ],
    "cast_items": [
        "Analyze fossil data to identify patterns of change over geological time",
        "Construct explanations for anatomical similarities between modern and ancient organisms",
        "Use evidence from the fossil record to support evolutionary relationships"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A scientist discovers that the flipper of a whale, the wing of a bat, and the arm of a human all contain the same bones. What does this evidence most likely indicate?"),
        ("Constructed Response:", "Using evidence from the fossil record, explain how scientists know that modern land vertebrates evolved from ancient fish. Include at least two types of evidence.")
    ],
    "background_intro": "The fossil record provides overwhelming evidence that life on Earth has changed dramatically over billions of years. By studying fossils and comparing anatomy, scientists reconstruct evolutionary relationships and understand how modern organisms are connected to ancient life.",
    "background_sections": [
        ("The Fossil Record", "Fossils form when organisms are buried in sediment before decomposition. Over millions of years, minerals replace organic material. The fossil record is incomplete — fossilization is rare — but it provides a clear timeline showing how life has changed across Earth's history."),
        ("Homologous Structures", "The arm of a human, the wing of a bat, the flipper of a whale, and the leg of a dog all contain the same basic bones: humerus, radius, and ulna. These homologous structures have the same evolutionary origin but have been modified for different functions, providing strong evidence for common ancestry."),
        ("Tiktaalik: Your Inner Fish", "In 2004, paleontologist Neil Shubin discovered Tiktaalik roseae, a 375-million-year-old fossil bridging fish and land animals. It had fish features (scales, fins) AND land features (flat head, neck, primitive wrist bones). It's one of the most famous transitional fossils ever found."),
        ("Extinction and Diversification", "Earth has experienced at least five mass extinction events. The most famous killed the non-avian dinosaurs 66 million years ago. But extinctions also open ecological niches — after the dinosaurs disappeared, mammals diversified rapidly, eventually leading to primates and humans.")
    ],
    "lever_L": "Students identify environmental change rate, geological time, anatomical similarity, and species diversity as components of the evolutionary system.",
    "lever_E": "Students determine that environmental change drives both extinction (reducing diversity) and adaptation (changing anatomy over time).",
    "lever_V": "Students build a model showing how environmental pressures and time interact to produce changes in species diversity and body structure.",
    "lever_Ev": "Students run stable, mass extinction, and gradual change scenarios to observe different evolutionary outcomes.",
    "lever_R": "Students add mutation rate or geographic isolation to explore more realistic evolutionary dynamics.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with fossil/human bone comparison", "say": "Look at your hand. Now look at this fish from 375 million years ago. Same bones.", "do": "Show side-by-side image of Tiktaalik and human arm bones.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we're investigating evidence that connects every animal alive to ancient ancestors.", "do": "Have students read objectives. Pre-teach 'homologous structure.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why do humans share bones with ancient fish?", "say": "This isn't coincidence. This is evidence of something incredible.", "do": "Show images of homologous structures. Ask: Why the same bones?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll model how the environment shapes life over millions of years.", "do": "Preview LEVER steps. Connect to prior knowledge about fossils.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for evolution model", "say": "What factors drive evolutionary change? What can the environment control?", "do": "Guide sorting. Discuss why time and environment are external inputs.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows", "say": "When the environment changes rapidly, what happens to species diversity?", "do": "Help students identify relationships. Discuss dual effects.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and results", "say": "Let's simulate a mass extinction and see what our model predicts!", "do": "Students predict first. Compare stable vs. mass extinction scenarios.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings", "say": "How does the fossil record match our model? What does Tiktaalik prove?", "do": "Show Tiktaalik fossil. Connect to model predictions.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Evolutionary evidence wall", "say": "You're now museum designers. Build an exhibit showing evidence for evolution.", "do": "Groups design evidence walls using fossil data.", "time": "12 min"}
    ],
    "sort_reasoning": "Environmental Change Rate and Time are external because organisms can't control how fast the environment changes or how much time passes. Anatomical Similarity and Species Diversity are internal because they change as a result of evolutionary responses to those external pressures.",
    "relationships": [
        ("Environmental Change Rate to Species Diversity", "NEGATIVE (-)", "Rapid environmental change causes extinctions, reducing the number of species. Organisms that can't adapt fast enough go extinct."),
        ("Time (Millions of Years) to Anatomical Similarity", "NEGATIVE (-)", "Over longer time periods, species diverge more from common ancestors, reducing anatomical similarity between distant relatives."),
        ("Species Diversity to Anatomical Similarity", "POSITIVE (+)", "Higher species diversity means more organisms share recent common ancestors, retaining more similar body structures.")
    ],
    "sim_answers": [
        ("Mass Extinction Scenario", "When Environmental Change Rate is maximized, Species Diversity crashes rapidly. Many species can't adapt fast enough. However, after change stabilizes, surviving species can diversify into empty niches. Anatomical Similarity decreases as survivors adapt to new environments."),
        ("Gradual Change Scenario", "With moderate change over long Time, Species Diversity stays relatively stable as organisms gradually adapt. Anatomical Similarity slowly decreases between diverging lineages, but homologous structures remain detectable even after millions of years.")
    ],
    "reflection_exemplars": [
        ("Why do different animals share the same bones?", "Homologous structures exist because all these animals evolved from the same common ancestor. The bones were inherited from that ancestor and modified over millions of years for different functions: grabbing, swimming, flying, and running."),
        ("Why do we still have fish?", "Humans didn't evolve FROM modern fish — we share a common ancestor WITH modern fish. About 375 million years ago, some fish-like creatures evolved features for land life, while others continued thriving in water. Both lineages kept evolving separately.")
    ],
    "stem_intro": "A natural history museum wants a new exhibit showing how fossils and anatomy prove evolutionary relationships. Your team will design an evidence wall telling the story of evolution from ancient fish to modern humans.",
    "stem_concepts": [
        ("Homologous vs. Analogous", "Homologous structures share the same origin (whale flipper = human arm). Analogous structures serve similar functions but have different origins (bird wing vs. butterfly wing). Only homologous structures prove common ancestry."),
        ("Transitional Fossils", "Fossils like Tiktaalik show features of two different groups, providing direct evidence of evolutionary transitions between major groups of organisms."),
        ("Biogeography", "The geographic distribution of species provides additional evidence — similar environments on different continents produce similar but unrelated species through convergent evolution.")
    ],
    "stem_eval": [
        ("Expert (4)", "Evidence wall includes homologous structures, transitional fossils, timeline, and clearly explains evolutionary relationships with model evidence"),
        ("Proficient (3)", "Evidence wall shows multiple types of evidence and connects them to evolutionary relationships"),
        ("Developing (2)", "Evidence wall includes some evidence but doesn't clearly connect it to evolution"),
        ("Beginning (1)", "Evidence wall is incomplete or shows misconceptions about evolutionary evidence")
    ],
    "support": [
        "Provide printed diagrams of homologous structures in 5 different animals for comparison",
        "Use a simplified geological timeline with major events pre-labeled",
        "Sentence frames: 'The fact that __ and __ share the same __ suggests they __'"
    ],
    "extensions": [
        "Research vestigial structures (human appendix, whale hip bones) as additional evolution evidence",
        "Compare embryological development across vertebrate species for shared patterns",
        "Create a cladogram showing evolutionary relationships between 6 species using anatomical data"
    ],
    "cross_curr": [
        ("Math", "Create a proportional timeline showing major evolutionary events across 4.5 billion years"),
        ("ELA", "Read excerpts from Neil Shubin's 'Your Inner Fish' and summarize the key evidence"),
        ("Social Studies", "Research how different cultures and time periods understood the origin of species")
    ],
    "misconceptions": [
        ("Humans evolved from monkeys", "Humans and modern apes share a common ancestor from about 6-7 million years ago. We didn't evolve FROM chimpanzees — we're evolutionary cousins. Both species have been evolving separately.", "Draw a family tree. Ask: Did you evolve from your cousin? No — you share a grandparent."),
        ("Evolution is just a theory", "In science, 'theory' means a well-tested explanation supported by massive evidence. Evolution is supported by fossils, genetics, anatomy, and direct observation. Gravity is also 'just a theory.'", "Compare everyday 'theory' (guess) with scientific 'theory' (tested explanation)."),
        ("Fossils should show every step", "Fossilization is extremely rare — most organisms decompose completely. The fossil record will always have gaps, but the fossils we DO have consistently support evolutionary patterns.", "Ask: If you lost most pages of a book but kept every 10th page, could you still figure out the story?")
    ]
}

L03 = {
    "id": "G07-L03",
    "title": "Earth Has a Fever",
    "subtitle": "Why 2 Degrees Could Change Everything",
    "ngss": "MS-ESS3-5",
    "ngss_desc": "Ask questions to clarify evidence of the factors that have caused the rise in global temperatures over the past century.",
    "big_question": "If Earth's temperature rises by just 2 degrees Celsius, why could it change everything?",
    "objectives": [
        "Explain how the greenhouse effect traps heat in Earth's atmosphere",
        "Model how increasing CO2 concentration affects global temperature and ice coverage",
        "Predict cascade effects of rising temperatures on sea level and weather patterns",
        "Evaluate human contributions to climate change using model evidence"
    ],
    "vocabulary": [
        ("Greenhouse Effect", "The process where certain gases in Earth's atmosphere trap heat from the Sun, warming the planet's surface"),
        ("Carbon Footprint", "The total amount of greenhouse gases produced by human activities, measured in CO2 equivalents"),
        ("Thermal Expansion", "When water warms, its molecules move faster and spread apart, causing ocean water to take up more space"),
        ("Feedback Loop", "When the output of a system amplifies or reduces the original input, creating a cycle")
    ],
    "components": [
        ("CO2 Concentration", "The amount of carbon dioxide in Earth's atmosphere from burning fossil fuels and deforestation", True),
        ("Solar Energy Input", "The amount of energy Earth receives from the Sun", True),
        ("Average Global Temperature", "The mean surface temperature of the entire planet", False),
        ("Ice Sheet Coverage", "The total area of Earth covered by glaciers and polar ice caps", False)
    ],
    "think_about_it": "When CO2 concentration increases, global temperature rises. But what happens to ice sheets when temperature rises — and does melting ice create a feedback loop?",
    "scenarios": [
        ("Pre-Industrial Baseline", "Set CO2 Concentration to low (280 ppm) and observe temperature stability"),
        ("Current Trajectory", "Lock CO2 Concentration to high levels and observe cascade effects on temperature and ice"),
        ("Paris Agreement Goals", "Set CO2 to moderate reduction levels and compare to current trajectory")
    ],
    "sim_scenarios": [
        ("Pre-Industrial", "CO2 at low historical levels, stable solar input", "What do you predict happens to Ice Sheet Coverage when CO2 is at pre-industrial levels?"),
        ("Current Trajectory", "CO2 locked at high and rising levels", "What do you predict will happen to Average Global Temperature and Ice Sheet Coverage if CO2 keeps rising?"),
        ("Emission Reduction", "CO2 reduced to moderate levels", "How much difference do you predict emission reduction makes compared to the current trajectory?")
    ],
    "discoveries": [
        "CO2 acts like a blanket — more CO2 traps more heat, raising global temperature",
        "Rising temperatures melt ice sheets, which reduces Earth's reflectivity and causes MORE warming (positive feedback)",
        "Even 2°C of warming dramatically changes weather patterns, sea levels, and ecosystems",
        "Human activities have increased atmospheric CO2 by over 50% since the Industrial Revolution"
    ],
    "answer": "Even 2°C of warming matters enormously because Earth's climate system has feedback loops. Rising CO2 traps heat, which melts ice, which exposes dark ocean that absorbs MORE heat, causing MORE melting. Small temperature changes cascade into massive effects on sea level, weather, and ecosystems!",
    "stem_title": "Design a School Climate Action Plan",
    "stem_mission": "Create an evidence-based climate action plan for your school that reduces carbon emissions and educates the community, using data from your model.",
    "stem_scenario": "Your school district wants to reduce its carbon footprint by 50% in 10 years. The superintendent needs your team to propose specific actions with evidence showing they'll work.",
    "stem_questions": [
        "Which actions would reduce your school's carbon footprint the most?",
        "How can you use your model to show the impact of different reduction strategies?",
        "What role can students play in fighting climate change at the local level?"
    ],
    "stem_design_qs": [
        "What are the biggest sources of CO2 emissions at your school?",
        "Which reduction strategies are most practical and cost-effective?",
        "How will you educate other students about climate science?",
        "How will you measure whether your plan is working?"
    ],
    "career": "Climate Scientists analyze climate data and build complex models to predict future conditions. They work for NOAA, NASA, universities, and environmental organizations, earning $80,000–$140,000/year.",
    "images": {
        "cover": ("cover-climate.png", "A dramatic split image showing a healthy green glacier landscape on one side and the same landscape with melted ice and rising water on the other, showing climate change impact"),
        "landscape": ("landscape-climate.png", "7th grade students outdoors measuring temperature, wind, and CO2 levels with portable science equipment, engaged in environmental monitoring"),
        "modeling": ("modeling-climate.png", "A diverse group of 7th grade students working on laptops building a digital climate model, classroom with climate change infographics on walls"),
        "discussion": ("discussion-climate.png", "A teacher leading an animated discussion with 7th grade students about climate data graphs on a smartboard, students asking questions and pointing at data"),
        "stem": ("stem-climate-action.png", "7th grade students presenting a climate action plan poster to classmates, showing graphs and reduction strategies, professional presentation style")
    },
    "pre_assessment": [
        "What do you think causes Earth's temperature to change?",
        "Why do you think ice at the North and South Poles is melting?",
        "What is the greenhouse effect? Draw what you think it looks like.",
        "How do human activities affect Earth's temperature?"
    ],
    "extend_components": [
        ("Methane Emissions", "Methane is a greenhouse gas 80x more potent than CO2, released by livestock, landfills, and permafrost"),
        ("Ocean Absorption", "Oceans absorb about 30% of CO2 from the atmosphere, but this makes them more acidic"),
        ("Albedo Effect", "The reflectivity of Earth's surface — ice reflects sunlight while dark ocean absorbs it")
    ],
    "reflections": [
        "Why is a 2°C rise in global temperature considered dangerous when daily temperatures vary by much more?",
        "How does the melting of ice sheets create a positive feedback loop that accelerates warming?",
        "What evidence from the last 100 years shows that human activity is driving climate change?",
        "How does your model help you understand why some people say climate change is 'accelerating'?",
        "What would it take to reverse the trend your model shows?"
    ],
    "dimensions": [
        ("Science Practice", "Asking Questions and Defining Problems", "Students ask questions to clarify evidence about factors causing global temperature rises."),
        ("Disciplinary Core Idea", "ESS3.D Global Climate Change", "Human activities have significantly altered the biosphere, sometimes damaging or destroying natural habitats and causing extinction of species."),
        ("Crosscutting Concept", "Stability and Change", "Students analyze how small changes in CO2 concentration create large, cascading changes in global climate systems.")
    ],
    "cast_items": [
        "Identify evidence that human activities have increased greenhouse gas concentrations",
        "Explain the relationship between CO2 concentration and global temperature",
        "Evaluate the potential impacts of different levels of global warming"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Since 1850, atmospheric CO2 has increased from 280 ppm to over 420 ppm. During the same period, average global temperature has risen about 1.1°C. Which statement best explains this relationship?"),
        ("Constructed Response:", "Using evidence from your climate model, explain why scientists are concerned about a 2°C rise in global temperature. Include at least one feedback loop in your explanation.")
    ],
    "background_intro": "Climate change is one of the defining challenges of the 21st century. Understanding the science behind it — greenhouse gases, feedback loops, and cascading effects — is essential for making informed decisions about our planet's future.",
    "background_sections": [
        ("The Greenhouse Effect", "Certain gases in Earth's atmosphere (CO2, methane, water vapor) allow sunlight to pass through but trap heat radiating back from Earth's surface. This natural greenhouse effect keeps Earth habitable — without it, average temperature would be -18°C. The problem is that human activities are dramatically increasing greenhouse gas concentrations."),
        ("CO2 and Temperature", "Atmospheric CO2 has increased from 280 ppm (pre-industrial) to over 420 ppm today — a 50% increase. Ice core data shows that CO2 and temperature have moved together for 800,000 years. The current rate of CO2 increase is unprecedented in the geological record."),
        ("Feedback Loops", "Climate change involves powerful feedback loops. As temperatures rise, ice melts, exposing dark ocean and land that absorb MORE heat (ice-albedo feedback). Warming permafrost releases stored methane, causing MORE warming. These positive feedbacks can accelerate change beyond what CO2 alone would cause."),
        ("Impacts of 2°C Warming", "At 2°C above pre-industrial levels: sea levels could rise 0.5m+ (flooding coastal cities), extreme weather events become more frequent, coral reefs face mass extinction, agricultural zones shift, and water scarcity affects billions. The difference between 1.5°C and 2°C is enormous in terms of human impact.")
    ],
    "lever_L": "Students identify CO2 concentration, solar energy, global temperature, and ice sheet coverage as key components of the climate system.",
    "lever_E": "Students determine that CO2 positively affects temperature, which negatively affects ice coverage, creating a cascade of effects.",
    "lever_V": "Students build a climate model showing how greenhouse gas increases drive temperature and ice changes.",
    "lever_Ev": "Students run pre-industrial, current trajectory, and emission reduction scenarios to compare outcomes.",
    "lever_R": "Students add methane emissions or albedo effect to explore feedback loops in the climate system.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with glacier/melting comparison", "say": "Earth has a fever. And we gave it to her. Let's understand why.", "do": "Show before/after photos of glaciers from the same location decades apart.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we're modeling the biggest science story of your lifetime.", "do": "Have students read objectives. Pre-teach 'greenhouse effect' and 'feedback loop.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why does 2°C matter?", "say": "Your body temperature varies by 1-2 degrees daily. No big deal. But for Earth? It changes EVERYTHING.", "do": "Show graph of global temperature over last century. Discuss scale.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll build a climate model to see why small changes have huge effects.", "do": "Preview LEVER steps.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for climate model", "say": "What controls Earth's temperature? What can humans influence?", "do": "Guide sorting. Discuss why CO2 is external (human-controlled input).", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows", "say": "More CO2 means more heat trapped. But what does that DO to ice?", "do": "Help students trace the cascade from CO2 to temperature to ice.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and results", "say": "Let's compare pre-industrial Earth to today. What does our model predict?", "do": "Students predict first. Compare scenarios side by side.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings", "say": "Why do scientists say climate change is accelerating? What did our model reveal?", "do": "Lead discussion about feedback loops. Connect to real data.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Climate action plan", "say": "You have the science. Now design a solution for YOUR school.", "do": "Groups design climate action plans with specific targets.", "time": "12 min"}
    ],
    "sort_reasoning": "CO2 Concentration and Solar Energy Input are external because they are inputs to the climate system — CO2 comes from human activities and natural sources, while solar energy comes from the Sun. Average Global Temperature and Ice Sheet Coverage are internal because they change as a result of those external energy inputs.",
    "relationships": [
        ("CO2 Concentration to Average Global Temperature", "POSITIVE (+)", "More CO2 in the atmosphere traps more heat through the greenhouse effect, causing average temperatures to rise."),
        ("Solar Energy Input to Average Global Temperature", "POSITIVE (+)", "More solar energy hitting Earth's surface increases the amount of heat available, raising temperatures."),
        ("Average Global Temperature to Ice Sheet Coverage", "NEGATIVE (-)", "As global temperatures rise, ice sheets and glaciers melt, reducing the total area of Earth covered by ice.")
    ],
    "sim_answers": [
        ("Current Trajectory Scenario", "When CO2 Concentration is locked at high levels, Average Global Temperature rises steadily. Ice Sheet Coverage decreases as temperatures climb. The model shows that sustained high CO2 leads to continuous warming and ice loss — matching real-world observations."),
        ("Emission Reduction Scenario", "When CO2 is reduced to moderate levels, temperature still rises but much more slowly. Ice Sheet Coverage decreases less dramatically. The key insight: even reduced emissions don't immediately reverse warming, but they significantly slow the rate of change.")
    ],
    "reflection_exemplars": [
        ("Why is 2°C dangerous if daily temps vary more?", "Daily temperature variations are LOCAL and TEMPORARY. A 2°C rise in AVERAGE GLOBAL temperature means the entire planet — every ocean, every continent, every ecosystem — is warmer all the time. It shifts weather patterns, melts ice caps permanently, raises sea levels globally, and disrupts ecosystems that evolved for specific temperature ranges."),
        ("How does ice melting create a feedback loop?", "Ice is white and reflects sunlight (high albedo). When ice melts, it exposes dark ocean water that ABSORBS heat instead. This absorbed heat raises temperatures further, melting MORE ice, exposing MORE dark water, absorbing MORE heat. The original warming AMPLIFIES itself — that's a positive feedback loop.")
    ],
    "stem_intro": "Your school district wants to cut carbon emissions by 50% in 10 years. The superintendent needs evidence-based recommendations. Use your climate model data to propose specific, measurable actions.",
    "stem_concepts": [
        ("Carbon Budget", "The total amount of CO2 that can still be emitted while keeping warming below a target. At current rates, the 1.5°C budget may be exhausted within a decade."),
        ("Mitigation vs. Adaptation", "Mitigation means reducing emissions to slow warming. Adaptation means preparing for changes that are already inevitable. Effective climate policy requires both."),
        ("Renewable Energy", "Solar, wind, and hydroelectric power produce electricity without burning fossil fuels, dramatically reducing CO2 emissions compared to coal, oil, and natural gas.")
    ],
    "stem_eval": [
        ("Expert (4)", "Plan includes specific emission reduction targets, references model evidence, addresses multiple strategies, and includes a measurement system"),
        ("Proficient (3)", "Plan references climate model data and includes at least two specific reduction strategies"),
        ("Developing (2)", "Plan mentions climate change but lacks specific evidence or measurable targets"),
        ("Beginning (1)", "Plan doesn't connect to model findings or lacks actionable strategies")
    ],
    "support": [
        "Provide a simplified CO2 vs. temperature graph for reference during model building",
        "Use ice cubes under a lamp to physically demonstrate the ice-albedo feedback loop",
        "Sentence frames: 'When CO2 increases, temperature __ because __, which causes ice to __'"
    ],
    "extensions": [
        "Research the ice-albedo feedback loop and add it as a component to the model",
        "Analyze real NASA temperature data and compare trends to model predictions",
        "Calculate your personal carbon footprint and design a reduction strategy"
    ],
    "cross_curr": [
        ("Math", "Graph CO2 concentration vs. temperature data from the last 200 years and calculate the rate of change"),
        ("ELA", "Write a persuasive letter to a local politician using your model evidence to argue for climate action"),
        ("Social Studies", "Research how climate change disproportionately affects developing nations and discuss climate justice")
    ],
    "misconceptions": [
        ("Weather and climate are the same thing", "Weather is short-term, local conditions (today's temperature). Climate is long-term, global patterns (average temperature over decades). A cold day doesn't disprove climate change — it's the long-term TREND that matters.", "Show a graph of daily temperatures (noisy) vs. the 30-year average trend (clearly rising). Ask: Which tells the real story?"),
        ("The greenhouse effect is bad", "The NATURAL greenhouse effect is essential — without it, Earth would be frozen. The problem is that humans have ENHANCED it by adding excess CO2, trapping more heat than the system can handle.", "Ask: Is a blanket bad? No — but if you pile on 10 blankets in summer, you'll overheat. Same concept."),
        ("Scientists disagree about climate change", "Over 97% of climate scientists agree that human activities are causing global warming. The scientific consensus is overwhelming. Disagreement exists about exact timelines and solutions, not about whether it's happening.", "Show the 97% statistic visually. Compare to: 97% of doctors agree smoking causes cancer — would you argue?")
    ]
}

L04 = {
    "id": "G07-L04",
    "title": "The Invisible Force That Charges Your Phone",
    "subtitle": "How Electricity and Magnetism Shape Our World",
    "ngss": "MS-PS2-3, MS-PS2-5",
    "ngss_desc": "Ask questions about data to determine the factors that affect the strength of electric and magnetic forces. Conduct an investigation and evaluate the experimental design to provide evidence that fields exist between objects exerting forces on each other even though the objects are not in contact.",
    "big_question": "How can a force you can't see, smell, or touch move objects and transfer energy?",
    "objectives": [
        "Explain how electric current flowing through a wire creates a magnetic field",
        "Model the factors that affect electromagnet strength — current, coils, and core material",
        "Predict how changing variables affects the strength of an electromagnetic force",
        "Design experiments to test how invisible fields exert real forces on objects"
    ],
    "vocabulary": [
        ("Electromagnet", "A magnet created by wrapping a current-carrying wire around a metal core — its strength can be controlled"),
        ("Magnetic Field", "The invisible area of force around a magnet that can attract or repel magnetic materials"),
        ("Electric Current", "The flow of electric charge through a conductor, measured in amperes"),
        ("Electromagnetic Induction", "The process of generating electric current by moving a magnet through a coil of wire")
    ],
    "components": [
        ("Electric Current", "The amount of electricity flowing through the wire, controlled by a power source", True),
        ("Number of Coil Wraps", "How many times the wire is wrapped around the metal core", True),
        ("Magnetic Field Strength", "How strong the invisible magnetic force is around the electromagnet", False),
        ("Lifting Capacity", "How much weight the electromagnet can pick up and hold against gravity", False)
    ],
    "think_about_it": "When you increase both the electric current AND the number of coil wraps, what do you predict happens to the magnetic field strength? Is it additive or multiplicative?",
    "scenarios": [
        ("Low Power", "Set Electric Current to low and Number of Coil Wraps to few — observe Lifting Capacity"),
        ("Maximum Coils", "Lock Number of Coil Wraps to maximum while keeping current moderate"),
        ("Full Power", "Set both Electric Current and Coil Wraps to maximum and observe the combined effect")
    ],
    "sim_scenarios": [
        ("Low Power", "Low current, few coils", "What do you predict the Lifting Capacity will be with a weak electromagnet?"),
        ("Maximum Coils", "Many coils, moderate current", "What do you predict happens to Magnetic Field Strength when you add more coils?"),
        ("Full Power", "Maximum current AND maximum coils", "How do you predict the combined effect compares to changing just one variable?")
    ],
    "discoveries": [
        "Electric current creates a magnetic field around a wire — electricity and magnetism are connected",
        "More coil wraps concentrate the magnetic field, making the electromagnet stronger",
        "Increasing current increases the force — more electrons flowing means a stronger field",
        "Electromagnets can be turned on and off, unlike permanent magnets — this makes them incredibly useful"
    ],
    "answer": "Invisible electromagnetic forces work because moving electric charges (current) create magnetic fields around them. By wrapping wire into coils and increasing current, we concentrate this invisible force into something strong enough to lift cars in junkyards — all from a force you can't see!",
    "stem_title": "Design the Ultimate Electromagnet",
    "stem_mission": "Engineer the strongest possible electromagnet using limited materials, then test it by measuring how much weight it can lift.",
    "stem_scenario": "A recycling facility needs a new electromagnet crane to sort metal from waste. Your engineering team must design and test a prototype that lifts the maximum weight using the materials provided.",
    "stem_questions": [
        "What combination of current and coils produces the strongest electromagnet?",
        "How does the core material affect electromagnet strength?",
        "What are the limits of your design — when does adding more coils or current stop helping?"
    ],
    "stem_design_qs": [
        "How many coil wraps will you use and why?",
        "What power level will you set your current to?",
        "What core material will give the best results?",
        "How will you measure and record your electromagnet's lifting capacity?"
    ],
    "career": "Electrical Engineers design circuits, motors, generators, and electromagnetic devices used in everything from phones to MRI machines. They earn $75,000–$130,000/year.",
    "images": {
        "cover": ("cover-electromagnet.png", "A dramatic close-up of a powerful industrial electromagnet lifting scrap metal at a junkyard, sparks of energy visible, with magnetic field lines artistically visible"),
        "landscape": ("landscape-magnets.png", "7th grade students conducting a hands-on electromagnet experiment with batteries, wire coils, and paper clips in a science lab, testing magnetic strength"),
        "modeling": ("modeling-electromagnet.png", "A diverse group of 7th grade students working on laptops building a digital electromagnet model, classroom with physics diagrams on walls"),
        "discussion": ("discussion-magnets.png", "A teacher demonstrating magnetic field lines with iron filings on paper over a magnet while 7th grade students watch closely and take notes"),
        "stem": ("stem-electromagnet.png", "7th grade students building electromagnets from wire, nails, and batteries, testing how many paper clips they can lift, competitive and engaged")
    },
    "pre_assessment": [
        "What is a magnet and how does it work?",
        "Can you make a magnet stronger or weaker? How?",
        "What do you think connects electricity and magnetism?",
        "Draw what you think a magnetic field looks like around a magnet."
    ],
    "extend_components": [
        ("Core Material", "The type of metal inside the coil — iron cores concentrate magnetic fields better than air"),
        ("Distance from Object", "Magnetic force decreases rapidly with distance — the closer the object, the stronger the pull"),
        ("Temperature", "Heating a magnet weakens it because thermal energy disrupts the alignment of magnetic domains")
    ],
    "reflections": [
        "Why are electromagnets more useful than permanent magnets in many applications?",
        "How does your phone use electromagnetic forces every day?",
        "What would happen to our technology if we couldn't create magnetic fields with electricity?",
        "Why does the magnetic force get weaker when you move farther away?",
        "How does your model prove that invisible forces are real even though we can't see them?"
    ],
    "dimensions": [
        ("Science Practice", "Asking Questions and Planning Investigations", "Students ask questions about data and design investigations to determine factors affecting electromagnetic force strength."),
        ("Disciplinary Core Idea", "PS2.B Types of Interactions", "Electric and magnetic forces between a pair of objects do not require contact. The sizes of the forces in each situation depend on the properties of the objects and their distances apart."),
        ("Crosscutting Concept", "Cause and Effect", "Students identify that specific changes in current and coils CAUSE predictable changes in magnetic field strength and lifting capacity.")
    ],
    "cast_items": [
        "Identify factors that affect the strength of electromagnetic forces",
        "Provide evidence that fields exist between objects not in contact",
        "Design investigations to test electromagnetic principles"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A student wraps 50 turns of wire around an iron nail and connects it to a battery. The electromagnet picks up 10 paper clips. Which change would most likely INCREASE the number of paper clips it can lift?"),
        ("Constructed Response:", "Design an experiment to test how the number of coil wraps affects the strength of an electromagnet. Include your hypothesis, variables, and how you would measure the results.")
    ],
    "background_intro": "Electromagnetism is one of the four fundamental forces of nature and the foundation of modern technology. Every electric motor, generator, speaker, and MRI machine relies on the connection between electricity and magnetism discovered in the 1800s.",
    "background_sections": [
        ("Electricity Creates Magnetism", "In 1820, Hans Christian Oersted discovered that electric current creates a magnetic field around a wire. This was revolutionary — it showed that electricity and magnetism are not separate forces but aspects of the same phenomenon. Every wire carrying current is a tiny magnet."),
        ("How Electromagnets Work", "Wrapping current-carrying wire into a coil concentrates the magnetic field. Each loop of wire adds its field to the next, creating a much stronger combined field. Adding an iron core further amplifies the effect because iron is easily magnetized, aligning its internal magnetic domains with the coil's field."),
        ("Factors Affecting Strength", "Three main factors control electromagnet strength: (1) Current — more current means a stronger field; (2) Number of coils — more wraps concentrate the field; (3) Core material — ferromagnetic materials like iron amplify the field. These factors combine to determine the total electromagnetic force."),
        ("Real-World Applications", "Electromagnets are everywhere: electric motors (fans, cars, power tools), generators (power plants), speakers (phones, headphones), MRI machines (hospitals), maglev trains, and junkyard cranes. The ability to turn magnetism on and off with a switch makes electromagnets far more versatile than permanent magnets.")
    ],
    "lever_L": "Students identify electric current, number of coil wraps, magnetic field strength, and lifting capacity as components of the electromagnetic system.",
    "lever_E": "Students determine that both current and coils positively affect field strength, which positively affects lifting capacity.",
    "lever_V": "Students build a model showing how electrical inputs create magnetic force outputs.",
    "lever_Ev": "Students run low power, maximum coils, and full power scenarios to test how variables affect strength.",
    "lever_R": "Students add core material or distance to explore more complex electromagnetic interactions.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with electromagnet crane imagery", "say": "Your phone charges wirelessly. Junkyard cranes lift cars with invisible force. How?", "do": "Show video of electromagnetic crane in action.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we're investigating a force that's literally invisible but runs our entire world.", "do": "Have students read objectives. Pre-teach 'electromagnet' vs. 'permanent magnet.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "How can an invisible force move objects?", "say": "You can't see it. Can't smell it. Can't taste it. But it can lift a CAR.", "do": "Demonstrate with magnet and paper clips. Ask: How does it work through air?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll model how electricity creates magnetism and what controls its strength.", "do": "Preview LEVER steps.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards", "say": "What inputs control an electromagnet? What outputs can we measure?", "do": "Guide sorting. Discuss why current and coils are external inputs.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows", "say": "More current, more coils — what happens to the invisible field?", "do": "Help students identify all-positive relationships in this system.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and results", "say": "Let's test: what creates the strongest electromagnet — more coils or more current?", "do": "Students predict first. Compare single vs. combined variable changes.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings", "say": "How does this invisible force work? What did our model reveal?", "do": "Discuss electricity-magnetism connection. Show field lines with iron filings.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Electromagnet design challenge", "say": "You're engineers now. Build the strongest electromagnet you can!", "do": "Distribute materials. Groups compete to lift the most paper clips.", "time": "12 min"}
    ],
    "sort_reasoning": "Electric Current and Number of Coil Wraps are external because they are design inputs that engineers control — you choose how much current to send and how many times to wrap the wire. Magnetic Field Strength and Lifting Capacity are internal because they are outputs that change as a result of those design choices.",
    "relationships": [
        ("Electric Current to Magnetic Field Strength", "POSITIVE (+)", "More electric current flowing through the wire creates a stronger magnetic field around the coil. More moving charges means more magnetic force."),
        ("Number of Coil Wraps to Magnetic Field Strength", "POSITIVE (+)", "Each additional wrap of wire adds its magnetic field to the total. More coils concentrate and amplify the field."),
        ("Magnetic Field Strength to Lifting Capacity", "POSITIVE (+)", "A stronger magnetic field exerts more force on magnetic objects, allowing the electromagnet to pick up and hold more weight.")
    ],
    "sim_answers": [
        ("Maximum Coils Scenario", "When Number of Coil Wraps is maximized with moderate current, Magnetic Field Strength increases significantly. Lifting Capacity rises proportionally. Each additional coil contributes to the total field strength."),
        ("Full Power Scenario", "When both Electric Current AND Coil Wraps are at maximum, Magnetic Field Strength reaches its peak. The combined effect is greater than either variable alone — they multiply rather than simply add. This demonstrates why real electromagnets optimize BOTH variables.")
    ],
    "reflection_exemplars": [
        ("Why are electromagnets more useful than permanent magnets?", "Electromagnets can be turned ON and OFF with a switch — permanent magnets can't. This is critical for applications like junkyard cranes (pick up, move, drop), MRI machines (controlled scanning), electric motors (alternating field creates rotation), and speakers (rapidly changing field creates sound waves)."),
        ("How does your phone use electromagnetic forces?", "Your phone's speaker uses an electromagnet to vibrate a diaphragm (sound). The vibration motor is a tiny electric motor (electromagnetic rotation). Wireless charging uses electromagnetic induction. The cellular antenna sends and receives electromagnetic waves. The touchscreen uses electric fields to detect your finger.")
    ],
    "stem_intro": "Present the challenge: A recycling facility needs a prototype electromagnet crane. Your team must design one that lifts the maximum weight using limited materials. Test, measure, and optimize your design.",
    "stem_concepts": [
        ("Magnetic Domains", "Inside ferromagnetic materials like iron, groups of atoms create tiny magnetic regions called domains. An external field aligns these domains, amplifying the effect."),
        ("Electromagnetic Induction", "Moving a magnet through a coil of wire generates electric current — the reverse of making an electromagnet. This is how generators and power plants produce electricity."),
        ("Field Strength vs. Distance", "Magnetic force follows an inverse relationship with distance — doubling the distance reduces the force dramatically. This is why electromagnets must be close to the object they're lifting.")
    ],
    "stem_eval": [
        ("Expert (4)", "Design optimizes both current and coils, tests multiple configurations, records data, and explains electromagnetic principles"),
        ("Proficient (3)", "Design systematically tests at least two variables and records lifting capacity data"),
        ("Developing (2)", "Design builds a working electromagnet but doesn't systematically test variables"),
        ("Beginning (1)", "Design is incomplete or electromagnet doesn't function")
    ],
    "support": [
        "Provide a step-by-step guide for building a basic electromagnet (battery + wire + nail)",
        "Use iron filings on paper to visualize magnetic field lines around the electromagnet",
        "Sentence frames: 'When I increased the number of coils, the lifting capacity __ because __'"
    ],
    "extensions": [
        "Research how MRI machines use powerful electromagnets to image the human body",
        "Build a simple electric motor using an electromagnet and permanent magnet",
        "Investigate electromagnetic induction by moving a magnet through a coil connected to an LED"
    ],
    "cross_curr": [
        ("Math", "Graph the relationship between number of coils and lifting capacity — is it linear or exponential?"),
        ("ELA", "Write a technical report documenting your electromagnet design process and results"),
        ("Social Studies", "Research how electromagnetic technology (telegraph, motors, generators) transformed society in the 1800s")
    ],
    "misconceptions": [
        ("Magnets are magic", "Magnetism is a fundamental force of nature with well-understood physics. It results from the motion of electric charges at the atomic level. Every magnet works because of electron behavior.", "Build an electromagnet. Turn current on = magnet. Turn off = not a magnet. It's physics, not magic."),
        ("Electricity and magnetism are unrelated", "Electricity and magnetism are two aspects of the SAME force — electromagnetism. Moving charges create magnetic fields, and moving magnets create electric current. They are fundamentally linked.", "Show Oersted's experiment: a compass needle deflects when current flows through a nearby wire."),
        ("Bigger magnets are always stronger", "Size alone doesn't determine magnet strength. An electromagnet's strength depends on current, number of coils, and core material — not just physical size. A small, well-designed electromagnet can be stronger than a large one.", "Compare a large weak magnet to a small powerful one. Measure lifting capacity of each.")
    ]
}

L05 = {
    "id": "G07-L05",
    "title": "Every Drop You Drink Is Recycled Dinosaur Water",
    "subtitle": "The Never-Ending Journey of Water on Earth",
    "ngss": "MS-ESS2-4",
    "ngss_desc": "Develop a model to describe the cycling of water through Earth's systems driven by energy from the Sun and the force of gravity.",
    "big_question": "Why doesn't Earth ever run out of water if we use billions of gallons every day?",
    "objectives": [
        "Model how solar energy drives the water cycle through evaporation and condensation",
        "Explain the role of gravity in precipitation and groundwater flow",
        "Predict how changing temperature affects water cycle rates and patterns",
        "Trace water through all phases and reservoirs in Earth's system"
    ],
    "vocabulary": [
        ("Evaporation", "When liquid water absorbs heat energy and transforms into water vapor gas"),
        ("Condensation", "When water vapor cools and transforms back into liquid water droplets, forming clouds"),
        ("Transpiration", "When plants release water vapor through tiny pores in their leaves"),
        ("Watershed", "An area of land where all water drains to a common outlet like a river, lake, or ocean")
    ],
    "components": [
        ("Solar Energy", "Heat energy from the Sun that drives evaporation from oceans, lakes, and land", True),
        ("Ground Temperature", "The temperature of Earth's surface, which affects how quickly water evaporates", True),
        ("Evaporation Rate", "How quickly liquid water transforms into water vapor and enters the atmosphere", False),
        ("Precipitation Rate", "How quickly water falls back to Earth's surface as rain, snow, sleet, or hail", False)
    ],
    "think_about_it": "When solar energy increases dramatically (like during summer), what happens to the evaporation rate — and does more evaporation always mean more precipitation in the same area?",
    "scenarios": [
        ("Summer Heat Wave", "Set Solar Energy and Ground Temperature to maximum and observe water cycle rates"),
        ("Winter Freeze", "Lock Ground Temperature to near-freezing and observe how the cycle slows"),
        ("Normal Conditions", "Set moderate values for both inputs and observe the balanced cycle")
    ],
    "sim_scenarios": [
        ("Summer Heat Wave", "Maximum solar energy and ground temperature", "What do you predict happens to Evaporation Rate during a heat wave?"),
        ("Winter Freeze", "Ground Temperature near freezing, reduced solar energy", "What do you predict happens to the water cycle when temperatures drop?"),
        ("Normal Conditions", "Moderate solar energy and temperature", "How do you predict the water cycle maintains balance under normal conditions?")
    ],
    "discoveries": [
        "The Sun is the engine of the water cycle — without solar energy, water wouldn't evaporate",
        "Gravity pulls precipitation back to Earth and drives groundwater flow downhill",
        "The same water molecules have been cycling through Earth's systems for billions of years",
        "Temperature controls the SPEED of the cycle — hotter conditions accelerate it"
    ],
    "answer": "Earth never runs out of water because it's continuously RECYCLED. Solar energy evaporates water from oceans and lakes, wind carries it as clouds, gravity pulls it back as rain, and it flows back to the ocean. The same water has been cycling for 4.5 billion years — every drop you drink was once a dinosaur's drink!",
    "stem_title": "Design a Water Purification System",
    "stem_mission": "Engineer a portable water purification system using your understanding of the water cycle — specifically evaporation and condensation — to make dirty water drinkable.",
    "stem_scenario": "After a natural disaster, clean water supplies are contaminated. Your engineering team must design a solar-powered water purification system using water cycle principles to provide clean drinking water.",
    "stem_questions": [
        "How can you use evaporation and condensation to separate clean water from contaminants?",
        "What role does solar energy play in your purification system?",
        "How would you scale your design to produce enough water for a family?"
    ],
    "stem_design_qs": [
        "How will you use solar energy to evaporate contaminated water?",
        "How will you capture and condense the water vapor?",
        "How will you collect the purified water?",
        "How will you test whether your purified water is actually clean?"
    ],
    "career": "Hydrologists study the movement, distribution, and quality of water on Earth. They work for government agencies, environmental firms, and water utilities, earning $65,000–$110,000/year.",
    "images": {
        "cover": ("cover-water-cycle.png", "A dramatic landscape showing the complete water cycle in action — sunlight evaporating ocean water, clouds forming over mountains, rain falling into a river flowing back to the sea, golden hour lighting"),
        "landscape": ("landscape-water.png", "7th grade students outdoors at a stream or lake collecting water samples and measuring temperature with science equipment, nature setting"),
        "modeling": ("modeling-water.png", "A diverse group of 7th grade students working on laptops building a digital water cycle model, classroom with water cycle diagrams on walls"),
        "discussion": ("discussion-water.png", "A teacher using a terrarium or sealed jar to demonstrate the water cycle while 7th grade students observe condensation forming, engaged classroom"),
        "stem": ("stem-water-purification.png", "7th grade students building solar water purification systems from plastic bottles, bowls, and plastic wrap, testing their designs with colored water")
    },
    "pre_assessment": [
        "Where does the water you drink come from originally?",
        "What happens to water in a puddle on a hot day?",
        "Draw what you think happens to water as it moves through Earth's systems.",
        "Could the water you drink today have once been in a dinosaur? Why or why not?"
    ],
    "extend_components": [
        ("Wind Patterns", "Wind carries water vapor from oceans to land, determining where precipitation falls"),
        ("Plant Transpiration", "Plants release water vapor through their leaves, adding significant moisture to the atmosphere"),
        ("Human Water Use", "Humans withdraw water from rivers, lakes, and aquifers, affecting how much is available for natural cycling")
    ],
    "reflections": [
        "Why is the water cycle called a CYCLE and not a one-way process?",
        "How does cutting down forests affect the water cycle in that region?",
        "Why do some places get floods while nearby places have droughts at the same time?",
        "What would happen to the water cycle if the Sun suddenly produced less energy?",
        "How does understanding the water cycle help us manage water resources?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop a computational model to describe the cycling of water through Earth's systems."),
        ("Disciplinary Core Idea", "ESS2.C The Roles of Water in Earth's Surface Processes", "Water continually cycles among land, ocean, and atmosphere via transpiration, evaporation, condensation, crystallization, and precipitation."),
        ("Crosscutting Concept", "Energy and Matter", "Students trace the flow of energy (solar) and matter (water) through the water cycle system, showing that matter is conserved as it changes form.")
    ],
    "cast_items": [
        "Describe how solar energy and gravity drive the water cycle",
        "Model the cycling of water through Earth's atmosphere, surface, and underground systems",
        "Explain how changes in one part of the water cycle affect other parts"
    ],
    "cast_questions": [
        ("Multiple Choice:", "During a heat wave, evaporation rates from a lake increase significantly. Which of the following is the most likely effect on the local water cycle?"),
        ("Constructed Response:", "Develop and describe a model showing how water cycles through Earth's systems. Explain the role of solar energy and gravity in driving this cycle.")
    ],
    "background_intro": "Water is the most important substance on Earth for supporting life. The water cycle — driven by solar energy and gravity — has been recycling the same water molecules for over 4 billion years, connecting every ocean, river, cloud, and living thing on the planet.",
    "background_sections": [
        ("How the Water Cycle Works", "Solar energy heats surface water in oceans, lakes, and soil, causing evaporation. Water vapor rises into the atmosphere, cools, and condenses into clouds. When droplets become heavy enough, gravity pulls them back to Earth as precipitation. Water then flows through rivers, soaks into groundwater, or is absorbed by plants — eventually returning to the ocean."),
        ("Energy Drives the Cycle", "The Sun provides the energy needed to break hydrogen bonds between water molecules during evaporation. About 86% of global evaporation occurs from ocean surfaces. The energy stored in water vapor is released as latent heat when condensation occurs, driving weather patterns and storms."),
        ("Gravity's Role", "Gravity is essential for precipitation — it pulls water droplets out of clouds. It also drives surface runoff (rivers flowing downhill), groundwater movement, and ocean circulation. Without gravity, water would float off into space as vapor."),
        ("Water Reservoirs", "Earth's water is stored in reservoirs: oceans (97.2%), ice caps and glaciers (2.1%), groundwater (0.6%), freshwater lakes and rivers (0.01%), and atmosphere (0.001%). The cycle moves water between these reservoirs continuously. A water molecule spends an average of 3,200 years in the ocean before evaporating.")
    ],
    "lever_L": "Students identify solar energy, ground temperature, evaporation rate, and precipitation rate as key components of the water cycle system.",
    "lever_E": "Students determine that solar energy and temperature positively drive evaporation, which positively drives precipitation.",
    "lever_V": "Students build a model showing how energy input controls the speed and volume of water cycling.",
    "lever_Ev": "Students run heat wave, winter, and normal scenarios to observe how temperature changes affect cycle rates.",
    "lever_R": "Students add wind patterns or transpiration to explore more complex water cycle dynamics.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with dramatic water cycle landscape", "say": "The water you drank this morning? A dinosaur probably drank the same water 100 million years ago.", "do": "Let that sink in. Show a timeline of water's journey.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we're tracking water on a journey that's been happening for 4.5 billion years.", "do": "Have students read objectives. Pre-teach 'transpiration.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why doesn't Earth run out of water?", "say": "7.8 billion people use water every day. Agriculture uses trillions of gallons. Why don't we run out?", "do": "Poll: Where does your tap water come from? Trace it backward.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll model the engine that recycles every drop on Earth.", "do": "Preview LEVER steps.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for water cycle", "say": "What drives the water cycle? What can we control versus what responds?", "do": "Guide sorting. Discuss why the Sun is the external energy source.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows", "say": "More heat, more evaporation. More evaporation, more clouds. More clouds, more rain.", "do": "Help students trace the positive relationship chain.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and results", "say": "What happens to the water cycle during a heat wave versus winter?", "do": "Students predict first. Compare seasonal scenarios.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings", "say": "Why is the Sun the engine of the water cycle? What role does gravity play?", "do": "Discuss energy flow. Demonstrate condensation on a cold glass.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Water purification system", "say": "You're engineers in a disaster zone. Build a system to make dirty water clean.", "do": "Groups build solar stills using cups, plastic wrap, and sunlight.", "time": "12 min"}
    ],
    "sort_reasoning": "Solar Energy and Ground Temperature are external because they are environmental inputs to the water cycle that water itself cannot control. Evaporation Rate and Precipitation Rate are internal because they change as a direct result of how much energy and heat is available in the system.",
    "relationships": [
        ("Solar Energy to Evaporation Rate", "POSITIVE (+)", "More solar energy provides more heat to break hydrogen bonds in liquid water, increasing the rate of evaporation from oceans, lakes, and soil."),
        ("Ground Temperature to Evaporation Rate", "POSITIVE (+)", "Higher ground temperatures mean warmer surface water, which evaporates more quickly. Hot pavement after rain demonstrates this effect."),
        ("Evaporation Rate to Precipitation Rate", "POSITIVE (+)", "More evaporation puts more water vapor into the atmosphere, which eventually condenses and falls as increased precipitation.")
    ],
    "sim_answers": [
        ("Summer Heat Wave Scenario", "When Solar Energy and Ground Temperature are maximized, Evaporation Rate increases dramatically. This puts much more water vapor into the atmosphere, which leads to increased Precipitation Rate. The cycle accelerates — more water moves through the system faster."),
        ("Winter Freeze Scenario", "When Ground Temperature drops near freezing, Evaporation Rate slows significantly because less energy is available to break water molecule bonds. Precipitation Rate also decreases, and what precipitation does occur often falls as snow, which can store water in frozen form for months.")
    ],
    "reflection_exemplars": [
        ("Why is it called a cycle?", "Water continuously moves through the system in a loop: evaporation lifts it up, condensation forms clouds, precipitation brings it down, runoff carries it to the ocean, and the process starts again. No water is created or destroyed — it just changes form and location. It's been cycling for over 4 billion years."),
        ("How does deforestation affect the water cycle?", "Trees release water vapor through transpiration — a large tree can release over 100 gallons per day. Removing forests reduces this moisture source, which can decrease local rainfall. Deforested areas also have more surface runoff and erosion because tree roots no longer hold soil and slow water flow.")
    ],
    "stem_intro": "Present the disaster scenario: After a flood, clean water is contaminated. Your team must design a solar-powered purification system using evaporation and condensation principles from the water cycle.",
    "stem_concepts": [
        ("Solar Distillation", "Using solar energy to evaporate contaminated water and collecting the pure condensation — contaminants are left behind because they don't evaporate with the water."),
        ("Phase Changes", "Water changes state between solid, liquid, and gas. Contaminants typically stay behind during evaporation because they have different boiling points."),
        ("Water Quality", "Clean water is essential for human health. Contaminated water can contain bacteria, chemicals, and sediment that cause disease. Purification removes these contaminants.")
    ],
    "stem_eval": [
        ("Expert (4)", "System successfully demonstrates evaporation-condensation purification, collects measurable clean water, and student explains water cycle connection"),
        ("Proficient (3)", "System demonstrates the purification concept and student can explain how it connects to the water cycle"),
        ("Developing (2)", "System is built but doesn't effectively separate contaminants or collect clean water"),
        ("Beginning (1)", "System is incomplete or student can't explain the water cycle connection")
    ],
    "support": [
        "Provide a labeled water cycle diagram showing all phases and processes",
        "Use a sealed terrarium to visually demonstrate evaporation, condensation, and precipitation",
        "Sentence frames: 'When solar energy increases, evaporation __ because __, which causes precipitation to __'"
    ],
    "extensions": [
        "Research how much water plants release through transpiration and add it to the model",
        "Calculate how long a water molecule spends in different reservoirs (ocean vs. atmosphere vs. glacier)",
        "Investigate how urbanization (concrete and asphalt) affects local water cycling and groundwater recharge"
    ],
    "cross_curr": [
        ("Math", "Calculate the percentage of Earth's water in each reservoir and create a proportional chart"),
        ("ELA", "Write a creative story from the perspective of a water molecule traveling through the complete cycle"),
        ("Social Studies", "Research water scarcity around the world and how the water cycle creates inequity in water access")
    ],
    "misconceptions": [
        ("New water is constantly being created", "Earth has had roughly the same amount of water for 4 billion years. No new water is being created — it's being RECYCLED endlessly. The water cycle moves water between reservoirs but doesn't create or destroy it.", "Seal water in a jar and place in sunlight. The water evaporates and condenses on the glass, but the total amount never changes."),
        ("Clouds are made of water vapor", "Clouds are made of tiny LIQUID water droplets or ice crystals — not water vapor. Water vapor is invisible gas. When we see a cloud, the vapor has already CONDENSED into visible droplets.", "Breathe out on a cold day. The visible fog is condensed droplets, not the invisible vapor in your breath."),
        ("Rain comes from the ocean directly above", "Rain can fall thousands of miles from where the water originally evaporated. Wind carries water vapor across continents before it condenses and falls. Water that evaporated from the Pacific Ocean can fall as rain in Kansas.", "Show a weather map with storm tracks crossing the continent. Trace where the moisture originated.")
    ]
}

L06 = {
    "id": "G07-L06",
    "title": "Why Hot Cheetos Make You Cry",
    "subtitle": "How Your Body's Alarm System Detects and Responds to the World",
    "ngss": "MS-LS1-8",
    "ngss_desc": "Gather and synthesize information that sensory receptors respond to stimuli by sending messages to the brain for immediate behavior or storage as memories.",
    "big_question": "How does your body know the difference between hot, cold, sweet, and pain — and why do Hot Cheetos trick your brain into thinking your mouth is on fire?",
    "objectives": [
        "Explain how sensory receptors detect different types of stimuli",
        "Model the relationship between stimulus intensity and nervous system response",
        "Describe how signals travel from receptors to brain to muscles",
        "Analyze why capsaicin triggers pain receptors instead of taste receptors"
    ],
    "vocabulary": [
        ("Sensory Receptor", "A specialized cell or nerve ending that detects a specific type of stimulus like light, sound, pressure, or chemicals"),
        ("Stimulus", "Any change in the environment that triggers a response from the nervous system"),
        ("Neuron", "A nerve cell that carries electrical signals from receptors to the brain and from the brain to muscles"),
        ("Capsaicin", "The chemical compound in hot peppers that binds to heat/pain receptors, tricking the brain into sensing burning")
    ],
    "components": [
        ("Stimulus Intensity", "How strong the environmental signal is — dim vs. bright light, soft vs. loud sound, mild vs. extreme heat", True),
        ("Receptor Sensitivity", "How responsive the sensory receptors are — some people have more sensitive receptors than others", True),
        ("Nerve Signal Strength", "How strong the electrical signal is as it travels from receptors through neurons to the brain", False),
        ("Brain Response", "The intensity of the brain's reaction — from barely noticing to emergency fight-or-flight", False)
    ],
    "think_about_it": "When stimulus intensity is extremely high (like touching a hot stove), nerve signal strength maxes out. But what happens to brain response — and how fast does it need to happen?",
    "scenarios": [
        ("Mild Stimulus", "Set Stimulus Intensity to low and observe the system's gentle response"),
        ("Hot Cheetos Attack", "Lock Stimulus Intensity to maximum (capsaicin!) and observe the pain cascade"),
        ("Adaptation", "Start with high Stimulus Intensity, then gradually reduce — observe how the system adjusts")
    ],
    "sim_scenarios": [
        ("Mild Stimulus", "Low stimulus intensity, normal receptor sensitivity", "What do you predict Brain Response will be when the stimulus is barely noticeable?"),
        ("Hot Cheetos Attack", "Maximum stimulus intensity (capsaicin binding to pain receptors)", "What do you predict happens to Nerve Signal Strength and Brain Response when capsaicin activates pain receptors at full intensity?"),
        ("Sensory Adaptation", "Sustained stimulus over time", "What do you predict happens to Nerve Signal Strength when you experience the same stimulus for a long time?")
    ],
    "discoveries": [
        "Different sensory receptors are specialized for different stimuli — you have separate detectors for heat, cold, pressure, and chemicals",
        "Capsaicin doesn't actually burn you — it activates the SAME heat receptors that real fire would, tricking your brain",
        "Nerve signals travel at up to 120 meters per second — that's faster than a car on the highway",
        "Your brain processes millions of sensory inputs simultaneously and decides which ones deserve a response"
    ],
    "answer": "Hot Cheetos make you cry because capsaicin chemically binds to TRPV1 receptors — the same heat/pain receptors that detect actual burning. Your brain receives the signal and responds as if your mouth is literally on fire: tears, sweating, runny nose. It's a chemical trick on your nervous system!",
    "stem_title": "Design a Sensory Experiment",
    "stem_mission": "Design and conduct a controlled experiment testing how different variables affect sensory perception — then explain your results using your nervous system model.",
    "stem_scenario": "A neuroscience lab needs student researchers to investigate sensory perception. Your team will design an experiment, collect data, and present findings about how the nervous system processes sensory information.",
    "stem_questions": [
        "What sensory perception question will your experiment investigate?",
        "How will you control variables to ensure your results are valid?",
        "How do your experimental results connect to your nervous system model?"
    ],
    "stem_design_qs": [
        "What specific sensory question are you testing (taste, touch, temperature, sight)?",
        "What is your independent variable and how will you change it?",
        "What is your dependent variable and how will you measure it?",
        "How many trials will you run and why?"
    ],
    "career": "Neuroscientists study the nervous system to understand how we perceive the world, form memories, and respond to stimuli. They work in hospitals, research labs, and pharmaceutical companies, earning $70,000–$120,000/year.",
    "images": {
        "cover": ("cover-hot-cheetos.png", "A dramatic close-up of someone eating extremely spicy food with visible tears and a red face, alongside a microscopic view of nerve endings in the tongue, split image"),
        "landscape": ("landscape-senses.png", "7th grade students doing a blind taste test experiment in a science lab, blindfolded students tasting different foods while partners record data"),
        "modeling": ("modeling-nerves.png", "A diverse group of 7th grade students working on laptops building a digital nervous system model, classroom with brain and neuron diagrams on walls"),
        "discussion": ("discussion-senses.png", "A teacher showing a diagram of the nervous system pathway from receptor to brain while 7th grade students discuss, students pointing at the diagram"),
        "stem": ("stem-sensory-lab.png", "7th grade students conducting sensory experiments at lab stations — testing temperature, taste, and touch sensitivity, recording data in notebooks")
    },
    "pre_assessment": [
        "How does your body know when something is hot, cold, or painful?",
        "Why do you think spicy food makes some people cry?",
        "Draw what you think happens inside your body between touching a hot pan and pulling your hand away.",
        "Can your senses be tricked? Give an example."
    ],
    "extend_components": [
        ("Reflex Arc Speed", "Some signals bypass the brain entirely — reflexes go from receptor to spinal cord to muscle for faster response"),
        ("Sensory Adaptation", "Receptors decrease their firing rate when exposed to a constant stimulus over time"),
        ("Pain Threshold", "The minimum stimulus intensity required to trigger a pain response — varies between individuals")
    ],
    "reflections": [
        "Why does your hand pull away from a hot stove BEFORE you consciously feel the pain?",
        "If capsaicin doesn't actually damage your mouth, why does your brain respond as if it does?",
        "Why do you eventually stop noticing a strong smell after being around it for a while?",
        "How would life be different if you had no pain receptors?",
        "How does understanding sensory receptors help doctors treat conditions like chronic pain?"
    ],
    "dimensions": [
        ("Science Practice", "Obtaining, Evaluating, and Communicating Information", "Students gather and synthesize information about how sensory receptors detect stimuli and communicate with the brain."),
        ("Disciplinary Core Idea", "LS1.D Information Processing", "Each sense receptor responds to different inputs (light, sound, chemicals), transmitting them as signals that travel along nerve cells to the brain for processing."),
        ("Crosscutting Concept", "Cause and Effect", "Students identify that specific stimuli CAUSE specific receptor activations, which trigger predictable nervous system responses.")
    ],
    "cast_items": [
        "Explain how sensory receptors respond to different types of stimuli",
        "Describe how signals travel from receptors to the brain",
        "Analyze how the brain processes sensory information for behavior or memory"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A person eats a Hot Cheeto and immediately starts sweating and tearing up. This response occurs because capsaicin in the chip:"),
        ("Constructed Response:", "Describe the pathway a signal takes from the moment you touch something hot to the moment you pull your hand away. Explain the role of sensory receptors, neurons, and the brain in this process.")
    ],
    "background_intro": "Your nervous system is the most sophisticated information processing system ever evolved. It detects millions of stimuli per second, transmits signals at highway speeds, and coordinates responses that keep you alive — all without you having to think about it.",
    "background_sections": [
        ("Sensory Receptors", "The human body contains dozens of receptor types: photoreceptors (light), mechanoreceptors (pressure/vibration), thermoreceptors (temperature), chemoreceptors (taste/smell), and nociceptors (pain). Each type responds to a specific stimulus and converts it into electrical nerve signals."),
        ("The Capsaicin Trick", "Capsaicin, the compound that makes peppers hot, binds to TRPV1 receptors — the same receptors that detect temperatures above 43°C (109°F). When capsaicin activates these receptors, the brain receives a signal indistinguishable from actual burning. The response is real (tears, sweating, pain) even though no tissue damage occurs."),
        ("Signal Transmission", "Nerve signals are electrical impulses that travel along neurons at speeds of 1-120 m/s depending on the nerve type. The signal passes from neuron to neuron across tiny gaps called synapses using chemical neurotransmitters. From stubbed toe to brain awareness takes about 0.1 seconds."),
        ("Brain Processing", "The brain receives sensory input and decides the response: ignore it (background noise), store it (memories), or act on it (pull hand away). The somatosensory cortex maps which body part sent the signal. Pain signals get priority processing — your brain is wired to respond to danger first.")
    ],
    "lever_L": "Students identify stimulus intensity, receptor sensitivity, nerve signal strength, and brain response as components of the sensory system.",
    "lever_E": "Students determine that stimulus intensity and receptor sensitivity both positively affect nerve signal strength, which positively affects brain response.",
    "lever_V": "Students build a model showing how environmental stimuli are converted to nerve signals and brain responses.",
    "lever_Ev": "Students run mild, capsaicin, and adaptation scenarios to observe how the system responds to different inputs.",
    "lever_R": "Students add reflex arc speed or sensory adaptation to explore more complex nervous system behaviors.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with spicy food reaction", "say": "Why do Hot Cheetos make you cry, sweat, and feel like your mouth is literally on fire?", "do": "Show a video of someone trying extremely spicy food. The reaction is real — but the 'fire' isn't.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we're investigating how your body's alarm system works — and how it can be tricked.", "do": "Have students read objectives. Pre-teach 'stimulus' and 'receptor.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "How does your body detect the world?", "say": "Right now your body is detecting thousands of things — temperature, light, sound, pressure. How?", "do": "Quick activity: close eyes. What can you still detect? Touch, sound, temperature.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll model the path from stimulus to response.", "do": "Preview LEVER steps.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for nervous system", "say": "What starts a nerve signal? What controls how strongly you react?", "do": "Guide sorting. Discuss why stimulus and receptor sensitivity are inputs.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows", "say": "Stronger stimulus, stronger signal, bigger response. But is it always that simple?", "do": "Help students build the signal pathway chain.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and results", "say": "Let's simulate what happens when capsaicin hits your tongue at full force!", "do": "Students predict first. Compare mild vs. capsaicin scenarios.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings", "say": "So capsaicin doesn't actually burn you — it TRICKS your pain receptors. What else does this?", "do": "Discuss sensory tricks. Mention menthol (cold receptor trick).", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Sensory experiment design", "say": "You're neuroscientists now. Design an experiment to test sensory perception.", "do": "Groups design and conduct sensory experiments.", "time": "12 min"}
    ],
    "sort_reasoning": "Stimulus Intensity and Receptor Sensitivity are external because they are inputs to the nervous system — the environment provides the stimulus and receptor sensitivity is a pre-existing trait. Nerve Signal Strength and Brain Response are internal because they change as a result of those inputs being processed by the nervous system.",
    "relationships": [
        ("Stimulus Intensity to Nerve Signal Strength", "POSITIVE (+)", "A stronger stimulus activates more receptors and triggers higher-frequency nerve impulses, creating a stronger signal."),
        ("Receptor Sensitivity to Nerve Signal Strength", "POSITIVE (+)", "More sensitive receptors fire at lower thresholds and generate stronger signals for the same stimulus level."),
        ("Nerve Signal Strength to Brain Response", "POSITIVE (+)", "Stronger nerve signals cause more intense brain responses — from barely noticing to full fight-or-flight reactions like crying and sweating.")
    ],
    "sim_answers": [
        ("Hot Cheetos Scenario", "When Stimulus Intensity is maxed (capsaicin binding to TRPV1 pain receptors), Nerve Signal Strength shoots to maximum. Brain Response is intense — the brain triggers tears, sweating, mucus production, and pain sensation. The response is identical to actual burning because the same receptors are activated."),
        ("Sensory Adaptation Scenario", "When a sustained stimulus continues over time, Nerve Signal Strength gradually decreases as receptors adapt and reduce their firing rate. Brain Response diminishes. This is why you stop noticing a strong perfume after a few minutes — your receptors have adapted.")
    ],
    "reflection_exemplars": [
        ("Why does your hand pull away before you feel pain?", "Reflexes bypass the brain entirely. The pain signal goes from receptors to the spinal cord, which immediately sends a motor signal back to your arm muscles to pull away. The signal reaches your brain AFTER your hand has already moved. This reflex arc takes about 0.05 seconds — your conscious awareness of pain comes later."),
        ("Why does capsaicin trigger pain but not damage?", "Capsaicin binds to TRPV1 receptors, which normally detect temperatures above 43°C. The receptor can't tell the difference between real heat and capsaicin — it sends the same signal either way. Your brain responds to the signal, not the actual stimulus. No cells are damaged, but the pain response is genuine.")
    ],
    "stem_intro": "Your team is a neuroscience research group. Design a controlled experiment testing a question about sensory perception — then present your findings to the class as a scientific poster.",
    "stem_concepts": [
        ("Receptor Specificity", "Different receptors respond to different stimuli. TRPV1 detects heat and capsaicin. TRPM8 detects cold and menthol. Taste receptors detect sweet, salty, sour, bitter, and umami."),
        ("Signal Transduction", "The process of converting an environmental stimulus (heat, light, chemicals) into an electrical nerve signal that the brain can interpret."),
        ("Sensory Adaptation", "When exposed to a constant stimulus, receptors gradually decrease their firing rate. This is why you stop noticing background noise or constant odors after a while.")
    ],
    "stem_eval": [
        ("Expert (4)", "Experiment has clear hypothesis, controlled variables, multiple trials, data collection, and connects results to the nervous system model"),
        ("Proficient (3)", "Experiment has a hypothesis and controlled variables, with data that connects to sensory concepts"),
        ("Developing (2)", "Experiment tests a sensory question but lacks controlled variables or clear data collection"),
        ("Beginning (1)", "Experiment is incomplete or doesn't connect to nervous system concepts")
    ],
    "support": [
        "Provide a diagram of the sensory pathway: stimulus → receptor → nerve → brain → response",
        "Use a reaction time test (ruler drop) to physically demonstrate nerve signal speed",
        "Sentence frames: 'When stimulus intensity increases, nerve signal strength __ because __'"
    ],
    "extensions": [
        "Research phantom limb pain and explain how the brain can perceive sensations from missing body parts",
        "Test reaction times under different conditions and calculate nerve signal speed",
        "Investigate how anesthetics block nerve signals and prevent pain perception"
    ],
    "cross_curr": [
        ("Math", "Calculate nerve signal speed by measuring reaction time and estimating the distance signals travel"),
        ("ELA", "Write a narrative describing the journey of a nerve signal from tongue (Hot Cheeto) to brain to tears"),
        ("Health", "Research how understanding pain receptors helps develop better pain medications for patients")
    ],
    "misconceptions": [
        ("Spicy food burns your mouth", "Capsaicin doesn't cause any tissue damage or burning. It binds to heat receptors (TRPV1) and tricks your brain into THINKING you're being burned. The pain is real, but the injury is not.", "Ask: If spicy food actually burned you, would your mouth heal overnight? The fact that it does proves no damage occurred."),
        ("We only have five senses", "Humans have far more than five senses. Beyond sight, hearing, taste, smell, and touch, we have proprioception (body position), vestibular sense (balance), thermoception (temperature), nociception (pain), and more.", "Close your eyes and touch your nose. How did you know where it was? That's proprioception — your sixth sense."),
        ("Pain is always bad", "Pain is actually a critical survival system. It alerts your brain to danger and triggers protective responses. People born without pain receptors (a real condition) suffer constant injuries because they can't detect damage.", "Ask: Would you want to NOT feel pain? What would happen if you left your hand on a hot stove and didn't know?")
    ]
}

L07 = {
    "id": "G07-L07",
    "title": "Why You Can't Slide Forever",
    "subtitle": "The Hidden Energy Transfers That Stop Everything",
    "ngss": "MS-PS3-5",
    "ngss_desc": "Construct, use, and present arguments to support the claim that when the kinetic energy of an object changes, energy is transferred to or from the object.",
    "big_question": "Why does every moving thing eventually stop — and where does the energy go?",
    "objectives": [
        "Explain the relationship between speed, mass, and kinetic energy",
        "Model how friction transfers kinetic energy into thermal energy",
        "Predict how surface type affects the rate of energy transfer",
        "Construct arguments about energy conservation using model evidence"
    ],
    "vocabulary": [
        ("Kinetic Energy", "The energy an object has because of its motion — faster and heavier objects have more"),
        ("Friction", "A force between surfaces that opposes motion and converts kinetic energy into heat"),
        ("Energy Transfer", "The movement of energy from one object or system to another, or from one form to another"),
        ("Thermal Energy", "Heat energy — the total kinetic energy of all particles in a substance")
    ],
    "components": [
        ("Initial Speed", "How fast the object is moving at the start — determines the starting kinetic energy", True),
        ("Surface Friction", "How rough or smooth the surface is — rougher surfaces create more friction force", True),
        ("Kinetic Energy", "The energy of motion — decreases as friction slows the object down", False),
        ("Thermal Energy Output", "The heat generated by friction — energy doesn't disappear, it transforms", False)
    ],
    "think_about_it": "When surface friction is very high, kinetic energy drops fast. But the total energy in the system hasn't changed — so where did it go?",
    "scenarios": [
        ("Ice Surface", "Set Surface Friction to very low (smooth ice) and observe how long kinetic energy lasts"),
        ("Concrete Surface", "Set Surface Friction to high and observe rapid energy transfer"),
        ("Carpet Surface", "Lock Surface Friction to maximum and observe the fastest energy conversion")
    ],
    "sim_scenarios": [
        ("Ice (Low Friction)", "Very low surface friction, moderate initial speed", "What do you predict happens to Kinetic Energy on a nearly frictionless surface?"),
        ("Concrete (High Friction)", "High surface friction, same initial speed", "What do you predict happens to Thermal Energy Output when friction is high?"),
        ("Speed Comparison", "Same surface, but double the initial speed", "How does doubling the speed affect Kinetic Energy and the time it takes to stop?")
    ],
    "discoveries": [
        "Energy is never created or destroyed — it only changes form (conservation of energy)",
        "Friction converts kinetic energy into thermal energy — that's why your hands get warm when you rub them",
        "Smoother surfaces mean less friction and slower energy conversion — objects slide farther",
        "Kinetic energy depends on speed SQUARED — doubling speed quadruples the energy"
    ],
    "answer": "Nothing ever slides forever because friction converts kinetic energy (motion) into thermal energy (heat). The energy doesn't disappear — it transforms. Rub your hands together and feel the heat — that's kinetic energy becoming thermal energy right in your palms! Energy is always conserved.",
    "stem_title": "Design the Longest Slide",
    "stem_mission": "Engineer a slide or ramp system that keeps an object moving the longest distance possible by minimizing energy lost to friction.",
    "stem_scenario": "A toy company wants to design the world's longest toy car track. Your engineering team must maximize the distance a toy car travels by understanding and minimizing energy losses.",
    "stem_questions": [
        "What surface materials minimize friction and maximize distance?",
        "How does the starting height (potential energy) affect how far the car travels?",
        "What is the relationship between the energy lost to friction and the distance traveled?"
    ],
    "stem_design_qs": [
        "What surface material will you use for your track and why?",
        "What starting height will give your car the most kinetic energy?",
        "How will you measure the distance traveled and energy lost?",
        "What modifications can you make to reduce friction even further?"
    ],
    "career": "Mechanical Engineers design systems that manage energy transfer — from car brakes to roller coasters to industrial machinery. They earn $75,000–$125,000/year.",
    "images": {
        "cover": ("cover-sliding.png", "A dramatic action shot of a skateboarder sliding on a rail with visible sparks from friction, motion blur showing speed, urban setting at golden hour"),
        "landscape": ("landscape-friction.png", "7th grade students testing toy cars on different surfaces — tile, carpet, sandpaper — measuring distances with tape measures, hands-on science lab"),
        "modeling": ("modeling-energy.png", "A diverse group of 7th grade students working on laptops building a digital energy transfer model, classroom with physics posters about energy"),
        "discussion": ("discussion-energy.png", "A teacher demonstrating friction by rubbing hands together while students feel their own hands warming up, engaged classroom discussion"),
        "stem": ("stem-longest-slide.png", "7th grade students building ramp-and-track systems from cardboard and various surface materials, testing toy cars for maximum distance")
    },
    "pre_assessment": [
        "Why does a ball eventually stop rolling across the floor?",
        "Where does the energy go when a moving object stops?",
        "Why do your hands get warm when you rub them together?",
        "Would an object ever stop moving in outer space? Why or why not?"
    ],
    "extend_components": [
        ("Air Resistance", "The friction force between a moving object and the air, which increases with speed"),
        ("Mass", "Heavier objects have more kinetic energy at the same speed and take more force to stop"),
        ("Surface Area", "More contact area between surfaces can increase the total friction force")
    ],
    "reflections": [
        "If energy can't be created or destroyed, where does ALL the energy from a moving car go when it brakes?",
        "Why do space probes keep moving for decades without engines — doesn't that violate your model?",
        "How is the friction that stops a skateboard the same concept as the friction that starts a campfire?",
        "Why does doubling your speed quadruple your kinetic energy instead of just doubling it?",
        "How does understanding energy transfer help engineers design better brakes?"
    ],
    "dimensions": [
        ("Science Practice", "Engaging in Argument from Evidence", "Students construct and present arguments using model evidence that energy is transferred when kinetic energy changes."),
        ("Disciplinary Core Idea", "PS3.B Conservation of Energy and Energy Transfer", "When the motion energy of an object changes, there is inevitably some other change in energy at the same time — energy is conserved."),
        ("Crosscutting Concept", "Energy and Matter", "Students track energy as it transfers from kinetic to thermal form, demonstrating that energy is conserved even as it changes form.")
    ],
    "cast_items": [
        "Construct arguments that energy is transferred when kinetic energy changes",
        "Use evidence to explain that energy is conserved during transformations",
        "Predict how changing variables affects energy transfer rates"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A toy car rolls down a ramp and across a rough carpet, gradually slowing to a stop. Which statement best explains where the car's kinetic energy went?"),
        ("Constructed Response:", "A student claims that when a ball stops rolling, the energy has been 'used up' and no longer exists. Using evidence from your model, construct an argument explaining what actually happens to the energy.")
    ],
    "background_intro": "Energy is one of the most fundamental concepts in all of science. The law of conservation of energy states that energy cannot be created or destroyed — only transferred or transformed. Understanding energy transfer is key to everything from designing brakes to building power plants.",
    "background_sections": [
        ("Kinetic Energy", "Kinetic energy is the energy of motion, calculated as KE = ½mv². This means kinetic energy depends on both mass and speed — but speed has a SQUARED effect. Doubling the mass doubles the energy, but doubling the speed QUADRUPLES it. This is why high-speed crashes are so much more destructive."),
        ("Friction and Heat", "Friction is a force that opposes motion between surfaces in contact. It converts kinetic energy into thermal energy (heat) through microscopic interactions between surface irregularities. This is why brakes get hot, why rubbing your hands warms them, and why meteors burn up entering the atmosphere."),
        ("Conservation of Energy", "The total energy in a closed system remains constant. When a sliding object stops, its kinetic energy hasn't disappeared — it has been transformed into thermal energy (heat in the surfaces and surrounding air). If you could measure all the heat produced, it would exactly equal the kinetic energy lost."),
        ("Real-World Applications", "Engineers use energy transfer principles everywhere: car brakes convert kinetic to thermal energy (disc brakes can reach 300°C), regenerative braking in electric cars converts kinetic back to electrical energy, and heat shields on spacecraft manage the enormous thermal energy from atmospheric friction.")
    ],
    "lever_L": "Students identify initial speed, surface friction, kinetic energy, and thermal energy output as components of the energy transfer system.",
    "lever_E": "Students determine that friction negatively affects kinetic energy but positively transfers it to thermal energy — energy is conserved through transformation.",
    "lever_V": "Students build a model showing how kinetic energy is converted to thermal energy through friction.",
    "lever_Ev": "Students run ice, concrete, and carpet scenarios to compare energy transfer rates on different surfaces.",
    "lever_R": "Students add air resistance or mass to explore more complex energy transfer dynamics.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with skateboard/sliding action", "say": "You push a ball. It rolls. Then it stops. WHERE DID THE ENERGY GO?", "do": "Roll a ball across the floor. When it stops, ask: The energy didn't vanish. Where is it?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we're solving one of physics' most important puzzles — what happens to energy.", "do": "Have students read objectives. Pre-teach 'kinetic energy' and 'friction.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why does everything stop?", "say": "In space, things move forever. On Earth, everything stops. Why the difference?", "do": "Discussion: What's different about space vs. Earth? (No friction in space.)", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll model where energy goes when motion stops.", "do": "Preview LEVER steps.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for energy model", "say": "What starts with energy? What takes energy away? Where does it end up?", "do": "Guide sorting. Discuss why speed and surface are inputs.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows", "say": "Friction TAKES kinetic energy. But it doesn't destroy it — it TRANSFORMS it.", "do": "Have students rub hands to feel KE→thermal. Build relationships.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and results", "say": "Let's test: ice vs. concrete vs. carpet. Which steals energy fastest?", "do": "Students predict first. Compare surface scenarios.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings", "say": "Energy is NEVER destroyed. So where is it right now?", "do": "Touch the floor where the ball stopped. Is it slightly warmer?", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Longest slide design", "say": "Engineer a track that keeps a toy car moving as far as possible!", "do": "Groups design tracks testing different surfaces for minimum friction.", "time": "12 min"}
    ],
    "sort_reasoning": "Initial Speed and Surface Friction are external because they are inputs that determine the starting conditions and the rate of energy transfer. Kinetic Energy and Thermal Energy Output are internal because they change as a result of the interaction between the moving object and the surface.",
    "relationships": [
        ("Initial Speed to Kinetic Energy", "POSITIVE (+)", "Faster initial speed means more kinetic energy. Speed has a squared relationship with KE — doubling speed quadruples kinetic energy."),
        ("Surface Friction to Kinetic Energy", "NEGATIVE (-)", "More friction means kinetic energy is lost faster. Rough surfaces oppose motion more strongly, slowing objects down quickly."),
        ("Surface Friction to Thermal Energy Output", "POSITIVE (+)", "More friction converts more kinetic energy into heat. The energy isn't lost — it's transformed into thermal energy in the surfaces.")
    ],
    "sim_answers": [
        ("Ice vs. Concrete Scenario", "On ice (low friction), Kinetic Energy decreases very slowly and the object slides a long distance. On concrete (high friction), Kinetic Energy drops rapidly. In both cases, Thermal Energy Output accounts for the lost kinetic energy — confirming energy conservation."),
        ("Speed Comparison Scenario", "When Initial Speed is doubled, Kinetic Energy quadruples (KE = ½mv²). The object takes much longer to stop because there's four times as much energy to convert to heat. This is why stopping distance increases dramatically at higher speeds — and why speed limits save lives.")
    ],
    "reflection_exemplars": [
        ("Where does all the energy go when a car brakes?", "When a car brakes, the brake pads press against the rotors, creating friction. The car's kinetic energy is converted into thermal energy — the brakes can reach 300°C or more. Some energy also goes into sound (squealing) and deforming the brake pad material. The total energy is conserved."),
        ("Why do space probes move forever?", "In space, there's essentially no friction — no air, no surface contact. Without friction, there's nothing to convert kinetic energy into another form. So objects in space keep their kinetic energy and continue moving at the same speed indefinitely. This is Newton's First Law in action.")
    ],
    "stem_intro": "A toy company needs the longest possible track for a new toy car product. Your engineering team must minimize energy lost to friction by choosing the best surface materials and track design.",
    "stem_concepts": [
        ("Coefficient of Friction", "A number representing how much friction a surface produces. Ice has a low coefficient (~0.03), rubber on concrete is high (~0.8). Lower coefficient means less energy lost."),
        ("Energy Conservation", "The total energy before and after must be equal. If a car starts with 10 joules of kinetic energy and ends with 0, then 10 joules of thermal energy must have been produced."),
        ("Regenerative Braking", "Electric cars can convert kinetic energy BACK into electrical energy instead of wasting it as heat. This is why electric cars are more energy-efficient than gas cars.")
    ],
    "stem_eval": [
        ("Expert (4)", "Track design tests multiple surfaces, records distance data, calculates energy transfer, and explains physics principles"),
        ("Proficient (3)", "Track design tests at least two surfaces with measured distances and connects to energy concepts"),
        ("Developing (2)", "Track is built but testing is unsystematic or energy concepts aren't clearly connected"),
        ("Beginning (1)", "Track is incomplete or student can't explain the energy transfer principles")
    ],
    "support": [
        "Provide toy cars and three pre-cut surface strips (smooth, medium, rough) for direct comparison",
        "Use a thermometer to measure temperature change on surfaces after friction experiments",
        "Sentence frames: 'When friction increases, kinetic energy __ and thermal energy __ because __'"
    ],
    "extensions": [
        "Calculate KE = ½mv² for different speeds and graph the quadratic relationship",
        "Research regenerative braking in electric vehicles and explain how it reverses energy transfer",
        "Investigate how lubricants reduce friction and calculate the energy savings"
    ],
    "cross_curr": [
        ("Math", "Calculate kinetic energy at different speeds using KE = ½mv² and graph the results"),
        ("ELA", "Write an argument essay: 'Energy can never be destroyed — only transformed.' Use model evidence."),
        ("Social Studies", "Research how understanding friction and energy transfer led to the Industrial Revolution")
    ],
    "misconceptions": [
        ("Energy disappears when objects stop", "Energy is NEVER created or destroyed — this is the law of conservation of energy. When a ball stops rolling, its kinetic energy has been converted to thermal energy (heat) in the surface and surrounding air.", "Rub your hands vigorously. The motion stops, but you feel HEAT. That's the energy — it transformed."),
        ("Friction only slows things down", "Friction also enables motion! Without friction, you couldn't walk (feet would slip), cars couldn't drive (tires wouldn't grip), and you couldn't hold anything. Friction is essential for controlled movement.", "Try to walk on ice. Friction is what you MISS when it's gone."),
        ("Heavier objects always stop faster", "Heavier objects have MORE kinetic energy at the same speed (KE = ½mv²), so they actually require MORE friction force to stop. This is why loaded trucks need longer stopping distances than empty ones.", "Push a heavy book and a light book at the same speed. The heavy one slides farther because it has more KE to convert.")
    ]
}

L08 = {
    "id": "G07-L08",
    "title": "The Crime Scene in Every Rock",
    "subtitle": "Reading Earth's History One Layer at a Time",
    "ngss": "MS-ESS1-4",
    "ngss_desc": "Construct a scientific explanation based on evidence from rock strata for how the geologic time scale is used to organize Earth's 4.6-billion-year-old history.",
    "big_question": "How can a single rock tell you what happened on Earth millions of years ago?",
    "objectives": [
        "Explain how rock strata form layers that represent different time periods",
        "Model the relationship between sedimentation, erosion, and fossil preservation",
        "Use the principle of superposition to determine relative age of rock layers",
        "Reconstruct past environments using evidence found in rock layers"
    ],
    "vocabulary": [
        ("Stratigraphy", "The study of rock layers (strata) and their arrangement to understand Earth's history"),
        ("Sedimentary Rock", "Rock formed from compressed layers of sediment — sand, mud, shells — that accumulate over time"),
        ("Superposition", "The principle that in undisturbed rock layers, the oldest layers are on the bottom and youngest on top"),
        ("Index Fossil", "A fossil from an organism that lived for a short time but across a wide area, used to date rock layers")
    ],
    "components": [
        ("Sedimentation Rate", "How quickly new layers of sediment are deposited by water, wind, or volcanic activity", True),
        ("Erosion Rate", "How quickly existing rock layers are worn away by water, wind, ice, or chemical processes", True),
        ("Rock Layer Thickness", "How thick the accumulated rock strata become over geological time", False),
        ("Fossil Preservation Quality", "How well organisms are preserved in the rock — depends on burial speed and conditions", False)
    ],
    "think_about_it": "When sedimentation rate is very high (like during a flood or volcanic eruption), what happens to fossil preservation quality compared to normal, slow deposition?",
    "scenarios": [
        ("Rapid Deposition", "Lock Sedimentation Rate to maximum (flood or volcanic ash) and observe layer thickness and preservation"),
        ("Heavy Erosion", "Set Erosion Rate to maximum and observe what happens to the rock record"),
        ("Normal Conditions", "Set moderate rates for both and observe balanced geological processes")
    ],
    "sim_scenarios": [
        ("Rapid Deposition", "Sedimentation Rate at maximum (flood event)", "What do you predict happens to Fossil Preservation Quality when organisms are buried quickly?"),
        ("Heavy Erosion", "Erosion Rate at maximum, normal sedimentation", "What do you predict happens to Rock Layer Thickness and fossil evidence when erosion dominates?"),
        ("Balanced System", "Moderate sedimentation and erosion", "How do you predict the rock record forms under normal conditions over millions of years?")
    ],
    "discoveries": [
        "Rock layers are like pages in a book — each one records conditions at the time it formed",
        "Rapid burial preserves fossils best because organisms are protected from decomposition and scavengers",
        "Erosion creates gaps in the rock record — millions of years of history can be missing from a single location",
        "The principle of superposition allows us to determine which layers (and fossils) are older or younger"
    ],
    "answer": "Rocks are history books written in stone. Each layer records the environment when it formed — ocean sediments contain marine fossils, desert layers contain sand dunes, volcanic layers contain ash. By reading layers from bottom to top (superposition), we can reconstruct millions of years of Earth's story!",
    "stem_title": "Create a Rock Core Sample Model",
    "stem_mission": "Build a physical model of a rock core sample showing at least 5 distinct geological periods, each with appropriate fossils and environmental evidence.",
    "stem_scenario": "A museum of natural history needs an educational core sample exhibit showing how geologists read Earth's history from rock layers. Your team will build the model and write the interpretive guide.",
    "stem_questions": [
        "What evidence in each layer tells you about the environment at that time?",
        "How do you show the principle of superposition in your core sample?",
        "What would a gap (unconformity) in your layers represent?"
    ],
    "stem_design_qs": [
        "How many geological periods will your core sample represent?",
        "What materials will represent different types of sediment and rock?",
        "What fossils or evidence will you include in each layer?",
        "How will you show at least one erosion gap (unconformity) in your record?"
    ],
    "career": "Geologists and Stratigraphers study rock formations to understand Earth's history, locate natural resources, and assess geological hazards. They earn $65,000–$115,000/year.",
    "images": {
        "cover": ("cover-rock-layers.png", "A dramatic photograph of exposed rock strata showing distinct colorful layers in a canyon wall — reds, oranges, tans, and grays — with visible fossils, geological formation"),
        "landscape": ("landscape-geology.png", "7th grade students on a field trip examining rock layers in a road cut or cliff face, pointing at different strata, wearing safety helmets"),
        "modeling": ("modeling-rocks.png", "A diverse group of 7th grade students working on laptops building a digital stratigraphy model, classroom with rock samples and geological maps"),
        "discussion": ("discussion-rocks.png", "A teacher holding rock samples and fossils while leading a discussion with 7th grade students, pointing at a geological column diagram on the board"),
        "stem": ("stem-core-sample.png", "7th grade students building layered core sample models using sand, clay, and small objects as fossils in clear containers, colorful layers visible")
    },
    "pre_assessment": [
        "What can you learn by looking at layers of rock in a cliff or canyon?",
        "Why do you think fossils are found inside certain types of rocks?",
        "If you found a fish fossil in a rock on top of a mountain, what would that tell you?",
        "Draw what you think rock layers look like underground."
    ],
    "extend_components": [
        ("Tectonic Activity", "Earthquakes, folding, and faulting can tilt, bend, or break rock layers after they form"),
        ("Sea Level Change", "Rising and falling oceans change what type of sediment is deposited in an area"),
        ("Volcanic Eruptions", "Volcanic ash creates distinct marker layers that can be dated and traced across continents")
    ],
    "reflections": [
        "Why is the fossil record incomplete — why don't we have fossils of every organism that ever lived?",
        "How does finding marine fossils on mountaintops prove that Earth's surface has changed dramatically?",
        "What's the difference between relative age (superposition) and absolute age (radiometric dating)?",
        "Why are sedimentary rocks the best type for finding fossils?",
        "How does erosion act like a thief, stealing pages from Earth's history book?"
    ],
    "dimensions": [
        ("Science Practice", "Constructing Explanations", "Students construct scientific explanations using evidence from rock strata to explain how geologists organize Earth's history."),
        ("Disciplinary Core Idea", "ESS1.C The History of Planet Earth", "Rock strata and the fossil record can be used as evidence to organize the relative occurrence of major historical events in Earth's history."),
        ("Crosscutting Concept", "Scale, Proportion, and Quantity", "Students work with vast timescales (millions to billions of years) and understand how thin layers of rock can represent enormous spans of geological time.")
    ],
    "cast_items": [
        "Use evidence from rock strata to organize events in Earth's history",
        "Apply the principle of superposition to determine relative age of rock layers",
        "Construct explanations for how geological processes create the rock record"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A geologist finds a rock layer containing marine fossils between two layers containing land plant fossils. Which interpretation is best supported by this evidence?"),
        ("Constructed Response:", "Examine a diagram of rock strata with different fossils in each layer. Using the principle of superposition and your knowledge of the fossil record, construct an explanation of the geological history this sequence represents.")
    ],
    "background_intro": "Earth is 4.6 billion years old, and its history is written in stone — literally. Rock strata (layers) form a record of environmental conditions, life forms, and geological events that have shaped our planet over deep time.",
    "background_sections": [
        ("How Rock Layers Form", "Sedimentary rock forms when particles (sand, mud, shells, organic material) settle and accumulate in layers. Over millions of years, pressure from overlying layers compresses and cements these sediments into solid rock. Each layer represents a specific time period and environment."),
        ("Principle of Superposition", "In undisturbed rock sequences, the oldest layers are at the bottom and the youngest are at the top. This principle, established by Nicolas Steno in 1669, allows geologists to determine the RELATIVE age of rock layers and the fossils they contain without needing absolute dates."),
        ("Fossils as Evidence", "Fossils are the preserved remains or traces of ancient organisms. They form when organisms are rapidly buried in sediment before decomposition. Index fossils — from organisms that lived for a short time but across a wide geographic area — are especially useful for dating and correlating rock layers across distant locations."),
        ("Gaps in the Record", "Unconformities are gaps in the rock record where erosion has removed layers or deposition didn't occur. These represent missing time — potentially millions of years of history erased. Geologists identify three types: angular unconformities, disconformities, and nonconformities.")
    ],
    "lever_L": "Students identify sedimentation rate, erosion rate, rock layer thickness, and fossil preservation quality as components of the geological record system.",
    "lever_E": "Students determine that sedimentation builds layers while erosion destroys them, and that rapid burial improves fossil preservation.",
    "lever_V": "Students build a model showing how sedimentation and erosion interact to create (or destroy) the rock record.",
    "lever_Ev": "Students run rapid deposition, heavy erosion, and balanced scenarios to observe different geological outcomes.",
    "lever_R": "Students add tectonic activity or sea level change to explore how geological forces alter the record after formation.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with dramatic rock layer canyon", "say": "Every rock layer is a page in Earth's history book. Let's learn to read it.", "do": "Show photos of Grand Canyon layers. Each color = different time period.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today you're becoming geological detectives — reading clues written in stone.", "do": "Have students read objectives. Pre-teach 'stratigraphy' and 'superposition.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "How does a rock tell you its story?", "say": "If I hand you a rock with a fish fossil in it, what can you figure out?", "do": "Pass around fossil samples. Students guess: marine, freshwater, or land?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll model how the rock record is created — and sometimes destroyed.", "do": "Preview LEVER steps.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for rock strata model", "say": "What builds layers? What destroys them? What determines fossil quality?", "do": "Guide sorting. Discuss why sedimentation and erosion are external processes.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows", "say": "Sedimentation builds the record. Erosion erases it. What wins?", "do": "Help students see the competing processes.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and results", "say": "What happens when a massive flood buries everything vs. when erosion dominates?", "do": "Students predict first. Compare scenarios.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings", "say": "Why is the fossil record incomplete? What creates gaps in Earth's story?", "do": "Discuss unconformities. Show real examples of missing time.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Core sample model", "say": "Build Earth's history in a jar — each layer tells a different story.", "do": "Groups build layered core samples with different materials and 'fossils.'", "time": "12 min"}
    ],
    "sort_reasoning": "Sedimentation Rate and Erosion Rate are external because they are geological processes driven by environmental forces — water, wind, volcanism, and gravity — that the rock itself cannot control. Rock Layer Thickness and Fossil Preservation Quality are internal because they are outcomes that change based on the balance between sedimentation and erosion.",
    "relationships": [
        ("Sedimentation Rate to Rock Layer Thickness", "POSITIVE (+)", "Faster sedimentation means more material is deposited, creating thicker rock layers over time."),
        ("Erosion Rate to Rock Layer Thickness", "NEGATIVE (-)", "Higher erosion rates wear away existing layers, reducing thickness and creating gaps (unconformities) in the rock record."),
        ("Rock Layer Thickness to Fossil Preservation Quality", "POSITIVE (+)", "Thicker, more rapidly deposited layers bury organisms quickly, protecting them from decomposition and creating better-preserved fossils.")
    ],
    "sim_answers": [
        ("Rapid Deposition Scenario", "When Sedimentation Rate is maximized (simulating a flood or volcanic ash fall), Rock Layer Thickness increases rapidly. Fossil Preservation Quality is excellent because organisms are buried quickly before they can decompose. This is why many of the best fossil sites are locations of ancient floods or volcanic events."),
        ("Heavy Erosion Scenario", "When Erosion Rate dominates, Rock Layer Thickness decreases as layers are worn away. Fossil Preservation Quality drops because exposed fossils are destroyed by weathering. Heavy erosion creates unconformities — gaps where millions of years of history are simply MISSING from the record.")
    ],
    "reflection_exemplars": [
        ("Why is the fossil record incomplete?", "Three main reasons: (1) Most organisms decompose before fossilization — you need rapid burial in the right conditions. (2) Erosion destroys existing fossils and rock layers. (3) Tectonic activity can metamorphose or melt fossil-bearing rocks. Scientists estimate we've found less than 1% of all species that have ever lived."),
        ("How do marine fossils end up on mountaintops?", "Millions of years ago, those rocks formed at the bottom of an ancient ocean. Marine organisms died and were buried in ocean sediment. Over millions of years, tectonic forces uplifted those ocean-floor rocks thousands of feet into the air, creating mountains. The fossils traveled with the rock from ocean floor to mountaintop.")
    ],
    "stem_intro": "A natural history museum needs a core sample exhibit showing Earth's history. Your team will build a physical model with at least 5 distinct layers, each containing evidence of the environment at that time period.",
    "stem_concepts": [
        ("Relative vs. Absolute Dating", "Relative dating (superposition) tells you which layer is older. Absolute dating (radiometric) tells you exactly how old a layer is in years. Both are essential for constructing geological timelines."),
        ("Unconformities", "Gaps in the rock record where layers are missing due to erosion or non-deposition. They represent lost time — potentially millions of years with no geological record at that location."),
        ("Correlation", "Geologists match rock layers across different locations using index fossils and distinctive marker layers (like volcanic ash). This allows them to reconstruct regional and global geological histories.")
    ],
    "stem_eval": [
        ("Expert (4)", "Core sample has 5+ distinct layers, each with appropriate evidence, shows at least one unconformity, and includes an interpretive guide explaining the history"),
        ("Proficient (3)", "Core sample has distinct layers with evidence and student can explain the geological history using superposition"),
        ("Developing (2)", "Core sample has some layers but evidence or explanation is vague"),
        ("Beginning (1)", "Core sample is incomplete or doesn't demonstrate understanding of rock strata principles")
    ],
    "support": [
        "Provide a simplified geological column showing major eras with example fossils",
        "Use pre-made layer kits with sand, clay, gravel, and small toy fossils",
        "Sentence frames: 'This layer is __ (older/younger) than that layer because __'"
    ],
    "extensions": [
        "Research radiometric dating and explain how scientists determine absolute age of rocks",
        "Investigate a local geological formation and identify the rock types and history it represents",
        "Create a geological timeline of your state showing major events recorded in local rock strata"
    ],
    "cross_curr": [
        ("Math", "Calculate sedimentation rates given layer thickness and time period — how many mm per year?"),
        ("ELA", "Write a detective story where the clues are all found in rock layers at a geological site"),
        ("Social Studies", "Research how geological knowledge helped early civilizations find water, minerals, and building materials")
    ],
    "misconceptions": [
        ("Rocks don't change", "Rocks are constantly being created, destroyed, and recycled through the rock cycle. Sedimentary rocks can be metamorphosed by heat and pressure, melted into magma, or eroded into sediment that forms new rock. Earth's surface is dynamic.", "Show images of the same location millions of years apart. Ask: Does this look like nothing changed?"),
        ("Fossils are just pretty rocks", "Fossils are preserved evidence of ancient life — they contain critical information about what organisms existed, what the environment was like, and how life has changed over time. Each fossil is a data point in the story of evolution.", "Give students real or replica fossils. Ask: What can you learn about this organism and its world from just this rock?"),
        ("The Earth has always looked like it does now", "Earth's surface has changed dramatically over 4.6 billion years. Continents have moved, oceans have appeared and disappeared, mountains have risen and eroded away. The landscape you see today is just a snapshot of an ever-changing planet.", "Show a time-lapse animation of continental drift from Pangaea to present. Earth never stays the same.")
    ]
}

L09 = {
    "id": "G07-L09",
    "title": "We Built a Better Dog (And Maybe a Mistake)",
    "subtitle": "How Humans Hack Evolution Through Selective Breeding",
    "ngss": "MS-LS4-5",
    "ngss_desc": "Gather and synthesize information about technologies that have changed the way humans influence the inheritance of desired traits in organisms.",
    "big_question": "How have humans changed plants and animals to suit our needs — and at what cost?",
    "objectives": [
        "Explain how artificial selection differs from natural selection",
        "Model how selection pressure affects trait frequency over generations",
        "Predict unintended consequences of extreme selective breeding",
        "Evaluate ethical implications of genetic modification technologies"
    ],
    "vocabulary": [
        ("Selective Breeding", "The process of choosing organisms with desired traits to reproduce, gradually changing the population over generations"),
        ("Artificial Selection", "Human-directed evolution — choosing which organisms reproduce based on traits we want, rather than natural survival"),
        ("Genetic Variation", "The differences in DNA between individuals in a population — raw material for selection"),
        ("Trait Frequency", "How common a specific trait is in a population — selective breeding changes this over generations")
    ],
    "components": [
        ("Selection Pressure", "How strongly humans select for a specific trait — from mild preference to extreme breeding programs", True),
        ("Generation Time", "How quickly organisms reproduce and create new generations — faster means faster change", True),
        ("Desired Trait Frequency", "How common the trait we want becomes in the population over time", False),
        ("Genetic Diversity", "The overall variety of genes in the population — drops when selection is too narrow", False)
    ],
    "think_about_it": "When selection pressure is extreme (like breeding only the flattest-faced bulldogs), desired trait frequency goes up — but what happens to genetic diversity? Is there a hidden cost?",
    "scenarios": [
        ("Mild Selection", "Set Selection Pressure to low and observe gradual changes over many generations"),
        ("Extreme Purebred Selection", "Lock Selection Pressure to maximum and observe both trait frequency AND genetic diversity"),
        ("No Selection (Wild)", "Set Selection Pressure to zero and observe what natural variation looks like")
    ],
    "sim_scenarios": [
        ("Mild Selection", "Low selection pressure over many generations", "What do you predict happens to Desired Trait Frequency with gentle selection over a long time?"),
        ("Extreme Purebred", "Maximum selection pressure, fast generations", "What do you predict happens to Genetic Diversity when only a few 'perfect' individuals are allowed to breed?"),
        ("Wild Population", "No selection pressure", "What do you predict Genetic Diversity looks like when humans don't interfere at all?")
    ],
    "discoveries": [
        "Artificial selection works the same as natural selection, but humans choose the 'fittest' traits instead of nature",
        "Extreme selection increases desired traits but DECREASES genetic diversity — making populations vulnerable",
        "Many purebred dogs suffer health problems directly caused by selective breeding for appearance",
        "All domestic dogs evolved from wolves through thousands of years of human-directed selection"
    ],
    "answer": "Humans change organisms through selective breeding — choosing individuals with desired traits to reproduce generation after generation. It works, but there's a hidden cost: extreme selection reduces genetic diversity, making populations vulnerable to disease and creating health problems. Purebred bulldogs can barely breathe because we bred them for flat faces!",
    "stem_title": "Design a Responsible Breeding Program",
    "stem_mission": "Design an ethical, evidence-based crop improvement program that increases yield while maintaining genetic diversity, using your understanding of artificial selection.",
    "stem_scenario": "A farming community is losing crop harvests to a new pest. They need your team to design a selective breeding program that develops pest-resistant crops WITHOUT sacrificing genetic diversity.",
    "stem_questions": [
        "How can you select for pest resistance without reducing genetic diversity too much?",
        "What's the difference between selective breeding and genetic modification (GMO)?",
        "What safeguards should be in place to prevent unintended consequences?"
    ],
    "stem_design_qs": [
        "What trait are you selecting for and how will you identify it?",
        "How will you maintain genetic diversity while selecting for your desired trait?",
        "How many generations will your program need to see results?",
        "What are the potential risks of your breeding program?"
    ],
    "career": "Geneticists and Agricultural Scientists develop improved crop varieties and animal breeds using selective breeding and biotechnology. They work for universities, USDA, and biotech companies, earning $65,000–$120,000/year.",
    "images": {
        "cover": ("cover-selective-breeding.png", "A dramatic comparison image showing a wolf on one side transforming into a variety of dog breeds on the other side — from Great Dane to Chihuahua — showing the power of artificial selection"),
        "landscape": ("landscape-breeding.png", "7th grade students in a greenhouse examining different varieties of plants — tomatoes, corn, peppers — comparing traits and taking notes"),
        "modeling": ("modeling-selection.png", "A diverse group of 7th grade students working on laptops building a digital model of selective breeding, classroom with genetics diagrams and Darwin posters"),
        "discussion": ("discussion-breeding.png", "A teacher showing images of dog breed changes over 100 years while 7th grade students discuss the ethical implications, students with hands raised"),
        "stem": ("stem-crop-program.png", "7th grade students presenting crop improvement program designs with diagrams showing trait selection over generations, poster presentations")
    },
    "pre_assessment": [
        "How do you think we got so many different dog breeds from wolves?",
        "What does it mean to 'breed' plants or animals for specific traits?",
        "Do you think humans should change organisms to suit our needs? Why or why not?",
        "What could go wrong if we only breed for one specific trait?"
    ],
    "extend_components": [
        ("Inbreeding Depression", "When closely related organisms breed, harmful recessive genes become more common, causing health problems"),
        ("GMO Technology", "Genetic modification directly edits DNA to insert desired traits, bypassing the slow process of selective breeding"),
        ("Wild Genetic Reservoir", "Wild populations contain genetic diversity that can be crossbred with domesticated populations to restore health")
    ],
    "reflections": [
        "How is artificial selection similar to and different from natural selection?",
        "Why do many purebred dogs have more health problems than mixed-breed dogs?",
        "Is it ethical to breed animals for traits that make them unhealthy but look cute to humans?",
        "How has selective breeding of crops like corn and wheat changed human civilization?",
        "What are the risks of reducing genetic diversity in our food crops?"
    ],
    "dimensions": [
        ("Science Practice", "Obtaining, Evaluating, and Communicating Information", "Students gather and synthesize information about how technologies like selective breeding and genetic modification change inheritance of traits."),
        ("Disciplinary Core Idea", "LS4.B Natural Selection and Artificial Selection", "In artificial selection, humans have the capacity to influence certain characteristics of organisms by selective breeding."),
        ("Crosscutting Concept", "Cause and Effect", "Students identify that human selection pressure CAUSES changes in trait frequency, with both intended effects (desired traits) and unintended consequences (reduced diversity).")
    ],
    "cast_items": [
        "Explain how artificial selection changes trait frequencies in populations over generations",
        "Compare natural selection and artificial selection",
        "Evaluate technologies that influence inheritance of traits"
    ],
    "cast_questions": [
        ("Multiple Choice:", "Over 15,000 years, humans selectively bred wolves into hundreds of dog breeds. Which statement best explains why all dog breeds can still interbreed with wolves?"),
        ("Constructed Response:", "Explain how selective breeding can both improve a desired trait AND create unintended health problems. Use a specific example in your answer.")
    ],
    "background_intro": "Humans have been modifying organisms through selective breeding for over 10,000 years — long before we understood genetics. From wolves to dogs, from wild grass to corn, artificial selection has shaped the living world to meet human needs.",
    "background_sections": [
        ("From Wolves to Dogs", "All domestic dogs (Canis lupus familiaris) descended from wolves through at least 15,000 years of selective breeding. Early humans selected wolves that were less aggressive and more cooperative. Over centuries, specialized breeding created everything from tiny Chihuahuas to massive Great Danes — all from the same ancestor."),
        ("Artificial vs. Natural Selection", "Both processes work through the same mechanism: variation exists, some individuals reproduce more than others, traits are inherited. The difference is WHO selects. In natural selection, the environment determines fitness. In artificial selection, HUMANS choose which traits to favor — often for our benefit rather than the organism's."),
        ("The Cost of Extreme Breeding", "Extreme selective breeding reduces genetic diversity, causing problems. Purebred English Bulldogs have such flat faces they can barely breathe. German Shepherds have sloped backs causing hip dysplasia. Cavalier King Charles Spaniels often have skulls too small for their brains. These are direct consequences of breeding for appearance over health."),
        ("Modern Genetic Technologies", "Today, selective breeding has been supplemented by genetic modification (GMOs), gene editing (CRISPR), and cloning. These technologies can achieve in one generation what would take decades of selective breeding. They raise important ethical questions about how far humans should go in modifying other organisms.")
    ],
    "lever_L": "Students identify selection pressure, generation time, desired trait frequency, and genetic diversity as components of the selective breeding system.",
    "lever_E": "Students determine that selection pressure increases desired traits but decreases overall genetic diversity — revealing the trade-off.",
    "lever_V": "Students build a model showing how human selection changes populations over generations.",
    "lever_Ev": "Students run mild, extreme, and no-selection scenarios to compare evolutionary outcomes.",
    "lever_R": "Students add inbreeding depression or GMO technology to explore more complex breeding dynamics.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with wolf-to-dogs transformation", "say": "Every dog breed on Earth came from ONE ancestor: the wolf. We did that. But should we have?", "do": "Show wolf → dog breed comparison. Ask: How did we get from wolf to Chihuahua?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we're investigating how humans hack evolution — and the consequences.", "do": "Have students read objectives. Pre-teach 'artificial selection.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "How have humans changed life on Earth?", "say": "Corn used to be a tiny grass. Dogs used to be wolves. How did WE do that?", "do": "Show before/after of corn (teosinte → modern corn). Discuss.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll model how selection pressure changes populations over generations.", "do": "Preview LEVER steps.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for breeding model", "say": "What do humans control in selective breeding? What changes as a result?", "do": "Guide sorting. Discuss why selection pressure is human-controlled.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows", "say": "Stronger selection gets you the trait faster. But what's the hidden cost?", "do": "Reveal the negative relationship to genetic diversity.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and results", "say": "Let's compare: gentle selection vs. extreme purebred breeding. What's the trade-off?", "do": "Students predict first. Show the diversity crash in extreme selection.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings", "say": "Why can't English Bulldogs breathe properly? What did our model reveal?", "do": "Show bulldog health problems. Connect to model's diversity crash.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Crop improvement program", "say": "Design a breeding program that gets the trait you want WITHOUT the cost.", "do": "Groups design programs balancing trait selection with diversity.", "time": "12 min"}
    ],
    "sort_reasoning": "Selection Pressure and Generation Time are external because they are controlled by humans — we decide how strongly to select and how quickly we breed organisms. Desired Trait Frequency and Genetic Diversity are internal because they are outcomes that change as a result of the selection process over time.",
    "relationships": [
        ("Selection Pressure to Desired Trait Frequency", "POSITIVE (+)", "Stronger selection pressure means only organisms with the desired trait reproduce, rapidly increasing how common that trait is in the population."),
        ("Generation Time to Desired Trait Frequency", "POSITIVE (+)", "More generations of selection allow the desired trait to become more common. Faster-reproducing organisms show results sooner."),
        ("Selection Pressure to Genetic Diversity", "NEGATIVE (-)", "Strong selection eliminates individuals without the desired trait, reducing the gene pool. Extreme selection dramatically narrows genetic diversity, making populations vulnerable.")
    ],
    "sim_answers": [
        ("Extreme Purebred Scenario", "When Selection Pressure is maximized, Desired Trait Frequency rises rapidly — the trait becomes nearly universal within a few generations. But Genetic Diversity crashes. With fewer genetic variants, the population becomes vulnerable to diseases, environmental changes, and inherited health problems."),
        ("Wild Population Scenario", "With no Selection Pressure, Desired Trait Frequency stays at natural levels (no change in any specific direction). Genetic Diversity remains high — the population has maximum variation, making it resilient and adaptable to environmental challenges.")
    ],
    "reflection_exemplars": [
        ("How is artificial selection like natural selection?", "Both work through the same mechanism: (1) Variation exists in the population, (2) Some individuals reproduce more, (3) Traits are inherited by offspring. The only difference is WHO decides which traits are 'fit.' In natural selection, the environment decides. In artificial selection, humans decide."),
        ("Why do purebred dogs have more health problems?", "Extreme selective breeding dramatically reduces genetic diversity. When only dogs with specific appearance traits are allowed to breed (generation after generation), harmful recessive genes become concentrated. English Bulldogs were bred for flat faces, creating breathing problems. German Shepherds were bred for sloped backs, causing hip dysplasia. The 'desired' appearance comes at the cost of health.")
    ],
    "stem_intro": "A farming community needs pest-resistant crops but is concerned about losing genetic diversity. Your team must design a breeding program that achieves resistance while maintaining a healthy gene pool.",
    "stem_concepts": [
        ("Gene Pool", "The total collection of genes in a breeding population. A larger gene pool means more genetic diversity and greater resilience against diseases and environmental changes."),
        ("Hybrid Vigor", "Crossing genetically different individuals often produces offspring that are healthier and more robust than either parent. This is the opposite of the problems caused by inbreeding."),
        ("Seed Banks", "Facilities like the Svalbard Global Seed Vault store seeds from thousands of crop varieties, preserving genetic diversity as insurance against crop failures and extinction.")
    ],
    "stem_eval": [
        ("Expert (4)", "Program balances trait selection with diversity maintenance, references model evidence, includes monitoring plan, and addresses ethical considerations"),
        ("Proficient (3)", "Program selects for desired traits while acknowledging diversity concerns, with model evidence"),
        ("Developing (2)", "Program focuses on trait selection but doesn't adequately address genetic diversity"),
        ("Beginning (1)", "Program is incomplete or doesn't connect to artificial selection concepts")
    ],
    "support": [
        "Provide visual charts showing dog breed changes over 100 years for concrete examples",
        "Use colored beads to physically simulate selection pressure on a 'population'",
        "Sentence frames: 'When selection pressure increases, desired trait frequency __ but genetic diversity __'"
    ],
    "extensions": [
        "Research CRISPR gene editing and compare its speed and precision to traditional selective breeding",
        "Investigate the Irish Potato Famine as a case study of what happens when genetic diversity is too low",
        "Debate: Should we use genetic modification to create 'designer babies'?"
    ],
    "cross_curr": [
        ("Math", "Calculate how many generations of selection it takes for a rare trait to become dominant in a population"),
        ("ELA", "Write a persuasive essay arguing for or against extreme selective breeding in dog shows"),
        ("Social Studies", "Research how the agricultural revolution (10,000 years of selective breeding) led to civilization")
    ],
    "misconceptions": [
        ("Selective breeding is the same as genetic modification", "Selective breeding uses natural reproduction — choosing which organisms mate based on their traits. Genetic modification directly alters DNA in a lab. Selective breeding has been done for 10,000+ years; GMOs are a modern technology. Both change organisms, but through very different methods.", "Analogy: Selective breeding is like choosing which songs to play on a playlist. GMO is like remixing the songs in a studio."),
        ("Artificial selection is unnatural", "Humans have been selectively breeding organisms for over 10,000 years — longer than recorded history. Every fruit, vegetable, and domestic animal has been modified by humans. The 'natural' versions of corn, bananas, and watermelon look nothing like what we eat today.", "Show images of wild banana (tiny, full of seeds) vs. modern banana. Wild corn (teosinte) vs. sweet corn. We changed these."),
        ("More selection is always better", "Extreme selection creates a dangerous trade-off. While the desired trait increases, genetic diversity crashes. Low diversity makes populations vulnerable to disease epidemics, environmental changes, and inherited disorders. The Irish Potato Famine killed over a million people because all the potatoes were genetically identical.", "Show the bulldog breathing problem. Ask: We got the flat face we wanted. Was it worth this cost?")
    ]
}

# ── L10 ───────────────────────────────────────────────────────────
L10 = {
    "id": "G07-L10",
    "title": "Your Phone Speaks in 1s and 0s",
    "subtitle": "How Digital Signals Carry Music, Messages, and Memes",
    "ngss": "MS-PS4-3",
    "ngss_desc": "Integrate qualitative scientific and technical information to support the claim that digitized signals are a more reliable way to encode and transmit information than analog signals.",
    "big_question": "Why does your music sound perfect every time you play it — but your grandparents' vinyl records got scratchy?",
    "objectives": [
        "Compare how analog and digital signals encode information",
        "Explain how sampling rate affects digital signal quality",
        "Model how compression reduces file size while trading off accuracy",
        "Evaluate why digital signals are more reliable for transmitting information"
    ],
    "vocabulary": [
        ("Analog Signal", "A continuous signal that varies smoothly over time, like a sound wave or vinyl record groove"),
        ("Digital Signal", "Information encoded as discrete values — typically 1s and 0s (binary) — that can be exactly copied"),
        ("Sampling Rate", "How many times per second an analog signal is measured to create a digital version (measured in Hz)"),
        ("Compression", "Reducing file size by removing some data — lossy compression removes data permanently, lossless preserves everything")
    ],
    "components": [
        ("Sampling Rate", "How many times per second the analog signal is measured and converted to digital values. Higher rates capture more detail.", True),
        ("Compression Level", "How aggressively the digital file is reduced in size. Higher compression removes more data to save space.", True),
        ("Signal Accuracy", "How faithfully the digital version reproduces the original analog signal. Measured by comparing digital output to original.", False),
        ("File Size", "The amount of digital storage space required. Smaller files are easier to transmit but may sacrifice quality.", False)
    ],
    "think_about_it": "When you download a song, you're choosing between file size and sound quality. What happens to the music when compression is pushed too far?",
    "scenarios": [
        ("Studio Quality", "Set Sampling Rate to maximum and Compression Level to minimum. Observe Signal Accuracy and File Size."),
        ("Phone Streaming", "Set Sampling Rate to medium and Compression Level to medium. Compare accuracy and file size to Studio Quality."),
        ("Extreme Compression", "Set Compression Level to maximum while keeping Sampling Rate at medium. What happens to Signal Accuracy?")
    ],
    "sim_scenarios": [
        ("Studio Quality", "Sampling Rate: HIGH | Compression Level: LOW", "What will Signal Accuracy and File Size look like with maximum quality settings?"),
        ("Phone Streaming", "Sampling Rate: MEDIUM | Compression Level: MEDIUM", "How does moderate compression affect quality? Is the trade-off worth it?"),
        ("Extreme Compression", "Sampling Rate: MEDIUM | Compression Level: HIGH", "At what point does compression destroy so much information that quality becomes unacceptable?")
    ],
    "discoveries": [
        "Higher sampling rates produce more accurate digital copies but create larger files",
        "Moderate compression reduces file size significantly with barely noticeable quality loss",
        "Extreme compression destroys enough data that quality drops dramatically — you can hear the difference",
        "Digital signals can be copied perfectly (unlike analog), making them ideal for storage and transmission"
    ],
    "answer": "Digital signals encode information as exact numbers (1s and 0s) that can be copied perfectly every time. Your grandparents' vinyl records were analog — each play physically wore the grooves, adding scratches and noise. A digital music file sounds identical on its millionth play because the 1s and 0s never change. The trade-off is that converting analog to digital requires choosing a sampling rate (detail level) and compression level (file size), which affects how closely the digital version matches the original.",
    "stem_title": "The Streaming Service Challenge",
    "stem_mission": "Design a music streaming service that delivers the best possible sound quality while keeping data usage low enough for mobile users.",
    "stem_scenario": "Your startup is launching a music streaming app. Users on Wi-Fi want studio quality, but mobile users have limited data plans. You need to design a system that automatically adjusts quality based on connection type — without making the music sound terrible.",
    "stem_questions": [
        "What sampling rate and compression settings should you use for Wi-Fi vs. mobile data?",
        "How do you decide the minimum acceptable quality before users notice degradation?",
        "What other factors besides sound quality matter to your streaming service users?"
    ],
    "stem_design_qs": [
        "What criteria define 'good enough' quality for mobile streaming?",
        "How will your system detect and adapt to different connection speeds?",
        "What happens when a user switches from Wi-Fi to mobile mid-song?",
        "How can you test whether users can actually hear the difference between quality levels?"
    ],
    "career": "Audio Engineers use signal processing to record, mix, and master music. They understand sampling rates, compression, and digital audio workstations (DAWs). They work in recording studios, live concerts, film production, and video game audio — combining physics, math, and creativity.",
    "images": {
        "cover": ("G07-L10-cover.png", "teenager wearing headphones with visible digital sound wave visualizations flowing from phone to headphones, showing binary 1s and 0s embedded in the sound waves, modern urban setting, dramatic lighting"),
        "landscape": ("G07-L10-landscape.png", "diverse group of 7th graders in a modern music lab comparing vinyl records with digital music on tablets, examining sound waves on screens, engaged and curious expressions"),
        "modeling": ("G07-L10-modeling.png", "diverse 7th grade students at computers building digital signal models, screens showing waveform comparisons between analog and digital signals, collaborative learning"),
        "discussion": ("G07-L10-discussion.png", "Black teacher leading classroom discussion about analog vs digital signals, whiteboard showing wave diagrams and binary code, students raising hands with questions"),
        "stem": ("G07-L10-stem.png", "diverse group of 7th graders designing a music streaming app interface on large screens, testing sound quality with headphones, engineering design process visible on whiteboards")
    },
    "pre_assessment": [
        "What is the difference between an analog signal and a digital signal? Give an example of each.",
        "Why might a digital copy of a song sound different from the original live performance?",
        "What does 'compression' mean when talking about digital files like MP3s?",
        "Why do some music files take up more storage space than others?"
    ],
    "extend_components": [
        ("Bit Depth", "The number of possible values for each sample. Higher bit depth captures more subtle volume differences, like the difference between a whisper and a shout."),
        ("Transmission Speed", "How quickly data can be sent from server to device. Faster connections allow higher quality streaming without buffering."),
        ("Error Correction", "Digital systems can detect and fix errors during transmission. This is why digital signals are more reliable than analog — damaged bits can be reconstructed.")
    ],
    "reflections": [
        "Why are digital signals considered more reliable than analog signals for storing and transmitting information?",
        "What trade-offs do engineers make when choosing sampling rate and compression settings?",
        "How does the concept of sampling rate connect to the quality of digital music?",
        "Why might a musician prefer vinyl (analog) even though digital is technically more reliable?",
        "How has the shift from analog to digital changed how we consume music, movies, and information?"
    ],
    "dimensions": [
        ("SEP", "Obtaining, Evaluating, and Communicating Information", "Students integrate qualitative scientific and technical information from multiple sources to compare analog and digital signal reliability."),
        ("DCI", "PS4.C: Information Technologies and Instrumentation", "Digitized signals (sent as wave pulses) are a more reliable way to encode and transmit information because they can be exactly copied."),
        ("CCC", "Structure and Function", "The structure of digital encoding (discrete binary values) gives it the function of perfect reproducibility, while analog's continuous structure makes it susceptible to degradation.")
    ],
    "cast_items": [
        "Model the relationship between sampling rate, compression, and signal fidelity",
        "Compare analog and digital signal behavior under different transmission conditions",
        "Evaluate engineering trade-offs in real-world digital communication systems"
    ],
    "cast_questions": [
        ("Evaluate:", "A podcast is recorded at 44,100 Hz sampling rate and compressed to MP3 at 128 kbps. A listener complains the audio sounds 'thin.' Using your model, explain what's happening and propose a solution."),
        ("Compare:", "Your model shows that increasing sampling rate improves signal accuracy. Why don't we just set sampling rate to maximum for everything? Use evidence from your simulation to explain the trade-off.")
    ],
    "background_intro": "We live in a digital world, but the sounds, images, and experiences we want to capture are analog. This lesson explores how we bridge that gap — converting continuous analog signals into discrete digital ones — and why that conversion involves fundamental trade-offs between quality and practicality.",
    "background_sections": [
        ("Analog vs. Digital: The Fundamental Difference", "Analog signals are continuous — they vary smoothly over time, like the air pressure changes that make up sound waves. A vinyl record stores sound as a continuous groove that physically mirrors the sound wave. Digital signals break this continuous information into discrete steps: measurements taken at regular intervals, each stored as a number. CDs sample sound 44,100 times per second, storing each measurement as a number with 65,536 possible values (16-bit depth)."),
        ("Sampling and the Nyquist Theorem", "The key insight of digital audio is the Nyquist-Shannon sampling theorem: to accurately capture a signal, you must sample at least twice as fast as the highest frequency you want to preserve. Human hearing ranges from 20 Hz to 20,000 Hz, which is why CD-quality audio samples at 44,100 Hz (just over 2× the maximum). Sample below this rate and high frequencies get distorted — a phenomenon called 'aliasing.'"),
        ("Compression: Lossy vs. Lossless", "Raw digital audio creates enormous files (a 3-minute song at CD quality is about 30 MB). Compression algorithms reduce this. Lossless compression (FLAC, ALAC) is like a zip file — it compresses without losing any data, achieving about 50% size reduction. Lossy compression (MP3, AAC) permanently removes data that psychoacoustic models predict humans won't notice, achieving 75-90% size reduction. The trade-off: lossy files are much smaller but can never be restored to full quality."),
        ("Why Digital Wins for Reliability", "The killer advantage of digital signals is perfect copyability. An analog signal degrades every time it's copied — like photocopying a photocopy, each generation gets worse. A digital signal is just numbers, and numbers can be copied exactly. Digital systems also include error correction: extra data that lets the receiver detect and fix transmission errors. This is why a scratched CD can still play (up to a point) while a scratched vinyl record pops and clicks permanently.")
    ],
    "lever_L": "Students identify sampling rate, compression level, signal accuracy, and file size as components of the digital signal system.",
    "lever_E": "Students discover that sampling rate positively affects accuracy while compression creates a trade-off between file size and quality.",
    "lever_V": "Students build a model showing how analog signals are converted to digital and how settings affect the output.",
    "lever_Ev": "Students run studio quality, streaming, and extreme compression scenarios to compare quality-vs-size trade-offs.",
    "lever_R": "Students add bit depth or error correction to explore more nuanced digital signal behavior.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with digital waveform imagery", "say": "Every text, every song, every TikTok you've ever seen traveled as 1s and 0s. How does THAT work?", "do": "Play the same song on vinyl (scratchy) and digital (clean). Ask: Why the difference?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we're investigating how your phone turns sound waves into numbers — and back again.", "do": "Have students read objectives. Pre-teach 'sampling rate' with a visual.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Vinyl record vs. digital waveform", "say": "Your grandparents' records got scratchy. Your digital music sounds perfect every time. Why?", "do": "Show vinyl groove under microscope vs. binary data. Discuss physical vs. numerical storage.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We'll model how digital encoding works — and find the trade-offs engineers face every day.", "do": "Preview LEVER steps.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for signal model", "say": "What do engineers CONTROL when digitizing sound? What CHANGES as a result?", "do": "Guide sorting. Discuss why sampling rate is a choice, not a result.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows", "say": "More samples per second means better quality. But more compression means... what?", "do": "Reveal the compression trade-off: smaller files but lower accuracy.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Quality comparison graphs", "say": "Let's compare: studio quality vs. phone streaming vs. extreme compression. Can you hear the difference?", "do": "Students predict quality-vs-size outcomes. Compare simulation results.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings and comparisons", "say": "So why did we switch from analog to digital? What does our model tell us?", "do": "Compare analog degradation (copies of copies) vs. digital perfection.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Streaming service design", "say": "Design a streaming service that sounds great on Wi-Fi AND doesn't burn through mobile data.", "do": "Groups design adaptive quality systems. Present trade-off decisions.", "time": "12 min"}
    ],
    "sort_reasoning": "Sampling Rate and Compression Level are external because they are engineering choices — humans decide how many samples to take and how much to compress. Signal Accuracy and File Size are internal because they are outcomes determined by those engineering choices.",
    "relationships": [
        ("Sampling Rate to Signal Accuracy", "POSITIVE (+)", "Higher sampling rates capture more detail from the original analog signal, producing a more accurate digital representation. Doubling the sampling rate roughly doubles the frequency range that can be faithfully reproduced."),
        ("Compression Level to File Size", "NEGATIVE (-)", "Higher compression reduces file size — that's the whole point. Aggressive compression can shrink a 30 MB song to 3 MB, but at the cost of permanently removing audio data."),
        ("Compression Level to Signal Accuracy", "NEGATIVE (-)", "Higher compression removes more data from the digital file, reducing how accurately it represents the original signal. At extreme compression, the quality loss becomes audible — thin sound, artifacts, and missing detail.")
    ],
    "sim_answers": [
        ("Studio Quality Scenario", "With maximum Sampling Rate and minimum Compression Level, Signal Accuracy is at its highest — the digital version closely matches the original analog signal. But File Size is enormous. A single album might take several gigabytes. This is ideal for professional studios but impractical for streaming on mobile devices."),
        ("Extreme Compression Scenario", "With maximum Compression Level, File Size drops dramatically — great for limited data plans. But Signal Accuracy plummets. The compression algorithm removes so much data that audible artifacts appear: the music sounds 'thin,' 'watery,' or 'metallic.' This demonstrates why engineers must balance quality against practicality.")
    ],
    "reflection_exemplars": [
        ("Why are digital signals more reliable than analog?", "Digital signals encode information as exact numbers (binary: 1s and 0s). These numbers can be copied perfectly — the millionth copy is identical to the first. Analog signals are physical patterns (grooves, magnetic fields) that degrade with each copy or playback. Digital systems also include error correction: extra data that detects and fixes transmission errors. This is why a digital photo shared a million times looks the same, while a photocopy of a photocopy gets blurry."),
        ("What trade-offs do engineers face with sampling and compression?", "Higher sampling rates capture more detail but create larger files. More compression shrinks files but reduces quality. Engineers must balance these based on the use case: a surgeon viewing an MRI needs maximum accuracy (no compression), while a teenager streaming music on a bus needs small files (moderate compression is fine because human ears can't detect the missing data in most cases). The 'right' setting depends entirely on the purpose.")
    ],
    "stem_intro": "A new music streaming startup needs to compete with Spotify and Apple Music. The key engineering challenge: deliver the best possible sound quality while keeping data usage low enough for users with limited mobile data plans.",
    "stem_concepts": [
        ("Adaptive Bitrate Streaming", "Technology that automatically adjusts audio quality based on network conditions. When on fast Wi-Fi, it streams high quality. When on slow mobile data, it reduces quality to prevent buffering."),
        ("Psychoacoustic Modeling", "The science of what sounds humans can and cannot hear. Compression algorithms use this to remove frequencies and details that most people won't notice, achieving smaller files with minimal perceived quality loss."),
        ("Codec", "Short for coder-decoder. Software that encodes analog audio into digital format and decodes it back for playback. Different codecs (MP3, AAC, Opus) use different algorithms with different quality-to-size ratios.")
    ],
    "stem_eval": [
        ("Expert (4)", "Design includes adaptive quality settings for different connections, references model evidence for quality thresholds, addresses user experience and data constraints"),
        ("Proficient (3)", "Design specifies different quality levels with clear trade-off reasoning supported by model data"),
        ("Developing (2)", "Design addresses quality or file size but doesn't effectively balance both trade-offs"),
        ("Beginning (1)", "Design is incomplete or doesn't connect to digital signal concepts from the lesson")
    ],
    "support": [
        "Use a visual 'pixel grid' analogy: show how a photo looks at 10×10 pixels vs. 100×100 vs. 1000×1000 to make sampling rate concrete",
        "Provide pre-made comparison audio clips at different compression levels so students can hear the difference",
        "Sentence frames: 'When sampling rate increases, signal accuracy __ because __, but file size __ because __'"
    ],
    "extensions": [
        "Research how streaming services like Spotify decide what quality to use — investigate their adaptive bitrate algorithms",
        "Compare the same song as WAV (uncompressed), FLAC (lossless), MP3 320kbps, and MP3 128kbps using waveform analysis software",
        "Investigate how digital signals enable error correction — how can a scratched CD still play while a scratched vinyl can't?"
    ],
    "cross_curr": [
        ("Math", "Calculate file sizes: a 3-minute song at 44,100 Hz × 16-bit × 2 channels = ? bytes. Then calculate compression ratios for MP3 vs. FLAC."),
        ("ELA", "Write a consumer guide explaining to non-technical users what audio quality settings mean and helping them choose the right ones."),
        ("Social Studies", "Research how the shift from physical media (vinyl, CDs) to digital streaming changed the music industry's economics and artist compensation.")
    ],
    "misconceptions": [
        ("Digital is always better than analog", "Digital is more RELIABLE (perfect copies, no degradation) but not necessarily 'better' in every way. Analog vinyl records capture a continuous signal with theoretically infinite resolution. Some audiophiles prefer vinyl's 'warmer' sound. The advantage of digital is consistency and copyability, not inherent superiority in every dimension.", "Ask: What does 'better' mean? Better for what purpose? A vinyl record in a quiet room might sound richer than a compressed MP3 on cheap earbuds. Context matters."),
        ("Higher numbers always mean better quality", "More sampling rate and less compression generally improve quality, but there are limits. Sampling above 96,000 Hz captures frequencies humans can't hear — it's wasted data. Similarly, 24-bit audio captures volume differences too subtle for human ears. 'Better' numbers only matter up to the limits of human perception.", "Ask: If you can't hear frequencies above 20,000 Hz, what's the point of sampling at 192,000 Hz? Engineers design for HUMAN listeners, not theoretical perfection."),
        ("Compressed files are missing most of their data", "A 128 kbps MP3 is about 1/10th the size of a CD-quality WAV file, but it doesn't sound 1/10th as good. Compression algorithms are smart — they remove data that psychoacoustic research shows humans won't notice (frequencies masked by louder sounds, details below the threshold of perception). Most people can't distinguish 256 kbps AAC from uncompressed audio in blind tests.", "Play a blind test: same song at 256 kbps AAC and uncompressed WAV. Most students won't hear a difference, proving that smart compression keeps what matters.")
    ]
}

ALL_LESSONS = [L01, L02, L03, L04, L05, L06, L07, L08, L09, L10]
