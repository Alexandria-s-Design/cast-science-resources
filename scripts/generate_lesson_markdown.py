#!/usr/bin/env python3
"""
Generate markdown lesson template files for the lessons/ directory.
Creates detailed lesson markdown files from the lesson data dictionaries,
following the same format as the Grade 5 exemplar files.

Usage:
    python generate_lesson_markdown.py          # Generate G06 + G08
    python generate_lesson_markdown.py G06      # Generate G06 only
    python generate_lesson_markdown.py G08      # Generate G08 only
"""

import os, re, sys

# Add scripts dir to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lesson_data_G06 import ALL_LESSONS as G06_LESSONS
from lesson_data_G08 import ALL_LESSONS as G08_LESSONS


def slugify(title):
    """Convert a lesson title to a URL-friendly filename slug."""
    s = title.lower()
    s = s.replace("'", "").replace("\u2019", "")  # Remove apostrophes
    s = re.sub(r'[^a-z0-9\s-]', '', s)            # Remove special chars
    s = re.sub(r'[\s-]+', '-', s).strip('-')       # Spaces/dashes to single dash
    return s


def get_grade_info(lesson_id):
    """Return grade label, full label, age range, and session time."""
    if lesson_id.startswith("G06"):
        return "6th", "6th Grade", "11-12 years old", "45-60 minutes"
    elif lesson_id.startswith("G08"):
        return "8th", "8th Grade", "13-14 years old", "50-70 minutes"
    else:
        return "5th", "5th Grade", "10-11 years old", "40-45 minutes"


def generate_markdown(L):
    """Generate a complete markdown lesson file from a lesson data dictionary."""
    grade, grade_label, age_range, session_time = get_grade_info(L["id"])

    # Separate external and internal components
    external = [(n, d) for n, d, e in L["components"] if e]
    internal = [(n, d) for n, d, e in L["components"] if not e]
    ext_names = [n for n, _, e in L["components"] if e]
    int_names = [n for n, _, e in L["components"] if not e]

    # Count positive/negative relationships
    pos_count = sum(1 for _, s, _ in L["relationships"] if "POSITIVE" in s.upper())
    neg_count = sum(1 for _, s, _ in L["relationships"] if "NEGATIVE" in s.upper())

    lines = []

    def add(*args):
        for a in args:
            lines.append(a)

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # HEADER INFORMATION
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    add(f'# Lesson: {L["title"]}', '')
    add('## Header Information', '')
    add('| Field | Value |')
    add('|-------|-------|')
    add(f'| **Lesson ID** | {L["id"]} |')
    add(f'| **Grade** | {grade} |')
    add(f'| **Lesson Name** | {L["title"]} |')
    add('| **Status** | Template |')
    add('', '---', '')

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # PLATFORM SECTION
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    add('## Platform', '')
    add('### Title')
    add(f'**{L["title"]} \u2014 {L["subtitle"]}**', '')

    add('### Overview')
    add(f'{L["background_intro"]} Students investigate the driving question: {L["big_question"]} Using the LEVER framework, students identify key components, establish cause-and-effect relationships, run simulations to test scenarios, and extend their understanding through research and engineering challenges.', '')

    add('### Cover Image')
    add(f'[{L["images"]["cover"][1]}]', '')

    add('### Grade')
    add(grade, '')

    add('### NGSS Standard')
    add(f'**{L["ngss"]}**: {L["ngss_desc"]}', '')

    add('### Learning Objectives')
    for obj in L["objectives"]:
        add(f'- {obj}')
    add('')

    add('### Component List (Starting Model: 3-4 Components)', '')
    add('| Component | Type | What It Represents |')
    add('|-----------|------|-------------------|')
    for name, desc, is_ext in L["components"]:
        comp_type = "External" if is_ext else "Internal"
        add(f'| {name} | {comp_type} | {desc} |')
    add('')

    add('### Research for Lesson')
    # Use background sections as research pointers
    for bg_title, _ in L["background_sections"]:
        add(f'- {bg_title} \u2014 reference materials and textbook resources')
    add('')
    add('---', '')

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # ACTIVITY 1: LOCATE
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    add('## Activity 1: LOCATE \u2014 Build Your System', '')
    add('### Text Editor', '')
    add('```')
    add(L["title"].upper())
    add('')
    add(f'{L["subtitle"]}.')
    add(f'{L["big_question"]}')
    add('')
    add("That's not just a question \u2014 it's something you can MODEL.")
    add("And you're about to build exactly that.")
    add('')
    add('\u2501' * 60)
    add('')
    add('STEP 1: CHOOSE YOUR COMPONENTS')
    add('\u2022 Look at the component panel on the RIGHT side of your screen')
    add('\u2022 Find the EXTERNAL components (things we can\'t control):')
    for name, desc, is_ext in L["components"]:
        if is_ext:
            short_desc = desc.split(',')[0].split('.')[0] if ',' in desc or '.' in desc else desc
            add(f'  \u25cb Click "{name}" \u2014 {short_desc.lower().rstrip(".")}')
    add('\u2022 Find the INTERNAL components (things that change because of other things):')
    for name, desc, is_ext in L["components"]:
        if not is_ext:
            short_desc = desc.split(',')[0].split('.')[0] if ',' in desc or '.' in desc else desc
            add(f'  \u25cb Click "{name}" \u2014 {short_desc.lower().rstrip(".")}')
    add('')
    add('STEP 2: ADD TO YOUR MODEL')
    add('\u2022 Click the PLUS (+) button to add each component to your picture')
    add(f'\u2022 You should now see {len(L["components"])} components on your canvas')
    add('')
    add('STEP 3: SORT YOUR COMPONENTS')
    add('\u2022 Sort your components into EXTERNAL and INTERNAL')
    add('\u2022 EXTERNAL = things we can\'t control (inputs from outside the system)')
    add('\u2022 INTERNAL = things that change because of other things in the system')
    add('\u2022 Your teacher will show you how this works in the video')
    add('')
    add('\u2501' * 60)
    add('')
    add('You now have the basic pieces of your system.')
    add("But pieces alone don't explain anything \u2014 next, we connect them.")
    add('```')
    add('')

    # Activity 1 Video Script
    add('### Video Script', '')
    add('```')
    add(f'"{L["big_question"]}')
    add('')
    add("That's what we're going to figure out today. Not by reading about")
    add("it \u2014 by MODELING it. You're going to build a system that shows")
    add("exactly how this works.")
    add('')
    add("Let's build our system. Look at the component panel on the right")
    add("side of your screen. You'll see two types of components:")
    add('')
    add('EXTERNAL components \u2014 things that come from outside the system.')
    add("Inputs we can't directly control.")
    add('')
    add('INTERNAL components \u2014 things that change BECAUSE of other things')
    add('in the system. They respond to the externals.')
    add('')
    for name, desc, is_ext in L["components"]:
        ext_label = "external" if is_ext else "internal"
        first_sentence = desc.split('.')[0] if '.' in desc else desc.split(',')[0] if ',' in desc else desc
        add(f"Click on '{name}' \u2014 that's {ext_label}. {first_sentence}.")
    add('')
    add("Now you need to SORT them. Which ones are external \u2014 things that")
    add("come from outside the system? Which ones are internal \u2014 things")
    add("that change because of what's happening inside?")
    add('')
    add(f'{L["sort_reasoning"]}')
    add('')
    add("Sort your components, then hit the PLUS button to add each one")
    add("to your model canvas.")
    add('')
    add("You've got your pieces. But right now they're just sitting there,")
    add("not connected. In the next activity, we'll draw the invisible")
    add("lines that show how everything affects everything else.")
    add('')
    add('Now it\'s your turn to ModelIt!"')
    add('```')
    add('')

    add('### Image')
    add(f'[Screenshot showing {len(L["components"])} components sorted: {", ".join(ext_names)} (External), {", ".join(int_names)} (Internal)]')
    add('')
    add('### Graph')
    add('[Empty graph panel \u2014 no simulation yet]')
    add('')
    add('---', '')

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # ACTIVITY 2: ESTABLISH
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    add('## Activity 2: ESTABLISH \u2014 Connect the Relationships', '')
    add('### Text Editor', '')
    add('```')
    add('TIME TO DRAW THE INVISIBLE LINES')
    add('')
    add(f"Those {len(L['components'])} components don't just sit there \u2014 they AFFECT each other.")
    add("When one changes, others change too. Let's map those connections.")
    add('')
    add('\u2501' * 60)
    add('')
    add('STEP 1: OPEN CONNECTION MODE')
    add('\u2022 Click the "Connect" icon in the TOP LEFT corner of your screen')
    add('\u2022 Your cursor is now ready to draw relationship arrows')
    add('')
    add('STEP 2: DRAW YOUR RELATIONSHIPS')
    for conn, sign, explanation in L["relationships"]:
        parts = conn.split(" to ")
        if len(parts) == 2:
            add(f'\u2022 Click on "{parts[0]}" and drag an arrow to "{parts[1]}"')
    add('')
    add('STEP 3: SET POSITIVE OR NEGATIVE')
    add('\u2022 Look at the +/\u2212 toggle in the TOP LEFT corner')
    add('\u2022 For each connection, ask: "When this goes UP, does the other go UP or DOWN?"')
    add('')
    for conn, sign, explanation in L["relationships"]:
        parts = conn.split(" to ")
        if len(parts) == 2:
            if "NEGATIVE" in sign.upper():
                sign_label = "NEGATIVE (\u2212)"
            else:
                sign_label = "POSITIVE (+)"
            add(f'  \u25cb {parts[0]} \u2192 {parts[1]} = {sign_label}')
            add(f'    {explanation}')
            add('')

    add('STEP 4: CHECK YOUR MODEL')
    add(f'\u2022 You should have {len(L["relationships"])} arrows total')
    add(f'\u2022 {neg_count} negative relationship(s), {pos_count} positive relationship(s)')
    add('\u2022 This is your system model!')
    add('')
    add('\u2501' * 60)
    add('')
    add(f'THINK ABOUT IT: {L["think_about_it"]}')
    add('```')
    add('')

    # Activity 2 Video Script
    add('### Video Script', '')
    add('```')
    add('"Your pieces are on the board, but they\'re not talking to each')
    add("other yet. Time to draw the invisible lines \u2014 the relationships")
    add("that make this a SYSTEM, not just a pile of parts.")
    add('')
    add("Click the 'Connect' icon in the top left corner. Now you're in")
    add("connection mode.")
    add('')
    ordinals = ["First", "Next", "Last", "Final"]
    for i, (conn, sign, explanation) in enumerate(L["relationships"]):
        parts = conn.split(" to ")
        if len(parts) == 2:
            ordinal = ordinals[min(i, len(ordinals) - 1)]
            is_neg = "NEGATIVE" in sign.upper()
            add(f"{ordinal} connection: Click on '{parts[0]}' and drag an arrow")
            add(f"over to '{parts[1]}.'")
            add('')
            add(f"Here's the key question: When {parts[0].lower()} goes UP, does")
            add(f"{parts[1].lower()} go UP or DOWN?")
            add('')
            add(f"{explanation}")
            if is_neg:
                add("That's a NEGATIVE relationship. When one goes up, the other")
                add("goes DOWN. Click the minus sign.")
            else:
                add("That's a POSITIVE relationship. They move in the same")
                add("direction. Click the plus sign.")
            add('')

    add(f"Look at your model now. You've got {neg_count} negative and {pos_count}")
    add(f"positive relationships. {len(L['relationships'])} arrows total.")
    add('')
    add(f"{L['think_about_it']}")
    add('')
    add('Now it\'s your turn to ModelIt!"')
    add('```')
    add('')

    add('### Image')
    arrows = []
    for conn, sign, _ in L["relationships"]:
        parts = conn.split(" to ")
        if len(parts) == 2:
            sym = "\u2212" if "NEGATIVE" in sign.upper() else "+"
            arrows.append(f"{parts[0]} {sym}\u2192 {parts[1]}")
    add(f'[Screenshot showing connected model with arrows: {", ".join(arrows)}]')
    add('')
    add('---', '')

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # ACTIVITY 3: VISUALIZE & EVALUATE
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    add('## Activity 3: VISUALIZE & EVALUATE \u2014 Run Your Model', '')
    add('### Text Editor', '')
    add('```')
    add('TIME TO SEE YOUR SYSTEM IN ACTION')
    add('')
    add("You built it. You connected it. Now let's see if it actually WORKS")
    add("like the real world.")
    add('')
    add('\u2501' * 60)
    add('')
    add('STEP 1: RUN THE SIMULATION')
    add('\u2022 Click the "Play" button in the TOP LEFT corner')
    add("\u2022 Watch the graph panel \u2014 you'll see percentage lines for each component")
    add('')
    add('STEP 2: OBSERVE THE BASELINE')
    add('\u2022 Let it run for about 30 time steps')
    add('\u2022 Notice how the lines relate to each other')

    # First external component observation
    if ext_names:
        add(f'\u2022 When {ext_names[0]} is HIGH, what happens to the internal components?')
    add('')

    # Scenario steps
    for i, (name, settings, prediction) in enumerate(L["sim_scenarios"]):
        step_num = i + 3
        add(f'STEP {step_num}: SCENARIO \u2014 {name.upper()}')
        add(f'\u2022 {settings}')
        add(f'\u2022 PREDICT FIRST: {prediction}')
        add('\u2022 Resume the simulation and observe what happens')
        add('\u2022 Was your prediction correct?')
        add('')

    add('\u2501' * 60)
    add('')
    add('WHAT DID YOU DISCOVER?')
    for disc in L["discoveries"]:
        add(f'\u2022 {disc}')
    add('')
    add(f'THE ANSWER: {L["answer"]}')
    add('```')
    add('')

    # Activity 3 Video Script
    add('### Video Script', '')
    add('```')
    add('"You\'ve built the machine. You\'ve wired the connections. Now let\'s')
    add("flip the switch and see if your model matches reality.")
    add('')
    add("Click the 'Play' button in the top left. Watch the graph panel \u2014")
    add("you'll see lines representing each component as a percentage.")
    add('')
    add("Let it run. Watch how the components interact at baseline levels.")
    add("Everything should be balanced, moving together.")
    add('')

    # Walk through scenarios
    s1 = L["sim_scenarios"][0]
    add(f"First scenario: {s1[0]}. {s1[1]}.")
    add(f"Watch the graph. What do you see happening?")
    add('')

    s2 = L["sim_scenarios"][1]
    add(f"Now let's push the system. Scenario two: {s2[0]}.")
    add(f"{s2[1]}.")
    add('')
    add(f"Before you run it \u2014 make a prediction. {s2[2]}")
    add('')
    add("Resume the simulation and watch what happens. Did your prediction")
    add("match the model? If not, that's actually a GOOD thing \u2014 it means")
    add("you learned something unexpected.")
    add('')

    if len(L["sim_scenarios"]) > 2:
        s3 = L["sim_scenarios"][2]
        add(f"One more scenario: {s3[0]}. {s3[1]}.")
        add(f"{s3[2]}")
        add('')

    add(f"Here's what our model reveals: {L['answer']}")
    add('')
    add("You just used a computational model to explain a real-world")
    add("phenomenon. That's what scientists do every day.")
    add('')
    add('Now it\'s your turn to ModelIt!"')
    add('```')
    add('')
    add('### Graph')
    add('[Screenshot showing simulation graph with scenario results \u2014 baseline vs. experimental conditions]')
    add('')
    add('---', '')

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # ACTIVITY 4: REVISE & EXTEND
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    add('## Activity 4: REVISE & EXTEND \u2014 Play, Research, Expand', '')
    add('### Text Editor', '')
    add('```')
    add("YOUR MODEL WORKS \u2014 BUT IT'S NOT COMPLETE")
    add('')
    add(f"You built a system model. It explains the basics. But real")
    add(f"systems involve WAY more factors.")
    add('')
    add("Time to play, explore, and make your model BETTER.")
    add('')
    add('\u2501' * 60)
    add('')
    add('PLAY TIME CHALLENGES:')
    add('')
    add('1. TELL THE STORY')
    add('   \u2022 Run your simulation')
    add('   \u2022 Pretend you\'re a scientist presenting your findings')
    add('   \u2022 Explain what\'s happening and WHY to your partner')
    add('')
    add('2. BREAK THE SYSTEM')
    for name, _, is_ext in L["components"]:
        if is_ext:
            add(f'   \u2022 What happens if you turn OFF {name}?')
    add('   \u2022 What happens if you change multiple variables at once?')
    add('   \u2022 Can you find a combination where the system stays stable?')
    add('')
    add("3. WHAT'S MISSING?")
    add('   Your model is simple. Real systems involve more. Think about:')
    add('')
    for name, desc in L["extend_components"]:
        add(f'   \u2022 {name} \u2014 {desc}')
    add('')
    add('\u2501' * 60)
    add('')
    add('RESEARCH DIRECTIONS:')
    add('')
    add("Don't just guess \u2014 find out! Here's what to look for:")
    add('')
    add('\U0001f4da IN YOUR TEXTBOOK:')
    for bg_title, _ in L["background_sections"][:2]:
        add(f'   \u2022 {bg_title} \u2014 how does this connect to your model?')
    add('')
    add('\U0001f50d QUESTIONS TO INVESTIGATE:')
    for refl in L["reflections"][:4]:
        add(f'   \u2022 {refl}')
    add('')
    add('\u2501' * 60)
    add('')
    add('ADD TO YOUR MODEL:')
    add('   \u2022 Pick ONE new component from your research')
    add('   \u2022 Decide: Is it INTERNAL or EXTERNAL?')
    add('   \u2022 Add it to your model (Plus button)')
    add('   \u2022 Connect it with relationships (+/\u2212)')
    add('   \u2022 Run the simulation \u2014 does it work like you expected?')
    add('')
    add('What story does your NEW model tell?')
    add('```')
    add('')

    # Activity 4 Video Script
    add('### Video Script', '')
    add('```')
    add('"Your model works. It showed us how the key components interact')
    add("and why things happen the way they do. But you and I both know")
    add("this isn't the whole story.")
    add('')
    add("Real systems are way more complicated. So now it's time to PLAY,")
    add("QUESTION, and EXPAND.")
    add('')
    add("First \u2014 tell the story. Run your simulation and pretend you're")
    add("a scientist presenting your findings at a conference. Explain")
    add("what's happening and WHY to someone next to you. If you can")
    add("explain it, you understand it.")
    add('')
    add("Second \u2014 break the system. Change the variables. Turn things")
    add("on and off. What combinations create extreme results? What")
    add("keeps things stable? This is where real insight happens.")
    add('')
    add("Third \u2014 and this is the big one \u2014 ask what's MISSING.")
    add('')
    add(f"Your model has {len(L['components'])} components. Real systems involve")
    add("way more. Think about...")
    add('')
    for name, desc in L["extend_components"]:
        add(f"{name}. {desc}")
        add("How would you model that?")
        add('')

    add("Here's your mission: Research ONE new factor. Find out how it")
    add("actually works in the real world. Then add it to your model.")
    add('')
    add("Is it internal or external? Click the plus button to add it.")
    add("Draw the connections. Set positive or negative. Run the simulation.")
    add('')
    add("Does your new model match reality better than before?")
    add('')
    add("This is how real scientists work. Start simple. Test it. Add")
    add("complexity. Test again. Your model is never 'done' \u2014 it's")
    add("always getting better.")
    add('')
    add("What story will YOUR expanded model tell?")
    add('')
    add('Now it\'s your turn to ModelIt!"')
    add('```')
    add('')
    add('### Activity Network')
    add('[Screenshot showing expanded model with 1-2 additional components added by student]')
    add('')
    add('---', '')

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # FUN FACT / CAREER CONNECTION
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    add('## Fun Fact (Career Connection)', '')
    add('```')
    add('\u2501' * 60)
    add('\U0001f52c CAREER CONNECTION')
    add('\u2501' * 60)
    add('')
    add(L["career"])
    add('')
    add("These professionals build models just like the one you made")
    add("today \u2014 understanding cause-and-effect relationships to solve")
    add("real-world problems. Your simple model? That's step one toward")
    add("this career.")
    add('')
    add('\u2501' * 60)
    add('```')
    add('')
    add('---', '')

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # TPT MATERIALS
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    add('## TPT Materials', '')

    # ---- PowerPoint Slides ----
    add('### PowerPoint Slides', '')
    add('```')
    for sg in L["slides_guide"]:
        add(f'{sg["num"].upper()}: {sg["title"].upper()}')
        add(f'Visual: {sg["visual"]}')
        add(f'Say: "{sg["say"]}"')
        add(f'Do: {sg["do"]}')
        add(f'Time: {sg["time"]}')
        add('')
    add('```')
    add('')

    # ---- Teacher Guide ----
    add('### Teacher Guide', '')
    add('```')
    add('\u2501' * 60)
    add(f'TEACHER GUIDE: {L["title"]}')
    add('\u2501' * 60)
    add('')

    add('LESSON PURPOSE:')
    add(f'{L["background_intro"]}')
    add('')

    add('NGSS ALIGNMENT:')
    add(f'{L["ngss"]}: {L["ngss_desc"]}')
    add('')

    add('THREE-DIMENSIONAL LEARNING:')
    for dim_type, dim_title, dim_desc in L["dimensions"]:
        add(f'\u2022 {dim_type}: {dim_title}')
        add(f'  {dim_desc}')
    add('')

    add('PACING GUIDE:')
    add('\u2022 Activity 1 (Locate): 8-10 minutes')
    add('\u2022 Activity 2 (Establish): 8-10 minutes')
    add('\u2022 Activity 3 (Visualize & Evaluate): 10-12 minutes')
    add('\u2022 Activity 4 (Revise & Extend): 10-15 minutes')
    add(f'\u2022 Total: {session_time} (or split across 2 class periods)')
    add('')

    add('PRE-LESSON PREP:')
    add('\u25a1 Test ModelIt access on student devices')
    add(f'\u25a1 Review vocabulary: {", ".join(t for t, _ in L["vocabulary"])}')
    add(f'\u25a1 Prepare {L["big_question"].rstrip("?")} discussion hook')
    add('\u25a1 Have images or video ready for phenomenon introduction')
    add('')

    add('LEVER FRAMEWORK:')
    add(f'\u2022 Locate: {L["lever_L"]}')
    add(f'\u2022 Establish: {L["lever_E"]}')
    add(f'\u2022 Visualize: {L["lever_V"]}')
    add(f'\u2022 Evaluate: {L["lever_Ev"]}')
    add(f'\u2022 Revise: {L["lever_R"]}')
    add('')

    add('BACKGROUND CONTENT:')
    for bg_title, bg_content in L["background_sections"]:
        add(f'\u2022 {bg_title}:')
        add(f'  {bg_content}')
        add('')

    add('COMMON MISCONCEPTIONS:')
    for misconception, reality, response in L["misconceptions"]:
        add(f'\u2022 "{misconception}"')
        add(f'  Reality: {reality}')
        add(f'  Strategy: {response}')
        add('')

    add('FACILITATION TIPS:')
    add("\u2022 Activity 1: Let students explore the interface. Don't over-explain.")
    add('  Let them discover. Circulate and support, don\'t lecture.')
    add('\u2022 Activity 2: Ask "When this goes up, what happens to that?" to')
    add('  guide positive/negative relationship decisions. Let students debate.')
    add('\u2022 Activity 3: Give time for students to "break" the model \u2014 turn')
    add("  things on/off and observe. This is where real insight happens.")
    add("\u2022 Activity 4: Don't give answers. Ask questions. Let curiosity drive")
    add("  the research. Celebrate when students' additions don't work as")
    add("  expected \u2014 that's authentic science.")
    add('')

    add('ANSWER KEY:')
    add(f'Big Question: {L["big_question"]}')
    add(f'Answer: {L["answer"]}')
    add('')
    add('Simulation Answers:')
    for scenario, answer in L["sim_answers"]:
        add(f'\u2022 {scenario}: {answer}')
    add('')
    add('Reflection Exemplars:')
    for q, a in L["reflection_exemplars"]:
        add(f'\u2022 Q: {q}')
        add(f'  A: {a}')
    add('')

    add('STEM CHALLENGE GUIDANCE:')
    add(f'Title: {L["stem_title"]}')
    add(f'Mission: {L["stem_mission"]}')
    add(f'Scenario: {L["stem_scenario"]}')
    add(f'Introduction: {L["stem_intro"]}')
    add('')
    add('Key Concepts:')
    for concept, explanation in L["stem_concepts"]:
        add(f'\u2022 {concept}: {explanation}')
    add('')
    add('Evaluation Rubric:')
    for level, criteria in L["stem_eval"]:
        add(f'\u2022 {level}: {criteria}')
    add('')

    add('DIFFERENTIATION:')
    add('Support (Struggling Learners):')
    for s in L["support"]:
        add(f'  \u2022 {s}')
    add('')
    add('Extensions (Advanced Learners):')
    for e in L["extensions"]:
        add(f'  \u2022 {e}')
    add('')
    add('Cross-Curricular Connections:')
    for subj, conn in L["cross_curr"]:
        add(f'  \u2022 {subj}: {conn}')
    add('')

    add('CAST ALIGNMENT:')
    for item in L["cast_items"]:
        add(f'\u2022 {item}')
    add('')
    add('CAST-Style Assessment Questions:')
    for q_type, question in L["cast_questions"]:
        add(f'\u2022 {q_type} {question}')
    add('')

    add('\u2501' * 60)
    add('```')
    add('')

    # ---- Activity Pack ----
    add('### Activity Pack', '')
    add('```')
    add('\u2501' * 60)
    add(f'STUDENT ACTIVITY PACK: {L["title"]}')
    add('\u2501' * 60)
    add('')
    add('NAME: _________________________ DATE: _____________')
    add('')

    # Pre-Assessment
    add('\u2501' * 60)
    add('PRE-ASSESSMENT')
    add('\u2501' * 60)
    add('')
    for i, q in enumerate(L["pre_assessment"], 1):
        add(f'{i}. {q}')
        add('')
        if "draw" in q.lower() or "sketch" in q.lower():
            add('   [DRAWING BOX]')
        else:
            add('   _________________________________________________________')
            add('')
            add('   _________________________________________________________')
        add('')

    # Vocabulary
    add('\u2501' * 60)
    add('VOCABULARY')
    add('\u2501' * 60)
    add('')
    add('Match the term to the definition:')
    add('')
    letters = "ABCDEFGH"
    for i, (term, _) in enumerate(L["vocabulary"]):
        add(f'___ {term:<30s}')
    add('')
    for i, (_, defn) in enumerate(L["vocabulary"]):
        add(f'{letters[i]}. {defn}')
    add('')

    # Model Planning Space
    add('\u2501' * 60)
    add('MODEL PLANNING SPACE')
    add('\u2501' * 60)
    add('')
    add('Before you build in ModelIt, sort your components here:')
    add('')
    add("EXTERNAL (can't control):")
    add('_______________ _______________ _______________')
    add('')
    add('INTERNAL (changes based on other things):')
    add('_______________ _______________ _______________')
    add('')
    add('Draw arrows showing relationships. Label each + or \u2212.')
    add('')
    add('[MODEL SKETCH BOX]')
    add('')

    # Simulation Observations
    add('\u2501' * 60)
    add('SIMULATION OBSERVATIONS')
    add('\u2501' * 60)
    add('')
    for name, settings, prediction in L["sim_scenarios"]:
        add(f'SCENARIO: {name}')
        add(f'Settings: {settings}')
        add(f'My prediction: ________________________________________________')
        add('')
        add(f'What actually happened: ________________________________________')
        add('')
        add(f'________________________________________')
        add('')

    add('The KEY discovery from my simulation is:')
    add('')
    add('_________________________________________________________')
    add('')
    add('_________________________________________________________')
    add('')

    # Research & Extend
    add('\u2501' * 60)
    add('RESEARCH & EXTEND')
    add('\u2501' * 60)
    add('')
    add('NEW COMPONENT I want to add: _____________________________')
    add('')
    add('Is it EXTERNAL or INTERNAL? (circle one)')
    add('')
    add('What does it connect to? _________________________________')
    add('')
    add('Is the relationship POSITIVE or NEGATIVE? _________________')
    add('')
    add('Why? ____________________________________________________')
    add('')
    add('_________________________________________________________')
    add('')
    add('After adding it, my simulation showed:')
    add('')
    add('_________________________________________________________')
    add('')
    add('_________________________________________________________')
    add('')

    # Reflection
    add('\u2501' * 60)
    add('REFLECTION')
    add('\u2501' * 60)
    add('')
    for i, refl in enumerate(L["reflections"], 1):
        add(f'{i}. {refl}')
        add('')
        add('   _________________________________________________________')
        add('')
        add('   _________________________________________________________')
        add('')

    # Post-Assessment
    add('\u2501' * 60)
    add('POST-ASSESSMENT')
    add('\u2501' * 60)
    add('')
    add(f'1. {L["big_question"]} Explain using evidence from your model:')
    add('')
    add('   _________________________________________________________')
    add('')
    add('   _________________________________________________________')
    add('')
    add('   _________________________________________________________')
    add('')
    add(f'2. Which NGSS dimensions did this lesson address?')
    add('   (Check all that apply)')
    for dim_type, dim_title, _ in L["dimensions"]:
        add(f'   \u25a1 {dim_type}: {dim_title}')
    add('')
    add(f'3. {L["reflections"][-1]}')
    add('')
    add('   _________________________________________________________')
    add('')
    add('   _________________________________________________________')
    add('')

    # STEM Challenge
    add('\u2501' * 60)
    add(f'STEM CHALLENGE: {L["stem_title"]}')
    add('\u2501' * 60)
    add('')
    add(f'MISSION: {L["stem_mission"]}')
    add('')
    add(f'SCENARIO: {L["stem_scenario"]}')
    add('')
    add('GUIDING QUESTIONS:')
    for q in L["stem_questions"]:
        add(f'\u2022 {q}')
    add('')
    add('DESIGN THINKING:')
    for q in L["stem_design_qs"]:
        add(f'\u2022 {q}')
        add('')
        add('  _________________________________________________________')
        add('')
    add('')

    # Rubric
    add('EVALUATION RUBRIC:')
    for level, criteria in L["stem_eval"]:
        add(f'\u2022 {level}: {criteria}')
    add('')

    add('\u2501' * 60)
    add('```')
    add('')
    add('---', '')

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # RESOURCES
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    add('## Resources', '')
    add('| Resource | Link |')
    add('|----------|------|')
    grade_folder = f'grade-{L["id"][1:3]}'
    add(f'| Activity Pack (DOCX) | [materials/{grade_folder}/{L["id"]}/{L["id"]}-Student-Activity-Pack.docx] |')
    add(f'| Teacher Guide (DOCX) | [materials/{grade_folder}/{L["id"]}/{L["id"]}-Teachers-Guide.docx] |')
    add(f'| PPT Presentation | [materials/{grade_folder}/{L["id"]}/{L["id"]}-Student-Presentation.pptx] |')
    add('| Platform Link | [ModelIt lesson link] |')
    add('')
    add('---', '')

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # LESSON METADATA
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    add('## Lesson Metadata', '')
    add('| Field | Value |')
    add('|-------|-------|')
    add('| Created | February 2026 |')
    add("| Author | Alexandria's Design |")
    add('| Template Version | 1.0 |')
    add('| Platform | ModelIt (formerly Cell Collective) |')
    add(f'| Estimated Time | {session_time} |')
    add('| Can Split Across | 2 class periods |')

    return '\n'.join(lines)


def main():
    """Generate all lesson markdown files."""
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'lessons')
    os.makedirs(out_dir, exist_ok=True)

    # Determine which grades to generate
    grades_to_gen = sys.argv[1:] if len(sys.argv) > 1 else ["G06", "G08"]

    all_lessons = []
    if "G06" in grades_to_gen:
        all_lessons.extend(G06_LESSONS)
    if "G08" in grades_to_gen:
        all_lessons.extend(G08_LESSONS)

    if not all_lessons:
        print("No lessons to generate. Use: python generate_lesson_markdown.py [G06] [G08]")
        return

    print(f"Generating {len(all_lessons)} lesson markdown files...\n")

    for lesson in all_lessons:
        slug = slugify(lesson["title"])
        filename = f'{lesson["id"]}-{slug}.md'
        filepath = os.path.join(out_dir, filename)

        md_content = generate_markdown(lesson)
        line_count = md_content.count('\n') + 1

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(md_content)

        print(f'  [OK] {filename} ({line_count} lines)')

    print(f'\n{"=" * 50}')
    print(f'Generated {len(all_lessons)} lesson markdown files in lessons/')
    print(f'{"=" * 50}')


if __name__ == '__main__':
    main()
