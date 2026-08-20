---
title: 64-Bit Transition Guide for Cocoa
apple_id: TP40004247
resource_type: Guide
platform: macOS
topic: General
technology: null
published: '2013-09-17'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Cocoa64BitGuide/MovingTo64Bit/MovingTo64Bit.html
archived_at: '2026-07-15T07:11:59.023875Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [64-Bit Transition Guide for Cocoa](Introduction%20to%2064-Bit%20Transition%20Guide%20For%20Cocoa.md)


[Next](64-Bit%20Changes%20To%20the%20Cocoa%20API.md)[Previous](Introduction%20to%2064-Bit%20Transition%20Guide%20For%20Cocoa.md)

# Moving to 64-Bit Addressing

This chapter describes the overall 64-bit initiative for OS X and offers advice and guidelines for moving your Cocoa projects to 64-bit addressing.

Since version 10.4 (Tiger), OS X has been moving to a model that supports a 64-bit address space. In this model, called LP64, `long` integers and pointers are both 8 bytes (64 bits) instead of 4 bytes. In addition, the `size_t` integer type is 8 bytes instead of 4 bytes. The alignment of these types for LP64 has also increased to 8 bytes. The sizes of all other primitive integer types (`char`, `int`, `off_t`, and so on) remain as they are in the 32-bit model (ILP32), but the alignment of some—namely `long long` and `pos_t`—has increased to 8 bytes for LP64.

On Intel architectures, 64-bit mode also entails an increase both in the number of registers and in their width, as well as a change in the calling conventions to pass arguments in registers instead of on the stack. As a direct consequence of these changes, 64-bit executables on Intel-based OS X systems may see a boost in performance. (The expansion of registers does not happen on the PowerPC architecture, because it was designed for 64-bit computing from the outset.) Although the kernel (Darwin) remains 32-bit, it supports 64-bit software in user space.

All pointers in a 64-bit process are 64 bits; there is no "mixed mode" in which some pointers are 32 bits and others are 64 bits. Consequently, all supporting binaries needed to run a process, including frameworks, libraries, and plug-ins, must be 64-bit capable if the process is to run in a 64-bit address space. All dependencies require porting to 64-bit.

As part of the 64-bit initiative for OS X v10.5 (Leopard), Apple is porting all system frameworks, libraries, and plug-ins to support 64-bit addressing. They are packaged to support both 32-bit and 64-bit executables. Thus, if you have a 32-bit application and a 64-bit application running at the same time, both framework stacks on which the applications have dependencies are loaded into memory. The GCC compiler, linker, debugger, and other development tools have also been modified to support 64-bit addressing. System daemons are also being modified to support 64-bit processes. The Cocoa frameworks as well as the Objective-C runtime and related development tools are part of the porting effort. (The Cocoa changes are described in 64-Bit Changes To the Cocoa API.)

Several changes have also been made to intermediate integer types in lower layers of the system. For example, the underlying primitive type for `CFIndex` in Core Foundation has been changed to be 64-bit while that for `SInt32` in Carbon Core has been changed to remain 32-bit in a 64-bit world. These changes percolate up into higher layers of the system, affecting frameworks where they expose these types in their APIs.

There are several consequences and implications of a transition to a 64-bit address space:

- A 64-bit executable can concurrently access 16 exabytes of virtual address space.
- System memory requirements will more than double, both because of larger data structures and the need for two framework stacks loaded simultaneously.

An important stake of the 64-bit initiative is to maintain binary compatibility for existing 32-bit applications once 64-bit changes are made to system frameworks, libraries, and plug-ins. Sometimes this means keeping the underlying primitive type the same for 32-bit values.

For OS X v10.5 (Leopard), just a small percentage of projects have any need to move to a 64-bit address space. Generally, these projects are for applications that require the increased address space for manipulating large data sets, or that need to have random access to data objects exceeding 4 GB. Some examples of applications that fall into this category include those that perform scientific computing, large-scale 3D rendering and animation, data mining, and specialized image processing.

For releases after OS X v10.5 it is expected that more and more software projects—including most consumer applications—will make the transition to 64-bit. There are several reasons for this expectation:

- __Competing platforms__. Microsoft Windows XP already has a 64-bit version and Windows Vista will also be 64-bit capable.
- __Hardware evolution__. As the downward trend in the price of hardware components (such as memory chips) continues, the typical configuration of computers will grow to allow 64-bit computing to become the norm. Moreover, as noted above, you may see performance improvements for 64-executables running on Intel-based Macintosh computers.
- __User demand__. Along with hardware configurations, user expectations will also grow. On a 64-bit capable OS X system with, say, 32 GB of memory, few users will be happy with an application that can access no more than 4 GB of data.

So although your application may not immediately need to make the transition to 64-bit, in a few years’ time it will. You can start now to prepare your projects for this transition, proceeding in stages. First, make your projects 64-bit clean by incorporating the new 64-bit types in your code and using the preprocessor conditionals to maintain source compatibility. The project should be able to compile without errors and run. Next make your projects 64-bit enabled by using APIs that express 64-bit quantities. Finally, make your projects 64-bit capable by ensuring that all code paths are capable of dealing with 64-bit quantities.

You can ease the transition process by adopting OS X-native technologies and data types. For example, if you use Core Data (see _[Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)_) to manage your application’s data you can reduce the number of parameters you have to consider in adoption. The attribute types that you specify for Core Data entities are the same on 32- and 64-bit platforms. The file format is platform-independent (it is the same whether the host is Intel- or PowerPC-based, 32- or 64-bit); moreover, using the lazy data initialization available with the SQLite store, Core Data allows you to work with data sets whose size is constrained primarily by the host. Together these features make it easier for you to scale seamlessly from 32- to 64-bit.

You can use existing technologies to make your application "universal" by packaging binaries in your application bundle with 64-bit and 32-bit variants combined with variants for PowerPC and Intel architectures. Thus your application could have four-way multi-architecture binaries, with binaries for PowerPC 32-bit, PowerPC 64-bit, Intel 32-bit, and Intel 64-bit. Generally, you will want an application that ships as 64-bit to ship as 32-bit as well, since you want it to run on 32-bit-only hardware, which will be common for many years.

[Next](64-Bit%20Changes%20To%20the%20Cocoa%20API.md)[Previous](Introduction%20to%2064-Bit%20Transition%20Guide%20For%20Cocoa.md)

