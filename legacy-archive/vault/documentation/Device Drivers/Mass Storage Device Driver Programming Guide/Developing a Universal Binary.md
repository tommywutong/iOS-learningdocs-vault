---
title: Mass Storage Device Driver Programming Guide
apple_id: TP40000974
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2007-04-03'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/MassStorage/05_Universal_Binary/MS_UniversalBinary.html
archived_at: '2026-07-15T07:31:32.837126Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Mass Storage Device Driver Programming Guide](Introduction%20to%20Mass%20Storage%20Device%20Driver%20Programming%20Guide.md)


[Next](Subclassing%20Logical%20Unit%20Drivers.md)[Previous](Mass%20Storage%20Driver%20Matching%20and%20Loading.md)

# Developing a Universal Binary

If you plan to create a universal binary version of your logical unit driver, protocol services driver, or filter scheme, first read _[Universal Binary Programming Guidelines, Second Edition](../../Mac%20OSX/Universal%20Binary%20Programming%20Guidelines%2C%20Second%20Edition/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjx)_. That document covers architectural differences and byte-ordering formats and provides comprehensive guidelines for code modification and building universal binaries. Then, to find out how to decide which compiler version and SDK you need, see “Developing a Device Driver to Run on an Intel-Based Macintosh” in _[IOKit Device Driver Design Guidelines](../IOKit%20Device%20Driver%20Design%20Guidelines/Introduction%20to%20I-O%20Kit%20Device%20Driver%20Design%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmoju)_.

This chapter briefly outlines a few of the mass storage–specific issues you should keep in mind as you create a universal binary version of your driver or filter scheme.

As you create a universal binary version of your logical unit or protocol services driver, be aware of places in your code where you might make assumptions about the byte ordering of multibyte numerical values. Be sure to replace any hard-coded byte swaps (such as code that always swaps a multibyte value from big endian to little endian) with the appropriate conditional byte-swapping macros defined in `libkern/OSByteOrder.h`.

For example, the Apple-provided `IOSCSIBlockCommandsDevice` class contains code that uses a byte-swapping macro defined in `OSByteOrder.h` to swap two four-byte fields in a `SCSI_Capacity_Data` structure, as shown in Listing 4-1. (The `SCSI_Capacity_Data` structure is defined as the capacity return structure for the `READ_CAPACITY 10` command in the `SCSICmds_READ_CAPACITYDefinitions.h` header file.)

__Listing 4-1__  Byte-swapping in IOSCSIBlockCommandsDevice code

```
bool IOSCSIBlockCommandsDevice::DetermineMediumCapacity (UInt64 * blockSize, UInt64 * blockCount) {
SCSI_Capacity_Data    capacityData = {0};
...
*blockSize = 0;
*blockCount = 0;
...
// Create and send READ_CAPACITY command.
// If the command completed successfully:
*blockSize = OSSwapBigToHostInt32 (capacityData.BLOCK_LENGTH_IN_BYTES);
*blockCount = ((UInt64) OSSwapBigToHostInt32 (capacityData.RETURNED_LOGICAL_BLOCK_ADDRESS)) + 1;
...
}
```

In general, data returned from devices that comply with the SCSI Architecture Model specifications is in the big-endian format. Fortunately, however, the SCSI command model specification defines the CDB (command descriptor block) as a byte array. This means that the bytes are stored in the defined order regardless of the native endian format of the computer the driver is running in.

As you create a universal binary version of your filter-scheme driver, be aware that filter schemes frequently handle data structures that are read from or written to disk. It's essential that the data structure on the disk remain in the correct endian format so the disk can be used with both PowerPC-based and Intel-based Macintosh computers. Depending on the native endian format of the computer in which your filter-scheme driver is running, therefore, your driver may need to byte swap the data structures it handles.

If you've determined that byte-swapping is necessary, you can implement it in either of the following two ways:

- Perform the appropriate byte swap in memory when the data structure is read in from the disk and perform the opposite byte swap when the data structure is written out to the disk. This means your driver can access the data structure in memory without having to worry about the data structure's endian format.
- Do not swap the endian format of the data structure while it is in memory, but perform the appropriate byte swap on each access. This keeps the data structure in the correct endian format for the disk while it resides in memory, which means your driver does not have to byte swap the data structure when reading it in or writing it out.

To avoid confusion, it's best to choose only one of these two alternatives and be consistent in its implementation. Whichever option you choose, however, be sure to use the conditional byte-swapping macros defined in `libkern/OSByteOrder.h`. When you use these macros, the compiler optimizes your code so the routines are executed only if they are necessary for the architecture in which your driver is running.

For example, the built-in Apple partition-scheme driver, `IOApplePartitionScheme`, uses a byte-swapping macro defined in `OSByteOrder.h` to swap a two-byte field in a `dpme` structure, as shown in Listing 4-2. (The `dpme` structure is defined as a disk partition map entry in the `IOApplePartitionScheme.h` header file.)

__Listing 4-2__  Byte-swapping in IOApplePartitionScheme code

```swift
OSSet * IOApplePartitionScheme::scan (SInt32 * score) {
...
dpme *     dpmeMap = 0;
...
// Read in a partition entry and assign to dpmeMap.
...
// Determine whether the partition entry signature is present.
if (OSSwapBigToHostInt16(dpmeMap->dpme_signature) != DPME_SIGNATURE)
    ...
}
```

[Next](Subclassing%20Logical%20Unit%20Drivers.md)[Previous](Mass%20Storage%20Driver%20Matching%20and%20Loading.md)

