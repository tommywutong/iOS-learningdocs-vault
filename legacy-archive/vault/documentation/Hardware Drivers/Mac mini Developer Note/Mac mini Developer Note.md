---
title: Mac mini Developer Note
apple_id: TP40004240
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-04-04'
source_url: https://developer.apple.com/library/archive/documentation/HardwareDrivers/Conceptual/Macmini_0602/Articles/architecture.html
archived_at: '2026-07-15T07:41:07.797622Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Mac mini Developer Note](Introduction%20to%20Mac%20mini%20Developer%20Note.md)


[Next](Document%20Revision%20History.md)[Previous](Introduction%20to%20Mac%20mini%20Developer%20Note.md)

# Mac mini Developer Note

This note describes the Mac mini computers based on the 1.66 GHz Intel Core Duo microprocessor or 1.5 GHz Intel Core Solo microprocessor and introduced in February 2006. It includes information about distinguishing features of the computer, including components on the main logic board: the microprocessor, the other main ICs, and the buses that connect them to each other and to the I/O interfaces.

The computer comes with Mac OS X version 10.4.5 or later installed.

The value of the Mac mini model identifier string is `Macmini1,1`.

The architecture of the Mac mini is based on the Intel Core Duo or Intel Core Solo microprocessor, the North Bridge memory controller, and the  South Bridge I/O controller,which are connected to each other by a Direct Media Interface (DMI) bus. The North Bridge IC provides the bridging functionality among the processor, the memory system, the DMI, and the internal graphics controller.  The South Bridge IC supports these components:

- Ultra ATA/100 bus for the optical drive (running at UATA/66)
- A 1.5 Gbps Serial ATA (SATA) bus for the disk drive
- 1-lane PCI Express link for the AirPort Extreme module
- SPI bus, direct memory access bus to the boot ROM
- USB 2.0 controller, which in turn supports the Bluetooth module, IR receiver, and 4 external USB 2.0 ports
- Channel to the audio subsystem
- 1-lane PCI Express link for the Ethernet controller
- 33 MHz, 32-bit internal PCI bus to the FireWire 400 (1394a) OHCI and PHY

A DMA controller internal to the South Bridge supports LPC DMA (low pin count direct memory access). The DMA controller has registers that are fixed in the lower 64 KB of I/O space. The DMA controller is configured using registers in the PCI configuration space.

Figure 1 provides a simplified block diagram of the North Bridge and South Bridge ICs and the buses that connect them together. 

__Figure 1__  Block diagram

![This block diagram shows the memory controller and I/O controller ICs and the buses that connect them on the main logic board. Each component in the block diagram is defined in text.](attachments/Art/060204001316_01.jpg)

The Mac mini computer includes an integrated IR receiver and the Apple Remote. For a complete list of user-visible features, see the Mac mini specification sheet at Apple's [Specifications](http://www.info.apple.com/support/applespec.html) site. Other features are described in this section.

The microprocessor in the Mac mini is either a 1.66 GHz Intel Core Duo or a 1.5 GHz Intel Core Solo. It has the following features:

- 1.66 GHz Intel Core Duo processors or a 1.5 GHz Intel Core Solo processor
- 2 MB on-chip L2 cache
- Digital Media Boost
- Connection to the North Bridge IC over a 667 MHz frontside bus

See the [Intel Core Duo Processors](http://www.intel.com/products/processor/coreduo/) or [Intel Core Solo Processors](http://www.intel.com/products/processor/coresolo/index.htm) support sites for detailed microprocessor documentation.

 Intel Digital Media Boost accelerates data manipulation by applying a single instruction to multiple data at the same time, known as SIMD processing. SIMD technology accelerates vector math operations and floating-point calculations. Digital Media Boost supports Intel Streaming SIMD Extensions (SSE) versions 1, 2, and 3.

For information on Digital Media Boost, refer to the following websites.

[http://www.intel.com/products/processor/coreduo/digitalmediaboost.htm](http://www.intel.com/products/processor/coreduo/digitalmediaboost.htm)

The processor bus is an up-to-667 MHz bus connecting the processor to the North Bridge IC. The bus has a 64-bit wide data path. The processor has 32-bit addressing. 

The point-to-point architecture provides each subsystem with dedicated bandwidth to main memory. The North Bridge IC implements an independent processor interface. The input clock to the processor PLL is 166 MHz.

The computer provides two RAM slots that accommodate 200-pin DDR2 SDRAM SO-DIMMs up to 1.25” in height. The SO-DIMMs must be DDR2 PC2-5300-compliant and must be unbuffered, unregistered, 8-byte, nonparity, and non-ECC. The computer ships with two 256 MB DDR2 SDRAM SO-DIMMs for a total of 512 MB. Additional RAM must be installed in pairs of equal sizes. For additional information, refer to _[RAM Expansion Developer Note](../RAM%20Expansion%20Developer%20Note/Introduction%20to%20RAM%20Expansion%20Developer%20Note.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztamzr)_.

The North Bridge and South Bridge ICs are connected by a Direct Media Interface (DMI) bus, a high-speed, bidirectional, point-to-point link supporting a clock rate of 1 GB per second in each direction

The Extensible Firmware Interface (EFI) Boot ROM consists of 2 MB of on-board flash EEPROM. It includes the hardware-specific code and tables needed to start up the computer, load an operating system, and provide common hardware access services.The EFI Boot ROM connects to the South Bridge via Serial Peripheral Interface (SPI) bus.

Internal to the North Bridge IC is the Intel GMA950 graphics subsystem. The Mac mini has a DVI connector for an external video monitor. For more information on the graphics subsystem and display capabilities, refer to _[Video Developer Note](../../Hardware/Video%20Developer%20Note/Introduction%20to%20Video%20Developer%20Note.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztkmbu)_.

The Mac mini comes with a 5400 rpm Serial ATA (SATA) Gen-I (1.5 Gbps) disk drive. The SATA disk drives operate through an AHCI 1.1 controller that supports advanced SATA-II features such as Native Command Queuing (NCQ) and PHY power management.

For more information on SATA, see the [Serial ATA International Organization](http://www.serialata.org/) (SATA-IO) website.

For information on the AHCI controller, see [http://www.intel.com/technology/serialata/ahci.htm](http://www.intel.com/technology/serialata/ahci.htm).

In the Mac mini computer, the South Bridge controller provides an Ultra ATA/100 interface (running at UATA/66) to the slot-loading, SuperDrive or Combo drive. The drive can read and write optical media, as shown in [Table 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2demzyfvjvomy) and [Table 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2demzyfvjvona).

The optical drive is configured as device 0 (master) and complies with the ATA/ATAPI-5 industry standard. For information on parallel ATA interfaces, see the International Committee on Information Technology Standards (INCITS) Technical Committee T13 [AT Attachment](http://www.t13.org/) website.

__Table 1__  Types of media read and written by the SuperDrive

| Media type | Reading speed | Writing speed |
| DVD +/- R | 6x (CAV) | 8x ZCLV |
| DVD+R DL | 6x (CAV) | 2.4x CLV |
| DVD +/- RW | 6x (CAV) | 4x ZCLV |
| DVD-ROM SL | 8x (CAV) | – |
| DVD-ROM DL | 6x (CAV) | – |
| CD-R | 24x (CAV) | 24x ZCLV |
| CD-RW | 24x (CAV) | 16x ZCLV |
| CD-ROM | 24x (CAV) | – |

__Table 2__  Types of media read and written by the Combo Drive

| Media type | Reading speed | Writing speed |
| DVD +/- R | 8x (CAV) | – |
| DVD+R DL | 5x (CAV) | – |
| DVD-ROM SL | 8x (CAV) | – |
| DVD-ROM DL | 5x (CAV) | – |
| DVD +/- RW | 5x (CAV) | – |
| CD-R | 24x (CAV) | 24x ZCLV |
| CD-RW | 24x (CAV) | 16x ZCLV |
| CD-ROM | 24x (CAV) | – |

The computer has one IEEE-1394a FireWire 400 port, which supports transfer rates of 100, 200, and 400 Mbps. For more information, see _[FireWire Developer Note](../FireWire%20Developer%20Note/Introduction%20to%20FireWire%20Developer%20Note.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztamry)_.

The computer has a built in Ethernet port for a 10BASE-T/UTP, 100BASE-TX and 1000BASE-T Gigabit operation. For more information, see _[Ethernet Developer Note](../Ethernet%20Developer%20Note/Introduction%20to%20Ethernet%20Developer%20Note.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztamrz)_.

The South Bridge IC includes an integrated USB 2.0 controller supporting the Bluetooth module, IR receiver, and 4 external USB 2.0 ports. The USB ports comply with the Universal Serial Bus Specification 2.0. For more information, see _[Universal Serial Bus Developer Note](../Universal%20Serial%20Bus%20Developer%20Note/Introduction%20to%20Universal%20Serial%20Bus%20Developer%20Note.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztamrw)_.

The Mac mini computer has an internal AirPort Extreme module, connected to a dedicated 1-lane PCI Express link, and a Bluetooth 2.0 + EDR (enhanced data rate) module, connected to the USB 2.0 controller. AirPort Extreme and Bluetooth have independent built-in antennas.  For more information, see _[AirPort Developer Note](../AirPort%20Developer%20Note/Introduction%20to%20AirPort%20Developer%20Note.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztamzq)_ and _[Bluetooth Developer Note](../Bluetooth%20Developer%20Note/Introduction%20to%20Bluetooth%20Developer%20Note.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztamzs)_.

The computer has a combination analog audio line-in and S/PDIF digital optical audio line-in jac, and a combined analog output and S/PDIF digital optical audio line-out jack. For more information, see _[Audio Developer Note](../../Hardware/Audio%20Developer%20Note/Introduction%20to%20Audio%20Developer%20Note.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztkmbv)_.

The Mac mini uses an advanced system management controller (SMC) to manage thermal and power conditions, while keeping the acoustic noise to a minimum. The SMC is fully independent of the operating system.

[Next](Document%20Revision%20History.md)[Previous](Introduction%20to%20Mac%20mini%20Developer%20Note.md)

