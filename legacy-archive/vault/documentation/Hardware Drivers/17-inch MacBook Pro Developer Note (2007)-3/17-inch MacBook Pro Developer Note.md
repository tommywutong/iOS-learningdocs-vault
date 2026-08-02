---
title: 17-inch MacBook Pro Developer Note
apple_id: TP40006713
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-14'
source_url: https://developer.apple.com/library/archive/documentation/HardwareDrivers/Conceptual/17inMacBookPro_0711/Articles/ProductDeveloperNote.html
archived_at: '2026-07-15T07:40:57.627639Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [17-inch MacBook Pro Developer Note](Introduction%20to%2017-inch%20MacBook%20Pro%20Developer%20Note.md)


[Next](Document%20Revision%20History.md)[Previous](Introduction%20to%2017-inch%20MacBook%20Pro%20Developer%20Note.md)

# 17-inch MacBook Pro Developer Note

This note describes the 17-inch MacBook Pro computers introduced in November 2007. The standard configuration is based on the 2.4 GHz Intel Core 2 Duo microprocessor and a 2.6 GHz configuration is available as a build-to-order option. It includes information about distinguishing features of the computer, including components on the main logic board: the microprocessor, the other main ICs, and the buses that connect them to each other and to the I/O interfaces.

The computer comes with Mac OS X version 10.5 installed.

The value of the 17-inch MacBook Pro model identifier string is `MacBookPro3,1`.

The architecture of the 17-inch MacBook Pro is based on the Intel Core 2 Duo microprocessor and two ICs, the North Bridge memory controller and the South Bridge I/O controller, connected to each other by a Direct Media Interface (DMI) bus. The North Bridge provides the bridging functionality among the processor, the memory system, the DMI bus, and the 16-lane PCI Express bus to the graphics controller. The South Bridge supports these components:

- Ultra ATA/100 bus for the optical drive (running at UATA/66)
- A 1.5 Gbps Serial ATA (SATA) bus for the hard disk drive
- 1-lane PCI Express link for the AirPort Extreme module
- SPI bus, direct memory access bus to the boot ROM
- USB 2.0 controller, which in turn supports the Bluetooth module, IR receiver, built-in iSight camera, built-in trackpad and keyboard, ExpressCard/34 slot, and 3 external USB 2.0 ports
- Channel to the audio subsystem
- 1-lane PCI Express link for the Ethernet PHY
- 33 MHz, 32-bit internal PCI bus to the FireWire 400 (1394a) and FireWire 800 (1394b) OHCI and PHY
- 1-lane PCI Express link and one USB 2.0 interface for the ExpressCard 34 mm slot
- Direct Media Interface (DMI) bus

A DMA controller internal to the South Bridge supports LPC DMA (low pin count direct memory access). The DMA controller has registers that are fixed in the lower 64 KB of I/O space. The DMA controller is configured using registers in the PCI configuration space.

Figure 1 provides a simplified block diagram of the North Bridge and South Bridge ICs and the buses that connect them together.

__Figure 1__  Block diagram

![This block diagram shows the memory controller and I/O controller ICs and the buses that connect them on the main logic board. Each component in the block diagram is defined in text.](attachments/Art/070267011321_01.jpg)

The 17-inch MacBook Pro computer includes a built-in iSight video camera, an integrated IR receiver, and the Apple Remote. For a complete list of user-visible features, see the 17-inch MacBook Pro specification sheet at Apple's [Specifications](http://www.info.apple.com/support/applespec.html) site. Other features are described in this section.

The microprocessor in the 17-inch MacBook Pro is an Intel Core 2 Duo with a clock speed of 2.4 GHz, or optionally 2.6 GHz. It has the following features:

- 2.4 GHz dual core processors
- 2.6 GHz dual core processors build-to-order option
- 4 MB shared L2 cache
- Intel Advanced Digital Media Boost
- Connection to the North Bridge IC over an 800 MHz frontside bus
- Supports Intel 64 Architecture

See the [Intel Core 2 Duo Processors](http://www.intel.com/products/processor/core2duo/index.htm) support site for detailed microprocessor documentation.

Intel Advanced Digital Media Boost accelerates data manipulation by applying a single instruction to multiple data at the same time, known as SIMD processing. SIMD technology accelerates vector math operations and floating-point calculations. Advanced Digital Media Boost supports Intel Streaming SIMD Extensions (SSE) versions 1, 2, and 3 and allows the processor to execute an SSE3 instruction every clock cycle.

For information on Advanced Digital Media Boost, refer to [Technology@Intel Magazine](http://www.intel.com/technology/magazine/computing/core-architecture-0306.htm?iid=hwd_center+coremicroww18&).

[Intel 64 Architecture](http://www.intel.com/technology/architecture-silicon/intel64/index.htm) increases the linear address space for software to 64 bits and supports physical address space up to 40 bits. The technology also introduces a new operating mode referred to as IA-32e mode. IA-32e mode operates in one of two sub-modes:

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

An Intel 64 Architecture processor supports existing IA-32 software because it is able to run all non-64-bit legacy modes supported by IA-32 architecture. Most existing IA-32 applications also run in compatibility mode.

For information on Intel 64 Architecture, refer to the following website:

The processor bus is an 800 MHz bus connecting the processor to the North Bridge. The bus has 32-bit wide data running in both directions.

The point-to-point architecture provides each subsystem with dedicated bandwidth to main memory. The North Bridge implements an independent processor interface. The input clock to the processor PLL is 200 MHz.

The computer provides two RAM slots that accommodate 200-pin DDR2 SDRAM SO-DIMMs up to 1.25” in height. The SO-DIMMs must be 667 MHz, PC2-5300, unbuffered, non-ECC compliant devices. The 17-inch MacBook Pro ships with two 1GB DDR2 SDRAM SO-DIMMs installed, for a total of 2GB. For additional information, refer to _[RAM Expansion Developer Note](../RAM%20Expansion%20Developer%20Note/Introduction%20to%20RAM%20Expansion%20Developer%20Note.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztamzr)_.

The North Bridge and South Bridge ICs are connected by a Direct Media Interface (DMI) bus, a high-speed, bidirectional, point-to-point link supporting a data rate of 1 GB per second in each direction.

The Extensible Firmware Interface (EFI) Boot ROM consists of 2 MB of on-board flash EEPROM. It includes the hardware-specific code and tables needed to start up the computer, load an operating system, and provide common hardware access services.The EFI Boot ROM connects to the South Bridge via Serial Peripheral Interface (SPI) bus.

The graphics subsystem includes an NVIDIA GeForce 8600M GT, with 256 MB GDDR3 SDRAM, connected to the North Bridge IC by a x16 link (16 lane), dual simplex, 2.5 GHz PCI Express bus. The 17-inch MacBook Pro has a dual-link DVI connector for an external video monitor and supports video mirroring mode and extended desktop display mode. For more information on the graphics subsystem and display capabilities, refer to _[Video Developer Note](../../Hardware/Video%20Developer%20Note/Introduction%20to%20Video%20Developer%20Note.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztkmbu)_.

For more information on PCI Express, refer to _[PCI Developer Note](../../Hardware/PCI%20Developer%20Note/Introduction%20to%20PCI%20Developer%20Note.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztamrx)_.

The 17-inch MacBook Pro comes with a 160 GB 5400 rpm (optionally, a 250 GB 5400 rpm or 200 GB 7200 rpm) Serial ATA (SATA) Gen-I (1.5 Gbps) hard disk drive. The SATA hard disk drives operate through an AHCI 1.1 controller that supports advanced SATA-II features such as Native Command Queuing (NCQ) and PHY power management.

For more information on SATA, see the [Serial ATA International Organization](http://www.serialata.org/) (SATA-IO) website.

For information on the AHCI controller, see [http://www.intel.com/technology/serialata/ahci.htm](http://www.intel.com/technology/serialata/ahci.htm).

In the 17-inch MacBook Pro computer, the South Bridge controller provides an Ultra ATA/100 interface (running at UATA/66) to the 12.7 mm high slot-loading, SuperDrive. The drive can read and write DVD media and CD media, as shown in Table 1.

__Table 1__  Types of media read and written by the SuperDrive

| Media type | Reading speed | Writing speed |
| DVD+/- R | 8x (CAV) | 8x (CAV) |
| DVD-R DL | 6x (CAV) | 4x ZCLV |
| DVD-ROM SL | 8x (CAV) | – |
| DVD-ROM DL | 6x (CAV) | – |
| DVD+RW | 8x (CAV) | 8x ZCLV |
| DVD-RW | 6x (CAV) | 6x ZCLV |
| CD-R | 24x (CAV) | 24x ZCLV |
| CD-RW | 24x (CAV) | 16x ZCLV |
| CD-ROM | 24x (CAV) | – |

The SuperDrive is configured as device 0 (master) and complies with the ATA/ATAPI-5 industry standard. For information on parallel ATA interfaces, see the International Committee on Information Technology Standards (INCITS) Technical Committee T13 [AT Attachment](http://www.t13.org/) website.

The computer has one IEEE-1394a FireWire 400 port, which supports transfer rates of 100, 200, and 400 Mbps and one IEEE-1394b FireWire 800 port, which supports 800 Mbps transfer rates in addition to 1394a transfer rates. For more information, see _[FireWire Developer Note](../FireWire%20Developer%20Note/Introduction%20to%20FireWire%20Developer%20Note.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztamry)_.

The computer has a built in Ethernet port for a 10BASE-T/UTP, 100BASE-TX and 1000BASE-T Gigabit operation. For more information, see _[Ethernet Developer Note](../Ethernet%20Developer%20Note/Introduction%20to%20Ethernet%20Developer%20Note.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztamrz)_.

The South Bridge IC includes an integrated USB 2.0 controller supporting the Bluetooth module, IR receiver, built-in iSight camera, built-in trackpad and keyboard, Express Card/34 slot, and 3 high-powered external USB 2.0 ports. The USB ports comply with the Universal Serial Bus Specification 2.0. For more information, see _[Universal Serial Bus Developer Note](../Universal%20Serial%20Bus%20Developer%20Note/Introduction%20to%20Universal%20Serial%20Bus%20Developer%20Note.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztamrw)_.

The 17-inch MacBook Pro computer has an internal AirPort Extreme module, connected to a dedicated 1-lane PCI Express link, and a Bluetooth 2.0 + EDR (enhanced data rate) module, connected to the USB 2.0 controller. AirPort Extreme and Bluetooth have independent built-in antennas. For more information, see _[AirPort Developer Note](../AirPort%20Developer%20Note/Introduction%20to%20AirPort%20Developer%20Note.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztamzq)_ and _[Bluetooth Developer Note](../Bluetooth%20Developer%20Note/Introduction%20to%20Bluetooth%20Developer%20Note.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztamzs)_.

The computer has a built-in microphone, a combination analog audio line-in and S/PDIF digital optical audio line-in jack, and a combined analog output and S/PDIF digital optical audio line-out jack. For more information, see _[Audio Developer Note](../../Hardware/Audio%20Developer%20Note/Introduction%20to%20Audio%20Developer%20Note.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztkmbv)_.

The 17-inch MacBook Pro uses an advanced system management controller (SMC) to manage thermal and power conditions, while keeping the acoustic noise to a minimum. The SMC is fully independent of the operating system.

[Next](Document%20Revision%20History.md)[Previous](Introduction%20to%2017-inch%20MacBook%20Pro%20Developer%20Note.md)

