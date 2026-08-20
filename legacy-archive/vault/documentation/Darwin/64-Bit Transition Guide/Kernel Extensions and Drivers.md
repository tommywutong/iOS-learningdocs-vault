---
title: 64-Bit Transition Guide
apple_id: TP40001064
resource_type: Guide
platform: macOS
topic: General
technology: null
published: '2012-12-13'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/64bitPorting/KernelExtensionsandDrivers/KernelExtensionsandDrivers.html
archived_at: '2026-07-15T07:23:04.052582Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [64-Bit Transition Guide](Introduction%20to%2064-Bit%20Transition%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](Performance%20Optimization.md)

# Kernel Extensions and Drivers

In OS X v10.8 and later, the kernel is 64-bit (and some hardware used a 64-bit kernel as far back as v10.6). This chapter describes the rationale for this change and explains how it affects you as a developer of device drivers or other kernel extensions.

This chapter is divided into four sections:

- [Why a 64-bit Kernel?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrsg4wvgvzu)—Explains why OS X is transitioning to a 64-bit kernel.
- [What You Must Do](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrsg4wugqkdi5buurce)—Describes the basic steps involved in transitioning a kernel extension or driver to 64-bit.
- [64-Bit Kernel Data Type Changes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrsg4wvgvzt)—Describes additional data type changes specific to kernel-space code in a 64-bit environment.
- [Additional Tips For 64-Bit KEXTs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrsg4wvgvzs)—Provides helpful tips for transitioning and debugging 64-bit kernel extensions and drivers.

In modern operating systems, applications run in a virtual address space. Thus, an application’s notion of an address is not the same as the physical hardware’s notion of an address. The benefit is that applications can “see” a huge address space even if there is not sufficient RAM to support it.

Underneath this abstraction is a virtual memory subsystem within the operating system kernel. This subsystem manages the mappings between an application’s view of the world and the hardware’s view. The virtual address space is broken up into fixed size blocks, called pages, each of which can be individually mapped to an arbitrary hardware address. The operating system then tells the CPU to associate these virtual pages with certain physical hardware addresses using a table known as the page table. Regardless of page table organization, this table eventually grows until it contains (at minimum) an entry for every page of physical RAM in the system.

In addition to these page table entries, the operating system maintains additional data structures that keep track of which physical pages are associated with which processes, which pages are free, and so on. Of these, the most common (by volume) is the `vm_page` structure (usually seen in the form of `vm_page_t` pointers to it), which describes various properties of free pages and resident (in physical memory) logical pages, such as their physical address, their paging state, the number of wired memory maps that reference the page, and so on. The OS maintains a `vm_page` structure for every physical page of RAM.

For a computer with 64 GB of RAM, given a 4 KB page size, the OS must manage almost 17 million pages of physical RAM, each of which has a page table entry and a `vm_page` structure. In total, these data structures would potentially consume well over a gigabyte of kernel memory by themselves. In a 32-bit (4GB) address space, this would significantly limit the kernel address space available for other purposes.

The space constraints are compounded by other data structures (mbuf storage, for example) that should ideally be allowed to scale with the size of available memory. By moving to a 64-bit address space (when run on supported hardware), the OS X kernel can accommodate these data structures in large memory configurations.

In OS X v10.8 and later, the kernel runs exclusively in 64-bit mode. In earlier operating systems, the kernel ran in different modes depending on hardware. (See [http://support.apple.com/kb/HT3770](http://support.apple.com/kb/HT3770) for details.)

As a driver developer, you `must` update your drivers with 64-bit binaries. The 64-bit kernel cannot load 32-bit kernel extensions. Fortunately, because the I/O Kit is a relatively modern environment with few legacy design constraints, most kernel extensions can be adapted fairly easily to 64-bit. Many drivers “just work” after changing the compile settings. However, there are a few steps you must take along the way.

**Recompile your code**
: In a 64-bit kernel environment, device drivers and kernel extensions must be made 64-bit clean and compiled as 64-bit executables. This process is essentially the same as for any other 64-bit code. In particular, you should be aware of the changes described in [Major 64-Bit Changes](Major%2064-Bit%20Changes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrqg4wviucykjcummjqge), [Making Code 64-Bit Clean](Making%20Code%2064-Bit%20Clean.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrsgywvgvzs), and [Compiling 64-Bit Code](Compiling%2064-Bit%20Code.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrqhawviucykjcummjqge). There is one small difference, however: you must use GCC 4.2 or later when compiling 64-bit kernel extensions. (64-bit applications can be compiled with GCC 4.0.)

**Update dependency information**
: In the 64-bit kernel, the kernel exports _only_ KPI dependencies, not the general kernel dependencies or unsupported dependencies. For example, `com.apple.kpi.iokit` is supported, but `com.apple.kernel.iokit` is not.

__Note:__ If you need to support operating systems that predate the availability of the KPI symbol sets, you must use a separate driver bundle with a different `Info.plist` file for those older operating systems.

**Stop using unsupported symbols**
: In addition, the exported KPI symbol lists are cleaned up for the 64-bit environment. If your code uses functions that are not exported by the 64-bit kernel, you will receive compile-time or load-time errors. You must fix these by moving off of these APIs and moving to APIs that are supported for 64-bit. You can learn more about these APIs in _[Kernel Framework Reference](https://developer.apple.com/documentation/kernel)_.

**Update user-client code**
: Device drivers that talk directly to a user-space application without using I/O Kit families (such as user clients and the I/O Kit families themselves) may need to be changed in order to correctly communicate with applications. A 32-bit kernel extension may have to communicate with a 64-bit application and vice-versa, which can cause problems with data structure size, alignment, and so on.

For more information about problems you may encounter when passing data between applications and kernel extensions with different word sizes, see [Data Type and Alignment Tips](Making%20Code%2064-Bit%20Clean.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrsgywvgvzy) and [Additional Tips For 64-Bit KEXTs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrsg4wvgvzs).

For more about user clients and device interfaces in general, read _[IOKit Fundamentals](../../Device%20Drivers/IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_.

**Complete the move to `IODMACommand`**
: On Intel-based Macintosh computers with 64-bit Intel processors, device drivers that support direct memory access (DMA) _must_ be updated to use the `IODMACommand` class.

The `IODMACommand` class provides bounce buffers for devices that do not support 64-bit physical addressing, and uses direct mapping for devices that do. For more information, see the documentation for [IODMACommand](https://developer.apple.com/documentation/kernel/iodmacommand).

**Check for kernel-specific data type changes**
: Two key data types used in the kernel have different underlying base types in a 64-bit kernel environment. This occasionally can cause problems when printing some numeric values and when subclassing other classes. These changes are described in [64-Bit Kernel Data Type Changes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrsg4wvgvzt).

**Fix bugs**
: After making these overarching changes, the remaining fixes, you should look for the problem described in [Additional Tips For 64-Bit KEXTs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrsg4wvgvzs) and correct them if necessary.

In addition to the general C data type changes described in [Data Type Changes](Major%2064-Bit%20Changes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrqg4wviucykjcummjqgm), the underlying type behind two kernel-specific data types has changed.

| Type name | 32-bit type | 64-bit type |
| --- | --- | --- |
| `SInt32` | `long` | `int` |
| `UInt32` | `unsigned long` | `unsigned int` |

These changes pose two potential problems: format strings and C++ method overriding.

First, these changes affect format strings for `printf` and `IOLog` calls. When printing these values, you can either modify your code to use `%ld` when compiling 32-bit and `%d` when compiling 64-bit or cast both values to an `int` and use `%d` explicitly to avoid the warning.

Second, these changes can affect overridden methods, as described in [Additional Tips For 64-Bit KEXTs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrsg4wvgvzs).

In addition to all of the common issues and changes described in [Making Code 64-Bit Clean](Making%20Code%2064-Bit%20Clean.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrsgywvgvzs), here are several other common kernel-specific mistakes you should watch for when porting your device driver or other kernel extension to 64-bit:

**__Use the Correct SDK Version__**
: Although user-space code may be compiled against the 10.5 SDK, you must compile your kernel-space driver code against the 10.6 SDK or later when compiling the 64-bit slice. To build a KEXT that supports existing 32-bit architectures, you must use per-architecture build settings, as described in [Using Architecture-Specific Flags](Compiling%2064-Bit%20Code.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrqhawvgvzs).

**__Check the Signatures of Overridden Methods__**
: As mentioned in [64-Bit Kernel Data Type Changes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrsg4wvgvzt), the data types `UInt32` and `SInt32` are of type `long` in the 32-bit kernel environment, but are of type `int` in the 64-bit kernel environment. These changes present a potential problem for overridden C++ methods.

If a C++ method has an argument of type `UInt32` (for example) and a subclass overrides that method but defines the parameter as being of type `long`, in the 32-bit environment, the subclass version overrides the method in the superclass correctly because the types are equivalent.

When recompiled for 64-bit, however, the subclass version is still of type `long`, but the original class version is now of type `int`. Because the two methods no longer have the same signature, the subclass version does not override the method in the superclass, and as a result, the method’s behavior will depend on which type of integer is used by the calling function. This behavior is almost certainly not what you want.

For this reason, it is imperative that you check all classes that override existing classes and make sure that any methods you write use the exact same named types as any methods they are overriding.

**__Avoid Truncating Virtual Addresses__**
: Inside the kernel, references to virtual memory addresses are often handled using non-pointer types. The most common use is the value returned by the [getVirtualAddress](https://developer.apple.com/documentation/kernel/iomemorymap/1441843-getvirtualaddress) method of [IOMemoryMap](https://developer.apple.com/documentation/kernel/iomemorymap). Be careful to assign these addresses only to variables with 64-bit integer types such as `mach_vm_address_t` and never to variables with 32-bit integer types such as `UInt32`.

**__Use the Large Zero Page Flag__**
: To help debug pointer truncation issues, pass the `-no_shared_cr3` flag as part of your boot arguments. (See [Building and Debugging Kernels](https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KernelProgramming/build/build.html#//apple_ref/doc/uid/TP30000905-CH221) for information about setting boot arguments.) This flag causes the kernel to enforce a 128 TB page zero in the kernel and provides similar benefits to the 4 GB page zero in user-space applications.

With a 64-bit kernel, the kernel itself occupies the top 128TB of virtual address space, while the currently active user-space application occupies the bottom 128TB (or 4 GB for a 32-bit application). Because the user mappings do not overlap with the kernel mappings, they do not need to be flushed when switching into kernel space and back. (Page permissions are used to ensure that the kernel’s address space cannot actually be accessed by the user-space application even though the mappings are in place.)

As a side effect, however, because this unified page table is used, pages in the currently executing user-space application remain accessible after transitioning into the kernel. If a 32-bit application (or a 64-bit application without a 4GB page zero) is running, any pointer used by the kernel that gets truncated to 32 bits may end up pointing into a valid address range that contains the application’s code or data. As a result, it is unsafe to assume that a truncated pointer in the kernel will result in an illegal access panic. (Further, such a stray pointer may cause applications to crash in hard-to-diagnose ways.)

By specifying the `-no_shared_cr3` flag during debugging and testing, a separate kernel mode page table is swapped in and the TLB is flushed during these transitions, thus ensuring that accessing a truncated pointer in the kernel results in an illegal access exception, which triggers a panic.

__Note:__ The `-no_shared_cr3` flag behaves somewhat differently with a 32-bit kernel. For most 64-bit applications, because the bottom 4GB region is usually unmapped, the kernel can be mapped into this region. Thus, when switching into the kernel, the page table remains the same and no TLB flush is needed. The `-no_shared_cr3` flag forces a page table reload and TLB flush during this transition.

**__Use IODMACommand for Devices with Limited Addressing Support__**
: Some devices can only handle physical addresses that fit into 32 bits. To the extent that it is possible to use 64-bit addresses you should do so, but for these devices, you can either use [IODMACommand](https://developer.apple.com/documentation/kernel/iodmacommand) or the `initWithPhysicalMask` method of [IOBufferMemoryDescriptor](https://developer.apple.com/documentation/kernel/iobuffermemorydescriptor) to allocate a bounce buffer within the bottom 4 GB of physical memory.

**__Fix User Client Code__**
: Communication between a user-space application and kernel code is basically the same whether you are in a 32-bit kernel or a 64-bit kernel. That said, if your user-space framework only supports 32-bit applications currently, the transition to a 64-bit kernel (and other changes in OS X v10.6) may require you to update this code to support 64-bit applications.

Your user client must be able to handle communication from any type of process supported by any OS version you support. For apps running in OS X v10.7 and later, this means 32-bit and 64-bit Intel. For apps running in v10.6, this includes 32-bit PowerPC (Rosetta). For apps running in older versions of OS X, this may even include 64-bit PowerPC.

Here are some tips for cross-architecture communication:

- __Maintain consistent structure sizes__—Where possible, build your data structures in such a way that they do not change in size between architectures. If your structures contain pointers, maintaining consistent structure sizes is more difficult, but not impossible. One way to make pointer-laden structures consistent is to use a union between the pointer and a larger data type. For example:

```
struct my_struct {
    int a;
    char b;
    union {
        void *c;
        uint64_t pad_01;
    };
};
```
- __Take advantage of__ `IOUserClient::initWithTask`—If you are writing a user client, the `IOUserClient::initWithTask` method has two forms. One form takes an additional `OSDictionary` parameter that provides information about the client. To determine whether the remote process is a 32-bit PowerPC client running in Rosetta, include this code in your user client:

```swift
if (properties && properties->getObject(kIOUserClientCrossEndianKey)) {
    // Connecting application is a 32-bit PowerPC
    // application running in Rosetta.  Byte
    // swap as needed.
}
```

  For more information, see the _[SimpleUserClient](../../../samplecode/SimpleUserClient/SimpleUserClient.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydanbvga)_ sample.
- __Use magic numbers__—A magic number is a number that you place inside a data structure to allow you to determine whether the structure is valid, is in the correct byte order, and so on. It can be as simple as a version number, so long as the version number is never zero and is not the same when its bytes are reversed.

  If you are communicating in some way other than a user client, you can determine the byte order of the remote application using a magic number, and with a bit more effort, you can also determine the word length (32-bit or 64-bit) using this technique.

  For example, consider the following structure and assignment statements:

```
struct mystruct {
    uint32_t magic;
    ....
};
struct mystruct mystruct_instance;
mystruct_instance.magic=0x32160804;
mystruct_instance.pad = 0xffffffff;
```

  If you receive such a structure as a block of data, you can trivially determine the byte order as follows:

```
void *blob = ...
uint32_t *magic = blob;
if (*magic == 0x32160804) {
    // no swap needed
} else {
    // byte swap needed
}
```

  If your data structures change size in 64-bit applications, you should use a different magic number to identify these 64-bit structures.

  As an alternative, if you can guarantee that the four bytes following the magic number will never be zero, you can check for 64-bit applications like this:

```
void *blob = ...
uint32_t *magic = blob;
if (*magic == 0x04081632) {
    // Application is 32-bits, byte swap needed.
} else if (*magic == 0x00000000) {
    // Application is 64-bit PowerPC.
} else if (*magic == 0x32160804) {
    // Application is built for the same
    // architecture as this code, but may
    // be either 32-bit or 64-bit on Intel.
    magic++
    if (*magic == 0x00000000) {
        // remote app is 64-bit Intel.
    } else {
        // remote app is 32-bit, built for the
        // same architecture as this code.
    }
}
```

  As a slight variation, if you cannot guarantee the four bytes will be nonzero but can guarantee that they will not be `0xffffffff`, you could use a signed `long` value instead, then use any hexadecimal value of `0x80000000` or greater for the magic number so that it will be sign extended on 64-bit architectures, then replace `0x00000000` with `0xffffffff` in both places in the above example.
- __Declare byte order and word size explicitly__—This is similar to the concept of magic numbers except that the remote end of the communication identifies its architecture explicitly. For example, you might write code like this:

```
#if defined(__LP64__)
    #ifdef __LITTLE_ENDIAN__
        #define HOST_ORDER=1
    #else
        #define HOST_ORDER=2
    #endif
#elif defined(__LITTLE_ENDIAN__)
        #define HOST_ORDER=3
#else
        #define HOST_ORDER=4
#endif

struct mystruct {
    int order;
};
struct mystruct mystruct_instance;
mystruct_instance.order = HOST_ORDER;
```

  This still puts the burden of reading the field squarely on the code receiving the structure, but makes it much easier.
- __Pre-convert data structures to a consistent size and order__—As an alternative to these techniques, you can write code in user space to convert all pointers to `uint64_t` values in a consistent byte order and make your kernel code convert it again if needed.
- __Replace outdated__ `IOConnectMethod*` __calls__—The following functions are not supported in a 64-bit environment:

  - `IOConnectMethodScalarIScalarO`
  - `IOConnectMethodScalarIStructureO`
  - `IOConnectMethodScalarIStructureI`
  - `IOConnectMethodStructureIStructureO`
  - `IOConnectMethodScalarIScalarO`
  - `IOConnectMethodScalarIStructureO`
  - `IOConnectMethodScalarIStructureI`
  - `IOConnectMethodStructureIStructureO`

  You should instead use the `IOConnectCall*` functions:

  - `IOConnectCallMethod`
  - `IOConnectCallAsyncMethod`
  - `IOConnectCallStructMethod`
  - `IOConnectCallAsyncStructMethod`
  - `IOConnectCallScalarMethod`
  - `IOConnectCallAsyncScalarMethod`

[Next](Document%20Revision%20History.md)[Previous](Performance%20Optimization.md)

