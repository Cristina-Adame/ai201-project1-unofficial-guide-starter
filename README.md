# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

<!-- What topic or category of knowledge does your system cover?
     Why is this knowledge valuable, and why is it hard to find through official channels?
     Example: "Student reviews of CS professors at [university] — useful because official
     course descriptions don't reflect teaching style, exam difficulty, or workload." -->
Student reviews of CS professors at the University of Texas at Austin - useful for students to get unofficial information from previous students about the professor's personality, course workload, and difficulty of the work assigned. This unofficial information is important because any university-sourced materials will likely not depict the honest truth a regular student may experience in a specific course from a specific professor. The anonymity provided by the site also allows for individuals to give unrestrained truth that may be found valuable to prospective students. Since universities like to keep a 'clean' reputation, they likely would not include any defects in a professor's teaching strategy that could be detrimental to students.

---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 | ahmed_gheith.txt | Variety of student reviews on professor gheith sourced from ratemyprofessor.com | C:\Users\Crist\Downloads\CODEPATH\AI201\project 1\ai201-project1-unofficial-guide-starter\documents\ahmed_gheith.txt |
| 2 | alison_norman.txt | Variety of student reviews on professor norman sourced from ratemyprofessor.com | C:\Users\Crist\Downloads\CODEPATH\AI201\project 1\ai201-project1-unofficial-guide-starter\documents\alison_norman.txt |
| 3 | angela_beasley.txt | Variety of student reviews on professor beasley sourced from ratemyprofessor.com | C:\Users\Crist\Downloads\CODEPATH\AI201\project 1\ai201-project1-unofficial-guide-starter\documents\angela_beasley.txt |
| 4 | bill_young.txt | Variety of student reviews on professor young sourced from ratemyprofessor.com | C:\Users\Crist\Downloads\CODEPATH\AI201\project 1\ai201-project1-unofficial-guide-starter\documents\bill_young.txt |
| 5 | carol_ramsey.txt | Variety of student reviews on professor ramsey sourced from ratemyprofessor.com | C:\Users\Crist\Downloads\CODEPATH\AI201\project 1\ai201-project1-unofficial-guide-starter\documents\carol_ramsey.txt |
| 6 | glenn_downing.txt | Variety of student reviews on professor downing sourced from ratemyprofessor.com | C:\Users\Crist\Downloads\CODEPATH\AI201\project 1\ai201-project1-unofficial-guide-starter\documents\glenn_downing.txt |
| 7 | morgan_fong.txt | Variety of student reviews on professor fong sourced from ratemyprofessor.com | C:\Users\Crist\Downloads\CODEPATH\AI201\project 1\ai201-project1-unofficial-guide-starter\documents\morgan_fong.txt |
| 8 | prashant_joshi.txt | Variety of student reviews on professor joshi sourced from ratemyprofessor.com | C:\Users\Crist\Downloads\CODEPATH\AI201\project 1\ai201-project1-unofficial-guide-starter\documents\prashant_joshi.txt |
| 9 | siddhartha_chatterjee.txt | Variety of student reviews on professor chatterjee sourced from ratemyprofessor.com | C:\Users\Crist\Downloads\CODEPATH\AI201\project 1\ai201-project1-unofficial-guide-starter\documents\siddhartha_chatterjee.txt |
| 10 | veena_ravishankar.txt | Variety of student reviews on professor ravishankar sourced from ratemyprofessor.com | C:\Users\Crist\Downloads\CODEPATH\AI201\project 1\ai201-project1-unofficial-guide-starter\documents\veena_ravishankar.txt |

---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:** 500 characters. 

**Overlap:**50 characters. 

**Why these choices fit your documents:**The documents contain reviews of students with some entries containing additional course information or tags regarding the workload or course design. 500 characters allows for the central review to be retrieved and the additional tags found above and below it. With the main body of the review secured, the overlap is to gather the additional course information(e.g course title, grade the reviewer got, etc) and the tags at the bottom that summarize a bit about the course with the professor. 50 characters is enough to gather any tags/labels that were cut off.

**Final chunk count:** 110

_____SAMPLE CHUNKS___:
Chunk 1 (source: ahmed_gheith.txt):
Quality
5.0
Difficulty
5.0
CS429H
Apr 28th, 2026
For Credit: Yes
Attendance: Not Mandatory
Would Take Again: Yes
Grade: Not sure yet
Textbook: N/A
Dr. Gheith is an exceptional professor, and the course is very challenging. Expect 30+ hours a week on the projects. However, it seems the majority of students use AI on the programming assignments and TAs/professor don't seem to care to punish cheaters (even blatant cases), which is quite unfair given the difference in workload.
Lots of homework
Qual
----------------------------------------

Chunk 2 (source: ahmed_gheith.txt):
 the difference in workload.
Lots of homework
Quality
5.0
Difficulty
5.0
CS439
Apr 21st, 2026
For Credit: Yes
Attendance: Not Mandatory
Would Take Again: Yes
Grade: B-
Textbook: N/A
He is an amazing lecturer and knows everything like the back of his hand whenever students have questions (99% of the time). He doesn't use slides which is sometimes a minus but he makes it engaging enough w/o slides. The projects require 30 hours commitment on avg per week. The class is amazing and I have come out l
----------------------------------------

Chunk 3 (source: ahmed_gheith.txt):
r week. The class is amazing and I have come out learning about operating systems.
Participation matters
Inspirational
Lots of homework
Quality
4.0
Difficulty
5.0
CS439
May 26th, 2025
For Credit: Yes
Attendance: Not Mandatory
Grade: Rather not say
Textbook: N/A
Gheith is an incredible lecturer, and I learned so much from his class. But the projects are brutal. Expect honors-level difficulty in an already very tough course. If you take this course you should probably clear out some other commitme
----------------------------------------
Chunk 4 (source: carol_ramsey.txt)
Quality
2.0
Difficulty
4.0
CS312
May 6th, 2026
For Credit: Yes
Attendance: Mandatory
Grade: B
Textbook: Yes
Professor Ramsey is a very sweet person, and she is willing to help you without judgement. However, it is really hard to earn an A in this class because she introduced some problems in the exams that are not covered in the textbook, practice exams, or the quizzes. The class is incredibly harder for people who have little to no coding experience.
Participation matters
Test
Quality
4.0
Diffi
----------------------------------------
Chunk 5 (Source: veena_ravishankar.txt)
Quality
5.0
Difficulty
2.0
CS303E
May 3rd, 2026
For Credit: Yes
Attendance: Not Mandatory
Would Take Again: Yes
Grade: A-
Textbook: Yes
Dr.Ravishankar is one of those professors who truly cares about her students. The hate is so unnecessary. It is completely possible to get an A in this class if you participate and stay consistently on top of the material. Totally do-able. She is easily the best professor for this course and I'm ecstatic to take CS 313E with her next sem
Clear grading criteria
C

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:** all-MiniLM-L6-v2 via sentence-transformers

**Production tradeoff reflection:** With such small reviews, it seems that the most important would be attempting to improve accuracy in domain-specific text. Some language appears to be misinterpreted as mixed when they generally agree on one viewpoint. Aside from those, context-length would be more of a apriority for a larger source template, and multilingual support doesn't seem useful in for a data set regarding a university teaching the CS department exclusively in English.

---


## Retrieval Test Results
----------------------------------------
what do students day about the lectures provided by Professor Ramsey?
Students have mixed reviews about the lectures provided by Professor Ramsey. Some students mention that she is "not a great lecturer" (carol_ramsey.txt, multiple sources), often gets "lost in lecture" (carol_ramsey.txt, Jan 9th, 2026), and "would often get lost in lecture, made many mistakes" (carol_ramsey.txt, Jan 9th, 2026). Additionally, one student notes that "Ramsey seems like she has no idea what she is talking about, and often even confuses herself when she is teaching" (carol_ramsey.txt, Apr 7th, 2026). However, another student mentions that "Ramsey is super sweet and cares about all her students. Although she is all over the place, she really does try her best to get her students to understand the content" (carol_ramsey.txt, Apr 19th, 2026). Overall, it seems that while Professor Ramsey may not be the strongest lecturer, she is at least trying to engage with her students and make the class enjoyable, with one student even describing her as "hilarious" (carol_ramsey.txt, Jan 19th, 2026, and Mar 6th, 2026).
• carol_ramsey.txt

TOP CHUNKS:
Source: carol_ramsey.txt | Distance: 0.716
ll likely be an easy class. Ramsey is not a great lecturer but she's not the worst either. For programming assignments utilize design sessions!! Focus on your exam grades because they are your ENTIRE class grade. Lectures are mandatory but at least she is actually the funniest person ever.
Hilarious
Test heavy
Graded by few things
Quality
2.0
Difficulty
3.0
CS312
Jan 19th, 2026
For Credit: Yes
Attendance: Mandatory
Grade: C+
Textbook: Yes
Professor Ramsey was not a great lecturer, would often ge
---
Source: carol_ramsey.txt | Distance: 0.753
e: Rather not say
Textbook: Yes
Ramsey is super sweet and cares about all her students. Although she is all over the place, she really does try her best to get her students to understand the content. CS is not an easy subject so coming in thinking the class will be easy is unrealistic. Get ready to try and put effort in and you'll do fine. Go to office hours and work with TAs.
Test heavy
Graded by few things
Accessible outside class
Quality
1.0
Difficulty
5.0
CS312
Apr 19th, 2026
For Credit: Yes
---
Source: carol_ramsey.txt | Distance: 0.793
de: Not sure yet
Textbook: Yes
My biggest mistake was not dropping this class after the first lecture. Ramsey seems like she has no idea what she is talking about, and often even confuses herself when she is teaching. There are so many mistakes and typos on assignments, please if you care about your well being do not take this class.
Tough grader
Get ready to read
Test heavy
Quality
5.0
Difficulty
3.0
CS313E
Apr 7th, 2026
For Credit: Yes
Attendance: Mandatory
Would Take Again: Yes
She definitely
---
EXPLANATION:
The chunks are relevant to the query as they are all about Professor Carol Ramsey and they include the word "lecture" and comments about her lecturing abilities.

----------------------------------------
what do students say about Professor Fong's reaction to AI use?
According to the documents, students say that Professor Fong is "strict about AI" and has a "reporting thing" that can be "cruel" (morgan_fong.txt, May 4th, 2026, and another morgan_fong.txt). One student mentions that their report was dismissed (morgan_fong.txt, May 4th, 2026). Another student states that "of course people are going to use AI, how else are we to learn the material", implying that Professor Fong's reaction to AI use is overly restrictive (morgan_fong.txt, May 3rd, 2026).
• morgan_fong.txt
• angela_beasley.txt
• ahmed_gheith.txt
• prashant_joshi.txt

TOP CHUNKS:
Source: morgan_fong.txt | Distance: 0.926
A
Textbook: Yes
If you want to learn python, then having a prof who's strict about AI is a good thing. However, she's a bit overzealous about reporting (mine was dismissed). Generally people who get their Ph Ds in education care about education, and I believe that to be true for Dr. Fong.
Get ready to read
Participation matters
EXTRA CREDIT
Quality
1.0
Difficulty
4.0
cs313e
May 4th, 2026
For Credit: Yes
Attendance: Not Mandatory
Grade: A
Textbook: Yes
I'm sure she has good knowledge of CS, but i
---
Source: morgan_fong.txt | Distance: 1.140
nce: Not Mandatory
Grade: F
Besides the AI stuff she is just not a good professor. I dont want to repeat what others are saying but she just doesn't teach that well. She presents the slides and then says "have fun coding" and walks around the classroom. She asks us to ask the TA if we have questions. Of course people are going to use AI how else are we to learn the material
Quality
1.0
Difficulty
5.0
cs313e
May 3rd, 2026
For Credit: Yes
Attendance: Not Mandatory
Textbook: Yes
Besides the fact th
---
Source: morgan_fong.txt | Distance: 1.191
ndance: Not Mandatory
Grade: Not sure yet
Textbook: Yes
Professor Fong has a flipped classroom with a textbook you teach yourself from, and then x2 a week, problem-solving sessions where she briefly touches on the material. The programming assignments are very difficult, TAs are somewhat helpful. Exams are easy. The reporting thing is cruel, considering there was no warning, but understandable.
Get ready to read
Lots of homework
---
EXPLANATION:
These top chunks are relevant to the query as they all discuss Professor Fong and they mention the topic of AI. They mention her being "strict about AI", they comment on the use of AI.

----------------------------------------
QUERY: which professor that teaches CS429 or CS429H has the best lectures?

TOP_CHUNKS:
Source: ahmed_gheith.txt | Distance: 0.818
-. The lectures are an absolute delight, he has immense understanding of the material. Likely the hardest programming projects you will do during your time at UT, but also thoroughly instructive and insightful. May have to no-life this class to do well.
Amazing lectures
Inspirational
Respected
Quality
5.0
Difficulty
5.0
CS439
Apr 29th, 2025
For Credit: Yes
Attendance: Not Mandatory
Would Take Again: Yes
Textbook: N/A
Dr. Gheith is the best professor I have ever had! His lectures are truly amazin
---
Source: ahmed_gheith.txt | Distance: 0.897
sor I have ever had! His lectures are truly amazing, and while the class is incredibly intensive project-wise, this finished product (a good chunk of an OS) is incredible and extremely rewarding. Having a small community with amazing TAs made the class experience even better. 10/10 would recommend!
Amazing lectures
Inspirational
Caring
Quality
5.0
Difficulty
4.0
CS439H
Dec 10th, 2024
For Credit: Yes
Attendance: Not Mandatory
Would Take Again: Yes
Grade: B+
Textbook: N/A
Incredible lectures. The
---
Source: prashant_joshi.txt | Distance: 0.919
 I would say attending his lecture or watching Chatterjee's videos are both good ways to do well in class.
Hilarious
Caring
Respected
Quality
5.0
Difficulty
5.0
CS429
Apr 14th, 2026
For Credit: Yes
Attendance: Not Mandatory
Would Take Again: Yes
Grade: B-
Textbook: N/A
Joshi makes one of the hardest classes for CS majors into an actual joy to learn, yes the exams are super difficult, and the projects are hard to start, but his passion for teaching and the subject pushes me to do more in this cla
---
EXPLANATION:
The top chunks mention reviews relevant to the course CS429 and lecturing, the most positive ones are seen from Professor Joshi and Gheith with students discussing their excellent lecturing abilities in these reviews.

----------------------------------------
---
## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**  

prompt = f"""You are a helpful assistant that answers questions about UT Austin CS professors based only on student reviews.

Answer the question using ONLY the information provided in the documents below.
If the documents do not contain enough information to answer the question, say "I don't have enough information on that."

Always cite which document(s) your answer comes from.

Additionally the chunk is labeled by its source text name and professor name."""


**How source attribution is surfaced in the response:**
The prompt includes being told to always cite the documents from the answer and the query portion of the pipeline also adds the source text name to the chunks.

##Sample Grounded Generation with Source Attribution
QUERY: which professor that teaches CS429 or CS429H has the best lectures?
REPLY: According to the documents, Prashant Joshi (prashant_joshi.txt) and Ahmed Gheith (ahmed_gheith.txt) teach CS429/CS429H. Both professors have received praise for their lectures. However, Ahmed Gheith's lectures are described as "truly amazing" and "amazing" in two separate reviews (ahmed_gheith.txt), while Prashant Joshi's lectures are described as making a hard class "into an actual joy to learn" (prashant_joshi.txt). Additionally, one of Ahmed Gheith's reviews states "The lectures are an absolute delight, he has immense understanding of the material" (ahmed_gheith.txt). Based on this information, it seems that Ahmed Gheith's lectures are considered to be particularly exceptional. (ahmed_gheith.txt, prashant_joshi.txt)

SOURCES:
• bill_young.txt
• veena_ravishankar.txt
• alison_norman.txt
• prashant_joshi.txt
• ahmed_gheith.txt
----------------------------------------
QUERY: what do students say about Professor Fong's reaction to AI use?
REPLY: According to the documents, students say that Professor Fong is "strict about AI" and has a "reporting thing" that can be "cruel" (morgan_fong.txt, May 4th, 2026, and another morgan_fong.txt). One student mentions that their report was dismissed (morgan_fong.txt, May 4th, 2026). Another student states that "of course people are going to use AI, how else are we to learn the material", implying that Professor Fong's reaction to AI use is overly restrictive (morgan_fong.txt, May 3rd, 2026).

SOURCES:
• morgan_fong.txt
• angela_beasley.txt
• ahmed_gheith.txt
• prashant_joshi.txt
----------------------------------------
QUERY: what do reviews say about Professor Ravishankar as a person?
REPLY: According to the reviews (veena_ravishankar.txt), Professor Ravishankar is described as "one of those professors who truly cares about her students" (May 3rd, 2026 review) and is said to be "very open to feedback" (May 1st, 2026 review). This suggests that students perceive her as a caring and approachable person. Additionally, one review states "Dr.Ravishankar is very open to feedback and her TAs are accessible through Ed discussion" (May 1st, 2026 review), which further emphasizes her caring nature. [Source: veena_ravishankar.txt]

SOURCES:
• prashant_joshi.txt
• veena_ravishankar.txt
• ahmed_gheith.txt

#Out-of-Scope Query Example with the System's Refusal Response Shown.
QUERY: What is the best off campus dining near UT Austin?
REPLY:I don't have enough information on that. The provided documents only contain reviews of UT Austin CS professors and do not mention off-campus dining options.
---
## Query Interface
INPUT: 
	-textbox labeled 'Your Question' where the user may type in their query for the program.
OUTPUT:
	-textbox labeled 'answer' where query reply is generated with cited sources in the response
	-textbox labeled 'sources' where the name of the documents/sources used to generate the reply

SAMPLE INTERACTION TRANSCRIPT-

QUERY: what do students say about the coding experience required for Professor Young's course? 
REPLY: 
According to the document bill_young.txt, one student mentioned that they had "No coding experience before" and took Professor Young's CS303E class as a pre-req. The student was able to succeed in the class, earning an A grade, but noted that they "really had to put in work to understand the content and do good on tests" and that practice was necessary to develop as a coder. (bill_young.txt)
SOURCES:
• morgan_fong.txt
• bill_young.txt
• ahmed_gheith.txt
• prashant_joshi.txt

---
## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | what do students say about Professor Fong's reaction to AI use? | She reports any/all/most AI use in her course. | She has an overly restrictive view on AI use| Relevant | Accurate |
| 2 | what do students day about the lectures provided by Professor Ramsey?| Her lectures and lecturing skills are lacking. | Not a great lecturer, but tries to engage with her students | Partially relevant | Accurate |
| 3 | what do students say about the coding experience required for Professor Young's course? | Not for a beginner, students will struggle if they don't have prior experience. | Coding experience not requires but a lot of effort needed for those with none | Relevant | Partially accurate |
| 4 | which professor that teaches CS429 or CS429H has the best lectures? | Professor Gheith or Joshi, but not Fong or Chatterjee. | Gheith and Joshi are good but Gheith overall is better | Relevant | Partially accurate |
| 5 | what do reviews say about Professor Ravishankar as a person?| Professor Ravishankar is very kind and cares about her students, even making exams easier to ensure they pass. | Cares about her students and open to feedback | Relevant | Accurate |

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:** what do students say about the coding experience required for Professor Young's course?

**What the system returned:** The system returned that not much coding experience was needed for the course.

**Root cause (tied to a specific pipeline stage):** At the retrieval stage, it didn't pull a chunk that mentioned where an individual struggles due to their lack of experience. The wording was clear to be but likely unclear to the program maybe due to the domain-specific accuracy from the embedding model as well

**What you would change to fix it:** Perhaps increasing the top-k to increase the amount of chunks pulled.

**Question that failed:** what do students day about the lectures provided by Professor Ramsey?

**What the system returned:** Mixed reviews about the lectures.

**Root cause (tied to a specific pipeline stage):** Generation issue where instead of seeing how these "mixed" reviews went together, it separated them into different categories.

**What you would change to fix it:** Likely need to emphasize the tone of the reviews in order to see that some where more negative views on the professors lecturing skills.

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**
The spec allowed me to have the major aspects of the project outlined to feed into the AI tool for the generation of the code. Without the guidance of the spec, I would not have known to think of chunk size, overlap size, or even model names for embedding. Doing the documents first, as shown in the planning.md, also allowed me to know how the data looked like and what it contained which heavily influenced how it would be chunked.

**One way your implementation diverged from the spec, and why:**
I originally had the top-k be 4 since online forums recommended 3-5, but the answers were very vague and not on topic. I would ask about a professor and have responses that were very vague and not quoting the sources well even though it was citing it. So after seeing that, I changed it to 6 in order to get more information with which to generate an answer from. I updated the planning document to reflect this change, but it was 4 originally.

---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- *What I gave the AI:* I gave Claude the Chunking strategy and asked it to show me the chunks produced by the source documents.
- *What it produced:* It showed that each chunk was roughly one review long, but still were sometimes cut off or had additional info.
- *What I changed or overrode:* I questioned whether I should switch to paragraph based chunking and attempted, but after reviewing the project requirements returned to character based.

**Instance 2**

- *What I gave the AI:* I gave Claude my planning document, query.py,app.py and project outline for the generation stage.
- *What it produced:* It produced the UI and a system that returned very vague answers to the questions asked.
- *What I changed or overrode:* I asked where exactly the line for the top-k was in order to increase the number from 4 to 6 due to the lack of information found in the generated responses.
