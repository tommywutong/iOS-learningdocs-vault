---
title: Shark User Guide
apple_id: TP40005233
resource_type: Guide
platform: iOS|macOS
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/SharkUserGuide/U4PMCTablesAppendix/U4PMCTablesAppendix.html
archived_at: '2026-07-15T07:26:53.383048Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Shark User Guide](Introduction.md)


[Next](ARM11%20Performance%20Counter%20Event%20List.md)[Previous](UniNorth-3%20%28U3%29%20Performance%20Counter%20Event%20List.md)

# Kodiak (U4) Performance Counter Event List

The U4/Kodiak North bridge chipsets contain two distinct sets of counters.

The first set of counters counts memory events, in a manner similar to the counters for the other North bridge chips. Six independent memory counters are present, each of which can count any one of 22 different general types of events. Each of these types may be focused further by filtering events on the basis of their source interface (any combination of the seven independently selectable sources may be counted).

The second set of counters (“API counters”) count queueing and buffering events internal to the chip, allowing a more detailed look at its inner workings. Six independent API counters are present, each of which can count any one of six different general types of events. Each of these types may be focused further by filtering events on the basis of their source queue/buffer (any one from among 33 possible sources) and source I/O interface (any combination of the six independently selectable interfaces may be counted simultaneously).

The first of the three tables in this appendix lists the memory events alphabetically by name, followed by the Event Number that needs to be selected to activate counting of a particular event. The second table does the same for the API performance counters. Finally, the third table provides a list of the sources for API events and their corresponding numbers.

For more information, see [U4 (Kodiak) North Bridge](Hardware%20Counter%20Configuration.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqmjqfvjvomrs).

| Memory Performance Counter Event Name | Event Number |
| --- | --- |
| Activate commands -- open page (filtered and counted) | 7 |
| Bottom entry aged (count events, no filters) | 64 |
| Cache line sized transfers -- 128 bytes (filtered and counted) | 3 |
| Commands with auto-precharge enabled (filtered and counted) | 5 |
| Conflict detected in oldest read reorder queue (count events, no filters) | 32 |
| DRAM Cycle Count (1/2 DDR frequency, no filters) | 255 |
| Entries in non-coherent request queue (accumulate events, no filters) | 113 |
| Entries in read reorder queue (accumulate events, no filters) | 81 |
| Entries in write reorder queue (accumulate events, no filters) | 80 |
| Issued transfer size (accumulate events, no filters) | 83 |
| Non-coherent read request [RT #24253] (count events, no filters) | 97 |
| Non-coherent request [RT #24252] (count events, no filters) | 96 |
| Nothing | 0 |
| Precharge commands -- close page (filtered and counted) | 6 |
| Read reorder queue empty (count events, no filters) | 17 |
| Read requests (filtered and counted) | 1 |
| Request queue empty [RT #23441] (count events, no filters) | 16 |
| Requested transfer size (accumulate events, no filters) | 82 |
| Requested transfer size from non-coherent queue (accumulate events, no filters) | 112 |
| RMW transfers (filtered and counted) | 4 |
| Write high watermark reached (count events, no filters) | 48 |
| Write reorder queue empty (count events, no filters) | 18 |
| Write requests (filtered and counted) | 2 |

| API Performance Counter Event Name | Event Number |
| --- | --- |
| Accumulate Queue Requests | 0x02 |
| API Cycles | 0x00 |
| Nothing | 0xFF |
| Queue Reservations | 0x03 |
| Queue Transactions | 0x01 |
| Retries | 0x05 |
| Transaction Size (bytes) | 0x04 |

| API Event Source Name | Source Number |
| --- | --- |
| API Wt Data Buffer | 0x28 |
| Bypass Queue | 0x10 |
| Command Slot | 0x01 |
| GCR Rd Data Queue | 0x27 |
| GCR Response Queue | 0x0B |
| GCR Target Rq Queue | 0x08 |
| GCR Wt Data Queue | 0x23 |
| Ht Coh Rd Pending Queue | 0x14 |
| Ht Coh Rd Rq Queue | 0x0E |
| Ht Coh Wt Pending Queue | 0x15 |
| Ht Coh Wt Rq Queue | 0x0F |
| Ht Rd Data Queue | 0x26 |
| Ht Rd Target Rq Queue | 0x07 |
| Ht Response Queue | 0x0A |
| Ht Wt Data Queue | 0x22 |
| Ht Wt Target Rq Queue | 0x06 |
| Intervention Buffer | 0x29 |
| Memory Rd Buffer (NI) | 0x2A |
| Memory Request Queue | 0x11 |
| Memory Response Buffer | 0x20 |
| Memory Wt Data Buffer | 0x24 |
| PCIE Coh Rd Pending Queue | 0x12 |
| PCIE Coh Rd Rq Queue | 0x0C |
| PCIE Coh Wt Pending Queue | 0x13 |
| PCIE Coh Wt Rq Queue | 0x0D |
| PCIE Rd Data Queue | 0x25 |
| PCIE Rd Target Rq Queue | 0x05 |
| PCIE Response Queue | 0x09 |
| PCIE Wt Data Queue | 0x21 |
| PCIE Wt Target Rq Queue | 0x04 |
| Power Management | 0x3F |
| Snoop Slots | 0x02 |
| Synchronization Queue | 0x00 |

[Next](ARM11%20Performance%20Counter%20Event%20List.md)[Previous](UniNorth-3%20%28U3%29%20Performance%20Counter%20Event%20List.md)

