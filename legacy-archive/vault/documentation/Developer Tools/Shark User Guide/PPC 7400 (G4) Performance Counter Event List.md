---
title: Shark User Guide
apple_id: TP40005233
resource_type: Guide
platform: iOS|macOS
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/SharkUserGuide/7400PMCTablesAppendix/7400PMCTablesAppendix.html
archived_at: '2026-07-15T07:25:29.297249Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Shark User Guide](Introduction.md)


[Next](PPC%207450%20%28G4%2B%29%20Performance%20Counter%20Event%20List.md)[Previous](PPC%20750%20%28G3%29%20Performance%20Counter%20Event%20List.md)

# PPC 7400 (G4) Performance Counter Event List

The PowerPC 7400 (G4) cores contain four independent performance counters, each of which can count 27–48 different types of events. Four commonly measured types of events (CPU cycles, instructions completed, timebase clock transitions, and instructions dispatched) can be counted on any counter, while other types of events can only be counted on a limited subset of the counters.

The table below lists each Event Name, the counter (PMC) number(s) for counters which can count the event, and each event’s number.

For more information on how to configure these counters, see [PowerPC G3/G4/G4+ CPU Performance Counter Configuration](Hardware%20Counter%20Configuration.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqmjqfvjvomjy).

| Performance Counter Event Name | PMC Number(s) | Event Number |
| --- | --- | --- |
| 1st Spec Branch Buffer Correct | 2 | 38 |
| 2nd Spec Branch Buffer Correct | 3 | 14 |
| AltiVec Load Instr | 1 | 48 |
| AltiVec MFVSCR Instr Sync Cycles | 1 | 14 |
| AltiVec MTVRSAVE Instr | 1 | 16 |
| AltiVec MTVSCR Instr | 1 | 15 |
| AltiVec VCIU Instr | 3 | 7 |
| AltiVec VFPU Instr | 4 | 7 |
| AltiVec VFPU Stall Cycles | 3 | 8 |
| AltiVec VFPU Traps | 2 | 34 |
| AltiVec VPU Instr | 1 | 7 |
| AltiVec VPU Stall Cycles | 4 | 8 |
| AltiVec VSCR[SAT] 0->1 | 1 | 17 |
| AltiVec VSIU Stall Cycles | 1 | 8 |
| Branch Unit LR/CTR Stall Cycles | 3 | 15 |
| Branch Unit Speculative Load Stall Cycles | 1 | 37 |
| Branch Unit Speculative Stall Cycles | 1 | 13 |
|  | 4 | 14 |
| Branches Taken | 3 | 5 |
| Bus Kill Transactions (Non-Retried) | 4 | 12 |
| Bus Multi Beat Write TAs | 4 | 25 |
| Bus Multi-Beat Read TAs | 2 | 21 |
| Bus Read TAs | 2 | 42 |
| Bus Retries | 2 | 20 |
| Bus Single Beat Read TAs | 1 | 28 |
| Bus Single Beat Write TAs | 3 | 29 |
| Bus Transactions (Non-Retried) | 1 | 27 |
| Cache Inhibited Stores | 2 | 24 |
| Clean L1 Castouts to L2 | 1 | 18 |
| Conditional Store Instr | 3 | 12 |
| CPU Cycles | 1, 2, 3, 4 | 1 |
| Data Bkpt match | 1 | 10 |
| Data Reload Table Snoop Hits | 2 | 35 |
| Data Reload Table Store Miss Merges | 2 | 22 |
| Dirty L1 Castouts to L2 | 2 | 13 |
| dL1 CacheOp Cycles | 3 | 17 |
| dL1 Castout to L2 Misses | 2 | 28 |
| dL1 Castouts to L2 | 4 | 19 |
| dL1 Cycles | 3 | 18 |
| dL1 Hits | 1 | 24 |
| dL1 Load Hits | 1 | 22 |
| dL1 Load Misses | 2 | 15 |
| dL1 Miss Cycles > Threshold | 1 | 11 |
| dL1 Misses | 2 | 17 |
| dL1 Reloads | 3 | 30 |
| dL1 Snoop Hits | 4 | 23 |
| dL1 Snoop Interventions | 4 | 16 |
|  | 4 | 26 |
| dL1 Store Hits | 1 | 23 |
| dL1 Store Misses | 2 | 16 |
| dL1 Touch Hits | 3 | 16 |
| dL1 Touch Misses | 4 | 15 |
| dL1 Writes Hit Shared | 1 | 30 |
| dL2 Hits | 1 | 33 |
| dL2 Misses | 2 | 26 |
| DSS Instr | 3 | 24 |
| DSSALL Instr | 4 | 22 |
| DST DTLB Table Successful Searches | 4 | 27 |
| DST Instr Dispatched | 1 | 38 |
| DTLB Misses | 3 | 6 |
| DTLB Search Cycles | 4 | 6 |
| DTLB Search Cycles > Threshold | 1 | 20 |
| EIEIO Instr | 1 | 5 |
| External Snoop Requests | 1 | 42 |
| Fall through Branches | 2 | 5 |
| Floating Point Instr | 3 | 11 |
| Full Cache Line Store Miss Merge | 3 | 21 |
| Hit Exclusive Interventions | 3 | 28 |
| Hit Interventions | 1 | 45 |
| Hit Modified Interventions | 2 | 36 |
| Hit Shared Interventions | 4 | 24 |
| iL1 Misses | 1 | 32 |
| iL1 Reloads | 2 | 25 |
| iL2 Hits | 2 | 27 |
| iL2 Misses | 1 | 34 |
| Instr Bkpt match | 1 | 9 |
| Instr Completed | 1, 2, 3, 4 | 2 |
| Instr Dispatched | 1, 2, 3, 4 | 4 |
| Integer Instr | 4 | 13 |
| ITLB Misses | 2 | 6 |
| ITLB Search Cycles | 1 | 6 |
| ITLB Search Cycles > Threshold | 1 | 19 |
| L1 Castout to L2 Hits | 1 | 35 |
| L1 Load Fold Queue Reload Hits | 1 | 29 |
| L1 Load Fold Queue Touch Hits | 1 | 46 |
| L1 Operations Queue Snoop Hits | 1 | 47 |
| L2 Allocations | 1 | 36 |
| L2 Castout Snoop Hits | 1 | 44 |
| L2 Sectors Castout | 2 | 29 |
| L2 Snoop Hits | 3 | 27 |
| L2 Snoop Interventions | 3 | 13 |
| L2 Tag Accesses | 1 | 26 |
| L2 Tag Lookup | 1 | 25 |
| L2 Tag Snoop Writes | 4 | 17 |
| L2 Tag Snoops | 3 | 19 |
| L2 Tag Writes | 2 | 18 |
| L2 Write Hit on Shared | 2 | 23 |
| L2SRAM Cycles | 4 | 18 |
| L2SRAM Read Cycles | 2 | 19 |
| L2SRAM Write Cycles | 3 | 20 |
| Load Instr | 2 | 11 |
| Mispredicted Branches | 4 | 5 |
| Nothing | 1, 2, 3, 4 | 0 |
| Reserved Loads | 2 | 10 |
| Snoop Hits | 2 | 37 |
| Snoop Retries | 3 | 26 |
| Snooped TLB Invalidations | 2 | 41 |
| Snoops Serviced | 2 | 12 |
| Store Instr | 1 | 21 |
| Successful STWCX Instr | 4 | 10 |
| SYNC Instr | 4 | 11 |
| System Register Unit Instr | 2 | 14 |
| TimeBase (Lower) 0->1 bit transitions | 1, 2, 3, 4 | 3 |
| TLBI Instr | 2 | 40 |
| TLBSYNC Instr | 3 | 10 |
| Unresolved Branches | 1 | 12 |
| User/Supervisor Switches | 2 | 9 |
| VCIU Wait Cycles | 2 | 8 |
| VSIU Instr | 2 | 7 |
| VTE Data Reload Table Hits | 3 | 22 |
| VTE dL1 Hits | 4 | 20 |
| VTE L1 Cache Misses | 2 | 30 |
| VTE Line Fetches | 2 | 32 |
| VTE Premature Cancels | 2 | 33 |
| VTE Refresh | 1 | 40 |
| VTE Resume on Context Switch | 2 | 39 |
| VTE Suspend Context Switch | 1 | 41 |
| VTE0 Fetches | 1 | 39 |
| VTE1 Line Fetches | 2 | 31 |
| VTE2 Line Fetches | 3 | 23 |
| VTE3 Line Fetches | 4 | 21 |
| Window of Opportunity Push Address Tenures | 1 | 43 |
| Write Through Stores | 1 | 31 |

[Next](PPC%207450%20%28G4%2B%29%20Performance%20Counter%20Event%20List.md)[Previous](PPC%20750%20%28G3%29%20Performance%20Counter%20Event%20List.md)

