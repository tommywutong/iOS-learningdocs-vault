---
title: Shark User Guide
apple_id: TP40005233
resource_type: Guide
platform: iOS|macOS
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/SharkUserGuide/ARM11PerformanceCounterEventList/ARM11PerformanceCounterEventList.html
archived_at: '2026-07-15T07:25:29.436847Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Shark User Guide](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Kodiak%20%28U4%29%20Performance%20Counter%20Event%20List.md)

# ARM11 Performance Counter Event List

The ARM11 cores used in iOS devices contain three independent performance counters. The first counter can count only cycle counts, while the other two (which are identical) can count 25 different types of events.

The table below lists each Event Name, the counter (PMC) number(s) for counters which can count the event, and each event’s number.

For more information on how to configure these counters, see [ARM11 CPU Performance Counter Configuration](Hardware%20Counter%20Configuration.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqmjqfvjvomzq).

| Performance Counter Event Name | PMC Number(s) | Event Number |
| --- | --- | --- |
| Branch instruction executed | 2-3 | 5 |
| Branch mispredicted | 2-3 | 6 |
| Cycle Count | 1,2-3 | 0,255 |
| Data cache access, no cache operations (cacheable accesses only) | 2-3 | 9 |
| Data cache access, no cache operations | 2-3 | 10 |
| Data cache miss, no cache operations | 2-3 | 11 |
| Data cache writeback per 4 words | 2-3 | 12 |
| Data MicroTLB miss | 2-3 | 4 |
| ETMEXTOUT[0,1] asserts | 2-3 | 34 |
| ETMEXTOUT[0] asserts | 2-3 | 32 |
| ETMEXTOUT[1] asserts | 2-3 | 33 |
| Explicit external data access | 2-3 | 16 |
| Instruction cache miss requires fetch | 2-3 | 0 |
| Instruction executed | 2-3 | 7 |
| Instruction MicroTLB miss | 2-3 | 3 |
| Main TLB miss | 2-3 | 15 |
| Procedure call instruction executed | 2-3 | 35 |
| Procedure return instruction executed, return address predicted incorrectly | 2-3 | 38 |
| Procedure return instruction executed, return address predicted | 2-3 | 37 |
| Procedure return instruction executed | 2-3 | 36 |
| Software changed the PC | 2-3 | 13 |
| Stall, data dependency | 2-3 | 2 |
| Stall, instruction buffer cannot deliver | 2-3 | 1 |
| Stall, LSU request queue full | 2-3 | 17 |
| Write buffer drained count | 2-3 | 18 |

[Next](Document%20Revision%20History.md)[Previous](Kodiak%20%28U4%29%20Performance%20Counter%20Event%20List.md)

