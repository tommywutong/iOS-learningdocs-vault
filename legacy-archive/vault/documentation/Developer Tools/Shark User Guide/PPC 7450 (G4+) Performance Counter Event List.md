---
title: Shark User Guide
apple_id: TP40005233
resource_type: Guide
platform: iOS|macOS
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/SharkUserGuide/7450PMCTablesAppendix/7450PMCTablesAppendix.html
archived_at: '2026-07-15T07:25:29.314475Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Shark User Guide](Introduction.md)


[Next](PPC%20970%20%28G5%29%20Performance%20Counter%20Event%20List.md)[Previous](PPC%207400%20%28G4%29%20Performance%20Counter%20Event%20List.md)

# PPC 7450 (G4+) Performance Counter Event List

The PowerPC 7450 (G4+) cores contain six independent performance counters, each of which can count 20–94 different types of events. CPU cycles can be measured on any counter, five other commonly measured types of events (instructions completed, timebase clock transitions, instructions dispatched, performance monitor interrupts, and external performance monitor events) can also be counted on any of the first four counters, while other types of events can only be counted on a limited subset of the counters.

The table below lists each Event Name, the counter (PMC) number(s) for counters which can count the event, and each event’s number.

For more information on how to configure these counters, see [PowerPC G3/G4/G4+ CPU Performance Counter Configuration](Hardware%20Counter%20Configuration.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqmjqfvjvomjy).

| Performance Counter Event Name | PMC Number(s) | Event Number |
| --- | --- | --- |
| 1st Spec Buffer Active Cycles | 1 | 24 |
| 2nd Spec Branch Buffer Active | 2 | 56 |
| 2nd Spec Branch Buffer Correct | 3 | 27 |
| 3rd Spec Branch Buffer Active | 3 | 28 |
| 3rd Spec Branch Buffer Correct | 4 | 27 |
| Aligned FP Store Instr | 1 | 65 |
| AltiVec CFX Instr | 1, 2, 4 | 11 |
| AltiVec CFX Stall Cycles | 1, 2 | 17 |
| AltiVec Float Instr | 1, 2, 4 | 9 |
| AltiVec Float Stall Cycles | 1, 2 | 15 |
| AltiVec Issue Queue > Threshold | 1 | 31 |
| AltiVec Issue Stalls | 3 | 11 |
| AltiVec Loads | 1 | 64 |
| AltiVec MFVSCR Instr Sync Cycles | 1, 2 | 18 |
| AltiVec MTVRSAVE Instr | 1, 2, 4 | 13 |
| AltiVec MTVSCR Instr | 1, 2, 4 | 12 |
| AltiVec Permute Instr | 1, 2, 4 | 8 |
| AltiVec Permute Stall Cycles | 1, 2 | 14 |
| AltiVec SFX Instr | 1, 2, 4 | 10 |
| AltiVec SFX Stall Cycles | 1, 2 | 16 |
| AltiVec VSCR[SAT] 0->1 | 1, 2 | 19 |
| Branch Flushes | 3 | 26 |
| Branch Instr | 1 | 34 |
| Branch Link Stack Correct | 2 | 59 |
| Branch Link Stack Mispredicts | 3 | 31 |
| Branch Link Stack Prediction Used | 1 | 27 |
| Branch Unit CTR Stall Cycles | 3 | 29 |
| Branch Unit Stall Cycles | 1 | 25 |
|  | 2 | 57 |
| BTIC Hits | 1 | 26 |
| BTIC Misses | 2 | 58 |
| Bus Outstanding Read Queue Full Cycles | 6 | 28 |
| Bus Read/Writes not Retried | 6 | 46 |
| Bus Reads not Retried | 6 | 44 |
| Bus Retries | 6 | 26 |
| Bus Retry from Collision | 6 | 49 |
| Bus Retry from Intervention | 6 | 50 |
| Bus Retry from L1 Retry | 6 | 47 |
| Bus Retry from Prev-Adjacent | 6 | 48 |
| Bus TA's for Reads | 6 | 42 |
| Bus TA's for Writes | 6 | 43 |
| Bus Writes not Retried | 6 | 45 |
| Cache-Inhibited Stores | 1 | 52 |
| Canceled iL1 Misses | 3 | 19 |
| Completed 0 Instr | 1 | 32 |
| Completed 1 Instr | 2 | 33 |
| Completed 2 Instr | 3 | 8 |
| Completed 3 Instr | 4 | 14 |
| Completion Queue > Threshold | 2 | 32 |
| Complex Integer Instr | 1 | 33 |
| CPU Cycles | 1, 2, 3, 4, 5, 6 | 1 |
| Data Bkpt Matches | 2 | 53 |
| DCBF/DCBST Instr dL1 Hits | 3 | 20 |
| Dispatched 0 Instr | 4 | 15 |
| Dispatched 1 Instr | 3 | 9 |
| Dispatched 2 Instr | 2 | 34 |
| Dispatched 3 Instructions | 1 | 29 |
| Dispatched AltiVec Instr | 3 | 10 |
| dL1 Castouts | 2 | 50 |
| dL1 Cycles | 2 | 41 |
| dL1 Hits | 1 | 56 |
| dL1 Load Hits | 1 | 53 |
| dL1 Load Miss Cycles | 3 | 21 |
| dL1 Load Misses | 2 | 37 |
| dL1 Load-Miss Cycles > Threshold | 1 | 43 |
| dL1 Misses | 2, 3 | 23 |
| dL1 Pushes | 3 | 22 |
| dL1 Reloads | 2 | 49 |
| dL1 Snoop Hit in COQ | 1 | 48 |
| dL1 Snoop Hit in COQ Retry | 1 | 49 |
| dL1 Snoop Hit Modified | 1 | 44 |
| dL1 Snoop Hits | 1 | 50 |
| dL1 Snoops | 1, 2 | 22 |
| dL1 Store Hits | 1 | 55 |
| dL1 Store Misses | 2 | 39 |
| dL1 Touch Hits | 1 | 54 |
| dL1 Touch Miss Cycles | 2 | 40 |
| dL1 Touch Misses | 2 | 38 |
| dL2 Misses | 5, 6 | 6 |
| dL3 Misses | 5, 6 | 7 |
|  | 6 | 34 |
| DSS Instr | 1 | 60 |
| DSSALL Instr | 4 | 19 |
| dst-Instr Dispatched | 1 | 57 |
| DSTx Search Success | 1 | 59 |
| DTLB Misses | 3 | 18 |
| DTLB Search Cycles | 4 | 23 |
| DTLB Search Cycles > Threshold | 1 | 40 |
| DTQ Full | 6 | 25 |
| EIEIO Instr | 1 | 35 |
| Extern Perf Monitor | 1, 2, 3, 4 | 7 |
| External Interventions | 6 | 22 |
| External Pushes | 6 | 23 |
| External Snoop Retries | 6 | 24 |
| Fall Thru Branches | 2 | 54 |
| Fast BTIC Hits | 3 | 30 |
| Folded Branches | 4 | 29 |
| FP Denorm Result | 1 | 94 |
| FP Denormalize | 1 | 67 |
| FP Instr Dispatched to FPR Queue | 2 | 24 |
| FP Issue Queue > Threshold | 3 | 13 |
| FP Issue Stalls | 2 | 60 |
| FP Load Instr | 1 | 79 |
| FP Load-Double Instr | 1 | 81 |
| FP Load-Single Instr | 1 | 80 |
| FP Renormalize | 1 | 66 |
| FP Store Double Instr | 4 | 30 |
| FP Store Single Instr | 2 | 62 |
| FP Store Stall Cycles | 1 | 68 |
| FPSCR Renames 1/2 Busy | 1 | 91 |
| FPSCR Renames 1/4 Busy | 1 | 90 |
| FPSCR Renames 3/4 Busy | 1 | 92 |
| FPSCR Renames All Busy | 1 | 93 |
| FPU Instr | 3 | 14 |
| GPR Issue Queue > Threshold Cycles | 4 | 16 |
| GPR Issue Queue Stall Cycles | 4 | 17 |
| GPR Rename Buffer > Threshold | 3 | 12 |
| iL1 Accesses | 1 | 41 |
| iL1 Miss Cycles | 2 | 36 |
| iL1 Misses | 1, 2 | 21 |
| iL1 Reloads | 2 | 48 |
| iL2 Misses | 5, 6 | 4 |
| iL3 Misses | 5, 6 | 5 |
|  | 6 | 33 |
| Instr Bkpt Matches | 1 | 42 |
| Instr Completed | 1, 2, 3, 4 | 2 |
| Instr Dispatched | 1, 2, 3, 4 | 4 |
| Instr Dispatched to GPR Queue | 1 | 28 |
| Instr Queue > Threshold | 1 | 30 |
| Interventions | 5, 6 | 18 |
| ITLB Misses | 2 | 35 |
| ITLB Search Cycles | 1 | 39 |
| ITLB Search Cycles > Threshold | 3 | 17 |
| L1 External Interventions | 6 | 19 |
| L2 Castout Queue Full Cycles | 6 | 10 |
| L2 Castouts | 6 | 8 |
| L2 External Interventions | 6 | 20 |
| L2 Hits | 5, 6 | 2 |
| L2 Load Hits | 5 | 8 |
| L2 Misses | 5 | 19 |
|  | 6 | 29 |
| L2 Store Hits | 5 | 9 |
| L2 Touch Hits | 5, 6 | 13 |
| L2 Valid Requests | 6 | 27 |
| L3 Castout Queue Full Cycles | 6 | 11 |
| L3 Castouts | 6 | 9 |
| L3 External Interventions | 6 | 21 |
| L3 Hits | 5, 6 | 3 |
|  | 6 | 31 |
| L3 Load Hits | 5 | 10 |
|  | 6 | 35 |
| L3 Misses | 5 | 20 |
|  | 6 | 30 |
|  | 6 | 32 |
| L3 Read Queue Full Cycles | 6 | 16 |
| L3 Store Hits | 5 | 11 |
|  | 6 | 36 |
| L3 Touch Hits | 5, 6 | 14 |
|  | 6 | 37 |
| L3 Write Queue Full Cycles | 6 | 17 |
| LD/ST Alias vs. CSQ | 1 | 73 |
| LD/ST Alias vs. FSQ/WB0/WB1 | 1 | 72 |
| LD/ST CSQ Forwards | 1 | 86 |
| LD/ST Indexed Alias Stalls | 1 | 71 |
| 1st Spec Branch Buffer Correct | 2 | 55 |
| LD/ST LMQ Full Stalls | 1 | 78 |
| LD/ST LMQ Index Alias Stalls | 1 | 84 |
| LD/ST Load vs. STQ Alias Stalls | 1 | 83 |
| LD/ST Load-Hit Line vs. CSQ0 | 1 | 74 |
| LD/ST Load-Miss Line vs. CSQ0 | 1 | 75 |
| LD/ST RA Latch Stall | 1 | 82 |
| LD/ST STQ Index Alias Stalls | 1 | 85 |
| LD/ST Touch Alias vs. CSQ | 1 | 77 |
| LD/ST Touch Alias vs. FSQ/WB0/WB1 | 1 | 76 |
| LD/ST True Alias Stalls | 1 | 70 |
| Load Instr | 2 | 26 |
| Load String/Multi Instr Pieces | 3 | 16 |
| Load-Miss Alias | 1 | 45 |
| Load-Miss Alias on Touch | 1 | 46 |
| Load/Store Instr | 2 | 25 |
| LSWI/LSWX/LMW Instr | 1 | 38 |
| LWARX Instr | 2 | 29 |
| MFSPR Instr | 2 | 30 |
| Mispredicted Branches | 4 | 28 |
| MTSPR Instr | 1 | 36 |
| Nothing | 1, 2, 3, 4, 5, 6 | 0 |
| Perf Monitor Interrupts | 1, 2, 3, 4 | 5 |
| Prefetch Engine Full | 6 | 57 |
| Prefetch Engine Requests | 6 | 52 |
| Prefetch Instr Fetch Collisions | 6 | 55 |
| Prefetch Load Collisions | 6 | 53 |
| Prefetch Load/Store/Instr Fetch Collisions | 6 | 56 |
| Prefetch Store Collisions | 6 | 54 |
| Refetch Serializations | 2 | 31 |
| Refreshed DSTs | 1 | 58 |
| SC Instr | 1 | 37 |
| Simple Integer Instr | 4 | 18 |
| Snoop Modified | 5 | 16 |
| Snoop Requests | 6 | 51 |
| Snoop Retries | 4 | 24 |
|  | 5, 6 | 15 |
| Snoop Valid | 5 | 17 |
| Store Instr | 1, 2 | 20 |
| Store Merge to 32 Bytes | 2 | 52 |
| Store Merge/Gathers | 2 | 51 |
| Store String/Multi Pieces | 4 | 22 |
| STSWI/STSWX/STMW Instr | 2 | 27 |
| STWCX Instr | 3 | 15 |
| Successful STWCX Instr | 4 | 25 |
| SYNC Instr | 4 | 21 |
| Taken Branches | 3 | 25 |
| TimeBase (Lower) 0->1 bit transitions | 1, 2, 3, 4 | 3 |
| TLBIE Instr | 2 | 28 |
| TLBIE Snoops | 2 | 47 |
| TLBSYNC Instr | 4 | 20 |
| Touch Alias | 1 | 47 |
| Unaligned Load Instr | 1 | 87 |
| Unaligned Load/Store Instr | 1 | 89 |
| Unaligned Store Instr | 1 | 88 |
| Unresolved Branches | 1 | 23 |
| User/Supervisor Switches | 2 | 61 |
| VTE Branch Speculation Cancel | 2 | 43 |
| VTE Line Fetch dL1 Hits | 1 | 63 |
| VTE Line Fetch dL1 Miss | 2 | 45 |
| VTE Line Fetches | 2 | 46 |
| VTE Resume on Context Switch | 2 | 44 |
| VTE Suspended on Context Switch | 1 | 62 |
| VTE0 Line Fetches | 1 | 61 |
| VTE1 Line Fetches | 2 | 42 |
| VTE2 Line Fetches | 3 | 24 |
| VTE3 Line Fetches | 4 | 26 |
| Write-Through Stores | 1 | 51 |

[Next](PPC%20970%20%28G5%29%20Performance%20Counter%20Event%20List.md)[Previous](PPC%207400%20%28G4%29%20Performance%20Counter%20Event%20List.md)

