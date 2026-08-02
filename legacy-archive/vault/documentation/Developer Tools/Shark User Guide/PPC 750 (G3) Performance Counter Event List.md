---
title: Shark User Guide
apple_id: TP40005233
resource_type: Guide
platform: iOS|macOS
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/SharkUserGuide/750PMCTablesAppendix/750PMCTablesAppendix.html
archived_at: '2026-07-15T07:25:29.338091Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Shark User Guide](Introduction.md)


[Next](PPC%207400%20%28G4%29%20Performance%20Counter%20Event%20List.md)[Previous](Intel%20Core%202%20Performance%20Counter%20Event%20List.md)

# PPC 750 (G3) Performance Counter Event List

The PowerPC 750 (G3) cores contain four independent performance counters, each of which can count 12–17 different types of events. Four commonly measured types of events (CPU cycles, instructions completed, timebase clock transitions, and instructions dispatched) can be counted on any counter, while other types of events can only be counted on a limited subset of the counters.

The table below lists each Event Name, the counter (PMC) number(s) for counters which can count the event, and each event’s number.

For more information on how to configure these counters, see [PowerPC G3/G4/G4+ CPU Performance Counter Configuration](Hardware%20Counter%20Configuration.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqmjqfvjvomjy).

| Performance Counter Event Name | PMC Number(s) | Event Number |
| --- | --- | --- |
| 2nd Spec Branch Buffer Correct | 3 | 16 |
| Branch Unit LR/CTR Stall Cycles | 3 | 17 |
| Branch Unit Speculative Stall Cycles | 1, 2 | 12 |
|  | 4 | 14 |
| CacheOp L2 Hits | 3 | 13 |
| CPU Cycles | 1, 2, 3, 4 | 1 |
| dL1 Load Miss Cycles | 3 | 15 |
| dL1 Miss Cycles > Threshold | 1, 2 | 10 |
| dL1 Misses | 3 | 5 |
| dL2 Misses | 3 | 7 |
| DTLB Misses | 3 | 6 |
| DTLB Search Cycles | 4 | 6 |
| EIEIO Instr | 1, 2 | 5 |
| Floating Point Instr | 3 | 11 |
| Instr Bkpt Matches | 1, 2 | 9 |
| Instr Completed | 1, 2, 3, 4 | 2 |
| Instr Dispatched | 1, 2, 3, 4 | 4 |
| Instr Fetches | 1, 2 | 8 |
| Integer Instr | 4 | 13 |
| ITLB Search Cycles | 1, 2 | 6 |
| L2 Castouts | 4 | 5 |
| L2 Hits | 1, 2 | 7 |
| L2 Snoop Castouts | 3 | 12 |
| Marked/Unmarked Supervisor Transitions | 4 | 9 |
| Marked/Unmarked User Transitions | 3 | 9 |
| Mispredicted Branches | 4 | 8 |
| Nothing | 1, 2, 3, 4 | 0 |
| Snoop Retries | 4 | 12 |
| STWCX Instr | 3 | 10 |
| Successful STWCX Instr | 4 | 10 |
| SYNC Instr | 4 | 11 |
| Taken Branches | 3 | 8 |
| TimeBase (Lower) 0->1 bit transitions | 3, 4 | 3 |
| TimeBase (Upper) 0->1 bit transitions | 1, 2 | 3 |
| Unresolved Branches | 1, 2 | 11 |

[Next](PPC%207400%20%28G4%29%20Performance%20Counter%20Event%20List.md)[Previous](Intel%20Core%202%20Performance%20Counter%20Event%20List.md)

