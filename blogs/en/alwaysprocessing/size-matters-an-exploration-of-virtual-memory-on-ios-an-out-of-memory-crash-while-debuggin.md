---
title: 'Size Matters: An Exploration of Virtual Memory on iOS An out-of-memory crash while debugging an iOS app led to investigating the iOS virtual memory system and finding the virtual address space size va'
source: Always Processing (Brian T. Kelley)
source_key: alwaysprocessing
source_url: 'https://alwaysprocessing.blog/2022/02/20/size-matters'
original_language: en
published: 2022-02-20
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:8a5cb66d0e6554e7'
translated: false
---

> 原文：[Size Matters: An Exploration of Virtual Memory on iOS An out-of-memory crash while debugging an iOS app led to investigating the iOS virtual memory system and finding the virtual address space size va](https://alwaysprocessing.blog/2022/02/20/size-matters)　·　Always Processing (Brian T. Kelley)

# Size Matters: An Exploration of Virtual Memory on iOS

![Two yellow/golden dogs sitting in a room with various measuring tapes strewn around.](https://alwaysprocessing.blog/cdn-cgi/imagedelivery/WFfM6PwcxpVzRRpdvDWNtg/ee42638f-aaf3-473e-3d9f-46d211051c00/public)

An out-of-memory crash while debugging an iOS app led to investigating the iOS virtual memory system and finding the virtual address space size varies across iOS devices. Fixing the debugging workflow required use of the _Extended Virtual Addressing_ entitlement to enable the full 64-bit address space.

I ran into an odd out-of-memory problem the other day when attempting to debug an iOS app on device. The app consistently crashed shortly after launch, preventing me from investigating the bug. To unblock myself, I learned a lot about the iOS virtual memory implementation and journaled my findings (including a fix!) here.

## Background

The term [_virtual memory_](https://en.wikipedia.org/wiki/Virtual_memory) describes an abstraction between a process (executable, app, etc.) and the computer’s physical memory (RAM). This is a feature provided by an operating system in conjunction with the computer’s CPU (specifically its [_memory management unit_](https://en.wikipedia.org/wiki/Memory_management_unit), or MMU).

In a system with virtual memory, each process has its own [_memory address space_](https://en.wikipedia.org/wiki/Address_space) that defines its valid logical (née virtual) memory addresses. When a process reads from or writes to a logical memory address, the logical memory address is translated by the MMU into a physical address. This is why the term _virtual_ is used—​a process’s memory address is not intrinsically related to any physical address on the machine.

A corollary of this abstraction is that two processes may have a pointer with the same value (a logical memory address), but each pointer may map to a different physical address. Similarly, two processes may have pointers with different values, but each maps to the same physical address (e.g. a shared library).

Virtual memory is divided into units called a [_page_](https://en.wikipedia.org/wiki/Page_(computer_memory)). A page is a contiguous address range, and each page has the same, fixed size. The size of a page varies by operating system and hardware. 4 KiB is common on 32-bit hardware and common sizes on 64-bit hardware include 4 KiB, 16 KiB, and 64 KiB.

Not all addresses in a virtual memory address space need map to a physical address. If a process accesses an address in an unmapped page, the MMU raises a [_page fault exception_](https://en.wikipedia.org/wiki/Page_fault).

The page fault exception may be used by the operating system to implement [_paging_](https://en.wikipedia.org/wiki/Memory_paging), or the movement of data from disk into main memory (typically called a _page in_, or reading a _page_ from disk _into_ RAM). This technique enables operating systems and applications to use more memory than is physically available on the machine by leveraging the disk to store pages that the operating system wants to evict from RAM (typically called _page out_, or moving a _page_ from RAM _out_ to disk). The process of transferring data between RAM and disk is also known as _swapping_.

The operating system may also handle a page fault by terminating the process (i.e. a crash). On 32-bit Apple platforms, the first page (addresses `[0x0000, 0x0FFF]`) is not accessible by the process, which is why a `NULL` pointer deference (an access of address `0`) crashes. On 64-bit Apple platforms, the entire 4 GiB 32-bit address space (addresses `[0x00000000, 0xFFFFFFFF]`) is not accessible by the process, which catches both `NULL` pointer dereference bugs and 64-bit to 32-bit pointer truncation bugs.

## Virtual Memory on iOS

In many respects, iOS virtual memory is similar to virtual memory in many other operating systems, but there are a few notable unique aspects of the iOS implementation.

### No Page Outs

Unlike macOS (and most operating systems with virtual memory), [iOS does not page out](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/ManagingMemory/Articles/AboutMemory.html) [_dirty_](https://en.wikipedia.org/wiki/Dirty_bit) memory to disk. (The term _dirty_ refers to memory that has been written to by the process.) iOS only discards read-only pages of a [_memory-mapped file_](https://en.wikipedia.org/wiki/Memory-mapped_file), which can be paged in again as necessary. The main executable, shared libraries, and some types of resources are typically memory-mapped into the process address space and are therefore candidates for eviction from RAM if the system is low on physical memory.

### 64-bit Virtual Address Space

A surprising aspect (to me at least!) of the iOS 64-bit virtual memory system is that the size of the virtual address space depends on the amount of physical memory installed on the device. Consider the following excerpts from **xnu-7195.141.2** (the operating system kernel):

`osfmk/mach/shared_region.h` lines [86-87](https://github.com/apple-oss-distributions/xnu/blob/xnu-7195.141.2/osfmk/mach/shared_region.h#L86-L87):

```
#define SHARED_REGION_BASE_ARM64                0x180000000ULL
#define SHARED_REGION_SIZE_ARM64                0x100000000ULL
```

`osfmk/arm/pmap.c` lines [13406](https://github.com/apple-oss-distributions/xnu/blob/xnu-7195.141.2/osfmk/arm/pmap.c#L13406), [13409](https://github.com/apple-oss-distributions/xnu/blob/xnu-7195.141.2/osfmk/arm/pmap.c#L13409), [13417-13425](https://github.com/apple-oss-distributions/xnu/blob/xnu-7195.141.2/osfmk/arm/pmap.c#L13417-L13425):

```
#define ARM64_MIN_MAX_ADDRESS (SHARED_REGION_BASE_ARM64 + SHARED_REGION_SIZE_ARM64 + 0x20000000) // end of shared region + 512MB for various purposes
const vm_map_offset_t min_max_offset = ARM64_MIN_MAX_ADDRESS; // end of shared region + 512MB for various purposes

if (arm64_pmap_max_offset_default) {
	max_offset_ret = arm64_pmap_max_offset_default;
} else if (max_mem > 0xC0000000) {
	max_offset_ret = min_max_offset + 0x138000000; // Max offset is 13.375GB for devices with > 3GB of memory
} else if (max_mem > 0x40000000) {
	max_offset_ret = min_max_offset + 0x38000000;  // Max offset is 9.375GB for devices with > 1GB and <= 3GB of memory
} else {
	max_offset_ret = min_max_offset;
}
```

Using the above information^[[1](#_footnotedef_1)], we can calculate the size of the virtual memory address space for various iOS devices running iOS 12 or later. (Subtract 3 GiB for iOS 11 and earlier.)

RAM

Address Space

Devices

```
 > 3 GiB
```

```
15.375 GiB
```

- iPhone XS – iPhone 13
- iPad Air (4th generation)
- iPad Pro (12.9-inch), (10.5-inch), (11-inch)

```
 > 1 GiB
```

```
11.375 GiB
```

- iPhone 6s – X, SE, XR
- iPad (5th generation) – iPad (8th generation)
- iPad Air 2, iPad Air (3rd generation)
- iPad mini 4, iPad mini (5th generation)
- iPad Pro (9.7-inch)

```
<= 1 GiB
```

```
10.5   GiB
```

- iPhone 5s, iPhone 6
- iPad Air
- iPad mini 2, iPad mini 3

### Available Address Space

8 GiB^[[2](#_footnotedef_2)] of the virtual address space is not available for use by the process. As mentioned earlier:

- The first 4 GiB of the 64-bit virtual address space (which is also the entire 32-bit address space!) cannot be read from, written to, or executed by the process. The Mach-O executable file format designates this area as `PAGE_ZERO`, and the kernel [requires `PAGE_ZERO` for arm64 processes](https://github.com/apple-oss-distributions/xnu/blob/xnu-7195.141.2/bsd/kern/mach_loader.c#L622-L630).
- The size of the [shared region](https://github.com/apple-oss-distributions/xnu/blob/xnu-7195.141.2/osfmk/vm/vm_shared_region.c#L30-L76), for use by the system, is [fixed to 4 GiB](https://github.com/apple-oss-distributions/xnu/blob/xnu-7195.141.2/osfmk/mach/shared_region.h#L87).

With this information, we can update the table to include the size of the virtual address space that’s usable by a process.

RAM

Address Space

Usable

Devices

```
 > 3 GiB
```

```
15.375 GiB
```

```
7.375 GiB
```

- iPhone XS – iPhone 13
- iPad Air (4th generation)
- iPad Pro (12.9-inch), (10.5-inch), (11-inch)

```
 > 1 GiB
```

```
11.375 GiB
```

```
3.375 GiB
```

- iPhone 6s – X, SE, XR
- iPad (5th generation) – iPad (8th generation)
- iPad Air 2, iPad Air (3rd generation)
- iPad mini 4, iPad mini (5th generation)
- iPad Pro (9.7-inch)

```
<= 1 GiB
```

```
10.5   GiB
```

```
2.5   GiB
```

- iPhone 5s, iPhone 6
- iPad Air
- iPad mini 2, iPad mini 3

### Considerations for Development

Generally speaking, when a Mach-O file is loaded into a process, the entire file is mapped into the process’s address space. This is particularly interesting for debug builds, which typically contain a considerable amount of debug information embedded into the executable binary.

And finally, we circle back to the origin of this post! 🤣 I was attempting to debug a large app on an iPhone X, but it would crash shortly after launch with this rather cryptic error message:

```
 can't allocate region
 :*** mach_vm_map(size=1048576, flags: 100) failed (error code=3)
 MyApp(1234,0x2d580000) malloc: *** set a breakpoint in malloc_error_break to debug
 warning: could not execute support code to read Objective-C class data in the process. This may reduce the quality of type information available.
```

Using Instruments, I observed the application executable and its libraries totaled over 3 GiB in size, leaving less than 370 MiB of address space for the heap and thread stacks. **I couldn’t debug the app on device because the debug information used so much of the address space there was literally no address space available for use by the allocator!**

### Extended Virtual Addressing

New in iOS 14 is the _Extended Virtual Addressing_ entitlement, whose plist key is `com.apple.developer.kernel.extended-virtual-addressing`. If a process has this entitlement, the [kernel enables jumbo mode](https://github.com/apple-oss-distributions/xnu/blob/xnu-7195.141.2//bsd/kern/kern_exec.c#L2930-L2932), which provides the process with access to the full 64-bit address space.

`osfmk/arm/pmap.c` lines [13426-13432](https://github.com/apple-oss-distributions/xnu/blob/xnu-7195.141.2/osfmk/arm/pmap.c#L13426-L13432):

```
} else if (option == ARM_PMAP_MAX_OFFSET_JUMBO) {
	if (arm64_pmap_max_offset_default) {
		// Allow the boot-arg to override jumbo size
		max_offset_ret = arm64_pmap_max_offset_default;
	} else {
		max_offset_ret = MACH_VM_MAX_ADDRESS;     // Max offset is 64GB for pmaps with special "jumbo" blessing
	}
```

Because this entitlement only increases the size of the virtual address space, it’s primarily useful for applications that map in a large amount of read-only data.

Mapping in a lot of read-only data is exactly what my large debug build is doing, so I added the entitlement to the app’s entitlements file for development builds. The entitlement resolved the out-of-memory crash after launch when debugging on device! 🚀 🎉 🎊 With that out of the way, I was able investigate the bug that brought me down this fascinating detour.

---

[1](#_footnoteref_1). The max offset comments are incorrect. **xnu-4903.221.2** (iOS 12) increased `SHARED_REGION_SIZE_ARM64` from 1 GiB to 4 GiB but only added 1 GiB to the values in the comments.

[2](#_footnoteref_2). On iOS 11 and earlier, the size of the shared region is [fixed to 1 GiB](https://github.com/apple-oss-distributions/xnu/blob/xnu-3789.1.32/osfmk/mach/shared_region.h#L77). So, only 5 GiB of the virtual address space is not available for use by the process. The amount of address space available to the process remains the same.
