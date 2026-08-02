---
title: Writing PCI Drivers
apple_id: TP40000975
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2006-04-04'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/WritingPCIDrivers/pci_controller/pci_controller.html
archived_at: '2026-07-15T07:31:54.204784Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Writing PCI Drivers](About%20This%20Book.md)


[Next](Writing%20a%20Driver%20for%20a%20PCI%20Device.md)[Previous](PCI%20Family%20Architecture.md)

# Writing a Driver for a PCI Bridge

Writing a driver for a PCI bridge is not a simple task. Most PCI bridges do not need any special drivers, and in general, if you are designing the hardware, you are urged to use bridge parts that comply with PCI specifications and thus do not need special drivers. This is not always possible in certain edge cases, however. This is generally because either the hardware already exists or because a transparent bridge does not provide the needed functionality.

This section explains how to write drivers for the most common types of programmable PCI bridges and explains some of the differences between those types of bridges from both a hardware perspective and from a programming perspective.

There are three basic types of PCI bridges: PCI host controllers, transparent PCI bus bridges, and nontransparent PCI bus bridges. They each have their own special issues.

- Host controllers—devices that bridge between a processor (host) bus and a PCI bus. These are generally built into a computer and cannot be added after the fact except via a processor-direct slot (PDS). Unless you are adding support for unsupported computers, you should never need to write a driver for a host controller. For more information, see [Writing Drivers for Host Controllers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnbwfvbuossijjeeqri).
- Transparent bus bridges—a traditional PCI bridge. These devices are commonly used to extend a PCI bus beyond the physical distance allowed for a simple bus by the PCI specification. Because they connect one standard PCI bus to another standard PCI bus, their interface is well-defined, and they do not need special drivers except to work around bugs in the hardware. For more information, see [Writing Drivers for Transparent Bridges](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnbwfvbuossdijfemqq).
- Nontransparent bus bridges—a translating PCI bridge, often used to connect two PCI busses that are managed by separate hosts. In some embedded systems, for example, two hosts can use a nontransparent bridge for backplane networking or to share memory between two systems. One side of the bridge is configured (usually in hardware) to be the master. That host sets up the bridge. The two sides may have different address space layouts and different bus address ranges. The bridge then does PCI address translation to rewrite requests as they come through the bridge. For more information, see [Writing Drivers for Nontransparent Bridges](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnbwfvbuosski5eumsa).
- Other bridges—Other bridges exist, such as CardBus to PCI and PCI to CardBus. Neither of these differs substantially from a transparent PCI bridge except that you need to provide certain additional services such as ejecting and detecting the insertion of cards. Some more extreme bridges, such as ISA to PCI also exist but are rare. You will probably never need to write a driver for any of these sorts of devices, and thus they are not covered here. However, some of the information regarding transparent bridges and host controllers should be a good stating point. For more information, see [Other Bridges](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnbwfvbuosskifeuiqy).

Many of the details of writing a driver for a PCI host controller are device-specific. In many respects, it is similar to writing any other device driver for a device on the main logic board. It is different, however, in that with a PCI host controller you must configure the controller in such a way that the rest of the PCI subsystem can talk to devices behind it. The issues of interrupt assignment and address range assignment are particularly significant in this regard.

The basic process is as follows. The host controller has certain Open Firmware properties (or for Darwin/x86, the platform expert presents certain properties) that identify the physical address and size of its register set. You should map this range into the kernel’s virtual address space using an `IOMemoryMap` object.

You then create a PCI address range for the bridge and set the registers on the device appropriately based on the range you obtained. You also need to provide a standard set of routines for communicating with devices on the PCI bus. The system then uses these routines to finish configuring the devices on the bus.

The following methods should be implemented in a PCI host controller driver:

**`start`**
: Gets information about the bridge (as needed) and maps the bridge hardware into the kernel’s address space.

**`configure`**
: Configures the controller with the base address and size of the PCI bus.

**`free`**
: Releases any data structures created by the driver, including the mapping of the controller into kernel memory, as well as any locks, queues, and other dynamically allocated structures that the driver may have created during operation or within the `start` routine.

**`ioDeviceMemory`**
: Returns a pointer of type `IODeviceMemory` to a class instance that contains information about the base address and size of the bus’s memory space. This pointer is created in the `start` routine.

**`firstBusNum`**
: Returns the first PCI bus number that lives beyond this controller.

**`lastBusNum`**
: Returns the last PCI bus number that lives beyond this controller.

**`getBridgeSpace`**
: Returns the `IOPCIAddressSpace` entry representing the bridge. This entry contains the bus number, device number, and configuration space bitfield for the bridge itself. The `bits` field, which holds the bitfield, should be set to `0` since it is not relevant except for devices that reside on the PCI bus.

**`setConfigSpace`**
: Sets a device’s configuration bits (bus master enable, memory space enable, and so on) using a write to PCI configuration space, based on information contained in an `IOPCIAddressSpace` entry (bus number, device number, and bitfield).

**`configRead32`, `configRead16`, and `configRead8`**
: Reads 32, 16, or 8 bytes from an address in PCI configuration space.

**`configWrite32`, `configWrite16`, and `configWrite8`**
: Writes 32, 16, or 8 bytes to an address in PCI configuration space.

**`callPlatformFunction`**
: Call a method in the platform expert. This method is defined in the `IOPCIBridge` base class, but it may be overridden in an individual PCI bridge driver to allow you to add additional calls specific to your bridge or to override the behavior of existing calls.

For more information, you should study the `AppleMacRiscPCI` driver and the other PCI drivers available from Apple’s Open Source website, which can be found at [http://www.opensource.apple.com](http://www.opensource.apple.com/), or contact Apple Developer Technical Support.

In general, transparent PCI bridges do not require special drivers, because they obey a very strict specification. However, if a transparent bridge fails to follow the PCI specification, you may need to change the behavior of the transparent bridge driver to support your particular device.

To easily create a driver for a non-compliant transparent bridge, you should subclass the standard Apple transparent bridge driver and modify or extend the basic initialization code. If you do this, be _certain_ to set appropriate passive matching parameters or use active matching so that your modified driver matches against only the particular bridge in question. Otherwise, your driver could break the normal operation of other PCI bridges in the system. For details on passive and active matching, see [Open Firmware Matching](Writing%20a%20Driver%20for%20a%20PCI%20Device.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnbxfvkfawcsivddcmbu) or read the appropriate parts of _[IOKit Fundamentals](../IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_.

Fundamentally, nontransparent bridges, which are also often called embedded bridges, are not what most people would describe as bridges, in that they do not generally make devices on one side of the bridge accessible to devices on the other side, nor do they pass traditional interrupts from one side to the other. What makes them bridges is that they are connected to and provide limited communication between two busses.

Drivers for nontransparent bridges are highly device-specific. They appear to each side as a single PCI device, not a bridge. Neither side can see devices on the opposite side of the bridge. They can, however, see address ranges that are explicitly mapped and perform basic interrupt-based communication between the two sides. Thus, it is possible, to a limited degree, to control devices across such a bridge, though they are not generally used in this way.

These devices generally have a series of BATs (block address translation registers) that map a large range onto another large range. In most cases, the client must actually know how to control these BATs whether it is a driver that controls a physical device behind the bridge or a pseudo-device that maps memory across the bridge for backplane networking. You can make the BATs accessible to the client through a user client if the client is in user space, or by simply publishing a nub if the client is another driver within the kernel.

Similarly, these devices often have “doorbell” interrupts for basic communication. These interrupts are triggered by the computer on one side of the bridge and are seen by the computer on the other. Your client interface should reflect this and should provide access as appropriate.

In all other respects, however, nontransparent bridges behave like normal PCI devices from a software perspective. Thus, if you need to write a driver for a nontransparent bridge, you should read [Writing a Driver for a PCI Device](Writing%20a%20Driver%20for%20a%20PCI%20Device.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnbxfvkfaoi) for more information.

Many other types of PCI bridges exist. Most of them fall into one of these categories:

- Bridges to add a non-PCI bus into a system where a PCI bus exists, such as a PCI to ISA bridge
- Bridges to add a PCI bus into a system where a non-PCI bus exists, such as an ISA to PCI bridge
- Bridges between CardBus (a removable PCI standard) and PCI.

With the exception of special features like ejection and device detection, CardBus devices are just PCI devices, and CardBus bridges behave like transparent bridges. Thus, you should read [Writing Drivers for Transparent Bridges](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnbwfvbuossdijfemqq) and [Writing a Driver for a PCI Device](Writing%20a%20Driver%20for%20a%20PCI%20Device.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnbxfvkfaoi) for general information, then look in the `IOPCCardFamily` from Apple’s Open Source website for CardBus-specific extensions.

Other bridges, such as those involving ISA or other busses, are beyond the scope of this document. For help with such bridges, you should contact Apple Developer Technical Support.

Because most Ethernet hardware is found on the PCI bus, debugging a PCI host bridge using traditional Ethernet-based (`gdb`) debugging can pose difficulties. For this reason, you should consider building a custom kernel with `ddb` (serial debugging) support enabled. With this option, you will still be able to debug if the address mappings in your host bridge get inadvertently changed and attaching by Ethernet becomes impossible.

For more information on building a kernel with `ddb` support, and for instructions and advice on debugging drivers using `gdb` and `ddb`, see _[Kernel Programming Guide](../../Darwin/Kernel%20Programming%20Guide/About%20This%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbv)_, available from the Darwin section of Apple’s developer documentation website, [http://developer.apple.com/Documentation](https://developer.apple.com/Documentation).

[Next](Writing%20a%20Driver%20for%20a%20PCI%20Device.md)[Previous](PCI%20Family%20Architecture.md)

