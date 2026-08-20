---
title: Xserve Developer Note
apple_id: TP40005210
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-01-12'
source_url: https://developer.apple.com/library/archive/documentation/HardwareDrivers/Conceptual/Xserve_0608/Articles/Xserve_arch.html
archived_at: '2026-07-15T07:41:11.963707Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xserve Developer Note](Introduction%20to%20Xserve%20Developer%20Note.md)


[Next](Document%20Revision%20History.md)[Previous](Introduction%20to%20Xserve%20Developer%20Note.md)

# Xserve Developer Note

This developer note describes the new Xserve introduced in August 2006. It includes information about distinguishing features of the computer, including components on the main logic board: the microprocessors, the North Bridge memory controller, the South Bridge I/O controller, and the buses that connect them to each other and to the I/O interfaces.

The computer comes with Mac OS X version 10.4.8 installed.

The value of the computer model machine identifier string is `Xserve1,1`.

For a description and graphical depiction of the Xserve enclosure and its ports and connectors, refer to the _Xserve User’s Guide_ that shipped with your system.

The architecture of the Xserve is based on two, dual-core Intel Xeon processors, the North Bridge memory controller, and the South Bridge I/O controller, as shown in the simplified block diagram in [Figure 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dsnjyfvbegskhifaugsq).

__Figure 1__  Xserve Block diagram

![This block diagram shows the memory controller and I/O controller ICs and the buses that connect them on the main logic board. Each component in the block diagram is defined in text.](attachments/Art/060944001305_01.jpg)

The Xserve is Apple’s fifth generation 1U server. For a complete list of user-visible features, see the Xserve specification sheet at Apple's [Specifications](http://www.info.apple.com/support/applespec.html) site. Other features are described in this section.

The microprocessors in the Xserve are dual-core Intel Xeon with the following features:

- Implements two dual-core, 2.0 GHz Intel Xeon processors; or configure to order: two dual-core 2.66 GHz or 3.0 GHz Intel Xeon processors
- 4 MB shared L2 cache per processor
- Intel Advanced Digital Media Boost
- Connection to the North Bridge over a 1333 MHz frontside bus
- Supports Intel 64 Architecture

See the [Intel Xeon Processor 5100 Series](http://www.intel.com/design/intarch/dualcorexeon/5100/index.htm) support site for detailed microprocessor documentation.

Intel Advanced Digital Media Boost accelerates data manipulation by applying a single instruction to multiple data at the same time, known as SIMD processing. SIMD technology accelerates vector math operations and floating-point calculations. Advanced Digital Media Boost supports Intel Streaming SIMD Extensions (SSE) versions 1, 2, and 3 and allows the processor to execute an SSE3 instruction every clock cycle.

For information on Advanced Digital Media Boost, refer to [Technology@Intel Magazine](http://www.intel.com/technology/magazine/computing/core-architecture-0306.htm?iid=hwd_center+coremicroww18&).

Intel 64 architecture increases the linear address space for software to 64 bits and supports physical address space up to 40 bits. The technology also introduces a new operating mode referred to as IA-32e mode. IA-32e mode operates in one of two sub-modes:

- Compatibility mode enables a 64-bit operating system to run most legacy 32-bit software unmodified
- 64-bit mode enables a 64-bit operating system to run applications written to access 64-bit address space

In the 64-bit mode, applications may access:

- 64-bit flat linear addressing
- 8 additional general-purpose registers (GPRs)
- 8 additional registers for streaming SIMD extensions (SSE, SSE2, SSE3 and SSSE3)
- 64-bit-wide GPRs and instruction pointers
- Uniform byte-register addressing
- Fast interrupt-prioritization mechanism
- New instruction-pointer relative-addressing mode

An Intel 64 architecture processor supports existing IA-32 software because it is able to run all non-64-bit legacy modes supported by IA-32 architecture. Most existing IA-32 applications also run in compatibility mode.

For information on Intel 64 Architecture, refer to the following website:

[http://www.intel.com/technology/intel64/index.htm](http://www.intel.com/technology/intel64/index.htm)

The dual, independent processor buses run at 1333 MHz and connect the processors to the North Bridge. Each front-side bus has a 64-bit wide data bus. Each processor has 64-bit addressing.

The point-to-point architecture provides each subsystem with dedicated bandwidth to main memory. The North Bridge implements an independent processor interface. The input clock to the processor PLL is 333 MHz.

The Xserve comes standard with two 512 MB (total 1 GB), 667 MHz (PC2-5300) SDRAM fully-buffered DIMM (FB-DIMM) memory. Memory is connected to the North Bridge via two 128-bit channels (256 bit). Each channel services two memory slots via the Advanced Memory Buffers (AMB) using FB-DIMMs. Maximum memory capacity is 32 GB. For additional information, refer to _[RAM Expansion Developer Note](../RAM%20Expansion%20Developer%20Note/Introduction%20to%20RAM%20Expansion%20Developer%20Note.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztamzr)_.

The North Bridge and South Bridge are connected by an Enterprise Southbridge Interface (ESI) bus, a high-speed, bidirectional, point-to-point link supporting a thruput of 1 GBps in each direction.

The Extensible Firmware Interface (EFI) boot ROM consists of 2 MB of on-board flash EEPROM. It includes the hardware-specific code and tables needed to start up the computer, load an operating system, and provide common hardware access services.The EFI boot ROM connects to the South Bridge via the Firmware hub (FWH) bus.

Xserve has two, open, 2.5 GHz, PCI Express x8 links. One dedicated link is connected to the North Bridge. A second link is configurable as a PCI Express x8 link connected to the North Bridge or a PCI-X link connected to the South Bridge. The mezzanine card is on a third dedicated PCI Express link to provide video capability.

For information on PCI Express and PCI-X, refer to _[PCI Developer Note](../../Hardware/PCI%20Developer%20Note/Introduction%20to%20PCI%20Developer%20Note.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztamrx)_.

The base configuration graphics subsystem on the Xserve is the ATI Radeon X1300 PCI Express card with 64 MB GDDR3 SDRAM. The card supports a mini-DVI port. A mini-DVI to VGA adapter is shipped with the Xserve.

Available as a configure-to-order option is the ATI Radeon X1300 PCI Express card with 256 MB GDDR2 memory and one dual-link DVI port.

For information on the graphics subsystem and the display capabilities, refer to _[Video Developer Note](../../Hardware/Video%20Developer%20Note/Introduction%20to%20Video%20Developer%20Note.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztkmbu)_.

For information on the PCI Express and/or PCI-X buses that support the graphics subsystem, refer to _[PCI Developer Note](../../Hardware/PCI%20Developer%20Note/Introduction%20to%20PCI%20Developer%20Note.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztamrx)_.

Xserve has three, 3-Gbps-capable Serial ATA (SATA)/Serial Attached SCSI (SAS) Apple Drive Modules hard drive bays. The base configuration provides one 80 GB, 7200 rpm, 1.5 Gbps Serial ATA (SATA) disk drive installed.

Available as a configure-to-order option is any combination of SATA or SAS Apple Drive Modules.

For more information on SATA, see [Serial ATA International Organization](http://www.serialata.org/).

SAS is the next generation of SCSI drives providing the serial communication protocol used for direct attached storage. SAS utilizes a 3 Gbps link and the same physical connection layer as SATA. For more information on SAS, see the [Serial Attached SCSI](http://www.scsita.org/) website.

In the Xserve, the South Bridge controller provides an Ultra ATA/100 interface (running at UATA/66) to a slot-loading optical drive. The Xserve comes standard with a 24x Combo drive and has an optional configure-to-order 8x double-layer SuperDrive. The drive can read and write DVD media and CD media, as shown in [Table 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dsnjyfvjvomq) and [Table 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dsnjyfvjvona).

__Table 1__  Types of media read and written by the Combo drive

| Media type | Reading speed | Writing speed |
| DVD+/-R | 6x (CAV) | – |
| DVD+/-R DL | 4x (CAV) | – |
| DVD-ROM | 8x (CAV) | – |
| DVD-ROM DL | 5x (CAV) | – |
| DVD+/-RW | 5x (CAV) (DVD-9) | – |
| CD-R | 24x (CAV) | 24x ZCLV |
| CD-RW | 24x (CAV) | 16x ZCLV (ultra speed media) |
| CD-ROM | 24x (CAV) | – |

__Table 2__  Types of media read and written by the SuperDrive

| Media type | Reading speed | Writing speed |
| DVD+/-R | 8x (CAV max) | 8x, 4x, 2x, 1x (CLV) single-layer, depending on media |
| DVD+R DL | 6x (CAV max) | 2.4x (CLV) double-layer, depending on media |
| DVD-ROM | 8x DVD5 (CAV max); 6x DVD9 (CAV max) | – |
| DVD-RW | 6x (CAV max) | 4x, 2x, 1x (CLV) depending on media |
| DVD+RW | 6x (CAV max) | 4x, 2.4x (CLV) depending on media |
| CD-R | 24x (CAV max) | 24x ZCLV |
| CD-RW | 24x (CAV max) | 16x ZCLV (high speed media) |
| CD-ROM | 24x (CAV max) | – |

The optical drive is configured as cable select and complies with the ATA/ATAPI-5 industry standard. For information on parallel ATA interfaces, see the International Committee on Information Technology Standards (INCITS) Technical Committee T13 [AT Attachment](http://www.t13.org/) website.

The Xserve has two IEEE-1394b FireWire 800 ports, which support transfer rates of 100, 200, 400, and 800 Mbps and one IEEE-1394a FireWire 400 port, which supports transfer rates of 100, 200, and 400 Mbps. For more information, see _[FireWire Developer Note](../FireWire%20Developer%20Note/Introduction%20to%20FireWire%20Developer%20Note.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztamry)_.

The Xserve has two Gigabit Ethernet ports with jumbo frame support for 10BASE-T/UTP, 100BASE-TX, and 1000BASE-T operation.The Ethernet MAC is internal to the South Bridge and interfaces via the I/O Acceleration Technology (IOAT) bus. For more information, see _[Ethernet Developer Note](../Ethernet%20Developer%20Note/Introduction%20to%20Ethernet%20Developer%20Note.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztamrz)_.

The South Bridge includes an integrated USB 2.0 controller supporting two external USB 2.0 ports. The USB ports comply with the Universal Serial Bus Specification 2.0. For more information, see _[Universal Serial Bus Developer Note](../Universal%20Serial%20Bus%20Developer%20Note/Introduction%20to%20Universal%20Serial%20Bus%20Developer%20Note.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztamrw)_.

The Xserve has one DB-9 (RS-232-compatible) serial port on the rear panel.

Xserve lights-out management (LOM) capabilities allow remote control of an Xserve system from anywhere on the network or over the Internet. Enabled by built-in hardware, the LOM remote management system continues to run as long as the system is plugged into power, even if the system is powered off or in a hung state. Xserve monitoring tools run securely over TCP/IP, using password authentication that is based on version 2.0 of the Intelligent Platform Management Interface (IPMI).

For information on Apple’s implementation of lights-out management , see [Lights-Out Management](http://www.apple.com/xserve/management.html).

For information on the Intel lights-out management specifications, see [Intelligent Platform Management Interface](http://www.intel.com/design/servers/ipmi/index.htm).

The Xserve uses an advanced system management controller (SMC) to manage thermal and power conditions, while keeping the acoustic noise to a minimum. The SMC is fully independent of the operating system.

[Next](Document%20Revision%20History.md)[Previous](Introduction%20to%20Xserve%20Developer%20Note.md)

