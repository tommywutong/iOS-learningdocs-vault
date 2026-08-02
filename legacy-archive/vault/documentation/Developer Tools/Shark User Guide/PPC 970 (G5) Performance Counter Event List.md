---
title: Shark User Guide
apple_id: TP40005233
resource_type: Guide
platform: iOS|macOS
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/SharkUserGuide/970PMCTablesAppendix/970PMCTablesAppendix.html
archived_at: '2026-07-15T07:25:29.347059Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Shark User Guide](Introduction.md)


[Next](UniNorth-2%20%28U1.5-2%29%20Performance%20Counter%20Event%20List.md)[Previous](PPC%207450%20%28G4%2B%29%20Performance%20Counter%20Event%20List.md)

# PPC 970 (G5) Performance Counter Event List

The PowerPC 970 (G5) cores contain an extremely sophisticated and complex set of performance counters. Unlike the other processors used in Macintoshes, one cannot simply choose a counter and type of performance counter event for it to count. There are simply too many different possible events in these processors that can be counted. Instead, one must first select various options on the “TTM” and “Byte Lane” muxes in order to narrow down the possible field of events that can be counted, before actually selecting one particular event to count.

The table below lists each Event Name followed by the various selections of event number(s), counter (PMC) number(s), TTM mux settings, and Byte Lane settings that can be used to count that type of event. Where lists of both event and PMC numbers are given in a single row of the table, the corresponding event and PMC numbers (first with first, second with second, etc.) should be used together.

For more information on how to configure these counters, see [PowerPC G5 (970) Performance Counter Configuration](Hardware%20Counter%20Configuration.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqmjqfvjvomjz).

| Performance Counter Event Name | Event Number(s) | PMC Number(s) | TTM Mux Number | Byte Lane Number |
| --- | --- | --- | --- | --- |
| 1 or more Instrs Completed | 3 | 5 |  |  |
| [FPU] fp0 add, mult, sub, compare, fsel | 19 | 1, 2, 5, 6 | 0: FPU | 0: TTM0 |
| [FPU] fp0 add, mult, sub, compare, fsel + fp1 add, mult, sub, compare, fsel | 0 | 5 | 0: FPU | 0: TTM0 |
| [FPU] fp0 denorm operand | 24 | 1, 2, 5, 6 | 0: FPU | 2: TTM0 |
| [FPU] fp0 denorm operand + fp1 denorm operand | 32 | 1 | 0: FPU | 2: TTM0 |
| [FPU] fp0 divide | 16 | 1, 2, 5, 6 | 0: FPU | 0: TTM0 |
| [FPU] fp0 divide + fp1 divide | 0 | 1 | 0: FPU | 0: TTM0 |
| [FPU] fp0 estimate | 18 | 3, 4, 7, 8 | 0: FPU | 1: TTM0 |
| [FPU] fp0 estimate + fp1 estimate | 0 | 3 | 0: FPU | 1: TTM0 |
| [FPU] fp0 finished and produced a result | 19 | 3, 4, 7, 8 | 0: FPU | 1: TTM0 |
| [FPU] fp0 finished and produced a result + fp1 finished and produced a result | 0 | 4 | 0: FPU | 1: TTM0 |
| [FPU] fp0 fpscr | 24 | 3, 4, 7, 8 | 0: FPU | 3: TTM0 |
| [FPU] fp0 fpscr + nothing | 32 | 8 | 0: FPU | 3: TTM0 |
| [FPU] fp0 move, estimate | 16 | 3, 4, 7, 8 | 0: FPU | 1: TTM0 |
| [FPU] fp0 move, estimate + fp1 move, estimate | 0 | 8 | 0: FPU | 1: TTM0 |
| [FPU] fp0 mult-add | 17 | 1, 2, 5, 6 | 0: FPU | 0: TTM0 |
| [FPU] fp0 mult-add + fp1 mult-add | 0 | 2 | 0: FPU | 0: TTM0 |
| [FPU] fp0 round, convert | 17 | 3, 4, 7, 8 | 0: FPU | 1: TTM0 |
| [FPU] fp0 round, convert + fp1 round, convert | 0 | 7 | 0: FPU | 1: TTM0 |
| [FPU] fp0 single precision | 27 | 1, 2, 5, 6 | 0: FPU | 2: TTM0 |
| [FPU] fp0 single precision + fp1 single precision | 32 | 5 | 0: FPU | 2: TTM0 |
| [FPU] fp0 square root | 18 | 1, 2, 5, 6 | 0: FPU | 0: TTM0 |
| [FPU] fp0 square root + fp1 square root | 0 | 6 | 0: FPU | 0: TTM0 |
| [FPU] fp0 stall 3 | 25 | 1, 2, 5, 6 | 0: FPU | 2: TTM0 |
| [FPU] fp0 stall 3 + fp1 stall 3 | 32 | 2 | 0: FPU | 2: TTM0 |
| [FPU] fp0 store | 26 | 1, 2, 5, 6 | 0: FPU | 2: TTM0 |
| [FPU] fp0 store + fp1 store | 32 | 6 | 0: FPU | 2: TTM0 |
| [FPU] fp1 add, mult, sub, compare, fsel | 23 | 1, 2, 5, 6 | 0: FPU | 0: TTM0 |
| [FPU] fp1 denorm operand | 28 | 1, 2, 5, 6 | 0: FPU | 2: TTM0 |
| [FPU] fp1 divide | 20 | 1, 2, 5, 6 | 0: FPU | 0: TTM0 |
| [FPU] fp1 estimate | 22 | 3, 4, 7, 8 | 0: FPU | 1: TTM0 |
| [FPU] fp1 finished and produced a result | 23 | 3, 4, 7, 8 | 0: FPU | 1: TTM0 |
| [FPU] fp1 move, estimate | 20 | 3, 4, 7, 8 | 0: FPU | 1: TTM0 |
| [FPU] fp1 mult-add | 21 | 1, 2, 5, 6 | 0: FPU | 0: TTM0 |
| [FPU] fp1 round, convert | 21 | 3, 4, 7, 8 | 0: FPU | 1: TTM0 |
| [FPU] fp1 single precision | 31 | 1, 2, 5, 6 | 0: FPU | 2: TTM0 |
| [FPU] fp1 square root | 22 | 1, 2, 5, 6 | 0: FPU | 0: TTM0 |
| [FPU] fp1 stall 3 | 29 | 1, 2, 6 | 0: FPU | 2: TTM0 |
| [FPU] fp1 store | 30 | 1, 2, 5, 6 | 0: FPU | 2: TTM0 |
| [GPS] All CO state machines busy | 28 | 1, 2, 5, 6 | 1: GPS | 2: TTM1 |
| [GPS] All read/claim state machines busy | 27 | 1, 2, 5, 6 | 1: GPS | 2: TTM1 |
| [GPS] All read/claim state machines busy + I=1 store queue full | 32 | 5 | 1: GPS | 2: TTM1 |
| [GPS] All snoop state machines busy | 29 | 1, 2, 6 | 1: GPS | 2: TTM1 |
| [GPS] Cacheable store operation (before gathering) | 17 | 3, 4, 7, 8 | 1: GPS | 1: TTM1 |
| [GPS] Cacheable store operation (before gathering) + Master L2 read transaction on bus was retried | 0 | 7 | 1: GPS | 1: TTM1 |
| [GPS] Cacheable store queue full | 30 | 1, 2, 5, 6 | 1: GPS | 2: TTM1 |
| [GPS] I=1 load operation completed on bus | 16 | 3, 4, 7, 8 | 1: GPS | 1: TTM1 |
| [GPS] I=1 load operation completed on bus + Master L2 store transaction on bus was retried | 0 | 8 | 1: GPS | 1: TTM1 |
| [GPS] I=1 store operation (before gathering) | 22 | 1, 2, 5, 6 | 1: GPS | 0: TTM1 |
| [GPS] I=1 store operation completed on bus | 23 | 1, 2, 5, 6 | 1: GPS | 0: TTM1 |
| [GPS] I=1 store queue full | 31 | 1, 2, 5, 6 | 1: GPS | 2: TTM1 |
| [GPS] L2 access collision with L2 prefetch (DST) | 16 | 1, 2, 5, 6 | 1: GPS | 0: TTM1 |
| [GPS] L2 access collision with L2 prefetch (DST) + L2 miss, bus response is modified intervention | 0 | 1 | 1: GPS | 0: TTM1 |
| [GPS] L2 access collision with L2 prefetch (non-DST) | 17 | 1, 2, 5, 6 | 1: GPS | 0: TTM1 |
| [GPS] L2 access collision with L2 prefetch (non-DST) + L2 miss, bus response is shared intervention | 0 | 2 | 1: GPS | 0: TTM1 |
| [GPS] L2 access for store | 18 | 1, 2, 5, 6 | 1: GPS | 0: TTM1 |
| [GPS] L2 access for store + I=1 store operation (before gathering) | 0 | 6 | 1: GPS | 0: TTM1 |
| [GPS] L2 miss on store access (R, S, I) | 19 | 1, 2, 5, 6 | 1: GPS | 0: TTM1 |
| [GPS] L2 miss on store access (R, S, I) + I=1 store operation completed on bus | 0 | 5 | 1: GPS | 0: TTM1 |
| [GPS] L2 miss, bus response is modified intervention | 20 | 1, 2, 5, 6 | 1: GPS | 0: TTM1 |
| [GPS] L2 miss, bus response is shared intervention | 21 | 1, 2, 5, 6 | 1: GPS | 0: TTM1 |
| [GPS] Load or store dispatch retries | 26 | 1, 2, 5, 6 | 1: GPS | 2: TTM1 |
| [GPS] Load or store dispatch retries + Cacheable store queue full | 32 | 6 | 1: GPS | 2: TTM1 |
| [GPS] Load or store dispatch retries due to CO conflicts | 24 | 1, 2, 5, 6 | 1: GPS | 2: TTM1 |
| [GPS] Load or store dispatch retries due to CO conflicts + All CO state machines busy | 32 | 1 | 1: GPS | 2: TTM1 |
| [GPS] Load or store dispatch retries due to Snoop conflicts | 25 | 1, 2, 5, 6 | 1: GPS | 2: TTM1 |
| [GPS] Load or store dispatch retries due to Snoop conflicts + All snoop state machines busy | 32 | 2 | 1: GPS | 2: TTM1 |
| [GPS] Master bus transactions completed | 18 | 3, 4, 7, 8 | 1: GPS | 1: TTM1 |
| [GPS] Master bus transactions completed + Master SYNC operation competed | 0 | 3 | 1: GPS | 1: TTM1 |
| [GPS] Master bus transactions retried | 19 | 3, 4, 7, 8 | 1: GPS | 1: TTM1 |
| [GPS] Master bus transactions retried + Master SYNC operation retried | 0 | 4 | 1: GPS | 1: TTM1 |
| [GPS] Master L2 read transaction on bus was retried | 21 | 3, 4, 7, 8 | 1: GPS | 1: TTM1 |
| [GPS] Master L2 store transaction on bus was retried | 20 | 3, 4, 7, 8 | 1: GPS | 1: TTM1 |
| [GPS] Master SYNC operation competed | 22 | 3, 4, 7, 8 | 1: GPS | 1: TTM1 |
| [GPS] Master SYNC operation retried | 23 | 3, 4, 7, 8 | 1: GPS | 1: TTM1 |
| [GPS] Snoop (external) | 24 | 3, 4, 7, 8 | 1: GPS | 3: TTM1 |
| [GPS] Snoop (external) + Snoop caused cache transition from M to E or S | 32 | 8 | 1: GPS | 3: TTM1 |
| [GPS] Snoop caused cache transition from E or S to R or I | 30 | 3, 4, 7, 8 | 1: GPS | 3: TTM1 |
| [GPS] Snoop caused cache transition from E to S | 29 | 3, 4, 7, 8 | 1: GPS | 3: TTM1 |
| [GPS] Snoop caused cache transition from M to E or S | 28 | 3, 4, 7, 8 | 1: GPS | 3: TTM1 |
| [GPS] Snoop caused cache transition from M to I | 31 | 3, 4, 7, 8 | 1: GPS | 3: TTM1 |
| [GPS] Snoop retried due to all snoop state machines busy | 27 | 3, 4, 7, 8 | 1: GPS | 3: TTM1 |
| [GPS] Snoop retried due to all snoop state machines busy + Snoop caused cache transition from M to I | 32 | 4 | 1: GPS | 3: TTM1 |
| [GPS] Snoop retried due to any conflict | 26 | 3, 4, 7, 8 | 1: GPS | 3: TTM1 |
| [GPS] Snoop retried due to any conflict + Snoop caused cache transition from E or S to R or I | 32 | 3 | 1: GPS | 3: TTM1 |
| [GPS] Snoop state machine dispatched | 25 | 3, 4, 7, 8 | 1: GPS | 3: TTM1 |
| [GPS] Snoop state machine dispatched + Snoop caused cache transition from E to S | 32 | 7 | 1: GPS | 3: TTM1 |
| [IDU] instruction queue fullness | 16, 17, 18, 19, 20, 21, 22, 23, 16, 17, 18, 19, 20, 21, 22, 23, 16, 17, 18, 19, 20, 21, 22, 23, 16, 17, 18, 19, 20, 21, 22, 23 | 3, 4, 4, 4, 4, 4, 4, 4, 4, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8 | 1: IDU | 1: TTM1 |
| [IDU] instruction queue fullness + instruction queue fullness | 0 | 3, 4, 7, 8 | 1: IDU | 1: TTM1 |
| [IFU] branch execution issue valid | 25 | 3, 4, 7, 8 | 0: IFU | 3: TTM0 |
| [IFU] branch execution issue valid + nothing | 32 | 7 | 0: IFU | 3: TTM0 |
| [IFU] branch mispredict due to CR value | 26 | 3, 4, 7, 8 | 0: IFU | 3: TTM0 |
| [IFU] branch mispredict due to CR value + nothing | 32 | 3 | 0: IFU | 3: TTM0 |
| [IFU] branch mispredict due to target address predict | 24 | 3, 4, 7, 8 | 0: IFU | 3: TTM0 |
| [IFU] branch mispredict due to target address predict + valid instructions available, but ifu held by BIQ or IDU | 32 | 8 | 0: IFU | 3: TTM0 |
| [IFU] cycles i L1 write active | 27 | 3, 4, 7, 8 | 0: IFU | 3: TTM0 |
| [IFU] cycles i L1 write active + nothing | 32 | 4 | 0: IFU | 3: TTM0 |
| [IFU] i cache data source | 24, 25, 26, 27, 24, 25, 26, 27, 24, 25, 26, 27, 24, 25, 26, 27 | 1, 2, 2, 2, 2, 5, 5, 5, 5, 6, 6, 6, 6 | 0: IFU | 2: TTM0 |
| [IFU] i cache data source + instr prefetch installed in prefetch buffer | 32 | 6 | 0: IFU | 2: TTM0 |
| [IFU] i cache data source + instruction prefetch request | 32 | 2 | 0: IFU | 2: TTM0 |
| [IFU] i cache data source + translation written to i erat | 32 | 5 | 0: IFU | 2: TTM0 |
| [IFU] i cache data source + valid instruction available | 32 | 1 | 0: IFU | 2: TTM0 |
| [IFU] instr prefetch installed in prefetch buffer | 30 | 1, 2, 5, 6 | 0: IFU | 2: TTM0 |
| [IFU] instruction prefetch request | 29 | 1, 2, 6 | 0: IFU | 2: TTM0 |
| [IFU] translation written to i erat | 31 | 1, 2, 5, 6 | 0: IFU | 2: TTM0 |
| [IFU] valid instruction available | 28 | 1, 2, 5, 6 | 0: IFU | 2: TTM0 |
| [IFU] valid instructions available, but ifu held by BIQ or IDU | 28 | 3, 4, 7, 8 | 0: IFU | 3: TTM0 |
| [ISU] br issue queue full | 21 | 1, 2, 5, 6 | 0: ISU | 0: TTM0 |
|  |  |  | 1: ISU | 0: TTM1 |
| [ISU] completion table full | 16 | 1, 2, 5, 6 | 0: ISU | 0: TTM0 |
|  |  |  | 1: ISU | 0: TTM1 |
| [ISU] completion table full + cr mapper full | 0 | 1 | 0: ISU | 0: TTM0 |
|  |  |  | 1: ISU | 0: TTM1 |
| [ISU] cr issue queue full | 17 | 3, 4, 7, 8 | 0: ISU | 1: TTM0 |
|  |  |  | 1: ISU | 1: TTM1 |
| [ISU] cr issue queue full + flush originated by LSU | 0 | 7 | 0: ISU | 1: TTM0 |
|  |  |  | 1: ISU | 1: TTM1 |
| [ISU] cr mapper full | 20 | 1, 2, 5, 6 | 0: ISU | 0: TTM0 |
|  |  |  | 1: ISU | 0: TTM1 |
| [ISU] dispatch blocked by scoreboard | 25 | 3, 4, 7, 8 | 0: ISU | 3: TTM0 |
|  |  |  | 1: ISU | 3: TTM1 |
| [ISU] dispatch blocked by scoreboard + gpr mapper full | 32 | 7 | 0: ISU | 3: TTM0 |
|  |  |  | 1: ISU | 3: TTM1 |
| [ISU] dispatch reject | 28 | 1, 2, 5, 6 | 0: ISU | 2: TTM0 |
|  |  |  | 1: ISU | 2: TTM1 |
| [ISU] dispatch valid | 27 | 1, 2, 5, 6 | 0: ISU | 2: TTM0 |
|  |  |  | 1: ISU | 2: TTM1 |
| [ISU] dispatch valid + group experienced a branch mispredict | 32 | 5 | 0: ISU | 2: TTM0 |
|  |  |  | 1: ISU | 2: TTM1 |
| [ISU] duration MSR(EE) = 0 | 27 | 3, 4, 7, 8 | 0: ISU | 3: TTM0 |
|  |  |  | 1: ISU | 3: TTM1 |
| [ISU] duration MSR(EE) = 0 + MSR(EE)=0 and interrupt pending | 32 | 4 | 0: ISU | 3: TTM0 |
|  |  |  | 1: ISU | 3: TTM1 |
| [ISU] flush (includes LSU, branch mispredict) | 23 | 3, 4, 7, 8 | 0: ISU | 1: TTM0 |
|  |  |  | 1: ISU | 1: TTM1 |
| [ISU] flush originated by branch mispredict | 22 | 3, 4, 7, 8 | 0: ISU | 1: TTM0 |
|  |  |  | 1: ISU | 1: TTM1 |
| [ISU] flush originated by LSU | 21 | 3, 4, 7, 8 | 0: ISU | 1: TTM0 |
|  |  |  | 1: ISU | 1: TTM1 |
| [ISU] fp0 issue queue full | 19 | 1, 2, 5, 6 | 0: ISU | 0: TTM0 |
|  |  |  | 1: ISU | 0: TTM1 |
| [ISU] fp0 issue queue full + fp1 issue queue full | 0 | 5 | 0: ISU | 0: TTM0 |
|  |  |  | 1: ISU | 0: TTM1 |
| [ISU] fp1 issue queue full | 23 | 1, 2, 5, 6 | 0: ISU | 0: TTM0 |
|  |  |  | 1: ISU | 0: TTM1 |
| [ISU] fpr mapper full | 17 | 1, 2, 5, 6 | 0: ISU | 0: TTM0 |
|  |  |  | 1: ISU | 0: TTM1 |
| [ISU] fpr mapper full + br issue queue full | 0 | 2 | 0: ISU | 0: TTM0 |
|  |  |  | 1: ISU | 0: TTM1 |
| [ISU] fx0 produced a result | 26 | 3, 4, 7, 8 | 0: ISU | 3: TTM0 |
|  |  |  | 1: ISU | 3: TTM1 |
| [ISU] fx0 produced a result + fx1 produced a result | 32 | 3 | 0: ISU | 3: TTM0 |
|  |  |  | 1: ISU | 3: TTM1 |
| [ISU] fx0/ls0 issue queue full | 16 | 3, 4, 7, 8 | 0: ISU | 1: TTM0 |
|  |  |  | 1: ISU | 1: TTM1 |
| [ISU] fx0/ls0 issue queue full + fx1/ls1 issue queue full | 0 | 8 | 0: ISU | 1: TTM0 |
|  |  |  | 1: ISU | 1: TTM1 |
| [ISU] fx1 produced a result | 30 | 3, 4, 7, 8 | 0: ISU | 3: TTM0 |
|  |  |  | 1: ISU | 3: TTM1 |
| [ISU] fx1/ls1 issue queue full | 20 | 3, 4, 7, 8 | 0: ISU | 1: TTM0 |
|  |  |  | 1: ISU | 1: TTM1 |
| [ISU] gpr mapper full | 29 | 3, 4, 7, 8 | 0: ISU | 3: TTM0 |
|  |  |  | 1: ISU | 3: TTM1 |
| [ISU] group experienced a branch mispredict | 31 | 1, 2, 5, 6 | 0: ISU | 2: TTM0 |
|  |  |  | 1: ISU | 2: TTM1 |
| [ISU] group experienced a branch redirect | 30 | 1, 2, 5, 6 | 0: ISU | 2: TTM0 |
|  |  |  | 1: ISU | 2: TTM1 |
| [ISU] instructions dispatched count | 24, 25, 26, 24, 25, 26, 24, 25, 26, 24, 25, 26 | 1, 2, 2, 2, 5, 5, 5, 6, 6, 6 | 0: ISU | 2: TTM0 |
|  |  |  | 1: ISU | 2: TTM1 |
| [ISU] instructions dispatched count + dispatch reject | 32 | 1 | 0: ISU | 2: TTM0 |
|  |  |  | 1: ISU | 2: TTM1 |
| [ISU] instructions dispatched count + group experienced a branch redirect | 32 | 6 | 0: ISU | 2: TTM0 |
|  |  |  | 1: ISU | 2: TTM1 |
| [ISU] instructions dispatched count + nothing | 32 | 2 | 0: ISU | 2: TTM0 |
|  |  |  | 1: ISU | 2: TTM1 |
| [ISU] lr/ctr mapper full | 22 | 1, 2, 5, 6 | 0: ISU | 0: TTM0 |
|  |  |  | 1: ISU | 0: TTM1 |
| [ISU] LRQ full | 18 | 3, 4, 7, 8 | 0: ISU | 1: TTM0 |
|  |  |  | 1: ISU | 1: TTM1 |
| [ISU] LRQ full + flush originated by branch mispredict | 0 | 3 | 0: ISU | 1: TTM0 |
|  |  |  | 1: ISU | 1: TTM1 |
| [ISU] MSR(EE)=0 and interrupt pending | 31 | 3, 4, 7, 8 | 0: ISU | 3: TTM0 |
|  |  |  | 1: ISU | 3: TTM1 |
| [ISU] SRQ full | 19 | 3, 4, 7, 8 | 0: ISU | 1: TTM0 |
|  |  |  | 1: ISU | 1: TTM1 |
| [ISU] SRQ full + flush (includes LSU, branch mispredict) | 0 | 4 | 0: ISU | 1: TTM0 |
|  |  |  | 1: ISU | 1: TTM1 |
| [ISU] xer mapper full | 18 | 1, 2, 5, 6 | 0: ISU | 0: TTM0 |
|  |  |  | 1: ISU | 0: TTM1 |
| [ISU] xer mapper full + lr/ctr mapper full | 0 | 6 | 0: ISU | 0: TTM0 |
|  |  |  | 1: ISU | 0: TTM1 |
| [LSU0] d erat miss side 0 | 18 | 1, 2, 5, 6 |  | 0: LSU0 |
| [LSU0] d erat miss side 0 + d erat miss side 1 | 0 | 6 |  | 0: LSU0 |
| [LSU0] d erat miss side 1 | 22 | 1, 2, 5, 6 |  | 0: LSU0 |
| [LSU0] d slb miss | 21 | 1, 2, 5, 6 |  | 0: LSU0 |
| [LSU0] d tlb miss | 20 | 1, 2, 5, 6 |  | 0: LSU0 |
| [LSU0] fl pt load side 0 | 24 | 3, 4, 7, 8 |  | 3: LSU0 |
| [LSU0] fl pt load side 0 + fl pt load side 1 | 32 | 8 |  | 3: LSU0 |
| [LSU0] fl pt load side 1 | 28 | 3, 4, 7, 8 |  | 3: LSU0 |
| [LSU0] i slb miss | 17 | 1, 2, 5, 6 |  | 0: LSU0 |
| [LSU0] i slb miss + d slb miss | 0 | 2 |  | 0: LSU0 |
| [LSU0] i tlb miss | 16 | 1, 2, 5, 6 |  | 0: LSU0 |
| [LSU0] i tlb miss + d tlb miss | 0 | 1 |  | 0: LSU0 |
| [LSU0] L1 Prefetch | 25 | 3, 4, 7, 8 |  | 3: LSU0 |
| [LSU0] L1 Prefetch + SRQ sync duration | 32 | 7 |  | 3: LSU0 |
| [LSU0] L2 Prefetch | 27 | 3, 4, 7, 8 |  | 3: LSU0 |
| [LSU0] L2 Prefetch + new stream allocated | 32 | 4 |  | 3: LSU0 |
| [LSU0] larx executed 0 | 31 | 1, 2, 5, 6 |  | 2: LSU0 |
| [LSU0] marked flush from LRQ shl, lhl side 0 | 18 | 3, 4, 7, 8 |  | 1: LSU0 |
| [LSU0] marked flush from LRQ shl, lhl side 0 + marked flush from LRQ shl, lhl side 1 | 0 | 3 |  | 1: LSU0 |
| [LSU0] marked flush from LRQ shl, lhl side 1 | 22 | 3, 4, 7, 8 |  | 1: LSU0 |
| [LSU0] marked flush SRQ lhs side 0 | 19 | 3, 4, 7, 8 |  | 1: LSU0 |
| [LSU0] marked flush SRQ lhs side 0 + marked flush SRQ lhs side 1 | 0 | 4 |  | 1: LSU0 |
| [LSU0] marked flush SRQ lhs side 1 | 23 | 3, 4, 7, 8 |  | 1: LSU0 |
| [LSU0] marked flush unaligned load side 0 | 16 | 3, 4, 7, 8 |  | 1: LSU0 |
| [LSU0] marked flush unaligned load side 0 + marked flush unaligned load side 1 | 0 | 8 |  | 1: LSU0 |
| [LSU0] marked flush unaligned load side 1 | 20 | 3, 4, 7, 8 |  | 1: LSU0 |
| [LSU0] marked flush unaligned store side 0 | 17 | 3, 4, 7, 8 |  | 1: LSU0 |
| [LSU0] marked flush unaligned store side 0 + marked flush unaligned store side 1 | 0 | 7 |  | 1: LSU0 |
| [LSU0] marked flush unaligned store side 1 | 21 | 3, 4, 7, 8 |  | 1: LSU0 |
| [LSU0] marked imr reload | 26 | 1, 2, 5, 6 |  | 2: LSU0 |
| [LSU0] marked imr reload + marked stcx fail | 32 | 6 |  | 2: LSU0 |
| [LSU0] marked L1 d cache store miss | 27 | 1, 2, 5, 6 |  | 2: LSU0 |
| [LSU0] marked L1 d cache store miss + larx executed 0 | 32 | 5 |  | 2: LSU0 |
| [LSU0] marked L1 dcache load miss side 0 | 24 | 1, 2, 5, 6 |  | 2: LSU0 |
| [LSU0] marked L1 dcache load miss side 0 + marked L1 dcache load miss side 1 | 32 | 1 |  | 2: LSU0 |
| [LSU0] marked L1 dcache load miss side 1 | 28 | 1, 2, 5, 6 |  | 2: LSU0 |
| [LSU0] marked stcx fail | 30 | 1, 2, 5, 6 |  | 2: LSU0 |
| [LSU0] new stream allocated | 31 | 3, 4, 7, 8 |  | 3: LSU0 |
| [LSU0] out of streams | 26 | 3, 4, 7, 8 |  | 3: LSU0 |
| [LSU0] out of streams + reserved | 32 | 3 |  | 3: LSU0 |
| [LSU0] reserved | 30 | 3, 4, 7, 8 |  | 3: LSU0 |
| [LSU0] snoop tlbie | 19 | 1, 2, 5, 6 |  | 0: LSU0 |
| [LSU0] snoop tlbie + tablewalk duration | 0 | 5 |  | 0: LSU0 |
| [LSU0] SRQ sync duration | 29 | 3, 4, 7, 8 |  | 3: LSU0 |
| [LSU0] stcx failed | 25 | 1, 2, 5, 6 |  | 2: LSU0 |
| [LSU0] stcx failed + stcx passed | 32 | 2 |  | 2: LSU0 |
| [LSU0] stcx passed | 29 | 1, 2, 6 |  | 2: LSU0 |
| [LSU0] tablewalk duration | 23 | 1, 2, 5, 6 |  | 0: LSU0 |
| [LSU1] flush from LRQ shl,lhl side 0 | 18 | 1, 2, 5, 6 | 3: LSU1 2|3 | 0: LSU1 |
|  |  |  | 3: LSU1 2|7 |  |
|  |  |  | 3: LSU1 6|3 |  |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] flush from LRQ shl,lhl side 0 + flush from LRQ shl,lhl side 1 | 0 | 6 | 3: LSU1 2|3 | 0: LSU1 |
|  |  |  | 3: LSU1 2|7 |  |
|  |  |  | 3: LSU1 6|3 |  |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] flush from LRQ shl,lhl side 1 | 22 | 1, 2, 5, 6 | 3: LSU1 2|3 | 0: LSU1 |
|  |  |  | 3: LSU1 2|7 |  |
|  |  |  | 3: LSU1 6|3 |  |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] flush SRQ lhs side 0 | 19 | 1, 2, 5, 6 | 3: LSU1 2|3 | 0: LSU1 |
|  |  |  | 3: LSU1 2|7 |  |
|  |  |  | 3: LSU1 6|3 |  |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] flush SRQ lhs side 0 + flush SRQ lhs side 1 | 0 | 5 | 3: LSU1 2|3 | 0: LSU1 |
|  |  |  | 3: LSU1 2|7 |  |
|  |  |  | 3: LSU1 6|3 |  |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] flush SRQ lhs side 1 | 23 | 1, 2, 5, 6 | 3: LSU1 2|3 | 0: LSU1 |
|  |  |  | 3: LSU1 2|7 |  |
|  |  |  | 3: LSU1 6|3 |  |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] flush unaligned load side 0 | 16 | 1, 2, 5, 6 | 3: LSU1 2|3 | 0: LSU1 |
|  |  |  | 3: LSU1 2|7 |  |
|  |  |  | 3: LSU1 6|3 |  |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] flush unaligned load side 0 + flush unaligned load side 1 | 0 | 1 | 3: LSU1 2|3 | 0: LSU1 |
|  |  |  | 3: LSU1 2|7 |  |
|  |  |  | 3: LSU1 6|3 |  |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] flush unaligned load side 1 | 20 | 1, 2, 5, 6 | 3: LSU1 2|3 | 0: LSU1 |
|  |  |  | 3: LSU1 2|7 |  |
|  |  |  | 3: LSU1 6|3 |  |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] flush unaligned store side 0 | 17 | 1, 2, 5, 6 | 3: LSU1 2|3 | 0: LSU1 |
|  |  |  | 3: LSU1 2|7 |  |
|  |  |  | 3: LSU1 6|3 |  |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] flush unaligned store side 0 + flush unaligned store side 1 | 0 | 2 | 3: LSU1 2|3 | 0: LSU1 |
|  |  |  | 3: LSU1 2|7 |  |
|  |  |  | 3: LSU1 6|3 |  |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] flush unaligned store side 1 | 21 | 1, 2, 5, 6 | 3: LSU1 2|3 | 0: LSU1 |
|  |  |  | 3: LSU1 2|7 |  |
|  |  |  | 3: LSU1 6|3 |  |
|  |  |  | 3: LSU1 6|7 |  |
|  | 29 | 5 | 0: FPU | 2: TTM0 |
|  |  |  | 0: ISU |  |
|  |  |  | 0: IFU |  |
|  |  |  | 0: VMX |  |
|  |  |  | 1: IDU | 2: TTM1 |
|  |  |  | 1: ISU |  |
|  |  |  | 1: GPS |  |
|  |  |  |  | 2: LSU0 |
|  |  |  | 3: LSU1 2|3 | 2: LSU1 |
|  |  |  | 3: LSU1 2|7 |  |
|  |  |  | 3: LSU1 6|3 |  |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] L1 d cache store miss | 19 | 3, 4, 7, 8 | 3: LSU1 2|3 | 1: LSU1 |
|  |  |  | 3: LSU1 2|7 |  |
|  |  |  | 3: LSU1 6|3 |  |
|  |  |  | 3: LSU1 6|7 |  |
|  | 27 | 1, 2, 5, 6 | 3: LSU1 2|3 | 2: LSU1 |
|  |  |  | 3: LSU1 2|7 |  |
| [LSU1] L1 d cache store miss + L1 dcache entries invalidated from L2 | 0 | 4 | 3: LSU1 2|3 | 1: LSU1 |
|  |  |  | 3: LSU1 2|7 |  |
|  |  |  | 3: LSU1 6|3 |  |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] L1 d cache store miss + LSU ls1 reject | 32 | 5 | 3: LSU1 2|3 | 2: LSU1 |
|  |  |  | 3: LSU1 2|7 |  |
| [LSU1] L1 dcache entries invalidated from L2 | 23 | 3, 4, 7, 8 | 3: LSU1 2|3 | 1: LSU1 |
|  |  |  | 3: LSU1 2|7 |  |
|  |  |  | 3: LSU1 6|3 |  |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] L1 dcache load miss side 0 | 18 | 3, 4, 7, 8 | 3: LSU1 2|3 | 1: LSU1 |
|  |  |  | 3: LSU1 2|7 |  |
|  |  |  | 3: LSU1 6|3 |  |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] L1 dcache load miss side 0 + L1 dcache load miss side 1 | 0 | 3 | 3: LSU1 2|3 | 1: LSU1 |
|  |  |  | 3: LSU1 2|7 |  |
|  |  |  | 3: LSU1 6|3 |  |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] L1 dcache load miss side 1 | 22 | 3, 4, 7, 8 | 3: LSU1 2|3 | 1: LSU1 |
|  |  |  | 3: LSU1 2|7 |  |
|  |  |  | 3: LSU1 6|3 |  |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] L1 dcache load side 0 | 16 | 3, 4, 7, 8 | 3: LSU1 2|3 | 1: LSU1 |
|  |  |  | 3: LSU1 2|7 |  |
|  |  |  | 3: LSU1 6|3 |  |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] L1 dcache load side 0 + L1 dcache load side 1 | 0 | 8 | 3: LSU1 2|3 | 1: LSU1 |
|  |  |  | 3: LSU1 2|7 |  |
|  |  |  | 3: LSU1 6|3 |  |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] L1 dcache load side 1 | 20 | 3, 4, 7, 8 | 3: LSU1 2|3 | 1: LSU1 |
|  |  |  | 3: LSU1 2|7 |  |
|  |  |  | 3: LSU1 6|3 |  |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] L1 dcache store side 0 | 17 | 3, 4, 7, 8 | 3: LSU1 2|3 | 1: LSU1 |
|  |  |  | 3: LSU1 2|7 |  |
|  |  |  | 3: LSU1 6|3 |  |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] L1 dcache store side 0 + L1 dcache store side 1 | 0 | 7 | 3: LSU1 2|3 | 1: LSU1 |
|  |  |  | 3: LSU1 2|7 |  |
|  |  |  | 3: LSU1 6|3 |  |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] L1 dcache store side 1 | 21 | 3, 4, 7, 8 | 3: LSU1 2|3 | 1: LSU1 |
|  |  |  | 3: LSU1 2|7 |  |
|  |  |  | 3: LSU1 6|3 |  |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] L1 reload data source | 24, 25, 26, 27, 24, 25, 26, 27, 24, 25, 26, 27, 24, 25, 26, 27 | 3, 4, 4, 4, 4, 7, 7, 7, 7, 8, 8, 8, 8 | 3: LSU1 2|3 | 3: LSU1 |
|  |  |  | 3: LSU1 2|7 |  |
|  |  |  | 3: LSU1 6|3 |  |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] L1 reload data source + L1 reload data valid | 32 | 8 | 3: LSU1 2|3 | 3: LSU1 |
|  |  |  | 3: LSU1 6|3 |  |
| [LSU1] L1 reload data source + LMQ full | 32 | 4 | 3: LSU1 2|3 | 3: LSU1 |
|  |  |  | 3: LSU1 6|3 |  |
| [LSU1] L1 reload data source + LMQ load hit reload merge | 32 | 7 | 3: LSU1 2|7 | 3: LSU1 |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] L1 reload data source + LMQ slot 0 allocated | 32 | 3 | 3: LSU1 2|3 | 3: LSU1 |
|  |  |  | 3: LSU1 6|3 |  |
| [LSU1] L1 reload data source + LMQ slot 0 valid | 32 | 7 | 3: LSU1 2|3 | 3: LSU1 |
|  |  |  | 3: LSU1 6|3 |  |
| [LSU1] L1 reload data source + Marked L1 reload data source valid | 32 | 8 | 3: LSU1 2|7 | 3: LSU1 |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] L1 reload data source + Marked SRQ valid | 32 | 3 | 3: LSU1 2|7 | 3: LSU1 |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] L1 reload data source + nothing | 32 | 4 | 3: LSU1 2|7 | 3: LSU1 |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] L1 reload data valid | 28 | 3, 4, 7, 8 | 3: LSU1 2|3 | 3: LSU1 |
|  |  |  | 3: LSU1 6|3 |  |
| [LSU1] LMQ full | 31 | 3, 4, 7, 8 | 3: LSU1 2|3 | 3: LSU1 |
|  |  |  | 3: LSU1 6|3 |  |
| [LSU1] LMQ load hit reload merge | 29 | 3, 4, 7, 8 | 3: LSU1 2|7 | 3: LSU1 |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] LMQ reject 0 - LMQ full or missed data coming | 25 | 1, 2, 5, 6 | 3: LSU1 6|3 | 2: LSU1 |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] LMQ reject 0 - LMQ full or missed data coming + LMQ reject 1- LMQ full or missed data coming | 32 | 2 | 3: LSU1 6|3 | 2: LSU1 |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] LMQ reject 1- LMQ full or missed data coming | 29 | 1, 2, 6 | 3: LSU1 6|3 | 2: LSU1 |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] LMQ slot 0 allocated | 30 | 3, 4, 7, 8 | 3: LSU1 2|3 | 3: LSU1 |
|  |  |  | 3: LSU1 6|3 |  |
| [LSU1] LMQ slot 0 valid | 29 | 3, 4, 7, 8 | 3: LSU1 2|3 | 3: LSU1 |
|  |  |  | 3: LSU1 6|3 |  |
| [LSU1] LRQ slot 0 allocated | 30 | 1, 2, 5, 6 | 3: LSU1 2|3 | 2: LSU1 |
|  |  |  | 3: LSU1 2|7 |  |
| [LSU1] LRQ slot 0 valid | 26 | 1, 2, 5, 6 | 3: LSU1 2|3 | 2: LSU1 |
|  |  |  | 3: LSU1 2|7 |  |
| [LSU1] LRQ slot 0 valid + LRQ slot 0 allocated | 32 | 6 | 3: LSU1 2|3 | 2: LSU1 |
|  |  |  | 3: LSU1 2|7 |  |
| [LSU1] LS0 reject - erat miss. | 27 | 1, 2, 5, 6 | 3: LSU1 6|3 | 2: LSU1 |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] LS0 reject - erat miss. + LS1 reject - erat miss | 32 | 5 | 3: LSU1 6|3 | 2: LSU1 |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] LS0 reject - reload cdf or tag updata collision | 26 | 1, 2, 5, 6 | 3: LSU1 6|3 | 2: LSU1 |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] LS0 reject - reload cdf or tag updata collision + LS1 reject - reload cdf or tag updata collision | 32 | 6 | 3: LSU1 6|3 | 2: LSU1 |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] LS1 reject - erat miss | 31 | 1, 2, 5, 6 | 3: LSU1 6|3 | 2: LSU1 |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] LS1 reject - reload cdf or tag updata collision | 30 | 1, 2, 5, 6 | 3: LSU1 6|3 | 2: LSU1 |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] LSU ls1 reject | 31 | 1, 2, 5, 6 | 3: LSU1 2|3 | 2: LSU1 |
|  |  |  | 3: LSU1 2|7 |  |
| [LSU1] Marked L1 reload data source valid | 28 | 3, 4, 7, 8 | 3: LSU1 2|7 | 3: LSU1 |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] Marked SRQ valid | 30 | 3, 4, 7, 8 | 3: LSU1 2|7 | 3: LSU1 |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] SRQ reject 0 - load hit store | 24 | 1, 2, 5, 6 | 3: LSU1 6|3 | 2: LSU1 |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] SRQ reject 0 - load hit store + SRQ reject 1- load hit store | 32 | 1 | 3: LSU1 6|3 | 2: LSU1 |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] SRQ reject 1- load hit store | 28 | 1, 2, 5, 6 | 3: LSU1 6|3 | 2: LSU1 |
|  |  |  | 3: LSU1 6|7 |  |
| [LSU1] SRQ slot 0 allocated | 29 | 1, 2, 6 | 3: LSU1 2|3 | 2: LSU1 |
|  |  |  | 3: LSU1 2|7 |  |
| [LSU1] SRQ slot 0 valid | 25 | 1, 2, 5, 6 | 3: LSU1 2|3 | 2: LSU1 |
|  |  |  | 3: LSU1 2|7 |  |
| [LSU1] SRQ slot 0 valid + SRQ slot 0 allocated | 32 | 2 | 3: LSU1 2|3 | 2: LSU1 |
|  |  |  | 3: LSU1 2|7 |  |
| [LSU1] SRQ store forwarding side 0 | 24 | 1, 2, 5, 6 | 3: LSU1 2|3 | 2: LSU1 |
|  |  |  | 3: LSU1 2|7 |  |
| [LSU1] SRQ store forwarding side 0 + SRQ store forwarding side 1 | 32 | 1 | 3: LSU1 2|3 | 2: LSU1 |
|  |  |  | 3: LSU1 2|7 |  |
| [LSU1] SRQ store forwarding side 1 | 28 | 1, 2, 5, 6 | 3: LSU1 2|3 | 2: LSU1 |
|  |  |  | 3: LSU1 2|7 |  |
| [SPECA] reserved | 11 | 5 |  |  |
| [SPECB] reserved | 11 | 7 |  |  |
| [SPECC] reserved | 12 | 5 |  |  |
| [SPECD] reserved | 12 | 7 |  |  |
| [VMX] ALU issue marked inst | 18 | 1, 2, 5, 6 | 0: VMX | 0: TTM0 |
| [VMX] ALU issue marked inst + Store issue marked inst | 0 | 6 | 0: VMX | 0: TTM0 |
| [VMX] ALU issue queue full | 16 | 1, 2, 5, 6 | 0: VMX | 0: TTM0 |
| [VMX] ALU issue queue full + Sat zero to one | 0 | 1 | 0: VMX | 0: TTM0 |
| [VMX] Denorm traps | 19 | 3, 4, 7, 8 | 0: VMX | 1: TTM0 |
| [VMX] Denorm traps + nothing | 0 | 4 | 0: VMX | 1: TTM0 |
| [VMX] finish contention cycle | 21 | 3, 4, 7, 8 | 0: VMX | 1: TTM0 |
| [VMX] Finish with IMR | 16 | 3, 4, 7, 8 | 0: VMX | 1: TTM0 |
| [VMX] Finish with IMR + Sat bit set | 0 | 8 | 0: VMX | 1: TTM0 |
| [VMX] forwarding occurred from perm or alu or load | 29 | 1, 2, 6 | 0: VMX | 2: TTM0 |
| [VMX] Generic forward | 17 | 3, 4, 7, 8 | 0: VMX | 1: TTM0 |
| [VMX] Generic forward + finish contention cycle | 0 | 7 | 0: VMX | 1: TTM0 |
| [VMX] instruction finish with IMR | 28 | 1, 2, 5, 6 | 0: VMX | 2: TTM0 |
| [VMX] issue valid | 30 | 1, 2, 5, 6 | 0: VMX | 2: TTM0 |
| [VMX] Perm issue marked inst | 19 | 1, 2, 5, 6 | 0: VMX | 0: TTM0 |
| [VMX] Perm issue marked inst + nothing | 0 | 5 | 0: VMX | 0: TTM0 |
| [VMX] Perm issue queue full | 17 | 1, 2, 5, 6 | 0: VMX | 0: TTM0 |
| [VMX] Perm issue queue full + VMX mapper full | 0 | 2 | 0: VMX | 0: TTM0 |
| [VMX] Sat bit set | 20 | 3, 4, 7, 8 | 0: VMX | 1: TTM0 |
| [VMX] Sat zero to one | 20 | 1, 2, 5, 6 | 0: VMX | 0: TTM0 |
| [VMX] saturation count for valid instruction | 31 | 1, 2, 5, 6 | 0: VMX | 2: TTM0 |
| [VMX] Store issue marked inst | 22 | 1, 2, 5, 6 | 0: VMX | 0: TTM0 |
| [VMX] VMA issue count | 18 | 3, 4, 7, 8 | 0: VMX | 1: TTM0 |
| [VMX] VMA issue count + nothing | 0 | 3 | 0: VMX | 1: TTM0 |
| [VMX] VMX mapper full | 21 | 1, 2, 5, 6 | 0: VMX | 0: TTM0 |
| BRU marked instr finish | 5 | 2 |  |  |
| Completion Stall by other reason | 11 | 1 |  |  |
| CPU Cycles | 15 | 1, 2, 3, 4, 5, 6, 7, 8 |  |  |
| CPU Cycles (hypervisor) | 4 | 3 |  |  |
| CPU Marked Instruction finish | 5 | 4 |  |  |
| Dispatch Successes | 1 | 5 |  |  |
| dL2 Hit (dL1 reload from L2) | 7 | 1 |  | 3: LSU1 |
| dL2 Miss (dL1 reload from Memory) | 7 | 3 |  | 3: LSU1 |
| External Interrupt | 2 | 8 |  |  |
| FPU marked instruction finish | 4 | 7 |  |  |
| FXU Marked Instr finish | 4 | 6 |  |  |
| FXU0 busy and FXU1 busy | 2 | 6 |  |  |
| FXU0 busy and FXU1 idle | 2 | 7 |  |  |
| FXU0 Idle and FXU1 Busy | 2 | 4 |  |  |
| FXU0 idle and FXU1 idle | 2 | 5 |  |  |
| GCT Empty | 4 | 1 |  |  |
| GCT empty by SRQ full | 11 | 2 |  |  |
| Group Completed | 3 | 7 |  |  |
| Group Dispatch | 4 | 2 |  |  |
| Group Dispatch Reject | 3 | 8 |  |  |
| Group Marked in IDU | 4 | 5 |  |  |
| iL2 Hit (iL1 reload from L2) | 6 | 1 | 0: IFU | 2: TTM0 |
| iL2 Miss (iL1 reload from Memory) | 6 | 3 | 0: IFU | 2: TTM0 |
| Instr Completed (ppc) | 9 | 1, 2, 3, 4, 5, 6, 7, 8 |  |  |
| Instr Completed (ppc,io,ld/st) | 1 | 4, 6, 7, 8 |  |  |
| Instr Src Encode 0 (Lane 2 not set to IFU) | 6 | 1 | 0: FPU | 2: TTM0 |
|  |  |  | 0: ISU |  |
|  |  |  | 0: VMX |  |
|  |  |  | 0: FPU | 2: TTM1 |
|  |  |  | 0: ISU |  |
|  |  |  | 0: IFU |  |
|  |  |  | 0: VMX |  |
|  |  |  | 0: FPU | 2: LSU0 |
|  |  |  | 0: ISU |  |
|  |  |  | 0: IFU |  |
|  |  |  | 0: VMX |  |
|  |  |  | 0: FPU | 2: LSU1 |
|  |  |  | 0: ISU |  |
|  |  |  | 0: IFU |  |
|  |  |  | 0: VMX |  |
| Instr Src Encode 1 (Lane 2 not set to IFU) | 6 | 2 | 0: FPU | 2: TTM0 |
|  |  |  | 0: ISU |  |
|  |  |  | 0: VMX |  |
|  |  |  | 0: FPU | 2: TTM1 |
|  |  |  | 0: ISU |  |
|  |  |  | 0: IFU |  |
|  |  |  | 0: VMX |  |
|  |  |  | 0: FPU | 2: LSU0 |
|  |  |  | 0: ISU |  |
|  |  |  | 0: IFU |  |
|  |  |  | 0: VMX |  |
|  |  |  | 0: FPU | 2: LSU1 |
|  |  |  | 0: ISU |  |
|  |  |  | 0: IFU |  |
|  |  |  | 0: VMX |  |
| Instr Src Encode 2 (Lane 2 not set to IFU) | 6 | 3 | 0: FPU | 2: TTM0 |
|  |  |  | 0: ISU |  |
|  |  |  | 0: VMX |  |
|  |  |  | 0: FPU | 2: TTM1 |
|  |  |  | 0: ISU |  |
|  |  |  | 0: IFU |  |
|  |  |  | 0: VMX |  |
|  |  |  | 0: FPU | 2: LSU0 |
|  |  |  | 0: ISU |  |
|  |  |  | 0: IFU |  |
|  |  |  | 0: VMX |  |
|  |  |  | 0: FPU | 2: LSU1 |
|  |  |  | 0: ISU |  |
|  |  |  | 0: IFU |  |
|  |  |  | 0: VMX |  |
| Instr Src Encode 3 (Lane 2 not set to IFU) | 6 | 4 | 0: FPU | 2: TTM0 |
|  |  |  | 0: ISU |  |
|  |  |  | 0: VMX |  |
|  |  |  | 0: FPU | 2: TTM1 |
|  |  |  | 0: ISU |  |
|  |  |  | 0: IFU |  |
|  |  |  | 0: VMX |  |
|  |  |  | 0: FPU | 2: LSU0 |
|  |  |  | 0: ISU |  |
|  |  |  | 0: IFU |  |
|  |  |  | 0: VMX |  |
|  |  |  | 0: FPU | 2: LSU1 |
|  |  |  | 0: ISU |  |
|  |  |  | 0: IFU |  |
|  |  |  | 0: VMX |  |
| Instr Src Encode 4 (Lane 2 not set to IFU) | 6 | 5 | 0: FPU | 2: TTM0 |
|  |  |  | 0: ISU |  |
|  |  |  | 0: VMX |  |
|  |  |  | 0: FPU | 2: TTM1 |
|  |  |  | 0: ISU |  |
|  |  |  | 0: IFU |  |
|  |  |  | 0: VMX |  |
|  |  |  | 0: FPU | 2: LSU0 |
|  |  |  | 0: ISU |  |
|  |  |  | 0: IFU |  |
|  |  |  | 0: VMX |  |
|  |  |  | 0: FPU | 2: LSU1 |
|  |  |  | 0: ISU |  |
|  |  |  | 0: IFU |  |
|  |  |  | 0: VMX |  |
| Instr Src Encode 5 (Lane 2 not set to IFU) | 6 | 6 | 0: FPU | 2: TTM0 |
|  |  |  | 0: ISU |  |
|  |  |  | 0: VMX |  |
|  |  |  | 0: FPU | 2: TTM1 |
|  |  |  | 0: ISU |  |
|  |  |  | 0: IFU |  |
|  |  |  | 0: VMX |  |
|  |  |  | 0: FPU | 2: LSU0 |
|  |  |  | 0: ISU |  |
|  |  |  | 0: IFU |  |
|  |  |  | 0: VMX |  |
|  |  |  | 0: FPU | 2: LSU1 |
|  |  |  | 0: ISU |  |
|  |  |  | 0: IFU |  |
|  |  |  | 0: VMX |  |
| Instr Src Encode 6 (Lane 2 not set to IFU) | 6 | 7 | 0: FPU | 2: TTM0 |
|  |  |  | 0: ISU |  |
|  |  |  | 0: VMX |  |
|  |  |  | 0: FPU | 2: TTM1 |
|  |  |  | 0: ISU |  |
|  |  |  | 0: IFU |  |
|  |  |  | 0: VMX |  |
|  |  |  | 0: FPU | 2: LSU0 |
|  |  |  | 0: ISU |  |
|  |  |  | 0: IFU |  |
|  |  |  | 0: VMX |  |
|  |  |  | 0: FPU | 2: LSU1 |
|  |  |  | 0: ISU |  |
|  |  |  | 0: IFU |  |
|  |  |  | 0: VMX |  |
| Instr Src Encode 7 (Lane 2 not set to IFU) | 6 | 8 | 0: FPU | 2: TTM0 |
|  |  |  | 0: ISU |  |
|  |  |  | 0: VMX |  |
|  |  |  | 0: FPU | 2: TTM1 |
|  |  |  | 0: ISU |  |
|  |  |  | 0: IFU |  |
|  |  |  | 0: VMX |  |
|  |  |  | 0: FPU | 2: LSU0 |
|  |  |  | 0: ISU |  |
|  |  |  | 0: IFU |  |
|  |  |  | 0: VMX |  |
|  |  |  | 0: FPU | 2: LSU1 |
|  |  |  | 0: ISU |  |
|  |  |  | 0: IFU |  |
|  |  |  | 0: VMX |  |
| Instructions Completed (ppc,io,ld/st) | 1 | 1 |  |  |
| LSU empty (LMQ and SRQ empty) | 2 | 2, 3 |  |  |
| LSU Marked Instr finish | 4 | 8 |  |  |
| Marked Group complete | 4 | 4 |  |  |
| Marked Group Complete Timeout | 5 | 5 |  |  |
| Marked group dispatch | 2 | 1 |  |  |
| Marked Group issued | 5 | 6 |  |  |
| Marked Instr finish in any unit | 5 | 7 |  |  |
| Marked store complete | 3 | 1 |  |  |
| Marked Store Complete w/int. | 3 | 3 |  |  |
| Marked Store sent to GPS | 3 | 6 |  |  |
| Nothing | 8 | 1, 2, 3, 4, 5, 6, 7, 8 |  |  |
| Overflow from PMC1 | 10 | 2 |  |  |
| Overflow from PMC2 | 10 | 3 |  |  |
| Overflow from PMC3 | 10 | 4 |  |  |
| Overflow from PMC4 | 10 | 5 |  |  |
| Overflow from PMC5 | 10 | 6 |  |  |
| Overflow from PMC6 | 10 | 7 |  |  |
| Overflow from PMC7 | 10 | 8 |  |  |
| Overflow from PMC8 | 10 | 1 |  |  |
| Run Cycles | 5 | 1 |  |  |
| SRQ empty | 3 | 4 |  |  |
| Stop Completion | 1 | 3 |  |  |
| Threshold Timeout | 3 | 2 |  |  |
| Timebase Event | 5 | 8 |  |  |
| VMX Marked Instruction finish | 5 | 3 |  |  |
| Work Held | 1 | 2 |  |  |

[Next](UniNorth-2%20%28U1.5-2%29%20Performance%20Counter%20Event%20List.md)[Previous](PPC%207450%20%28G4%2B%29%20Performance%20Counter%20Event%20List.md)

