---
title: IOKit Device Driver Design Guidelines
apple_id: TP30000694
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2009-08-14'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/WritingDeviceDriver/UBDeviceDriver/UBDeviceDriver.html
archived_at: '2026-07-15T07:31:53.077385Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [IOKit Device Driver Design Guidelines](Introduction%20to%20I-O%20Kit%20Device%20Driver%20Design%20Guidelines.md)


[Next](Glossary.md)[Previous](Testing%20and%20Deploying%20Drivers.md)

# Developing a Device Driver to Run on an Intel-Based Macintosh

This chapter provides an overview of some of the issues related to developing a universal binary version of an I/O Kit device driver. Before you read this chapter, be sure to read _[Universal Binary Programming Guidelines, Second Edition](../../Mac%20OSX/Universal%20Binary%20Programming%20Guidelines%2C%20Second%20Edition/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjx)_. That document covers architectural differences and byte-ordering formats and provides comprehensive guidelines for code modification and building universal binaries. Most of the guidelines in that document apply to kernel extensions as well as to applications.

Before you build your device driver as a universal binary, make sure that:

- All targets in your Xcode project are native
- You develop your project in Xcode 2.2.1 or later

The Intel side of your universal I/O Kit driver must be built using GCC 4.0 and the OS X v10.4u (Universal) SDK available in Xcode 2.2.1 or later. This allows your driver to load and run on Intel-based Macintosh computers running OS X v10.4.4 or later.

To determine the compiler version and SDK to use when building the PowerPC side of your universal I/O Kit driver, decide which versions of OS X you plan to target:

- If you’re targeting versions of OS X earlier than 10.4, use GCC 3.3 and the OS X SDK representing the oldest version of OS X you need to support.
- If you’re targeting OS X v10.4.x and you’re using Xcode 2.2.x or Xcode 2.3, use GCC 4.0 and the OS X v10.4.0 SDK (_not_ the OS X v10.4u (Universal) SDK). Note that this differs from universal applications, which can be built using the OS X v10.4u (Universal) SDK for both architectures.
- If you’re targeting OS X v10.4.x and you’re using Xcode 2.4 or later, you can define the `KPI_10_4_0_PPC_COMPAT` preprocessor symbol when building for the PowerPC architecture. Defining this symbol allows you to use the OS X v10.4u (Universal) SDK for both PowerPC and Intel architectures.

For more details on building a universal binary version of your driver, including Xcode project settings, see [Technical Note TN2163: Building Universal I/O Kit Drivers](https://developer.apple.com/technotes/tn2006/tn2163.html).

As a device driver developer, you are keenly aware of the native byte-ordering format of the device with which you're working. This familiarity, coupled with the fact that the PowerPC processor uses big-endian byte ordering, may mean that your code makes byte-order assumptions that are not appropriate for a universal binary. If, for example, a device driver communicates with a natively little-endian device (such as a USB device), it may perform little-to-big byte swaps because it was developed to run in a PowerPC-based Macintosh. Such hard-coded byte swaps will cause problems when the device driver is run in an Intel-based Macintosh.

To avoid these problems, search for hard-coded byte swaps in your device driver and replace them with the conditional byte-swapping macros defined in `libkern/OSByteOrder.h`. These macros are designed to perform the most efficient byte swap for the given situation. For example, using the `OSSwapConst` macros (and the `OSSwap*Const` variants) in `OSByteOrder.h` to swap constant values prevents byte-swapping at runtime.

As described in _[Universal Binary Programming Guidelines, Second Edition](../../Mac%20OSX/Universal%20Binary%20Programming%20Guidelines%2C%20Second%20Edition/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjx)_, there are differences in the PowerPC and x86 architectures that can prevent code developed for one architecture from running properly in the other architecture. This section highlights two architectural differences that have consequences device driver developers need to be aware of.

In an Intel-based Macintosh, an integer divide-by-zero operation is fatal, whereas in a PowerPC-based Macintosh (in which the operation returns 0), it is not. Although it is not likely your device driver purposely performs a divide-by-zero operation, it may occur as a consequence of other operations. Examine your code for places where this might happen and add code to prevent it.

Device drivers often define software data structures that mirror hardware data structures. It's important to realize that some data types have one size in one architecture and a different size in the other. For example, the `bool` data type is one byte in the x86 architecture and four bytes in the PowerPC architecture. If your device driver uses a data structure that contains a `bool` value, consider replacing it with a fixed-size data type to avoid alignment problems.

In a PowerPC-based Macintosh, Open Firmware populates the device tree plane of the I/O Registry with device hierarchy information. In an Intel-based Macintosh, the device tree plane may contain entirely different values. In fact, the device tree planes of different PowerPC-based Macintosh computers may contain different values.

Because you cannot predict what values an individual computer's device tree plane will contain, your device driver should not rely on the existence of specific values or locations. Instead, it should use APIs provided by I/O Kit classes, such as IORegistryEntry, to access values in the I/O Registry.

It's important for your device driver to pass along any interrupts it might receive that aren't directed at it. In a PowerPC-based Macintosh each internal PCI slot has its own dedicated interrupt line, which means that a driver might be able to get away with ignoring interrupts that aren't destined for it, even though this is not recommended. In an Intel-based Macintosh, however, it is likely that a driver will share an interrupt line with other drivers. Under these circumstances, ignoring interrupts for other drivers can cause problems for these drivers and for the user.

It's possible that your driver might receive a very large number of interrupts destined for other drivers. Besides being sure to pass them on, your driver should not consider the arrival of such interrupts as an event that requires some sort of error logging. If, for example, your driver uses [IOLog](https://developer.apple.com/documentation/kernel/1575337-iolog) to log every spurious interrupt it receives, it will quickly overflow the console log and may degrade system performance. (For more information on using `IOLog`, see [Using IOLog](Debugging%20Drivers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombrfvbecssijbeeiqi).)

Your PowerPC device driver may use the [OSSynchronizeIO](https://developer.apple.com/documentation/kernel/1576454-ossynchronizeio) function to, for example, enforce in-order execution of a write operation. In a PowerPC-based Macintosh, this function issues an `eieio` instruction. In an Intel-based Macintosh, however, this function does nothing because the x86 architecture supports strong memory ordering by default.

A universal binary version of a device driver that uses the `OSSynchronizeIO` function should continue to do so to ensure that it still runs correctly on a PowerPC-based Macintosh.

In a PowerPC-based Macintosh, PCI I/O space is mapped into memory. A PCI device driver accesses the I/O space using the `ioRead*` functions of the IOPCIDevice class (for more on these functions, see `IOPCIDevice` documentation in _[Kernel Framework Reference](https://developer.apple.com/documentation/kernel)_). In a PowerPC-based Macintosh, these functions translate into memory accesses and in an Intel-based Macintosh they translate into the appropriate x86 instructions. If you're developing a universal binary version of a PCI driver, therefore, you can use the `ioRead*` functions to access I/O space and your driver will run in both PowerPC-based and Intel-based Macintosh computers.

For other devices that use I/O space, however, such as an ATA controller, you may have to add x86-specific instructions that execute when the driver is running on an Intel-based Macintosh.

For the most part, debugging a device driver running on an Intel-based Macintosh computer is the same as debugging a driver running on a PowerPC-based Macintosh computer. Even though an Intel-based Macintosh computer uses EFI (extensible firmware interface) instead of the Open Firmware used in a PowerPC-based Macintosh computer, you still need to set the appropriate NVRAM (nonvolatile RAM) variables to enable two-machine debugging (for more information on two-machine debugging, see [Two-Machine Debugging](Debugging%20Drivers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombrfvbuuqsiincuora)). To change NVRAM variables on any Macintosh computer running OS X, you use the `nvram` utility as `root` on the command line. For example, you can set the following kernel debug flag:

```
nvram boot-args="debug=0x14e"
```

Intel-based Macintosh computers also provide a way to store a persistent set of boot arguments on a particular machine. The set of boot arguments is _not_ required for kernel debugging, but it can make it easier for you if you often perform netbooting or if you boot from different partitions and you’d like to have different boot arguments associated with each partition.

The boot arguments are contained in a property list file named `com.apple.Boot.plist`, which is located in `/Library/Preferences/SystemConfiguration`. The `com.apple.Boot.plist` file contains the following keys:

- Boot Graphics. This obsolete property was used to determine whether the Apple logo is drawn during booting. Instead, use the `-v` boot-argument flag to disable boot-time graphics.
- Kernel. The value of the Kernel property identifies the kernel to boot. The default value is `mach_kernel`, but you can use this property to select an alternate kernel, such as an experimental or debug kernel.
- Kernel Flags. The Kernel Flags property may contain any set of valid flags, such as `debug=0x144`, separated by spaces. By default, the value of this property is the empty string.

If you perform netbooting, be sure to make a copy of the `com.apple.Boot.plist` file and place it in the same folder that contains the kernel on the netboot server. A typical development scenario is to have a kernel, an mkext file (a previously cached set of device drivers for hardware involved in the boot process), and a `com.apple.Boot.plist` file for each netboot configuration you work with.

[Next](Glossary.md)[Previous](Testing%20and%20Deploying%20Drivers.md)

