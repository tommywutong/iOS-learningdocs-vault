---
title: Shark User Guide
apple_id: TP40005233
resource_type: Guide
platform: iOS|macOS
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/SharkUserGuide/IntelCorePMCTablesAppendix/IntelCorePMCTablesAppendix.html
archived_at: '2026-07-15T07:26:09.158412Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Shark User Guide](Introduction.md)


[Next](Intel%20Core%202%20Performance%20Counter%20Event%20List.md)[Previous](Miscellaneous%20Topics.md)

# Intel Core Performance Counter Event List

Intel’s Core processors have 2 performance counters per core. Both are programmable, and can count 111 (#1) or 112 (#2) different types of events.

Most of the events are reserved, and not listed here. The available events can be modified by enabling _Event-Mask_ bits, in the PMC control registers. There are eight such bits in each programmable PMC.

In addition, the available events can be modified by enabling any of the eight _Event-Mask_ bits associated with each programmable counter. The event-mask bits are critical to determining exactly which events will be counted. Most of the events can be selected without enabling any event-mask bits at all. The mask bits just modify the type of event slightly or the way the counter gets incremented when the event occurs. In particular, the mask settings often act as an event filter, limiting or expanding the selection of related events that can be counted simultaneously. In contrast, for some types of events you_must_ set event-mask bits properly, in order to count anything at all. These bits are labeled ‘Required’ in the event-mask bit list.

The table below lists each Event Name, the counter (PMC) number(s) for counters which can count the event, the event’s number, and the valid mask bits that can be enabled, for every useful event type. This last column lists mask bits using numbers between 0 and 7. Missing numbers indicate bits that are reserved and should not be enabled. If no mask bits are valid for that type of event, then “none” is listed.

In Shark, more complete documentation as to what the event names mean and how each mask bit modifies the count are provided as “tool-tips” when you hover the mouse over an event name in the popup menu, or over a specific bit name in the event-mask list. The event-mask bit controls are only accessible from the _Advanced View_ controls shown in the “[The Counters Menu](Other%20Profiling%20and%20Tracing%20Techniques.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqnrnknltm).

For more information on how to configure these counters, see [Intel CPU Performance Counter Configuration](Hardware%20Counter%20Configuration.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqmjqfvjvomjx).

| Performance Counter Event Name | Event Number | PMC Number | Valid Event-Mask Bits |
| --- | --- | --- | --- |
| BACLEARS | 230 | 1,2 | none |
| BR_BAC_MISSP_EXEC | 138 | 1,2 | none |
| BR_BOGUS | 228 | 1,2 | none |
| BR_CALL_EXEC | 146 | 1,2 | none |
| BR_CALL_MISSP_EXEC | 147 | 1,2 | none |
| BR_CND_EXEC | 139 | 1,2 | none |
| BR_CND_MISSP_EXEC | 140 | 1,2 | none |
| BR_IND_CALL_EXEC | 148 | 1,2 | none |
| BR_IND_EXEC | 141 | 1,2 | none |
| BR_IND_MISSP_EXEC | 142 | 1,2 | none |
| BR_INST_DECODED | 224 | 1,2 | none |
| BR_INST_EXEC | 136 | 1,2 | none |
| BR_INST_RETIRED | 196 | 1,2 | none |
| BR_MISS_PRED_RETIRED | 197 | 1,2 | none |
| BR_MISS_PRED_TAKEN_RET | 202 | 1,2 | none |
| BR_MISSP_EXEC | 137 | 1,2 | none |
| BR_RET_BAC_MISSP_EXEC | 145 | 1,2 | none |
| BR_RET_EXEC | 143 | 1,2 | none |
| BR_RET_MISSP_EXEC | 144 | 1,2 | none |
| BR_TAKEN_RETIRED | 201 | 1,2 | none |
| BTB_MISSES | 226 | 1,2 | none |
| BUS_BNR_DRV | 97 | 1,2 | none |
| BUS_DATA_RCV | 100 | 1,2 | 6 |
| BUS_DRDY_CLOCKS | 98 | 1,2 | 5 |
| BUS_LOCK_CLOCKS | 99 | 1,2 | 6 |
| BUS_REQ_OUTSTANDING | 96 | 1,2 | 4 5 6 7 |
| BUS_SNOOP_STALL | 126 | 1,2 | none |
| BUS_TRAN_ANY | 112 | 1,2 | 5 6 7 |
| BUS_TRAN_BRD | 101 | 1,2 | 6 |
| BUS_TRAN_BURST | 110 | 1,2 | 5 6 7 |
| BUS_TRAN_DEF | 109 | 1,2 | 5 6 7 |
| BUS_TRAN_IFETCH | 104 | 1,2 | 6 |
| BUS_TRAN_INVAL | 105 | 1,2 | 6 |
| BUS_TRAN_MEM | 111 | 1,2 | 5 6 7 |
| BUS_TRAN_PWR | 106 | 1,2 | 6 |
| BUS_TRAN_RFO | 102 | 1,2 | 6 |
| BUS_TRANS_IO | 108 | 1,2 | 6 |
| BUS_TRANS_P | 107 | 1,2 | 6 |
| BUS_TRANS_WB | 103 | 1,2 | 5 6 7 |
| CPU_CLK_UNHALTED | 60 | 1,2 | 0 1 |
| CYCLES_DIV_BUSY | 20 | 1 | none |
| CYCLES_INT_MASKED | 198 | 1,2 | none |
| CYCLES_INT_PENDING_AND_MASKED | 199 | 1,2 | none |
| DATA_MEM_REFS | 67 | 1,2 | none |
| DCU_LINES_IN | 69 | 1,2 | none |
| DCU_M_LINES_IN | 70 | 1,2 | none |
| DCU_M_LINES_OUT | 71 | 1,2 | none |
| DCU_MISS_OUTSTANDING | 72 | 1,2 | none |
| DCU_SNOOPS | 120 | 1,2 | 0 1 6 |
| DIV | 19 | 2 | 0 1 6 |
| DTLB Misses | 73 | 1,2 | none |
| EMON_ESP_UOPS | 215 | 1,2 | none |
| EMON_FUSED_UOPS_RET | 218 | 1,2 | 0 1 |
| EMON_KNI_PREF_DISPATCHED | 7 | 1,2 | 0 1 |
| EMON_KNI_PREF_MISS | 75 | 1,2 | 0 1 |
| EMON_PREF_RQSTS_DN | 248 | 1,2 | none |
| EMON_PREF_RQSTS_UP | 240 | 1,2 | none |
| EMON_SIMD_INSTR_RETIRED | 206 | 1,2 | none |
| EMON_SSE_SSE2_COMP_INST_RETIRED | 217 | 1,2 | 0 1 |
| EMON_SSE_SSE2_INST_RETIRED | 216 | 1,2 | 0 1 2 |
| EMON_SYNCH_UOPS | 211 | 1,2 | none |
| EMON_UNFUSION | 219 | 1,2 | none |
| EST_TRANS | 58 | 1,2 | 0 1 |
| EXTERNAL_BUS_CYCLES | 119 | 1,2 | 0 1 2 4 |
| EXTERNAL_BUS_QUEUE | 125 | 1,2 | 6 |
| FLOPS | 193 | 1,2 | none |
| FP_ASSIST | 17 | 2 | none |
| FP_COMP_OPS_EXE | 16 | 1 | none |
| FP_MMX_TRANS | 204 | 1,2 | 0 |
| HW_INT_RX | 200 | 1,2 | none |
| IFU_IFETCH | 128 | 1,2 | none |
| IFU_IFETCH_MISS | 129 | 1,2 | none |
| IFU_MEM_STALL | 134 | 1,2 | none |
| ILD_STALL | 135 | 1,2 | none |
| INST_DECODED | 208 | 1,2 | none |
| INST_RETIRED | 192 | 1,2 | none |
| ITLB_MISS | 133 | 1,2 | none |
| L1_CACHEABLE_DATA_READS | 64 | 1,2 | 0 1 2 3 |
| L1_CACHEABLE_DATA_READS_AND_WRITES | 68 | 1,2 | 0 1 2 3 |
| L1_CACHEABLE_DATA_WRITES | 65 | 1,2 | 0 1 2 3 |
| L1_CACHEABLE_LOCK_READS | 66 | 1,2 | 0 1 2 3 |
| L1_PREFETCH_REQUEST_MISSES | 79 | 1,2 | none |
| L2_ADS | 33 | 1,2 | 6 |
| L2_DBUS_BUSY | 34 | 1,2 | none |
| L2_DBUS_BUSY_RD | 35 | 1,2 | 6 |
| L2_IFETCH | 40 | 1,2 | 0 1 2 3 4 5 6 |
| L2_LD | 41 | 1,2 | 0 1 2 3 4 5 6 |
| L2_LINES_IN | 36 | 1,2 | 0 1 2 3 4 5 6 |
| L2_LINES_OUT | 38 | 1,2 | 0 1 2 3 4 5 6 |
| L2_M_LINES_INM | 37 | 1,2 | 6 |
| L2_M_LINES_OUT | 39 | 1,2 | 0 1 2 3 4 5 6 |
| L2_NO_REQUEST_CYCLES | 50 | 1,2 | 6 |
| L2_REJECT_CYCLES | 48 | 1,2 | 6 |
| L2_RQSTS | 46 | 1,2 | 0 1 2 3 4 5 6 |
| L2_ST | 42 | 1,2 | 0 1 2 3 4 5 6 |
| LD_BLOCKS | 3 | 1,2 | none |
| MISALIGN_MEM_REF | 5 | 1,2 | none |
| MMX_ASSIST | 205 | 1,2 | none |
| MMX_INSTR_EXEC | 176 | 1,2 | none |
| MMX_INSTR_TYPE_EXEC | 179 | 1,2 | 0 1 2 3 4 5 |
| MMX_SAT_INSTR_EXEC | 177 | 1,2 | none |
| MMX_SAT_INSTR_RET | 207 | 1,2 | none |
| MMX_UOPS_EXEC | 178 | 1,2 | none |
| MUL | 18 | 2 | none |
| PARTIAL_RAT_STALLS | 210 | 1,2 | none |
| RESOURCE_STALLS | 162 | 1,2 | none |
| RET_SEG_RENAMES | 214 | 1,2 | none |
| SB_DRAINS | 4 | 1,2 | none |
| SEG_REG_RENAMES | 213 | 1,2 | 0 1 2 3 |
| SEG_RENAME_STALLS | 212 | 1,2 | 0 1 2 3 |
| SEGMENT_REG_LOADS | 6 | 1,2 | none |
| SELF_MODIFYING_CODE | 195 | 1,2 | none |
| THERMAL_TRIP | 59 | 1,2 | 6 7 |
| UOPS_RETIRED | 194 | 1,2 | none |

[Next](Intel%20Core%202%20Performance%20Counter%20Event%20List.md)[Previous](Miscellaneous%20Topics.md)

