---
title: Writing PCI Drivers
apple_id: TP40000975
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2006-04-04'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/WritingPCIDrivers/pci_device/pci_device.html
archived_at: '2026-07-15T07:31:54.214454Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Writing PCI Drivers](About%20This%20Book.md)


[Next](Writing%20a%20Driver%20for%20an%20AGP%20Device.md)[Previous](Writing%20a%20Driver%20for%20a%20PCI%20Bridge.md)

# Writing a Driver for a PCI Device

A PCI device driver manages a device attached to a PCI bus. The driver matches and attaches to a nub object of the `IOPCIDevice` or `IOAGPDevice` class, configures the device through the PCI configuration space, and sets up the memory-mapped registers or the I/O space to make it possible to control the device. Little else is necessary other than the code to control the device itself.

A driver that is capable of controlling a device on a PCI bus announces this fact by including a personality in its property list. This personality includes the key `IOProviderClass` with the value `IOPCIDevice`.

Because `IOAGPDevice` is a subclass of `IOPCIDevice`, it is not necessary to match on `IOAGPDevice` for your driver to attach to AGP devices. Thus, you should generally only match on `IOPCIDevice`.

`IOPCIDevice` and `IOAGPDevice` both define two sets of keys that a driver can use for matching, one based on standard PCI registers and another based on Open Firmware. A PCI device driver can use either type of key. It can even use a combination of the two as long as they are in separate personalities.

PCI device drivers can base their property matching on the PCI configuration space registers for vendor and device ID (offsets 0x00 and 0x02), subsystem vendor and device ID (offsets 0x2C and 0x2E), and class code (offset 0x09). Other registers, such as revision ID and header type, are not available in property matching and must be examined by the `probe` method. The PCI matching dictionary keys are:

| Key | Matching behavior |
| --- | --- |
| `IOPCIMatch` | Matches against the primary vendor/device ID registers or the subsystem vendor/device ID registers. The primary IDs are checked first; if either of these doesn’t match then the subsystem IDs are checked. |
| `IOPCIPrimaryMatch` | Matches only against the primary vendor/device ID registers. |
| `IOPCISecondaryMatch` | Matches only against the subsystem vendor/device ID registers. |
| `IOPCIClassMatch` | Matches against the class code register. |

The value for a key can be a single register value or a list of register values separated by spaces. Register values are given as little-endian hexadecimal strings, with the device ID first and the vendor ID second. See [Endianness and Addressing](Endianness%20and%20Addressing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnbzfvbuqrcjjbeuora) for more information on endianness.

In addition to the value itself, each key value can include a mask indicating that only part of the value should be compared.

Here are some examples of matching dictionary entries. The first example matches a PCI device with a primary vendor ID of 0x8086 and primary device ID of 0x1229, or with subsystem IDs of those values.

```
<key>IOPCIMatch</key>
    <string>0x12298086</string>
```

The second example matches a PCI device with a primary vendor ID of 0x8086 and a primary device ID of 0x1229 or 0x1227, or with subsystem IDs of those values.

```
<key>IOPCIMatch</key>
    <string>0x12298086 0x12278086</string>
```

The third example matches a PCI device with a primary vendor ID of 0x8086 and a primary device ID of 0x1229. Subsystem IDs aren’t checked.

```
<key>IOPCIMatch</key>
    <string>0x12298086</string>
```

The fourth example uses a mask to match a PCI device with a primary vendor ID of 0x8086 and any primary device ID whose first two digits are 0x12. Subsystem IDs aren’t checked.

```
<key>IOPCIPrimaryMatch</key>
    <string>0x12008086&amp;0xFF00FFFF</string>
```

The mask is attached to the register value using an ampersand character, which must be encoded as `&` in XML if you are editing it directly. If you are using Xcode or Property List Editor, the `&` escape is represented simply as an ampersand (&).

This entry matches a PCI device with a primary vendor ID of 0x8086 and a class code beginning with 0x0200, the class code for Ethernet controllers.

```
<key>IOPCIMatch</key>
    <string>0x00008086&0x0000FFFF</string>
<key>IOPCIClassMatch</key>
    <string>0x02000000&0xFFFFFF00</string>
```


A PCI device driver can use Open Firmware matching in a personality by specifying a value for the `IONameMatch` key. The value is either a single string or an array of strings, which are compared against the values for the Open Firmware device properties `name`, `compatible`, `device_type`, or `model`.

If any of the values for the `IONameMatch` key match any of the Open Firmware properties, the match is considered a success and an instance of the driver is created for the personality. The name that resulted in a match is stored as a property in the driver’s I/O Registry entry in the `IONameMatched` key (`kIONameMatchedKey`).

For more information on name matching, you should consult the documentation for the `IOService` class.

Before a driver begins interacting with a PCI device, whether in the `probe` method or the `start` method, it typically examines the values in the PCI configuration space registers and sets some of them as required. The IOPCIDevice class defines several methods and register masks to make doing so easy.

The most general methods are `configRead32`, `configWrite32`, and `setConfigBits`. The first method reads a full 32-bit value from a 4-byte aligned address in the PCI configuration space. The driver can then extract the specific register value. A driver might use this method during probing to examine the value of the revision ID register, for example. `IOPCIDevice` defines a number of constants for the various register offsets.

The method `configWrite32` writes a full 32-bit value into a 4-byte aligned address in the PCI configuration space. The more flexible method `setConfigBits` can write individual bits into the configuration space without disturbing others. It takes a 32-bit value to write along with a 32-bit mask indicating which bits to set or clear. This is commonly used to write to the command register. This code fragment, for example, enables the memory write and invalidate (MWI) transaction on the bus:

```swift
UInt32 configMask = 0;
UInt32 configBits = 0;

configMask = configBits = kIOPCICommandMemWrInvalidate;

// provider is the PCI nub object
provider->setConfigBits(kIOPCIConfigCommand,
    configMask, configBits);
```

For commonly used configuration settings, IOPCIDevice defines convenience methods that take a `bool` argument for enabling and disabling the settings. These methods are `setMemoryEnable` for memory-mapped control of the PCI device and `setIOEnable` for I/O-mapped control.

Some devices require bus mastering to work properly. For most cards, Open Firmware should set this up automatically based on information in the card’s declaration ROM before OS X even starts to boot. However, this automatic setup does not always occur, depending on the specifics of the particular card and on decisions made by the card vendor when populating the card with ROMs. If a card is not configured correctly in this regard, you can use `setBusMasterEnable` to manually turn bus mastering on or off for the device.

Other methods for inspecting the PCI device include `findPCICapability`, `getBusNumber`, `getDeviceNumber`, and `getFunctionNumber`. For details on these and all other methods, see the reference documentation in `/System/Developer/Documentation`.

The `start` method is where a driver sets up its hardware for operation. For PCI devices this involves configuring the hardware as described above, setting up the communication channel between the CPU and the device, and then performing whatever device-specific initialization is required. You can gain access to PCI device by mapping the device’s registers (its memory space) into the kernel’s address space, or by reading and writing in the device’s I/O space using the nub object.

Mapping the device registers is the most convenient way to set up device control. Once this is done, the driver has very little further interaction with the `IOPCIDevice` nub. Instead, it interacts with the hardware as if it were ordinary memory, albeit uncached memory, using either device accessor methods for byte swapping or by directly dereferencing pointers into the card’s memory space.

I/O space access provides a single programming interface for using I/O space. On processors with a separate I/O memory bus, the I/O space methods actually use this bus. On processors without a separate I/O memory bus, the methods simply use memory-mapped space and handle the required synchronization automatically.

Setting up memory-mapped device control is a two-step process. The driver must first get an `IOMemoryMap` object for one of the device’s base address registers, using the `mapDeviceMemoryWithRegister` method. Constants are available for the base address register offsets. The driver then calls the memory map’s `getVirtualAddress` method to retrieve a pointer to the memory-mapped register block in the kernel’s virtual address space. Here’s an example of the standard idiom for setting up memory-mapped registers, which is typically done in the driver’s`start` method:

```swift
IOMemoryMap *map;

map = provider->mapDeviceMemoryWithRegister(kIOPCIConfigBaseAddress0);
if (!map) {
    // Handle error
}
deviceRegisterPointer = (deviceStruct *)map->getVirtualAddress();
```

Both `map` and `deviceRegisterPointer` are instance variables of the driver. Because the driver created the map object by invoking `mapDeviceMemoryWithRegister`, it must cache the pointer and later release the map object in its `stop` method. `deviceRegisterPointer` is a pointer to a structure defined by the driver that corresponds to the layout of the device-specific registers.

You should note two things when using memory-mapped control of a PCI device. First, the PCI bus standard uses little-endian byte addressing. The endianness of the bus generally has minimal impact on device driver writers. However, the endianness also encourages a related model of register layout that directly affects most driver writers. For more information, see [Endianness and Addressing](Endianness%20and%20Addressing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnbzfvbuqrcjjbeuora).

Second, while accesses into PCI space are explicitly uncached, in-order execution of these accesses is not guaranteed. When order of execution is important, I/O barriers may be used.

I/O barriers are often used for the following reasons:

- To ensure that the operands of a command sent to a device are written into the device’s registers before stating the command.
- To ensure that a command has started executing before polling for its completion status.
- To ensure that an interrupt line is cleared before waiting for that interrupt again.

A general-purpose I/O barrier in OS X is provided by the `libkern` function `OSSynchronizeIO`. On the PowerPC architecture, for example, this issues an `eieio` instruction to enforce in-order execution of the write operation. Because of the performance impact, you should only use an I/O barrier when in-order execution is required for correct operation.

Synchronization is required only when writing directly to hardware registers; when setting up buffers and structures used by hardware, it is not necessary. See an example PCI driver from Apple’s open source collection for examples of how to use `OSSynchronizeIO`.

In unusual circumstances, you might find it desirable to enable caching on portions of I/O space. If you do this, then writes to that portion of PCI space are no longer guaranteed to be written back to the device’s memory space. Additional synchronization is necessary in these cases. Enabling caching and performing I/O to cached I/O spaces is beyond the scope of this book. If you need such support you should contact Apple Developer Technical Support for additional information.

Setting up I/O space access is required only for devices with relocatable I/O spaces. In this case, the driver must obtain an IOMemoryMap object, just as for memory-mapped access. Apart from this, however, I/O space access is performed using a set of six methods for reading and writing 32-bit, 16-bit, and 8-bit values. The `ioWrite16` method, for example, takes a byte offset into the memory space, the value to write, and the memory map for the I/O space. For devices with nonrelocatable I/O spaces, the memory map argument is omitted. The I/O space methods perform all necessary byte swapping and synchronization. For more information on these methods, see the IOPCIDevice reference documentation in `/System/Developer/Documentation/Kernel/IOKit/IOPCIDevice`.

[Next](Writing%20a%20Driver%20for%20an%20AGP%20Device.md)[Previous](Writing%20a%20Driver%20for%20a%20PCI%20Bridge.md)

