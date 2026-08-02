---
title: RAM Expansion Developer Note
apple_id: TP40003031
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2008-04-28'
source_url: https://developer.apple.com/library/archive/documentation/HardwareDrivers/Conceptual/HWTech_RAM/Articles/RAM_concepts.html
archived_at: '2026-07-15T07:40:59.622488Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [RAM Expansion Developer Note](Introduction%20to%20RAM%20Expansion%20Developer%20Note.md)


[Next](RAM%20Expansion%20Product-Specific%20Details.md)[Previous](Introduction%20to%20RAM%20Expansion%20Developer%20Note.md)

# RAM Expansion Concepts

This article provides an overview of random access memory (RAM) considerations for Mac computers.

The mechanical and electrical characteristics of RAM modules for Mac computers are consistent with the Electronic Industries Alliance (EIA) JEDEC Solid State Technology Association division specifications, which can be found on the EIA [JEDEC download](http://www.jedec.org/DOWNLOAD/default.cfm) site.

This section outlines characteristics common to certain RAM types. Details specific to a particular Mac product line or computer and details regarding which device configurations are supported by a particular computer, are provided in [RAM Expansion Product-Specific Details](RAM%20Expansion%20Product-Specific%20Details.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztqojzfvjvomk7gezdambtgmytcnzx).

The SDRAM specifications for DDR2 DIMMs, DDR2 SO-DIMMs, and Fully-Buffered DIMMs (FB-DIMM) can be found on the [Electronics Industry Associations](http://www.jedec.org/DOWNLOAD/default.cfm) website.

The mechanical electrical design of the DDR2 SDRAM SO-DIMM is defined by the JEDEC specifications JESD21-C.MODULE4_20_14 and JESD79-2B.

The mechanical design of the DDR2 SDRAM DIMM is defined by the JEDEC specification JESD21-C.MODULE4_20_14.

The electrical design of the DDR2 SDRAM DIMM is defined by the JEDEC specifications JESD21-C.MODULE4_20_14 and JESD79-2B.

The mechanical design of the FB-DIMM is defined by the JEDEC Publication 95, Outline M0256, latest revision.

Additional useful FB-DIMM standards and publications include:

- FBD240 Connector Draft Specification - Intel
- FB-DIMM Architecture and Protocol Spec - JEDEC JC-40
- Advanced Memory Buffer Design Draft Specification - JEDEC JC-40
- Fully Buffered Dual Inline Memory Module Family. (Module Outline) - JEDEC MO-256B
- FBDIMM Socket Outline - JEDEC SO-003
- JEDEC spec PC2-4200/PC2-5300/PC2-6400 DDR2 Fully Buffered DIMM Design Specification, current revision, JEDEC Buffered DIMM and Socket Task Group
- Electrostatic Discharge (ESD) Sensitivity Testing (HBM) - JEDEC JESD22A114
- FB4300/5300/6400 DDR Fully Buffered DIMM Design Specification - JEDEC JC-45

The Serial Presence Detect (SPD) EEPROM specified in the JEDEC standard is required and must be set to properly define the DIMM configuration. The EEPROM is powered (Vddspd) by 1.7 V to 3.6 V. For the FB-DIMM SPD Spec, search for the strings: hp00302a_ddr2_fbdimm_spd_10.pdf or SPD4_01_02_0.

This section contains details about full-size DDR2 modules.

[Table 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztqojyfvjvoms7gezdambtgmytcnzx) shows information about the different sizes of DDR2 SDRAM devices used in the memory modules. The DIMM size is the memory size of the largest DIMM with the corresponding device size (from the second column) that the computer can accommodate.

The device configuration includes three specifications: address range, word size, and number of banks. For example, a 1 M x 16 x 4 device addresses 1 M, stores 16 bits at a time, and has 4 banks.

Devices per rank specifies the number of devices needed to make up the 8-byte width of the data bus. The fifth column in the table shows the size of each rank of devices, which is based on the number of internal banks in each device and the number of devices per rank. A rank is a side of a DIMM; 2 ranks indicate a 2-sided DIMM. 

__Table 1__  Sizes of DDR2 SDRAM expansion full-size DIMMS and devices

| DIMM size | Device size | Configuration | Devices per rank | Rank size | # of ranks |
| 256 MB\* | 256 Mb | 8 M x 8 x 4 | 8 | 256 MB | 1 |
| 256 MB | 512 Mb | 8 M x 16 x 4 | 4 | 256 MB | 1 |
| 512 MB\* | 256 Mb | 8 M x 8 x 4 | 8 | 256 MB | 2 |
| 512 MB | 512 Mb | 16 M x 8 x 4 | 8 | 512 MB | 1 |
| 1 GB | 512 Mb | 16 M x 8 x 4 | 8 | 512 MB | 2 |
| 2 GB | 1 Gb | 32 M x 8 x 4 | 8 | 1 GB | 2 |
|
| \* Theoretical values. Requires extensive testing. | \* Theoretical values. Requires extensive testing. | \* Theoretical values. Requires extensive testing. | \* Theoretical values. Requires extensive testing. | \* Theoretical values. Requires extensive testing. | \* Theoretical values. Requires extensive testing. |

[Table 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztqojyfvjvonc7gezdambtgmytcnzx) shows the address multiplexing modes used with the devices.

__Table 2__  Address multiplexing modes for SDRAM full-size devices

| Device size | Device configuration | Size of row address | Size of column address | Bank address | # of Banks |
| 256 Mb\* | 4 M x 16 x 4 | 13 | 9 | ba[0-1] | 4 |
| 256 Mb\* | 8 M x 8 x 4 | 13 | 10 | ba[0-1] | 4 |
| 512 Mb | 8 M x 16 x 4 | 13 | 10 | ba[0-1] | 4 |
| 512 Mb | 16 M x 8 x 4 | 14 | 10 | ba[0-1] | 4 |
| 1 Gb | 8 M x 16 x 4 | 13 | 10 | ba[0-2] | 4 |
| 1 Gb\* | 32 M x 8 x 4 | 14 | 10 | ba[0-2] | 4 |
| 1 Gb | 16 M x 8 x 8 | 14 | 10 | ba[0-2] | 8 |
|
| \* Theoretical values. Requires extensive testing. | \* Theoretical values. Requires extensive testing. | \* Theoretical values. Requires extensive testing. | \* Theoretical values. Requires extensive testing. | \* Theoretical values. Requires extensive testing. | \* Theoretical values. Requires extensive testing. |

This section contains details on the compact format small outline modules (SO-DIMMs), typically used in computers such as laptops, for which the compact size is a requirement.

[Table 3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztqojyfvjvom27gezdambtgmytcnzx) shows information about the different sizes of DDR2 SDRAM SO-DIMM devices used in the memory modules.

__Table 3__  Sizes of DDR2 SDRAM expansion SO-DIMMS and devices

| DIMM size | Device size | Configuration | Devices per rank | Rank size | # of ranks |
| 256 MB | 256 Mb | 8 M x 8 x 4 | 8 | 256 MB | 1 |
| 256 MB | 512 Mb | 8 M x 16 x 4 | 4 | 256 MB | 1 |
| 512 MB | 256 Mb | 8 M x 8 x 4 | 8 | 256 MB | 2 |
| 512 MB | 512 Mb | 16 M x 8 x 4 | 8 | 512 MB | 1 |
| 512 MB | 1 Gb | 8 M x 16 x 8 | 4 | 512 MB | 1 |
| 1 GB | 512 Mb | 16 M x 8 x 4 | 8 | 512 MB | 2 |
| 1 GB | 1 Gb | 16 M x 8 x 8 | 8 | 1 GB | 1 |
| 1 GB | 1 Gb | 8 M x 16 x 8 | 4 | 512 MB | 2 |
| 2 GB | 1 Gb | 16 M x 8 x 8 | 8 | 1 GB | 2 |
| 2 GB | 2 Gb | 2 x (16 M x 8 x 8)\* | 8 shared\* | 1 GB | 2 |
|
| \* denotes Dual Die Package (DDP) | \* denotes Dual Die Package (DDP) | \* denotes Dual Die Package (DDP) | \* denotes Dual Die Package (DDP) | \* denotes Dual Die Package (DDP) | \* denotes Dual Die Package (DDP) |

[Table 4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztqojyfvjvonk7gezdambtgmytcnzx) shows the address multiplexing modes used with the devices.

__Table 4__  Address multiplexing modes for SDRAM SO-DIMM devices

| Device size | Device configuration | Size of row address | Size of column address | Bank address | Num of Banks |
| 256 Mb | 4 M x 16 x 4 | 13 | 9 | ba[0-1] | 4 |
| 256 Mb | 8 M x 8 x 4 | 13 | 10 | ba[0-1] | 4 |
| 512 Mb | 8 M x 16 x 4 | 13 | 10 | ba[0-1] | 4 |
| 512 Mb | 16 M x 8 x 4 | 14 | 10 | ba[0-1] | 4 |
| 1 Gb | 8 M x 16 x 8 | 13 | 10 | ba[0-2] | 4 |
| 1 Gb | 16 M x 8 x 8 | 14 | 10 | ba[0-2] | 8 |
| 2 Gb | 2 x (16 M x 8 x 8)\* | 14 | 10 | ba[0-2] | 8 |
|
| \* denotes Dual Die Package (DDP) | \* denotes Dual Die Package (DDP) | \* denotes Dual Die Package (DDP) | \* denotes Dual Die Package (DDP) | \* denotes Dual Die Package (DDP) | \* denotes Dual Die Package (DDP) |

This section contains details about fully-buffered DIMM modules.

The Fully Buffered DIMM (FB-DIMM) memory module technology provides more memory speed, capacity, and reliability than standard DIMM modules. On standard DIMM modules, communication between the memory controller and the module is parallel. On FB-DIMMs, the communication is serial, similar to PCI Express. Serial communication requires fewer wires to connect the memory controller hub to the memory module, allowing more memory channels.

FB-DIMM serial communication uses pairs of wires to enable a technique called differential transmission to ensure accurate data transmission. With differential transmission, a signal is transmitted on both strands of the wire pair: one with the standard signal and one with the inverted signal.

Another benefit of the FB-DIMM is that it uses different paths for data transmission and data reception. Standard DIMM modules use the same path to both transmit and receive data. The system used on FB-DIMM modules helps to increase the performance of the memory subsystem.

FB-DIMMs have Advanced Memory Buffers (AMBs) that interface between the serial communication to the memory controller IC and the parallel communication to the SDRAM chips. AMBs contain temperature sensors that maintain proper operating temperature of the FB-DIMMs.

[Next](RAM%20Expansion%20Product-Specific%20Details.md)[Previous](Introduction%20to%20RAM%20Expansion%20Developer%20Note.md)

