---
title: Thunderbolt Device Driver Programming Guide
apple_id: TP40011138
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/documentation/HardwareDrivers/Conceptual/ThunderboltDevGuide/DebuggingThunderboltDrivers/DebuggingThunderboltDrivers.html
archived_at: '2026-07-15T07:41:11.934142Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Thunderbolt Device Driver Programming Guide](About%20the%20Thunderbolt%20Technology.md)


[Next](Document%20Revision%20History.md)[Previous](Handling%20and%20Routing%20Interrupts.md)

# Debugging Thunderbolt Drivers

This chapter contains debugging tips that may be useful when tracking down problems in Thunderbolt drivers.

Newer Thunderbolt-capable Macs provide support for I/O MMU virtualization (VT-d). This technology allows virtual machines to have direct access to hardware. As a consequence of this support, when your device performs DMA operations, the I/O addresses it uses may be different from the physical addresses as seen by the OS X kernel.

The complete spec can be found here: [Intel® Virtualization Technology for Directed I/O Specification](https://www-ssl.intel.com/content/www/us/en/intelligent-systems/intel-technology/vt-directed-io-spec.html).

Ivy Bridge systems running OS X v10.8.2 and later enable the Intel VT-d unit as a DMA remapper. This functionality is supported by the current APIs in much the same way as the DART controller on PowerMac G5 computers. (To learn how this works at a high level, read [Supporting DMA on 64-Bit System Architectures](../../Device%20Drivers/IOKit%20Fundamentals/Managing%20Data.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcojnknlte)).

When VT-d is enabled, some of the changes you'll see as a results of this are:

- If you are writing DMA programs, although physical segments returned by `IOMemoryDescriptor` or `IODMACommand` are contiguous ranges of I/O addresses, the I/O addresses for the segments may be different than the CPU physical addresses, and the ranges are no longer necessarily contiguous in physical memory from perspective of the CPU.

  As a result, segments will usually be the same size as the full `IOMemoryDescriptor` size (for a virtually contiguous `IOMemoryDescriptor` object with a single source buffer).
- By default, requests for physically contiguous memory return memory that is contiguous only from the perspective of I/O devices, and may not be physically contiguous in RAM.

  If the memory must be contiguous to the CPU as well, you must pass the `kIOMemoryHostPhysicallyContiguous` option to `IOBufferMemoryDescriptor` when you request the memory. As before, such requests can fail if no physically contiguous blocks are available.
- Transactions now fail if memory descriptors or DMA commands are not properly prepared for reading or writing.

  The `prepare` method adds a mapping entry into the I/O address translation table. You must call `prepare` (and specify the correct direction) before you tell the device to read data from or write data to that region of memory.

  You must also balance each `prepare` call with a matching call to the `complete` method. If you do not, your driver will eventually fill up the mapping table, and you will get a kernel panic the next time a driver tries to add a mapping table entry.
- The `prepare` and `complete` methods have additional overhead, though this impact is partially counterbalanced by shorter scatter-gather lists.

If you ask for unmapped physical addresses—by calling an `IOMemoryDescriptor` object’s `getPhysicalSegment` method with the option `kIOMapperNone` or an `IODMACommand` object’s `initWithSpecification` method with `mappingOptions` set to something other than `kMapped`—and try to use them for DMA, your driver will break.

By default, VT-d faults are logged to `/var/log/system.log`. A VT-d fault looks like the following:

```
vtd[0] fault: device 13:0:0 reason 0x6 R:0x3dff000
```

In the example above, `13:0:0` is the bus, device, and function of the device that generated the fault. You can determine if your device produced the fault by looking at the `pci-debug` field in the output of the `ioreg` or in the IORegistryExplorer application and comparing the values.

For a list of reason codes, see the [Intel® Virtualization Technology for Directed I/O Specification](https://www-ssl.intel.com/content/www/us/en/intelligent-systems/intel-technology/vt-directed-io-spec.html).

The R indicates that a read operation triggered the fault. (A W indicates a write.) The final value is the address that the device was trying to read or write (expressed as an I/O-space address).

When debugging faults, it can be useful to configure your kernel to panic whenever a fault occurs. To do this, add the following flag in your kernel boot args:

```
pci=0x100
```


When debugging PCIe device drivers, it is often useful to temporarily disable VT-d so that I/O addresses are the same as the corresponding physical addresses. To disable VT-d, add the following to your kernel boot args:

```
dart=0x0
```

If the problem you are debugging goes away in this mode, it usually indicates one of the following mistakes:

- Some part of your code is incorrectly passing a physical address in RAM to your device for DMA purposes instead of an I/O address.
- Your code failed to call `prepare` or called `prepare` incorrectly on an `IOMemoryDescriptor` object before using it to perform DMA.

By default, the OS X kernel spreads out PCI address allocations. As a result, PCIe pause events occur infrequently, which makes these events challenging to debug. You can make debugging easier by disabling this allocation spreading behavior. With spreading disabled, nearly every hot plug event triggers a pause event.

To disable allocation spreading, add the following to your kernel `boot-args` string:

```
pci=0x200
```


Drivers should ensure release of any and all resources acquired over the lifecycle of the driver. In particular, memory mapped I/O ranges, memory, and objects should all be freed and double-checked for any leaks. Use of tools such as [ioclasscount](https://developer.apple.com/library/mac/#documentation/Darwin/Reference/ManPages/man8/ioclasscount.8.html) can help identify some of these types of leaks. A common form of leaks is introduced by references (that is, retain counts). Often, it is difficult to determine the source of these references. One way to determine the source of these references is to override the `taggedRetain()` method and obtain a backtrace of the caller, which you can then send to `printf()`, `kprintf()`, or `IOTimeStampConstant()`.

__Listing 4-1__  Searching for Memory Leaks

```
   void
   AppleSamplePCI::taggedRetain ( const void * tag ) const
   {
             void *    bt[16] = { 0 };

             OSBacktrace ( &amp;bt[0], sizeof ( bt ) / sizeof ( bt[0] ) );
             super::taggedRetain ( tag );
   }
```

Using standard symbolication tools allows you to determine which functions or methods caused the reference(s) to be taken. Furthermore, you can override `taggedRelease()` and match the retains and releases to find calls to `taggedRetain()`, which have no corresponding call to `taggedRelease()`.

[Next](Document%20Revision%20History.md)[Previous](Handling%20and%20Routing%20Interrupts.md)

