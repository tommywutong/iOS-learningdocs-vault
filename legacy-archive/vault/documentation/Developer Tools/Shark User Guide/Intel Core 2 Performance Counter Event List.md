---
title: Shark User Guide
apple_id: TP40005233
resource_type: Guide
platform: iOS|macOS
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/SharkUserGuide/IntelCore2PMCTablesAppendix/IntelCore2PMCTablesAppendix.html
archived_at: '2026-07-15T07:26:09.128677Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Shark User Guide](Introduction.md)


[Next](PPC%20750%20%28G3%29%20Performance%20Counter%20Event%20List.md)[Previous](Intel%20Core%20Performance%20Counter%20Event%20List.md)

# Intel Core 2 Performance Counter Event List

Intel’s Core 2 processors have 5 performance counters per core. Two of these are fully programmable, and can count 116 (#1) or 115 (#2) different types of events. The other three counters are fixed, and can only count one type of event (for counter 3: INSTR_RETIRED.ANY, 4: CPU_CLK_UNHALTED.CORE, and 5: CPU_CLK_UNHALTED.REF).

In addition, the available events can be modified by enabling any of the eight _Event-Mask_ bits associated with each programmable counter. The event-mask bits are critical to determining exactly which events will be counted. Most of the events can be selected without enabling any event-mask bits at all. The mask bits just modify the type of event slightly or the way the counter gets incremented when the event occurs. In particular, the mask settings often act as an event filter, limiting or expanding the selection of related events that can be counted simultaneously. In contrast, for some types of events you_must_ set event-mask bits properly, in order to count anything at all. These bits are labeled ‘Required’ in the event-mask bit list.

The table below lists each Event Name, the counter (PMC) number(s) for counters which can count the event, the event’s number, and the valid mask bits that can be enabled, for every useful event type. This last column lists mask bits using numbers between 0 and 7. Missing numbers indicate bits that are reserved and should not be enabled. If no mask bits are valid for that type of event, then “none” is listed.

In Shark, more complete documentation as to what the event names mean and how each mask bit modifies the count are provided as “tool-tips” when you hover the mouse over an event name in the popup menu, or over a specific bit name in the event-mask list. The event-mask bit controls are only accessible from the _Advanced View_ controls shown in the [Timed Counters: The Performance Counter Spreadsheet](Other%20Profiling%20and%20Tracing%20Techniques.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqnrnknlto).

For more information on how to configure these counters, see [Intel CPU Performance Counter Configuration](Hardware%20Counter%20Configuration.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqmjqfvjvomjx).

| Performance Counter Event Name | Event Number | PMC Number | Valid Event-Mask Bits |
| --- | --- | --- | --- |
| BACLEARS | 230 | 1 | none |
|  |  | 2 | 0 |
| BR_BAC_MISSP_EXEC | 138 | 1 | none |
|  |  | 2 | 0 |
| BR_BOGUS | 228 | 1 | none |
|  |  | 2 | 0 |
| BR_CALL_EXEC | 146 | 1 | none |
|  |  | 2 | 0 |
| BR_CALL_MISSP_EXEC | 147 | 1 | none |
|  |  | 2 | 0 |
| BR_CND_EXEC | 139 | 1 | none |
|  |  | 2 | 0 |
| BR_CND_MISSP_EXEC | 140 | 1 | none |
|  |  | 2 | 0 |
| BR_IND_CALL_EXEC | 148 | 1 | none |
|  |  | 2 | 0 |
| BR_IND_EXEC | 141 | 1 | none |
|  |  | 2 | 0 |
| BR_IND_MISSP_EXEC | 142 | 1 | none |
|  |  | 2 | 0 |
| BR_INST_DECODED | 224 | 1 | none |
|  |  | 2 | 0 |
| BR_INST_EXEC | 136 | 1 | none |
|  |  | 2 | 0 |
| BR_INST_RETIRED | 196 | 1 | 0 1 2 3 6 7 |
|  |  | 2 | 0 2 3 4 5 6 7 |
| BR_INST_RETIRED.MISPRED | 197 | 1 | none |
|  |  | 2 | 0 2 3 4 5 |
| BR_MISSP_EXEC | 137 | 1 | none |
|  |  | 2 | 0 |
| BR_RET_BAC_MISSP_EXEC | 145 | 1 | none |
|  |  | 2 | 0 |
| BR_RET_EXEC | 143 | 1 | none |
|  |  | 2 | 0 |
| BR_RET_MISSP_EXEC | 144 | 1 | none |
|  |  | 2 | 0 |
| BR_TKN_BUBBLE_1 | 151 | 1 | none |
|  |  | 2 | 0 |
| BR_TKN_BUBBLE_2 | 152 | 1 | none |
|  |  | 2 | 0 |
| BUS_BNR_DRV | 97 | 1 | 5 |
|  |  | 2 | 0 |
| BUS_DATA_RCV | 100 | 1 | 6 7 |
|  |  | 2 | 0 7 |
| BUS_DRDY_CLOCKS | 98 | 1 | 5 |
|  |  | 2 | 0 |
| BUS_HIT_DRV | 122 | 1 | 5 |
|  |  | 2 | 0 2 3 5 7 |
| BUS_HITM_DRV | 123 | 1 | 5 |
|  |  | 2 | 0 2 3 |
| BUS_IO_WAIT | 127 | 1 | 6 7 |
|  |  | 2 | 0 |
| BUS_LOCK_CLOCKS (Core and Bus Agents masks apply) | 99 | 1 | 5 6 7 |
|  |  | 2 | 0 6 7 |
| BUS_REQ_OUTSTANDING | 96 | 1 | 4 5 6 7 |
|  |  | 2 | 0 |
| BUS_TRAN_RFO | 102 | 1 | 5 6 7 |
|  |  | 2 | 0 7 |
| BUS_TRANS_ANY | 112 | 1 | 5 6 7 |
|  |  | 2 | 0 7 |
| BUS_TRANS_BRD | 101 | 1 | 5 6 7 |
|  |  | 2 | 0 7 |
| BUS_TRANS_BURST | 110 | 1 | 5 6 7 |
|  |  | 2 | 0 7 |
| BUS_TRANS_DEF | 109 | 1 | 5 6 7 |
|  |  | 2 | 0 7 |
| BUS_TRANS_IFETCH | 104 | 1 | 5 6 7 |
|  |  | 2 | 0 7 |
| BUS_TRANS_INVAL | 105 | 1 | 5 6 7 |
|  |  | 2 | 0 7 |
| BUS_TRANS_IO | 108 | 1 | 5 6 7 |
|  |  | 2 | 0 7 |
| BUS_TRANS_MEM | 111 | 1 | 5 6 7 |
|  |  | 2 | 0 7 |
| BUS_TRANS_P | 107 | 1 | 5 6 7 |
|  |  | 2 | 0 7 |
| BUS_TRANS_PWR | 106 | 1 | 5 6 7 |
|  |  | 2 | 0 7 |
| BUS_TRANS_WB | 103 | 1 | 5 6 7 |
|  |  | 2 | 0 |
| BUSQ_EMPTY | 125 | 1 | 6 7 |
|  |  | 2 | 0 7 |
| CMP_SNOOP | 120 | 1 | 0 1 6 7 |
|  |  | 2 | 0 |
| CPU_CLK_UNHALTED | 60 | 1 | 0 1 |
|  |  | 2 | 0 |
| CPU_CLK_UNHALTED.CORE | 0 | 4 | none |
| CPU_CLK_UNHALTED.REF | 0 | 5 | none |
| CYCLES_DIV_BUSY | 20 | 1 | none |
| CYCLES_INT | 198 | 1 | 0 1 |
|  |  | 2 | 0 2 4 |
| CYCLES_L1I_MEM_STALLED | 134 | 1 | none |
|  |  | 2 | 0 3 |
| DELAYED_BYPASS | 25 | 2 | 0 |
| DIVIDES | 19 | 2 | 0 |
| DTLB_MISSES | 8 | 1 | 0 1 2 3 |
|  |  | 2 | 0 |
| EIST_TRANS | 58 | 1 | none |
|  |  | 2 | 0 |
| ESP Register | 171 | 1 | 0 1 |
|  |  | 2 | 0 |
| EXT_SNOOP | 119 | 1 | 0 1 3 5 |
|  |  | 2 | 0 |
| FP_ASSIST | 17 | 2 | 0 |
| FP_COMP_OPS_EXE | 16 | 1 | none |
| FP_MMX_TRANS | 204 | 1 | 0 1 |
|  |  | 2 | 0 |
| HW_INT_RCV | 200 | 1 | none |
|  |  | 2 | 0 |
| IDLE_DURING_DIV | 24 | 1 | none |
| ILD_STALL | 135 | 1 | none |
|  |  | 2 | 0 |
| INST_QUEUE.FULL | 131 | 1 | 1 |
|  |  | 2 | 0 |
| INST_RETIRED | 192 | 1 | 0 1 2 |
|  |  | 2 | 0 |
| INSTR_RETIRED.ANY | 0 | 3 | none |
| ITLB | 130 | 1 | 1 4 6 |
|  |  | 2 | 0 |
| ITLB_MISS_RETIRED | 201 | 1 | none |
|  |  | 2 | 0 2 3 |
| L1D_ALL_REF | 67 | 1 | 0 1 |
|  |  | 2 | 0 2 3 4 5 |
| L1D_CACHE_LD | 64 | 1 | 0 1 2 3 |
|  |  | 2 | 0 |
| L1D_CACHE_LOCK | 66 | 1 | 0 1 2 3 4 |
|  |  | 2 | 0 |
| L1D_CACHE_ST | 65 | 1 | 0 1 2 3 |
|  |  | 2 | 0 |
| L1D_M_EVICT | 71 | 1 | none |
|  |  | 2 | 0 |
| L1D_M_REPL | 70 | 1 | none |
|  |  | 2 | 0 2 3 |
| L1D_PEND_MISS | 72 | 1 | none |
|  |  | 2 | 0 2 3 4 5 |
| L1D_PREFETCH.REQUESTS | 78 | 1 | 4 |
|  |  | 2 | 0 2 3 |
| L1D_REPL | 69 | 1 | 0 1 2 3 |
|  |  | 2 | 0 2 3 4 5 6 |
| L1D_SPLIT | 73 | 1 | 0 1 |
|  |  | 2 | 0 |
| L1I_MISSES | 129 | 1 | none |
|  |  | 2 | 0 6 7 |
| L1I_READS | 128 | 1 | none |
|  |  | 2 | 0 |
| L2_ADS | 33 | 1 | 6 7 |
|  |  | 2 | 0 |
| L2_DBUS_BUSY_RD | 35 | 1 | 6 7 |
|  |  | 2 | 0 |
| L2_IFETCH | 40 | 1 | 0 1 2 3 6 7 |
|  |  | 2 | 0 |
| L2_LD | 41 | 1 | 0 1 2 3 4 5 6 7 |
|  |  | 2 | 0 6 7 |
| L2_LINES_IN | 36 | 1 | 4 5 6 7 |
|  |  | 2 | 0 |
| L2_LINES_OUT | 38 | 1 | 4 5 6 7 |
|  |  | 2 | 0 |
| L2_LOCK | 43 | 1 | 0 1 2 3 4 5 6 7 |
|  |  | 2 | 0 2 3 4 5 |
| L2_M_LINES_IN | 37 | 1 | 6 7 |
|  |  | 2 | 0 |
| L2_M_LINES_OUT | 39 | 1 | 4 5 6 7 |
|  |  | 2 | 0 6 7 |
| L2_NO_REQ | 50 | 1 | 6 7 |
|  |  | 2 | 0 |
| L2_REJECT_BUSQ | 48 | 1 | 0 1 2 3 4 5 6 7 |
|  |  | 2 | 0 |
| L2_RQSTS | 46 | 1 | 0 1 2 3 4 5 6 7 |
|  |  | 2 | 0 2 3 4 5 6 7 |
| L2_ST | 42 | 1 | 0 1 2 3 6 7 |
|  |  | 2 | 0 6 7 |
| LOAD_BLOCK | 3 | 1 | 1 2 3 4 5 |
|  |  | 2 | 0 |
| LOAD_HIT_PRE | 76 | 1 | none |
|  |  | 2 | 0 2 3 |
| MACHINE_NUKES | 195 | 1 | 0 2 |
|  |  | 2 | 0 2 3 4 |
| MACRO_INSTS.CISC_DECODED | 170 | 1 | 3 |
|  |  | 2 | 0 |
| MEM_LOAD_RETIRED | 203 | 1 | none |
| MEMORY_DISAMBIGUATION | 9 | 1 | 0 1 |
|  |  | 2 | 0 |
| MISALIGN_MEM_REF | 5 | 1 | none |
|  |  | 2 | 0 |
| MULTIPLIES | 18 | 2 | 0 |
| PAGE_WALKS | 12 | 1 | 0 1 |
|  |  | 2 | 0 2 3 |
| PREF_RQSTS_DN | 248 | 1 | none |
|  |  | 2 | 0 |
| PREF_RQSTS_UP | 240 | 1 | none |
|  |  | 2 | 0 |
| RAT_STALLS | 210 | 1 | 0 1 2 3 |
|  |  | 2 | 0 |
| RESOURCE_STALLS | 220 | 1 | 0 1 2 3 4 |
|  |  | 2 | 0 |
| RS_UOPS_DISPATCHED | 160 | 1 | none |
|  |  | 2 | 0 |
| SEG_REG_RENAMES | 213 | 1 | 0 1 2 3 |
|  |  | 2 | 0 2 3 4 5 |
| SEG_RENAME_STALLS | 212 | 1 | 0 1 2 3 |
|  |  | 2 | 0 |
| SEGMENT_REG_LOADS | 6 | 1 | none |
|  |  | 2 | 0 3 4 5 6 7 |
| SIMD_ASSIST | 205 | 1 | none |
|  |  | 2 | 0 2 3 4 5 |
| SIMD_COMP_INST_RETIRED | 202 | 1 | 0 1 2 3 |
|  |  | 2 | 0 2 3 4 5 6 |
| SIMD_INST_RETIRED | 199 | 1 | 0 1 2 3 4 |
|  |  | 2 | 0 2 3 4 5 |
| SIMD_INSTR_RETIRED | 206 | 1 | none |
|  |  | 2 | 0 2 3 4 5 6 |
| SIMD_SAT_INSTR_RETIRED | 207 | 1 | none |
|  |  | 2 | 0 2 3 |
| SIMD_SAT_UOP_EXEC | 177 | 1 | none |
|  |  | 2 | 0 |
| SIMD_UOP_TYPE_EXEC | 179 | 1 | 0 1 2 3 4 5 |
|  |  | 2 | 0 |
| SIMD_UOPS_EXEC | 176 | 1 | none |
|  |  | 2 | 0 |
| SNOOP_STALL_DRV | 126 | 1 | 4 5 6 7 |
|  |  | 2 | 0 7 |
| SSE_PRE_EXEC | 7 | 1 | 0 1 |
|  |  | 2 | 0 2 3 5 |
| SSE_PRE_MISS | 75 | 1 | 0 1 |
|  |  | 2 | 0 |
| STORES BLOCKED | 4 | 1 | 0 1 3 |
|  |  | 2 | 0 |
| THERMAL_TRIP | 59 | 1 | 6 7 |
|  |  | 2 | 0 |
| UOPS_RETIRED | 194 | 1 | 0 1 2 3 |
|  |  | 2 | 0 |
| X87_OPS_RETIRED | 193 | 1 | 0 1 2 3 4 5 6 |
|  |  | 2 | 0 |

[Next](PPC%20750%20%28G3%29%20Performance%20Counter%20Event%20List.md)[Previous](Intel%20Core%20Performance%20Counter%20Event%20List.md)

