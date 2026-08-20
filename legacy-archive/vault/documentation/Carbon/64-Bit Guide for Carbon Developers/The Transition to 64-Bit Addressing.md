---
title: 64-Bit Guide for Carbon Developers
apple_id: TP40004381
resource_type: Guide
platform: macOS
topic: General
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/Carbon64BitGuide/TransitionTo64Bit/TransitionTo64Bit.html
archived_at: '2026-07-15T05:22:31.505416Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [64-Bit Guide for Carbon Developers](Introduction%20to%2064-Bit%20Guide%20for%20Carbon%20Developers.md)


[Next](Modifying%20Your%20Application%20to%20Use%2064-Bit%20Addressing.md)[Previous](Introduction%20to%2064-Bit%20Guide%20for%20Carbon%20Developers.md)

# The Transition to 64-Bit Addressing

This chapter describes the overall 64-bit initiative for OS X and offers advice and guidelines for moving your projects to 64-bit addressing.

Since version 10.4 (Tiger), OS X has been moving to a model that supports a 64-bit address space. In this model, called LP64, both `long` integers and pointers are 8 bytes (64 bits) instead of 4 bytes. In addition, the `size_t` integer type is 8 bytes instead of 4 bytes. The alignment of these types for LP64 has also increased to 8 bytes. The sizes of all other primitive integer types (`char`, `int`, `off_t`, and so on) remain as they are in the 32-bit model (ILP32), but the alignment of some—namely `long long` and `pos_t`—has increased to 8 bytes for LP64.

On Intel architectures, 64-bit mode also entails an increase both in the number of registers and in their width, as well as a change in the calling conventions to pass arguments in registers instead of on the stack. As a direct consequence of these changes, 64-bit executables running on Intel-based Macintosh computers may see a boost in performance. (The expansion of registers does not happen on the PowerPC architecture, because it was designed for 64-bit computing from the outset.) Although the kernel remains 32-bit in OS X v10.5, it supports 64-bit software in user space.

All pointers in a 64-bit process are 64 bits—there is no "mixed mode" in which some pointers are 32 bits and others are 64 bits. Consequently, all supporting binaries needed to run a process, including frameworks, libraries, and plug-ins, must be 64-bit capable if the process is to run in a 64-bit address space. All dependencies require porting to 64 bit.

As part of the 64-bit initiative for OS X v10.5 (Leopard), Apple is porting system frameworks, libraries, and plug-ins to support 64-bit addressing. They are packaged to support both 32-bit and 64-bit executables. Thus, if you have a 32-bit application and a 64-bit application running at the same time, both framework stacks on which the applications have dependencies are loaded into memory. The GCC compiler, linker, debugger, and other development tools have also been modified to support 64-bit addressing. System daemons are also being modified to support 64-bit processes. The Cocoa frameworks as well as the Objective-C runtime and related development tools are part of the porting effort. Frameworks with procedural C APIs support 64-bit executables as well, although a number of Carbon managers, system services, and individual functions are not available.

Several changes have also been made to intermediate integer types in lower layers of the system. For example, the underlying primitive type for `CFIndex` in Core Foundation has been changed to a 64-bit type, while the underlying type for `SInt32` in Carbon Core has been changed to remain 32 bits in a 64-bit world. These changes percolate up into higher layers of the system, affecting frameworks where they expose these types in their APIs.

There are several consequences and implications of a transition to a 64-bit address space:

- A 64-bit executable can concurrently access 16 exabytes of virtual address space.
- System memory requirements will more than double, because data structures are larger and two framework stacks are loaded simultaneously.

An important stake of the 64-bit initiative is to maintain binary compatibility for existing 32-bit applications after 64-bit changes are made to system frameworks, libraries, and plug-ins. Sometimes this means keeping the underlying primitive type the same for 32-bit values.

For OS X v10.5 (Leopard), just a small percentage of projects have any need to move to a 64-bit address space. Generally, these projects are for applications that require the increased address space for manipulating large data sets, or that need to have random access to data objects exceeding 4 GB. Some examples of applications that fall into this category include those that perform scientific computing, large-scale 3D rendering and animation, data mining, and specialized image processing.

For releases after OS X v10.5, Apple expects that more and more software projects—including most consumer applications—will make the transition to 64 bit. There are several reasons for this expectation:

- __Competing platforms__. Microsoft Windows XP already has a 64-bit version, and Windows Vista is also 64-bit capable.
- __Hardware evolution__. As the downward trend in the price of hardware components (such as memory chips) continues, the typical configuration of computers will grow to allow 64-bit computing to become the norm. Moreover, as noted above, you may see performance improvements for 64-bit executables running on Intel-based Macintosh computers.
- __User demand__. Along with hardware configurations, user expectations will also grow. On a 64-bit-capable OS X system with, say, 32 GB of memory, many users will be unhappy with an application that can access no more than 4 GB of data.

So although most applications don’t immediately need to make the transition to 64-bit addressing, in a few years’ time they will. You can start now to prepare your projects for this transition, proceeding in stages.

1. Begin adopting OS X APIs that are available to 64-bit applications. Modify your own interfaces and code to take advantage of a 64-bit address space and 64-bit quantities. Add preprocessor conditionals as needed to maintain source compatibility.
2. Fix any assignments that result in pointer or long integer truncation in 64-bit mode. Ensure identical size and alignment for data structures that are shared between 32-bit and 64-bit code (across a network or in a file, for example).
3. Test your project to ensure that all code paths are capable of dealing with pointers and quantities that take on values greater than 2^32.

You can use existing technologies to make your application "universal" by packaging binaries in your application bundle with 64-bit and 32-bit variants combined with variants for PowerPC and Intel architectures. Thus your application could have four-way multi-architecture binaries, with binaries for 32-bit PowerPC, 64-bit PowerPC, 32-bit Intel, and 64-bit Intel. Generally, you will want a 64-bit application to ship with 32-bit binaries as well, since you want it to run on 32-bit-only hardware, which will be common for many years.

[Next](Modifying%20Your%20Application%20to%20Use%2064-Bit%20Addressing.md)[Previous](Introduction%20to%2064-Bit%20Guide%20for%20Carbon%20Developers.md)

