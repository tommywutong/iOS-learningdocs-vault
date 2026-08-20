---
title: FireWire Device Interface Guide
apple_id: TP40000969
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: IOKit
published: '2007-02-08'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/WorkingWFireWireDI/FWDevEndianness/FWDevEndianness.html
archived_at: '2026-07-15T07:31:34.754512Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [FireWire Device Interface Guide](Introduction%20to%20FireWire%20Device%20Interface%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](Using%20the%20FireWire%20Device%20Interface%20Libraries.md)

# FireWire Device Access in an Intel-Based Macintosh

This chapter provides an overview of some of the issues related to developing a universal binary version of an application that accesses a FireWire device. Before you read this chapter, be sure to read _[Universal Binary Programming Guidelines, Second Edition](../../Mac%20OSX/Universal%20Binary%20Programming%20Guidelines%2C%20Second%20Edition/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjx)_. That document covers architectural differences and byte-ordering formats and provides comprehensive guidelines for code modification and building universal binaries. The guidelines in that document apply to all types of applications, including those that access hardware.

Before you build your application as a universal binary, make sure that:

- You port your project to GCC 4 (Xcode uses GCC 4 to target Intel-based Macintosh computers)
- You install the OS X v10.4 universal SDK
- You develop your project in Xcode 2.1 or later

The FireWire bus is a big-endian bus. Structured data (such as a FireWire address or configuration ROM) appears on the bus in big-endian format, regardless of the native endian format of the computer an application is running in. Data that has no FireWire-specific structure, such as disk block (or sector) data, appears on the bus in its original format, regardless of the native endian format of the computer sending or receiving that data.

Although the IOFireWire family does not need to swap data buffers for transmission on the FireWire bus, your application must be careful with the arguments passed to and received from FireWire APIs and services. This is because those arguments may need to be byte swapped if they express payload data in numerical ways, such as with `UInt32` values. For example, if an application uses the `Write` function of the IOFireWireDeviceInterface, it must pass the following parameters (among others):

- The target address for the command
- A pointer to a buffer containing the data to write
- The number of bytes to write
- The FireWire bus generation during which the command should be executed

The target address is passed in a `FWAddress` structure. Because the IOFireWire family knows how to interpret a `FWAddress` structure as numeric values, the family expects those values to be in host-native format. This means that you don’t have to do any byte-swapping when you populate the structure with, for instance, the target address. Continuing the `Write` function example, Listing 4-1 shows an example of how to create a target address that will produce correct results whether the application is running in a PowerPC-based or Intel-based Macintosh.

__Listing 4-1__  Universal way to create a FireWire target address

```
FWAddress a;
a.nodeID = 0xffc0;
a.addressHi = 0xffff;
a.addressLo = 0xf000040c;
```

Internally, the IOFireWire family may need to swap these values when it programs the hardware, but it will not modify the contents of the structure you prepare.

Similarly, the `Write` function arguments for byte count and bus generation should also be in host-native format, as should the pointer to the buffer. The IOFireWire family does not interpret the data in the buffer, so it is sent on the bus unmodified.

Because the data in the buffer is not modified by the IOFireWire family, your application must use endian-safe ways to express the data when filling a buffer for transmission. To see why this is so, imagine your application puts a FireWire address in a buffer to be sent as payload (as you would in an SBP-2 ORB). If your application uses code similar to that shown in Listing 4-2 to fill the buffer, the application would work only in a PowerPC-based Macintosh, not an Intel-based Macintosh:

__Listing 4-2__  PowerPC-only way to fill a buffer for transmission on the FireWire bus

```
// Fill a buffer with the FireWire address 0xffc2ee33.00f01234
// to send as payload (works only in a PowerPC-based Macintosh).
UInt32 myBuffer[2];
myBuffer[0] = 0xffc2ee33;
myBuffer[1] = 0x00f01234;
```

If you pass the version of `myBuffer` defined in Listing 4-2 to the `Write` function in an application running in an Intel-based Macintosh, the address will be received as `0x33eec2ff.3412f000`. This is because an Intel-based Macintosh stores numerical values such as `0xffc2ee33` in little-endian format and the IOFireWire family sends the buffer unmodified. To avoid this problem, use endian-neutral code that will produce correctly ordered bytes on both types of computer, as shown in Listing 4-3.

__Listing 4-3__  Universal way to fill a buffer for transmission on the FireWire bus

```
// Fill a buffer with the FireWire address 0xffc2ee33.00f01234
// to send as payload (works in both PowerPC-based and Intel-based
// Macintosh computers).
UInt32 myBuffer[2];
myBuffer[0] = OSSwapHostToBigInt32 (0xffc2ee33);
myBuffer[1] = OSSwapHostToBigInt32 (0x00f01234);
```

In general, wherever you use a multibyte constant (such as `0xffc2ee33`) to represent bytes in a buffer instead using of a numeric value, you will probably need to swap that constant the ensure the bytes appear in the correct order in memory and on the FireWire bus.

For a few specific types of data, the IOFireWire family does perform automatic byte-swapping to the host computer’s native endian format. These exceptions are listed below.

- Configuration ROM data. A FireWire device’s configuration ROM (or config ROM) contains information such as vendor ID, special register addresses, and unit directories. The information in the config ROM is assumed to be in the format defined by the IEEE 1394 specification and is organized as a hierarchy of key-value pairs. Most of these values represent key-specific data (called immediate values), but some values are pointers to blocks of data (called data leaves). When your application uses IOFireWire family APIs to get or set immediate values, the values are swapped to the host format because the IOFireWire family can correctly interpret the value. The IOFireWire family cannot interpret data leaves, however, so these blocks of data are left in big-endian format.

  Note that this differs from the byte order of a device’s config ROM data as published in the I/O Registry in the value of the FireWire Device ROM key. The value of the FireWire Device ROM key is all the information the IOFireWire family has read from the device’s config ROM. In this case, the data is not parsed into specific values, but is placed in the I/O Registry as it came from the FireWire bus—in big-endian format.
- AV/C plug control register values. The plug control registers (or PCRs) allow an application to create point-to-point or broadcast connections between AV/C devices or between the Macintosh and an external AV/C device. The format of the 32-bit PCR values are well defined and the built-in drivers automatically swap these values to host-native format for your convenience.
- Isochronous packet headers. Although all data is transmitted on the FireWire bus in big-endian format, the FireWire DMA processes isochronous packet headers in little-endian format. The IOFireWire family swaps these headers to host format. On a PowerPC-based Macintosh, this results in both header and packet being stored in big-endian format. On an Intel-based Macintosh, however, the header is stored in little-endian format whereas the packet is stored in big-endian format. Therefore, you can expect an isochronous header to be in host-native format, even though it represents data transmitted on the FireWire bus.

This section lists some specific hints to help you prepare your application to run in an Intel-based Macintosh. When you’ve determined that conditional byte swapping is necessary, use the functions and macros defined in the `libkern/OSByteOrder.h` header file in the Kernel framework. For guidelines on various byte-swapping strategies, see “Swapping Bytes” in _[Universal Binary Programming Guidelines, Second Edition](../../Mac%20OSX/Universal%20Binary%20Programming%20Guidelines%2C%20Second%20Edition/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjx)_.

In general, if you developed your application on a PowerPC-based Macintosh, you may have taken advantage of the fact that the PowerPC processor and the FireWire bus both use the big-endian format. You should search for places where you assume that your data is automatically in the correct byte order and insert conditional byte-swapping code if necessary.

Pay particular attention to how you formulate structures, such as the `FWAddress` structure, when you plan to pass them as pointers to blocks of data in buffers. Depending on how you fill such structures, you may have to perform byte swapping. For example, the IOFireWire family defines the `FWAddress` structure as:

```
typedef struct FWAddressStruct
{
    UInt16  nodeID;     // bus/node
    UInt16  addressHi;  // Top 16 bits of node address.
    UInt32  addressLo;  // Bottom 32 bits of node address
} FWAddress, *FWAddressPtr;
```

You might choose to create this structure by formulating a single `UInt64` value or two `UInt32` values. If your application is running in an Intel-based Macintosh, you’ll have to perform the appropriate byte swap on these values before you place them in a buffer for transmission on the FireWire bus.

Because an Intel-based Macintosh does not use Open Firmware, some information provided by Open Firmware on a PowerPC-based Macintosh (such as the complete device tree) is not available in the I/O Registry of an Intel-based Macintosh. However, many parts of the I/O Registry are present, including the information provided by the IOFireWire family.

If your application accesses values in the I/O Registry, you should be aware that values of type number, such as the value of the GUID key, are in host-endian format. Values of type data, however, are in big-endian format. As described in [Byte Ordering on the FireWire Bus](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrzfvbuqmrqgqwugq2ijbbeir2e), the IOFireWire family places the unparsed bytes of a device’s config ROM into the value of the FireWire Device ROM key in big-endian format.

Sometimes, the buffers you use in your application are created by some other entity, such as a member of the IOFireWire family. If you byte swap the values in such a buffer itself, you may find that these same values get swapped again at some later point. For this reason, it’s best to create your own copy of the buffer so you can swap its values without affecting the original buffer.

[Next](Document%20Revision%20History.md)[Previous](Using%20the%20FireWire%20Device%20Interface%20Libraries.md)

