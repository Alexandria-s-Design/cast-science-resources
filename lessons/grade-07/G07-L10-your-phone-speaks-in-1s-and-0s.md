# Lesson: Your Phone Speaks in 1s and 0s

## Header Information

| Field | Value |
|-------|-------|
| **Lesson ID** | G07-L10 |
| **Grade** | 7th |
| **Lesson Name** | Your Phone Speaks in 1s and 0s |
| **Status** | Template |

---

## Platform

### Title
**Your Phone Speaks in 1s and 0s — How Digital Signals Carry Music, Messages, and Memes**

### Overview
We live in a digital world, but the sounds, images, and experiences we want to capture are analog. This lesson explores how we bridge that gap — converting continuous analog signals into discrete digital ones — and why that conversion involves fundamental trade-offs between quality and practicality. Students investigate the driving question: Why does your music sound perfect every time you play it — but your grandparents' vinyl records got scratchy? Using the LEVER framework, students identify key components, establish cause-and-effect relationships, run simulations to test scenarios, and extend their understanding through research and engineering challenges.

### Cover Image
[teenager wearing headphones with visible digital sound wave visualizations flowing from phone to headphones, showing binary 1s and 0s embedded in the sound waves, modern urban setting, dramatic lighting]

### Grade
7th

### NGSS Standard
**MS-PS4-3**: Integrate qualitative scientific and technical information to support the claim that digitized signals are a more reliable way to encode and transmit information than analog signals.

### Learning Objectives
- Compare how analog and digital signals encode information
- Explain how sampling rate affects digital signal quality
- Model how compression reduces file size while trading off accuracy
- Evaluate why digital signals are more reliable for transmitting information

### Component List (Starting Model: 3-4 Components)

| Component | Type | What It Represents |
|-----------|------|-------------------|
| Sampling Rate | External | How many times per second the analog signal is measured and converted to digital values. Higher rates capture more detail. |
| Compression Level | External | How aggressively the digital file is reduced in size. Higher compression removes more data to save space. |
| Signal Accuracy | Internal | How faithfully the digital version reproduces the original analog signal. Measured by comparing digital output to original. |
| File Size | Internal | The amount of digital storage space required. Smaller files are easier to transmit but may sacrifice quality. |

### Research for Lesson
- Analog vs. Digital: The Fundamental Difference — reference materials and textbook resources
- Sampling and the Nyquist Theorem — reference materials and textbook resources
- Compression: Lossy vs. Lossless — reference materials and textbook resources
- Why Digital Wins for Reliability — reference materials and textbook resources

---

## Activity 1: LOCATE — Build Your System

### Text Editor

```
YOUR PHONE SPEAKS IN 1S AND 0S

How Digital Signals Carry Music, Messages, and Memes.
Why does your music sound perfect every time you play it — but your grandparents' vinyl records got scratchy?

That's not just a question — it's something you can MODEL.
And you're about to build exactly that.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1: CHOOSE YOUR COMPONENTS
• Look at the component panel on the RIGHT side of your screen
• Find the EXTERNAL components (things we can't control):
  ○ Click "Sampling Rate" — how many times per second the analog signal is measured and converted to digital values
  ○ Click "Compression Level" — how aggressively the digital file is reduced in size
• Find the INTERNAL components (things that change because of other things):
  ○ Click "Signal Accuracy" — how faithfully the digital version reproduces the original analog signal
  ○ Click "File Size" — the amount of digital storage space required

STEP 2: ADD TO YOUR MODEL
• Click the PLUS (+) button to add each component to your picture
• You should now see 4 components on your canvas

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
"Why does your music sound perfect every time you play it — but your grandparents' vinyl records got scratchy?

That's what we're going to figure out today. Not by reading about
it — by MODELING it. You're going to build a system that shows
exactly how this works.

Let's build our system. Look at the component panel on the right
side of your screen. You'll see two types of components:

EXTERNAL components — things that come from outside the system.
Inputs we can't directly control.

INTERNAL components — things that change BECAUSE of other things
in the system. They respond to the externals.

Click on 'Sampling Rate' — that's external. How many times per second the analog signal is measured and converted to digital values.
Click on 'Compression Level' — that's external. How aggressively the digital file is reduced in size.
Click on 'Signal Accuracy' — that's internal. How faithfully the digital version reproduces the original analog signal.
Click on 'File Size' — that's internal. The amount of digital storage space required.

Now you need to SORT them. Which ones are external — things that
come from outside the system? Which ones are internal — things
that change because of what's happening inside?

Sampling Rate and Compression Level are external because they are engineering choices — humans decide how many samples to take and how much to compress. Signal Accuracy and File Size are internal because they are outcomes determined by those engineering choices.

Sort your components, then hit the PLUS button to add each one
to your model canvas.

You've got your pieces. But right now they're just sitting there,
not connected. In the next activity, we'll draw the invisible
lines that show how everything affects everything else.

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing 4 components sorted: Sampling Rate, Compression Level (External), Signal Accuracy, File Size (Internal)]

### Graph
[Empty graph panel — no simulation yet]

---

## Activity 2: ESTABLISH — Connect the Relationships

### Text Editor

```
TIME TO DRAW THE INVISIBLE LINES

Those 4 components don't just sit there — they AFFECT each other.
When one changes, others change too. Let's map those connections.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1: OPEN CONNECTION MODE
• Click the "Connect" icon in the TOP LEFT corner of your screen
• Your cursor is now ready to draw relationship arrows

STEP 2: DRAW YOUR RELATIONSHIPS
• Click on "Sampling Rate" and drag an arrow to "Signal Accuracy"
• Click on "Compression Level" and drag an arrow to "File Size"
• Click on "Compression Level" and drag an arrow to "Signal Accuracy"

STEP 3: SET POSITIVE OR NEGATIVE
• Look at the +/− toggle in the TOP LEFT corner
• For each connection, ask: "When this goes UP, does the other go UP or DOWN?"

  ○ Sampling Rate → Signal Accuracy = POSITIVE (+)
    Higher sampling rates capture more detail from the original analog signal, producing a more accurate digital representation. Doubling the sampling rate roughly doubles the frequency range that can be faithfully reproduced.

  ○ Compression Level → File Size = NEGATIVE (−)
    Higher compression reduces file size — that's the whole point. Aggressive compression can shrink a 30 MB song to 3 MB, but at the cost of permanently removing audio data.

  ○ Compression Level → Signal Accuracy = NEGATIVE (−)
    Higher compression removes more data from the digital file, reducing how accurately it represents the original signal. At extreme compression, the quality loss becomes audible — thin sound, artifacts, and missing detail.

STEP 4: CHECK YOUR MODEL
• You should have 3 arrows total
• 2 negative relationship(s), 1 positive relationship(s)
• This is your system model!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THINK ABOUT IT: When you download a song, you're choosing between file size and sound quality. What happens to the music when compression is pushed too far?
```

### Video Script

```
"Your pieces are on the board, but they're not talking to each
other yet. Time to draw the invisible lines — the relationships
that make this a SYSTEM, not just a pile of parts.

Click the 'Connect' icon in the top left corner. Now you're in
connection mode.

First connection: Click on 'Sampling Rate' and drag an arrow
over to 'Signal Accuracy.'

Here's the key question: When sampling rate goes UP, does
signal accuracy go UP or DOWN?

Higher sampling rates capture more detail from the original analog signal, producing a more accurate digital representation. Doubling the sampling rate roughly doubles the frequency range that can be faithfully reproduced.
That's a POSITIVE relationship. They move in the same
direction. Click the plus sign.

Next connection: Click on 'Compression Level' and drag an arrow
over to 'File Size.'

Here's the key question: When compression level goes UP, does
file size go UP or DOWN?

Higher compression reduces file size — that's the whole point. Aggressive compression can shrink a 30 MB song to 3 MB, but at the cost of permanently removing audio data.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Last connection: Click on 'Compression Level' and drag an arrow
over to 'Signal Accuracy.'

Here's the key question: When compression level goes UP, does
signal accuracy go UP or DOWN?

Higher compression removes more data from the digital file, reducing how accurately it represents the original signal. At extreme compression, the quality loss becomes audible — thin sound, artifacts, and missing detail.
That's a NEGATIVE relationship. When one goes up, the other
goes DOWN. Click the minus sign.

Look at your model now. You've got 2 negative and 1
positive relationships. 3 arrows total.

When you download a song, you're choosing between file size and sound quality. What happens to the music when compression is pushed too far?

Now it's your turn to ModelIt!"
```

### Image
[Screenshot showing connected model with arrows: Sampling Rate +→ Signal Accuracy, Compression Level −→ File Size, Compression Level −→ Signal Accuracy]

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
• When Sampling Rate is HIGH, what happens to the internal components?

STEP 3: SCENARIO — STUDIO QUALITY
• Sampling Rate: HIGH | Compression Level: LOW
• PREDICT FIRST: What will Signal Accuracy and File Size look like with maximum quality settings?
• Resume the simulation and observe what happens
• Was your prediction correct?

STEP 4: SCENARIO — PHONE STREAMING
• Sampling Rate: MEDIUM | Compression Level: MEDIUM
• PREDICT FIRST: How does moderate compression affect quality? Is the trade-off worth it?
• Resume the simulation and observe what happens
• Was your prediction correct?

STEP 5: SCENARIO — EXTREME COMPRESSION
• Sampling Rate: MEDIUM | Compression Level: HIGH
• PREDICT FIRST: At what point does compression destroy so much information that quality becomes unacceptable?
• Resume the simulation and observe what happens
• Was your prediction correct?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT DID YOU DISCOVER?
• Higher sampling rates produce more accurate digital copies but create larger files
• Moderate compression reduces file size significantly with barely noticeable quality loss
• Extreme compression destroys enough data that quality drops dramatically — you can hear the difference
• Digital signals can be copied perfectly (unlike analog), making them ideal for storage and transmission

THE ANSWER: Digital signals encode information as exact numbers (1s and 0s) that can be copied perfectly every time. Your grandparents' vinyl records were analog — each play physically wore the grooves, adding scratches and noise. A digital music file sounds identical on its millionth play because the 1s and 0s never change. The trade-off is that converting analog to digital requires choosing a sampling rate (detail level) and compression level (file size), which affects how closely the digital version matches the original.
```

### Video Script

```
"You've built the machine. You've wired the connections. Now let's
flip the switch and see if your model matches reality.

Click the 'Play' button in the top left. Watch the graph panel —
you'll see lines representing each component as a percentage.

Let it run. Watch how the components interact at baseline levels.
Everything should be balanced, moving together.

First scenario: Studio Quality. Sampling Rate: HIGH | Compression Level: LOW.
Watch the graph. What do you see happening?

Now let's push the system. Scenario two: Phone Streaming.
Sampling Rate: MEDIUM | Compression Level: MEDIUM.

Before you run it — make a prediction. How does moderate compression affect quality? Is the trade-off worth it?

Resume the simulation and watch what happens. Did your prediction
match the model? If not, that's actually a GOOD thing — it means
you learned something unexpected.

One more scenario: Extreme Compression. Sampling Rate: MEDIUM | Compression Level: HIGH.
At what point does compression destroy so much information that quality becomes unacceptable?

Here's what our model reveals: Digital signals encode information as exact numbers (1s and 0s) that can be copied perfectly every time. Your grandparents' vinyl records were analog — each play physically wore the grooves, adding scratches and noise. A digital music file sounds identical on its millionth play because the 1s and 0s never change. The trade-off is that converting analog to digital requires choosing a sampling rate (detail level) and compression level (file size), which affects how closely the digital version matches the original.

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
   • What happens if you turn OFF Sampling Rate?
   • What happens if you turn OFF Compression Level?
   • What happens if you change multiple variables at once?
   • Can you find a combination where the system stays stable?

3. WHAT'S MISSING?
   Your model is simple. Real systems involve more. Think about:

   • Bit Depth — The number of possible values for each sample. Higher bit depth captures more subtle volume differences, like the difference between a whisper and a shout.
   • Transmission Speed — How quickly data can be sent from server to device. Faster connections allow higher quality streaming without buffering.
   • Error Correction — Digital systems can detect and fix errors during transmission. This is why digital signals are more reliable than analog — damaged bits can be reconstructed.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RESEARCH DIRECTIONS:

Don't just guess — find out! Here's what to look for:

📚 IN YOUR TEXTBOOK:
   • Analog vs. Digital: The Fundamental Difference — how does this connect to your model?
   • Sampling and the Nyquist Theorem — how does this connect to your model?

🔍 QUESTIONS TO INVESTIGATE:
   • Why are digital signals considered more reliable than analog signals for storing and transmitting information?
   • What trade-offs do engineers make when choosing sampling rate and compression settings?
   • How does the concept of sampling rate connect to the quality of digital music?
   • Why might a musician prefer vinyl (analog) even though digital is technically more reliable?

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

Your model has 4 components. Real systems involve
way more. Think about...

Bit Depth. The number of possible values for each sample. Higher bit depth captures more subtle volume differences, like the difference between a whisper and a shout.
How would you model that?

Transmission Speed. How quickly data can be sent from server to device. Faster connections allow higher quality streaming without buffering.
How would you model that?

Error Correction. Digital systems can detect and fix errors during transmission. This is why digital signals are more reliable than analog — damaged bits can be reconstructed.
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

Audio Engineers use signal processing to record, mix, and master music. They understand sampling rates, compression, and digital audio workstations (DAWs). They work in recording studios, live concerts, film production, and video game audio — combining physics, math, and creativity.

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
Visual: Title slide with digital waveform imagery
Say: "Every text, every song, every TikTok you've ever seen traveled as 1s and 0s. How does THAT work?"
Do: Play the same song on vinyl (scratchy) and digital (clean). Ask: Why the difference?
Time: 2 min

SLIDE 2: LEARNING OBJECTIVES
Visual: Learning goals and vocabulary
Say: "Today we're investigating how your phone turns sound waves into numbers — and back again."
Do: Have students read objectives. Pre-teach 'sampling rate' with a visual.
Time: 3 min

SLIDE 3: BIG QUESTION
Visual: Vinyl record vs. digital waveform
Say: "Your grandparents' records got scratchy. Your digital music sounds perfect every time. Why?"
Do: Show vinyl groove under microscope vs. binary data. Discuss physical vs. numerical storage.
Time: 3 min

SLIDE 4: LEVER FRAMEWORK
Visual: LEVER steps overview
Say: "We'll model how digital encoding works — and find the trade-offs engineers face every day."
Do: Preview LEVER steps.
Time: 2 min

SLIDE 5: ACTIVITY 1: COMPONENTS
Visual: Component cards for signal model
Say: "What do engineers CONTROL when digitizing sound? What CHANGES as a result?"
Do: Guide sorting. Discuss why sampling rate is a choice, not a result.
Time: 8 min

SLIDE 6: ACTIVITY 2: CONNECTIONS
Visual: Relationship arrows
Say: "More samples per second means better quality. But more compression means... what?"
Do: Reveal the compression trade-off: smaller files but lower accuracy.
Time: 8 min

SLIDE 7: ACTIVITY 3: SIMULATION
Visual: Quality comparison graphs
Say: "Let's compare: studio quality vs. phone streaming vs. extreme compression. Can you hear the difference?"
Do: Students predict quality-vs-size outcomes. Compare simulation results.
Time: 10 min

SLIDE 8: DISCOVERIES
Visual: Key findings and comparisons
Say: "So why did we switch from analog to digital? What does our model tell us?"
Do: Compare analog degradation (copies of copies) vs. digital perfection.
Time: 5 min

SLIDE 9: STEM CHALLENGE
Visual: Streaming service design
Say: "Design a streaming service that sounds great on Wi-Fi AND doesn't burn through mobile data."
Do: Groups design adaptive quality systems. Present trade-off decisions.
Time: 12 min

```

### Teacher Guide

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TEACHER GUIDE: Your Phone Speaks in 1s and 0s
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LESSON PURPOSE:
We live in a digital world, but the sounds, images, and experiences we want to capture are analog. This lesson explores how we bridge that gap — converting continuous analog signals into discrete digital ones — and why that conversion involves fundamental trade-offs between quality and practicality.

NGSS ALIGNMENT:
MS-PS4-3: Integrate qualitative scientific and technical information to support the claim that digitized signals are a more reliable way to encode and transmit information than analog signals.

THREE-DIMENSIONAL LEARNING:
• SEP: Obtaining, Evaluating, and Communicating Information
  Students integrate qualitative scientific and technical information from multiple sources to compare analog and digital signal reliability.
• DCI: PS4.C: Information Technologies and Instrumentation
  Digitized signals (sent as wave pulses) are a more reliable way to encode and transmit information because they can be exactly copied.
• CCC: Structure and Function
  The structure of digital encoding (discrete binary values) gives it the function of perfect reproducibility, while analog's continuous structure makes it susceptible to degradation.

PACING GUIDE:
• Activity 1 (Locate): 8-10 minutes
• Activity 2 (Establish): 8-10 minutes
• Activity 3 (Visualize & Evaluate): 10-12 minutes
• Activity 4 (Revise & Extend): 10-15 minutes
• Total: 45-60 minutes (or split across 2 class periods)

PRE-LESSON PREP:
□ Test ModelIt access on student devices
□ Review vocabulary: Analog Signal, Digital Signal, Sampling Rate, Compression
□ Prepare Why does your music sound perfect every time you play it — but your grandparents' vinyl records got scratchy discussion hook
□ Have images or video ready for phenomenon introduction

LEVER FRAMEWORK:
• Locate: Students identify sampling rate, compression level, signal accuracy, and file size as components of the digital signal system.
• Establish: Students discover that sampling rate positively affects accuracy while compression creates a trade-off between file size and quality.
• Visualize: Students build a model showing how analog signals are converted to digital and how settings affect the output.
• Evaluate: Students run studio quality, streaming, and extreme compression scenarios to compare quality-vs-size trade-offs.
• Revise: Students add bit depth or error correction to explore more nuanced digital signal behavior.

BACKGROUND CONTENT:
• Analog vs. Digital: The Fundamental Difference:
  Analog signals are continuous — they vary smoothly over time, like the air pressure changes that make up sound waves. A vinyl record stores sound as a continuous groove that physically mirrors the sound wave. Digital signals break this continuous information into discrete steps: measurements taken at regular intervals, each stored as a number. CDs sample sound 44,100 times per second, storing each measurement as a number with 65,536 possible values (16-bit depth).

• Sampling and the Nyquist Theorem:
  The key insight of digital audio is the Nyquist-Shannon sampling theorem: to accurately capture a signal, you must sample at least twice as fast as the highest frequency you want to preserve. Human hearing ranges from 20 Hz to 20,000 Hz, which is why CD-quality audio samples at 44,100 Hz (just over 2× the maximum). Sample below this rate and high frequencies get distorted — a phenomenon called 'aliasing.'

• Compression: Lossy vs. Lossless:
  Raw digital audio creates enormous files (a 3-minute song at CD quality is about 30 MB). Compression algorithms reduce this. Lossless compression (FLAC, ALAC) is like a zip file — it compresses without losing any data, achieving about 50% size reduction. Lossy compression (MP3, AAC) permanently removes data that psychoacoustic models predict humans won't notice, achieving 75-90% size reduction. The trade-off: lossy files are much smaller but can never be restored to full quality.

• Why Digital Wins for Reliability:
  The killer advantage of digital signals is perfect copyability. An analog signal degrades every time it's copied — like photocopying a photocopy, each generation gets worse. A digital signal is just numbers, and numbers can be copied exactly. Digital systems also include error correction: extra data that lets the receiver detect and fix transmission errors. This is why a scratched CD can still play (up to a point) while a scratched vinyl record pops and clicks permanently.

COMMON MISCONCEPTIONS:
• "Digital is always better than analog"
  Reality: Digital is more RELIABLE (perfect copies, no degradation) but not necessarily 'better' in every way. Analog vinyl records capture a continuous signal with theoretically infinite resolution. Some audiophiles prefer vinyl's 'warmer' sound. The advantage of digital is consistency and copyability, not inherent superiority in every dimension.
  Strategy: Ask: What does 'better' mean? Better for what purpose? A vinyl record in a quiet room might sound richer than a compressed MP3 on cheap earbuds. Context matters.

• "Higher numbers always mean better quality"
  Reality: More sampling rate and less compression generally improve quality, but there are limits. Sampling above 96,000 Hz captures frequencies humans can't hear — it's wasted data. Similarly, 24-bit audio captures volume differences too subtle for human ears. 'Better' numbers only matter up to the limits of human perception.
  Strategy: Ask: If you can't hear frequencies above 20,000 Hz, what's the point of sampling at 192,000 Hz? Engineers design for HUMAN listeners, not theoretical perfection.

• "Compressed files are missing most of their data"
  Reality: A 128 kbps MP3 is about 1/10th the size of a CD-quality WAV file, but it doesn't sound 1/10th as good. Compression algorithms are smart — they remove data that psychoacoustic research shows humans won't notice (frequencies masked by louder sounds, details below the threshold of perception). Most people can't distinguish 256 kbps AAC from uncompressed audio in blind tests.
  Strategy: Play a blind test: same song at 256 kbps AAC and uncompressed WAV. Most students won't hear a difference, proving that smart compression keeps what matters.

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
Big Question: Why does your music sound perfect every time you play it — but your grandparents' vinyl records got scratchy?
Answer: Digital signals encode information as exact numbers (1s and 0s) that can be copied perfectly every time. Your grandparents' vinyl records were analog — each play physically wore the grooves, adding scratches and noise. A digital music file sounds identical on its millionth play because the 1s and 0s never change. The trade-off is that converting analog to digital requires choosing a sampling rate (detail level) and compression level (file size), which affects how closely the digital version matches the original.

Simulation Answers:
• Studio Quality Scenario: With maximum Sampling Rate and minimum Compression Level, Signal Accuracy is at its highest — the digital version closely matches the original analog signal. But File Size is enormous. A single album might take several gigabytes. This is ideal for professional studios but impractical for streaming on mobile devices.
• Extreme Compression Scenario: With maximum Compression Level, File Size drops dramatically — great for limited data plans. But Signal Accuracy plummets. The compression algorithm removes so much data that audible artifacts appear: the music sounds 'thin,' 'watery,' or 'metallic.' This demonstrates why engineers must balance quality against practicality.

Reflection Exemplars:
• Q: Why are digital signals more reliable than analog?
  A: Digital signals encode information as exact numbers (binary: 1s and 0s). These numbers can be copied perfectly — the millionth copy is identical to the first. Analog signals are physical patterns (grooves, magnetic fields) that degrade with each copy or playback. Digital systems also include error correction: extra data that detects and fixes transmission errors. This is why a digital photo shared a million times looks the same, while a photocopy of a photocopy gets blurry.
• Q: What trade-offs do engineers face with sampling and compression?
  A: Higher sampling rates capture more detail but create larger files. More compression shrinks files but reduces quality. Engineers must balance these based on the use case: a surgeon viewing an MRI needs maximum accuracy (no compression), while a teenager streaming music on a bus needs small files (moderate compression is fine because human ears can't detect the missing data in most cases). The 'right' setting depends entirely on the purpose.

STEM CHALLENGE GUIDANCE:
Title: The Streaming Service Challenge
Mission: Design a music streaming service that delivers the best possible sound quality while keeping data usage low enough for mobile users.
Scenario: Your startup is launching a music streaming app. Users on Wi-Fi want studio quality, but mobile users have limited data plans. You need to design a system that automatically adjusts quality based on connection type — without making the music sound terrible.
Introduction: A new music streaming startup needs to compete with Spotify and Apple Music. The key engineering challenge: deliver the best possible sound quality while keeping data usage low enough for users with limited mobile data plans.

Key Concepts:
• Adaptive Bitrate Streaming: Technology that automatically adjusts audio quality based on network conditions. When on fast Wi-Fi, it streams high quality. When on slow mobile data, it reduces quality to prevent buffering.
• Psychoacoustic Modeling: The science of what sounds humans can and cannot hear. Compression algorithms use this to remove frequencies and details that most people won't notice, achieving smaller files with minimal perceived quality loss.
• Codec: Short for coder-decoder. Software that encodes analog audio into digital format and decodes it back for playback. Different codecs (MP3, AAC, Opus) use different algorithms with different quality-to-size ratios.

Evaluation Rubric:
• Expert (4): Design includes adaptive quality settings for different connections, references model evidence for quality thresholds, addresses user experience and data constraints
• Proficient (3): Design specifies different quality levels with clear trade-off reasoning supported by model data
• Developing (2): Design addresses quality or file size but doesn't effectively balance both trade-offs
• Beginning (1): Design is incomplete or doesn't connect to digital signal concepts from the lesson

DIFFERENTIATION:
Support (Struggling Learners):
  • Use a visual 'pixel grid' analogy: show how a photo looks at 10×10 pixels vs. 100×100 vs. 1000×1000 to make sampling rate concrete
  • Provide pre-made comparison audio clips at different compression levels so students can hear the difference
  • Sentence frames: 'When sampling rate increases, signal accuracy __ because __, but file size __ because __'

Extensions (Advanced Learners):
  • Research how streaming services like Spotify decide what quality to use — investigate their adaptive bitrate algorithms
  • Compare the same song as WAV (uncompressed), FLAC (lossless), MP3 320kbps, and MP3 128kbps using waveform analysis software
  • Investigate how digital signals enable error correction — how can a scratched CD still play while a scratched vinyl can't?

Cross-Curricular Connections:
  • Math: Calculate file sizes: a 3-minute song at 44,100 Hz × 16-bit × 2 channels = ? bytes. Then calculate compression ratios for MP3 vs. FLAC.
  • ELA: Write a consumer guide explaining to non-technical users what audio quality settings mean and helping them choose the right ones.
  • Social Studies: Research how the shift from physical media (vinyl, CDs) to digital streaming changed the music industry's economics and artist compensation.

CAST ALIGNMENT:
• Model the relationship between sampling rate, compression, and signal fidelity
• Compare analog and digital signal behavior under different transmission conditions
• Evaluate engineering trade-offs in real-world digital communication systems

CAST-Style Assessment Questions:
• Evaluate: A podcast is recorded at 44,100 Hz sampling rate and compressed to MP3 at 128 kbps. A listener complains the audio sounds 'thin.' Using your model, explain what's happening and propose a solution.
• Compare: Your model shows that increasing sampling rate improves signal accuracy. Why don't we just set sampling rate to maximum for everything? Use evidence from your simulation to explain the trade-off.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Activity Pack

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STUDENT ACTIVITY PACK: Your Phone Speaks in 1s and 0s
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NAME: _________________________ DATE: _____________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRE-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. What is the difference between an analog signal and a digital signal? Give an example of each.

   _________________________________________________________

   _________________________________________________________

2. Why might a digital copy of a song sound different from the original live performance?

   _________________________________________________________

   _________________________________________________________

3. What does 'compression' mean when talking about digital files like MP3s?

   _________________________________________________________

   _________________________________________________________

4. Why do some music files take up more storage space than others?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VOCABULARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Match the term to the definition:

___ Analog Signal                 
___ Digital Signal                
___ Sampling Rate                 
___ Compression                   

A. A continuous signal that varies smoothly over time, like a sound wave or vinyl record groove
B. Information encoded as discrete values — typically 1s and 0s (binary) — that can be exactly copied
C. How many times per second an analog signal is measured to create a digital version (measured in Hz)
D. Reducing file size by removing some data — lossy compression removes data permanently, lossless preserves everything

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

SCENARIO: Studio Quality
Settings: Sampling Rate: HIGH | Compression Level: LOW
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Phone Streaming
Settings: Sampling Rate: MEDIUM | Compression Level: MEDIUM
My prediction: ________________________________________________

What actually happened: ________________________________________

________________________________________

SCENARIO: Extreme Compression
Settings: Sampling Rate: MEDIUM | Compression Level: HIGH
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

1. Why are digital signals considered more reliable than analog signals for storing and transmitting information?

   _________________________________________________________

   _________________________________________________________

2. What trade-offs do engineers make when choosing sampling rate and compression settings?

   _________________________________________________________

   _________________________________________________________

3. How does the concept of sampling rate connect to the quality of digital music?

   _________________________________________________________

   _________________________________________________________

4. Why might a musician prefer vinyl (analog) even though digital is technically more reliable?

   _________________________________________________________

   _________________________________________________________

5. How has the shift from analog to digital changed how we consume music, movies, and information?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
POST-ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Why does your music sound perfect every time you play it — but your grandparents' vinyl records got scratchy? Explain using evidence from your model:

   _________________________________________________________

   _________________________________________________________

   _________________________________________________________

2. Which NGSS dimensions did this lesson address?
   (Check all that apply)
   □ SEP: Obtaining, Evaluating, and Communicating Information
   □ DCI: PS4.C: Information Technologies and Instrumentation
   □ CCC: Structure and Function

3. How has the shift from analog to digital changed how we consume music, movies, and information?

   _________________________________________________________

   _________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEM CHALLENGE: The Streaming Service Challenge
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MISSION: Design a music streaming service that delivers the best possible sound quality while keeping data usage low enough for mobile users.

SCENARIO: Your startup is launching a music streaming app. Users on Wi-Fi want studio quality, but mobile users have limited data plans. You need to design a system that automatically adjusts quality based on connection type — without making the music sound terrible.

GUIDING QUESTIONS:
• What sampling rate and compression settings should you use for Wi-Fi vs. mobile data?
• How do you decide the minimum acceptable quality before users notice degradation?
• What other factors besides sound quality matter to your streaming service users?

DESIGN THINKING:
• What criteria define 'good enough' quality for mobile streaming?

  _________________________________________________________

• How will your system detect and adapt to different connection speeds?

  _________________________________________________________

• What happens when a user switches from Wi-Fi to mobile mid-song?

  _________________________________________________________

• How can you test whether users can actually hear the difference between quality levels?

  _________________________________________________________


EVALUATION RUBRIC:
• Expert (4): Design includes adaptive quality settings for different connections, references model evidence for quality thresholds, addresses user experience and data constraints
• Proficient (3): Design specifies different quality levels with clear trade-off reasoning supported by model data
• Developing (2): Design addresses quality or file size but doesn't effectively balance both trade-offs
• Beginning (1): Design is incomplete or doesn't connect to digital signal concepts from the lesson

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Resources

| Resource | Link |
|----------|------|
| Activity Pack (DOCX) | [materials/grade-07/G07-L10/G07-L10-Student-Activity-Pack.docx] |
| Teacher Guide (DOCX) | [materials/grade-07/G07-L10/G07-L10-Teachers-Guide.docx] |
| PPT Presentation | [materials/grade-07/G07-L10/G07-L10-Student-Presentation.pptx] |
| Platform Link | [ModelIt lesson link] |

---

## Lesson Metadata

| Field | Value |
|-------|-------|
| Created | February 2026 |
| Author | Alexandria's Design |
| Template Version | 1.0 |
| Platform | ModelIt (formerly Cell Collective) |
| Estimated Time | 45-60 minutes |
| Can Split Across | 2 class periods |