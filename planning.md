# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

<!-- What domain did you choose? Why is this knowledge valuable and hard to find through official channels? -->
Domain used were student reviews of Professors in the Computer Science department at the University of Texas at Austin. 
---

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

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

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:**500 characters

**Overlap:**50 characters

**Reasoning:** The reviews contain some amount of tags, labels, and general information about the course before the review, so 500 characters seems to be big enough to capture that. Some reviews are shorter and do not have tags, so a 50 character overlap seems enough to get any information about the course that is a bit outside the review

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:** all-MiniLM-L6-v2 via sentence-transformers

**Top-k:** 6

**Production tradeoff reflection:**
Accuracy on domain-specific text would likely be the most important to have with a different model, most universities are one language so multilingual support isn't necessary.

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | what do students say about Professor Fong's reaction to AI use? | She reports any/all/most AI use in her course. |
| 2 | what do students day about the lectures provided by Professor Ramsey? | Her lectures and lecturing skills are lacking. |
| 3 | what do students say about the coding experience required for Professor Young's course? | Not for a beginner, students will struggle if they don't have prior experience.  |
| 4 | which professor that teaches CS429 or CS429H has the best lectures? | Professor Gheith or Joshi, but not Fong or Chatterjee. |
| 5 | what do reviews say about Professor Ravishankar as a person? | Professor Ravishankar is very kind and cares about her students, even making exams easier to ensure they pass. |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1. With review length, labels and tags being different lengths or not even being included in each review, there is a concern about chunks splitting in areas that would cut off information.

2. I am not sure if the document name will be taken into account, it might be the only place where the professor's name is in some of the data. Some people include the professor names in their review but others don't.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

Document Ingestion(txt files)→ Chunking(script) → Embedding+Vector Store(sentence-transformers (all-MiniLM-L6-v2))  → Retrieval(ChromaDB) → Generation(Groq (llama-3.3-70b-versatile))

---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

**Milestone 3 — Ingestion and chunking:**
Claude.
The chunking strategy section of the planning.md requirements and information about how the documents are formatted.
It will likely produce some code that will take in the documents and process them into chunks based on my specifics above.
I will need to actually look at the chunks produce to see if they look around the 500 character size specified.

**Milestone 4 — Embedding and retrieval:**
Claude
The retrieval section of the planning.md requirements.
It produce something that will embed the chunks with the embedding model, sentence-transformers (all-MiniLM-L6-v2), and that will only pull the amount of chunks specified with the retrieval using ChromaDB.
Testing will have to be through queries to see if any relevant information is brought about.

**Milestone 5 — Generation and interface:**
Claude
The project description, my planning document, and any specifics I have about the interface.
Expect it to produce the working final product with Groq (llama-3.3-70b-versatile).
Will have to test it with questions specific to the document and questions that involve topics not included.

