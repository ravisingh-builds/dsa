---
name: database-staff-depth
description: >-
  Teaches and writes topics in the database/ folder from layman language
  through the depth a staff engineer at Google needs. Use when the user is
  studying, adding, or revising anything under database/, including universal
  IDs, UUIDv7, primary keys, indexes, B-trees, LSM trees, transactions,
  isolation, replication, sharding, or other database internals. Do not use
  for dsa_families, hld_topics, lld_topics, or low_level_design_topics.
---

# Database topics — layman to Google staff

## User rule (verbatim)

I need to go in as deep in a topic as required by a staff engineer at google. Beginner layman to staff engineer, this is what we have to cover in each topic.

## Scope

This skill applies only to the `database/` folder and to questions about a topic that lives there. Leave DSA, HLD, and LLD to their own skills.

## Depth of every topic

Every topic file under `database/` holds three layers. A topic is unfinished while any layer is missing.

1. **Layman.** What it is, in everyday words, with one example. No engine names required.
2. **Working engineer.** The mechanism that changes a design choice, and the failure you get if you ignore it.
3. **Staff engineer at Google.** The depth used in a design review: make the choice, name the failure mode, and name when the usual choice breaks at high write rate or across machines.

Staff layer is deep enough when the user can:

- Explain the idea to a new teammate in plain words.
- Say what changes on a single-node B-tree and what changes on a range-sharded or LSM store, when both matter for this topic.
- Name the failure mode: hotspot, clock skew, broken sort order, trusting an embedded timestamp, or a coordination bottleneck.
- Name what the service stores itself and what it trusts a library or the database to do.
- Stop before trivia a staff engineer looks up (bit diagrams, fill-factor formulas) unless the user is writing that library.

Google-specific mechanisms (Bigtable row-key hotspots, Spanner TrueTime, and similar) belong in the staff layer when they change the choice. One or two sentences. Do not turn the topic into a product lecture.

## How to talk

One concept at a time. About 3–8 short sentences. One everyday example. Define a jargon term in that concept, then use it.

After the concept, ask only whether they want the next one. Do not start it.

If they ask two things, answer the first and name the second as the one waiting.

The note holds the whole ladder. Chat walks one step of it.

## How to write a topic

When they ask to add or revise a topic, edit only what they asked. Use this shape:

```markdown
# <topic name>

**Layman line:** <one sentence they could say>
**Working line:** <one sentence>
**Staff line:** <one sentence>

## Layman
## Working engineer
## Staff engineer
```

Each layer gets a meaning and one example. Keep their wording when they already wrote a note.
