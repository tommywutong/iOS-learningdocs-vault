---
title: 64-Bit Transition Guide
apple_id: TP40001064
resource_type: Guide
platform: macOS
topic: General
technology: null
published: '2012-12-13'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/64bitPorting/transition/transition.html
archived_at: '2026-07-15T07:23:04.119617Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [64-Bit Transition Guide](Introduction%20to%2064-Bit%20Transition%20Guide.md)


[Next](Making%20Code%2064-Bit%20Clean.md)[Previous](Should%20You%20Recompile%20Your%20Software%20as%20a%2064-Bit%20Executable.md)

# Major 64-Bit Changes

There are many differences between 32-bit and 64-bit environments in OS X, including tool usage changes, changes to the size and alignment of data types, alignment pragmas, and I/O Kit drivers. This chapter describes the main changes developers should be aware of when porting code to 64-bit. You should read this chapter if you've decided to port your code to 64-bit or if you are writing a new code from scratch.

You'll find a number of issues when porting code to a 64-bit executable. You can address most of these issues with subtle tweaks to your code. However, before you touch the first line of code, there are a few broad issues you should be aware of:

- Compiling an application as a 64-bit executable requires you to use GCC 4.0 or later. See [Compiling 64-Bit Code Using GCC](Compiling%2064-Bit%20Code.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrqhawuescdjbcecrsc) for information about related compiler flags.
- Xcode has additional options related to 64-bit compilation. For information about compiling 64-bit applications with Xcode, see [Compiling 64-Bit Code Using Xcode](Compiling%2064-Bit%20Code.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrqhawueq2hivbumrkk).
- Any tools that understand the Mach-O ABI (stack frames, calling convention, and so on) must change. These changes affect mainly third-party compilers and linkers. For more information, see _OS X ABI Mach-O File Format Reference_.

This section describes the changes to data type sizes and alignment in 64-bit executables, and explains how these changes will impact your code.

OS X uses two data models: ILP32 (in which integers, `long` integers, and pointers are 32-bit quantities) and LP64 (in which integers are 32-bit quantities, and `long` integers and pointers are 64-bit quantities). Other types are equivalent to their 32-bit counterparts (except for `size_t` and a few others that are defined based on the size of `long` integers or pointers).

While almost all UNIX and Linux implementations use LP64, other operating systems use various data models. Windows, for example, uses LLP64, in which `long long` variables and pointers are 64-bit quantities, while `long` integers are 32-bit quantities. Cray, by contrast, uses ILP64, in which `int` variables are also 64-bit quantities.

In OS X, the default alignment used for data structure layout is natural alignment (with a few exceptions noted below). Natural alignment means that data elements within a structure are aligned at intervals corresponding to the width of the underlying data type. For example, an `int` variable, which is 4 bytes wide, would be aligned on a 4-byte boundary.

Table 2-1 shows the base (compiler-defined) data types and common cross-platform data types used in OS X, along with their size and alignment. LP64 differences are highlighted in bold.

__Table 2-1__  Size and alignment of base data types in OS X

| Data type | ILP32 size | ILP32 alignment | LP64 size | LP64 alignment |
| char | 1 byte | 1 byte | 1 byte | 1 byte |
| short | 2 bytes | 2 bytes | 2 bytes | 2 bytes |
| int | 4 bytes | 4 bytes | 4 bytes | 4 bytes |
| __long__ | 4 bytes | 4 bytes | __8 bytes__ | __8 bytes__ |
| __pointer__ | 4 bytes | 4 bytes | __8 bytes__ | __8 bytes__ |
| __size_t__ | 4 bytes | 4 bytes | __8 bytes__ | __8 bytes__ |
| __long long__ | 8 bytes | 4 bytes | 8 bytes | __8 bytes__ |
| __fpos_t__ | 8 bytes | 4 bytes | 8 bytes | __8 bytes__ |
| __off_t__ | 8 bytes | 4 bytes | 8 bytes | __8 bytes__ |

In addition to these changes to the base data types, various layers of OS X have other data types that change size or underlying type in a 64-bit environment. The most notable of these changes is that `NSInteger` and `NSUInteger` (Cocoa data types) are 64-bit in a 64-bit environment and 32-bit in a 32-bit environment. These changes are described in _[64-Bit Guide for Carbon Developers](../../Carbon/64-Bit%20Guide%20for%20Carbon%20Developers/Introduction%20to%2064-Bit%20Guide%20for%20Carbon%20Developers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgobr)_, _[64-Bit Transition Guide for Cocoa](../../Cocoa/64-Bit%20Transition%20Guide%20for%20Cocoa/Introduction%20to%2064-Bit%20Transition%20Guide%20For%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denbx)_, and [Kernel Extensions and Drivers](Kernel%20Extensions%20and%20Drivers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrsg4wvgvzr).

Because changes in size and alignment can significantly affect the data size produced by your code, you should generally pack structures so that the largest data types appear first, followed by progressively smaller data types. In this way, you maximize the use of space.

If, for compatibility, you need to support on-disk or network data structures containing 64-bit values aligned on 4-byte boundaries, you can override the default alignment using pragmas. See [Making Code 64-Bit Clean](Making%20Code%2064-Bit%20Clean.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrsgywvgvzs) for more information.

Data type and alignment changes impact developers in several broad areas.

- Interprocess communication, networking, shared memory, and user-kernel boundary crossings

  If you need your 64-bit software to communicate with 32-bit software (whether over a network, through local IPC mechanisms, through shared memory, or through crossing the user-kernel boundary in any way), choose data types carefully. A good practice is to always use explicitly sized data types, such as `uint32_t`, rather than generic data types (such as `long`).

  You may find it hard to use some mechanisms of interprocess communication, such as shared memory, when sharing data between 32-bit and 64-bit code. In particular, you should avoid passing pointers into shared memory regions and instead use offsets into the shared buffer.
- Files stored on disk

  If you need your application to write binary data in a file format that is shared between 64-bit and 32-bit versions, make sure that the size and alignment of data structures are the same in both versions. Specifically, these programs should avoid storing data of type `long` to disk.

  Alternatively, you can create a separate file format that is specific to the 64-bit version of your application. For some applications, creating a new format may be easier than maintaining a shared file format. This should be considered the exception rather than the rule, however.

  Finally, never underestimate the convenience of a generic exchange format such as XML.
- Libraries

  All libraries used by 64-bit applications or kernel extensions must be recompiled with a 64-bit compiler. If these libraries are also needed for 32-bit applications or kernel extensions, you must use a dual-architecture library (or have multiple copies of the library).
- Plug-ins

  Applications you compile as a 64-bit executable cannot load 32-bit plug-ins directly. Similarly, applications you compile as a 32-bit executable cannot load 64-bit plug-ins.

  If your application must support plug-ins compiled for multiple architectures, you should use a helper application and communicate with that helper using an interprocess communication mechanism. This is described further in [Cross-Architecture Plug-in Support](Cross-Architecture%20Plug-in%20Support.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrsguwvgvzx).
- Graphical user interfaces

  Higher-level frameworks used for graphical user interfaces are available as 64-bit frameworks _only_ in OS X v10.5 and later. Previous versions of OS X will automatically use the 32-bit version of your executable.
- Data alignment differences

  When you are compiling code with a 64-bit target, keep in mind that the default alignment for 64-bit data types is 64-bit rather than the 32-bit alignment you may be used to. If you require interoperability with 32-bit software (file formats, network protocols, user-kernel boundary crossings, and so on), you must change the code.

  If you do not have to maintain format compatibility with existing data, to avoid wasting memory and storage, you should reorder the members of the structure so that the 64-bit data types fall on a 64-bit offset from the start of the structure. If such a change is not possible for compatibility reasons, you can override the alignment rules using a pragma. See [Making Code 64-Bit Clean](Making%20Code%2064-Bit%20Clean.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrsgywvgvzs) for details.

In 64-bit executables, executing code in data segments is not allowed. To achieve this, the NX (no execute) bit is set on the page table entries for the stack, heap, and initialized and uninitialized data segments.

In general, this should have no impact on developers unless you are doing something nonstandard such as writing self-modifying code. If you are writing code that requires execution on the stack or in the heap, you must explicitly mark the pages executable using [mprotect](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/mprotect.2.html#//apple_ref/doc/man/2/mprotect) or other similar calls.

[Next](Making%20Code%2064-Bit%20Clean.md)[Previous](Should%20You%20Recompile%20Your%20Software%20as%20a%2064-Bit%20Executable.md)

