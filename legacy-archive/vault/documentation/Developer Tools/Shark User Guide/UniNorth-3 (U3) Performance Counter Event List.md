---
title: Shark User Guide
apple_id: TP40005233
resource_type: Guide
platform: iOS|macOS
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/SharkUserGuide/U3PMCTablesAppendix/U3PMCTablesAppendix.html
archived_at: '2026-07-15T07:26:53.373575Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Shark User Guide](Introduction.md)


[Next](Kodiak%20%28U4%29%20Performance%20Counter%20Event%20List.md)[Previous](UniNorth-2%20%28U1.5-2%29%20Performance%20Counter%20Event%20List.md)

# UniNorth-3 (U3) Performance Counter Event List

The U3 North bridge chipsets contain two distinct sets of counters.

The first set of counters counts memory events, in a manner similar to the counters for the other North bridge chips. Six independent memory counters are present, each of which can count any one of five different general types of events. Each of these types may be focused further by filtering events on the basis of their source I/O interface (any combination of the nine independently selectable interfaces may be counted) and three memory page states (for events involving DRAM interaction).

The second set of counters (“API counters”) count queueing and buffering events internal to the chip, allowing a more detailed look at its inner workings. Six independent API counters are present, each of which can count any one of six different general types of events. Each of these types may be focused further by filtering events on the basis of their source queue/buffer (any one from among 51 possible sources).

The first of the three tables in this appendix lists the memory events alphabetically by name, followed by the Event Number that needs to be selected to activate counting of a particular event. The second table does the same for the API performance counters. Finally, the third table provides a list of the sources for API events and their corresponding numbers.

For more information, see [U3 North Bridge](Hardware%20Counter%20Configuration.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temztfvbuqmjqfvjvomrr).

| Memory Performance Counter Event Name | Event Number |
| --- | --- |
| Cycles 1 or more queues have 0 entries | 8 |
| Cycles 1 or more queues have 2 entries | 16 |
| DRAM Clock Cycles (no filters apply, 1/2 DDR freq.) | 1 |
| Nothing | 0 |
| Number of Memory Transactions | 2 |
| Read/write request beats (bytes=beats\*16) | 4 |

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
| API0 Mem MI Target Rq Queue | 0x1A |
| API0 Mem Rd Target Rq Queue | 0x16 |
| API0 Mem Wt Target Rq Queue | 0x18 |
| API1 Mem MI Target Rq Queue | 0x1B |
| API1 Mem Rd Target Rq Queue | 0x17 |
| API1 Mem Wt Target Rq Queue | 0x19 |
| Command Slot | 0x01 |
| Ht Coh Rd Rq Queue | 0x13 |
| Ht Coh Wt Rq Queue | 0x14 |
| Ht Rd Data Queue | 0x90 |
| Ht Rd Target Rq Queue | 0x09 |
| Ht Response Queue | 0x0E |
| Ht Wt Data Queue | 0x40 |
| Ht Wt Target Rq Queue | 0x08 |
| Intervention Queue | 0x03 |
| Master Tag: All | 0xE00 |
| Master Tag: API0 | 0x200 |
| Master Tag: API0 and API1 | 0x400 |
| Master Tag: API1 | 0x300 |
| Master Tag: HT | 0xA00 |
| Master Tag: PCI | 0x900 |
| Master Tag: VSP | 0x800 |
| Master Tag: VSP, PCI, and HT | 0xC00 |
| Mem Rd Data Queue | 0x70 |
| Mem Rd Target Rq Queue | 0x05 |
| Mem Response Queue | 0x0C |
| Mem Wt Data Queue | 0x20 |
| Mem Wt Target Rq Queue | 0x04 |
| Pci Coh Rd Rq Queue | 0x11 |
| Pci Coh Wt Rq Queue | 0x12 |
| Pci Rd Data Queue | 0x80 |
| Pci Rd Target Rq Queue | 0x07 |
| Pci Response Queue | 0x0D |
| Pci Wt Data Queue | 0x30 |
| Pci Wt Target Rq Queue | 0x06 |
| Reg Rd Data Queue | 0xB0 |
| Reg Response Queue | 0x10 |
| Reg Target Rq Queue | 0x0B |
| Reg Wt Data Queue | 0x60 |
| Snoop Slots | 0x02 |
| Synchronization Queue | 0x00 |
| Vsp Coh Rd Rq Queue | 0x15 |
| Vsp Rd Data Queue | 0xA0 |
| Vsp Response Queue | 0x0F |
| Vsp Target Rq Queue | 0x0A |
| Vsp Wt Data Queue | 0x50 |
| Write Data Buffer | 0x100 |
| Write Data Buffer API0 MI | 0x130 |
| Write Data Buffer API0 Wr | 0x110 |
| Write Data Buffer API1 MI | 0x140 |
| Write Data Buffer API1 Wr | 0x120 |

[Next](Kodiak%20%28U4%29%20Performance%20Counter%20Event%20List.md)[Previous](UniNorth-2%20%28U1.5-2%29%20Performance%20Counter%20Event%20List.md)

