---
title: '大小问题：iOS 虚拟内存探究'
source: Always Processing (Brian T. Kelley)
source_key: alwaysprocessing
source_url: 'https://alwaysprocessing.blog/2022/02/20/size-matters'
original_language: en
published: 2022-02-20
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:8a5cb66d0e6554e7'
translated: true
---

> 原文：[大小问题：iOS 虚拟内存探究——调试 iOS App 时发生内存不足崩溃，从而研究 iOS 虚拟内存系统并发现虚拟地址空间大小因](https://alwaysprocessing.blog/2022/02/20/size-matters)　·　Always Processing (Brian T. Kelley)

# 大小问题：iOS 虚拟内存探究

![两只黄/金色的狗坐在房间里，周围散落着各种卷尺。](https://alwaysprocessing.blog/cdn-cgi/imagedelivery/WFfM6PwcxpVzRRpdvDWNtg/ee42638f-aaf3-473e-3d9f-46d211051c00/public)

在调试 iOS App 时发生内存不足（out-of-memory）崩溃，这让我开始研究 iOS 虚拟内存系统，并发现虚拟地址空间大小在不同 iOS 设备上有所不同。修复调试工作流需要使用 _Extended Virtual Addressing_ entitlement，才能启用完整的 64 位地址空间。

前几天，我尝试在设备上调试 iOS App 时遇到了一个奇怪的内存不足问题。该 App 在启动后不久就会持续崩溃，导致我无法调查这个 bug。为了摆脱困境，我学到了很多关于 iOS 虚拟内存实现的知识，并将我的发现（包括修复方法！）记录在了这里。

## 背景

[_虚拟内存_](https://en.wikipedia.org/wiki/Virtual_memory)这个术语描述的是进程（可执行文件、App 等）与计算机物理内存（RAM）之间的一种抽象。这是由操作系统配合计算机 CPU（具体来说是它的[_内存管理单元_](https://en.wikipedia.org/wiki/Memory_management_unit)，简称 MMU）提供的一项功能。

在采用虚拟内存的系统中，每个进程都有自己的[_内存地址空间_](https://en.wikipedia.org/wiki/Address_space)，该空间定义了其有效的逻辑（原名虚拟）内存地址。当一个进程读取或写入某个逻辑内存地址时，MMU 会将该逻辑内存地址转换为一个物理地址。这就是使用_虚拟_这个术语的原因——进程的内存地址与机器上的任何物理地址都没有内在联系。

这种抽象的一个推论是，两个进程可能持有值相同（逻辑内存地址）的指针，但每个指针可能映射到不同的物理地址。同样，两个进程可能持有值不同的指针，但每个指针都映射到相同的物理地址（例如共享库）。

虚拟内存被划分为称为[_页_](https://en.wikipedia.org/wiki/Page_(computer_memory))的单位。一个页是一个连续的地址范围，每个页都有相同且固定的大小。页的大小因操作系统和硬件而异。4 KiB 在 32 位硬件上很常见，而 64 位硬件上的常见大小包括 4 KiB、16 KiB 和 64 KiB。

并非虚拟内存地址空间中的所有地址都需要映射到物理地址。如果一个进程访问了未映射页中的地址，MMU 会引发一个[_缺页异常_](https://en.wikipedia.org/wiki/Page_fault)。

操作系统可以利用缺页异常来实现[_分页_](https://en.wikipedia.org/wiki/Memory_paging)，即将数据从磁盘移动到主存（通常称为_页调入_，或从磁盘_将_页_读入_RAM）。这种技术使操作系统和应用程序能够利用磁盘来存储操作系统想要从 RAM 中驱逐的页（通常称为_页调出_，或_将_页从 RAM _移出_到磁盘），从而使用比机器物理可用内存更多的内存。RAM 与磁盘之间传输数据的过程也称为_交换_。

操作系统也可能通过终止进程（即崩溃）来处理缺页异常。在 32 位 Apple 平台上，第一个页（地址 `[0x0000, 0x0FFF]`）进程不可访问，这就是解引用 `NULL` 指针（访问地址 `0`）会崩溃的原因。在 64 位 Apple 平台上，整个 4 GiB 的 32 位地址空间（地址 `[0x00000000, 0xFFFFFFFF]`）进程不可访问，这既捕获了 `NULL` 指针解引用 bug，也捕获了 64 位到 32 位指针截断 bug。

## iOS 上的虚拟内存

在许多方面，iOS 的虚拟内存与许多其他操作系统的虚拟内存类似，但 iOS 的实现有几个值得注意的独特之处。

### 无页调出

与 macOS（以及大多数具有虚拟内存的操作系统）不同，iOS 不会将[_脏_](https://en.wikipedia.org/wiki/Dirty_bit)内存[调出到磁盘](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/ManagingMemory/Articles/AboutMemory.html)。（术语_脏_指的是已被进程写入的内存。）iOS 只丢弃[_内存映射文件_](https://en.wikipedia.org/wiki/Memory-mapped_file)的只读页，这些页可以在需要时再次调入。主可执行文件、共享库以及某些类型的资源通常会被内存映射到进程地址空间中，因此如果系统物理内存不足，它们就可能被从 RAM 中驱逐。

### 64 位虚拟地址空间

iOS 64 位虚拟内存系统的一个令人惊讶的方面（至少对我来说是！）是虚拟地址空间的大小取决于设备上安装的物理内存量。考虑以下来自 **xnu-7195.141.2**（操作系统内核）的摘录：

`osfmk/mach/shared_region.h` 第 [86-87](https://github.com/apple-oss-distributions/xnu/blob/xnu-7195.141.2/osfmk/mach/shared_region.h#L86-L87) 行：

```
#define SHARED_REGION_BASE_ARM64                0x180000000ULL
#define SHARED_REGION_SIZE_ARM64                0x100000000ULL
```

`osfmk/arm/pmap.c` 第 [13406](https://github.com/apple-oss-distributions/xnu/blob/xnu-7195.141.2/osfmk/arm/pmap.c#L13406)、[13409](https://github.com/apple-oss-distributions/xnu/blob/xnu-7195.141.2/osfmk/arm/pmap.c#L13409)、[13417-13425](https://github.com/apple-oss-distributions/xnu/blob/xnu-7195.141.2/osfmk/arm/pmap.c#L13417-L13425) 行：

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

利用上述信息^[[1](#_footnotedef_1)]，我们可以计算出运行 iOS 12 或更高版本的各种 iOS 设备的虚拟内存地址空间大小。（对于 iOS 11 及更早版本，减去 3 GiB。）

RAM

地址空间

设备

```
 > 3 GiB
```

```
15.375 GiB
```

- iPhone XS – iPhone 13
- iPad Air（第 4 代）
- iPad Pro（12.9 英寸）、（10.5 英寸）、（11 英寸）

```
 > 1 GiB
```

```
11.375 GiB
```

- iPhone 6s – X、SE、XR
- iPad（第 5 代）– iPad（第 8 代）
- iPad Air 2、iPad Air（第 3 代）
- iPad mini 4、iPad mini（第 5 代）
- iPad Pro（9.7 英寸）

```
<= 1 GiB
```

```
10.5   GiB
```

- iPhone 5s、iPhone 6
- iPad Air
- iPad mini 2、iPad mini 3

### 可用地址空间

虚拟地址空间中有 8 GiB^[[2](#_footnotedef_2)] 不可供进程使用。如前所述：

- 64 位虚拟地址空间的前 4 GiB（也就是整个 32 位地址空间！）进程无法读取、写入或执行。Mach-O 可执行文件格式将此区域指定为 `PAGE_ZERO`，内核[要求 arm64 进程具有 `PAGE_ZERO`](https://github.com/apple-oss-distributions/xnu/blob/xnu-7195.141.2/bsd/kern/mach_loader.c#L622-L630)。
- 供系统使用的[共享区域](https://github.com/apple-oss-distributions/xnu/blob/xnu-7195.141.2/osfmk/vm/vm_shared_region.c#L30-L76)的大小[固定为 4 GiB](https://github.com/apple-oss-distributions/xnu/blob/xnu-7195.141.2/osfmk/mach/shared_region.h#L87)。

根据这些信息，我们可以更新表格，以包含进程可用的虚拟地址空间大小。

RAM

地址空间

可用大小

设备

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
- iPad Air（第 4 代）
- iPad Pro（12.9 英寸）、（10.5 英寸）、（11 英寸）

```
 > 1 GiB
```

```
11.375 GiB
```

```
3.375 GiB
```

- iPhone 6s – X、SE、XR
- iPad（第 5 代）– iPad（第 8 代）
- iPad Air 2、iPad Air（第 3 代）
- iPad mini 4、iPad mini（第 5 代）
- iPad Pro（9.7 英寸）

```
<= 1 GiB
```

```
10.5   GiB
```

```
2.5   GiB
```

- iPhone 5s、iPhone 6
- iPad Air
- iPad mini 2、iPad mini 3

### 开发注意事项

一般来说，当一个 Mach-O 文件被加载到进程中时，整个文件都会被映射到进程的地址空间中。这对于调试构建尤其有意义，因为调试构建通常包含嵌入到可执行二进制文件中的大量调试信息。

最后，我们回到这篇博文的原点！🤣 我当时正尝试在 iPhone X 上调试一个大型 App，但它在启动后不久就崩溃了，并显示这条相当隐晦的错误信息：

```
 can't allocate region
 :*** mach_vm_map(size=1048576, flags: 100) failed (error code=3)
 MyApp(1234,0x2d580000) malloc: *** set a breakpoint in malloc_error_break to debug
 warning: could not execute support code to read Objective-C class data in the process. This may reduce the quality of type information available.
```

使用 Instruments，我观察到应用程序可执行文件及其库的总大小超过 3 GiB，只剩下不到 370 MiB 的地址空间给堆和线程栈。**我无法在设备上调试该 App，因为调试信息占用了太多地址空间，以至于根本没有可用地址空间给分配器！**

### Extended Virtual Addressing

iOS 14 新增了 _Extended Virtual Addressing_ entitlement，其 plist 键为 `com.apple.developer.kernel.extended-virtual-addressing`。如果进程拥有此 entitlement，[内核会启用巨型模式](https://github.com/apple-oss-distributions/xnu/blob/xnu-7195.141.2//bsd/kern/kern_exec.c#L2930-L2932)，从而为进程提供对整个 64 位地址空间的访问权限。

`osfmk/arm/pmap.c` 第 [13426-13432](https://github.com/apple-oss-distributions/xnu/blob/xnu-7195.141.2/osfmk/arm/pmap.c#L13426-L13432) 行：

```
} else if (option == ARM_PMAP_MAX_OFFSET_JUMBO) {
	if (arm64_pmap_max_offset_default) {
		// Allow the boot-arg to override jumbo size
		max_offset_ret = arm64_pmap_max_offset_default;
	} else {
		max_offset_ret = MACH_VM_MAX_ADDRESS;     // Max offset is 64GB for pmaps with special "jumbo" blessing
	}
```

由于此 entitlement 仅增加虚拟地址空间的大小，因此它主要适用于映射大量只读数据的应用程序。

大量映射只读数据正是我那个大型调试构建所做的，因此我将此 entitlement 添加到了开发构建的 App 的 entitlements 文件中。这个 entitlement 解决了在设备上调试时启动后发生的内存不足崩溃！🚀 🎉 🎊 解决了这个问题后，我得以调查那个引领我走上这次迷人绕道之旅的 bug。

---

[1](#_footnoteref_1). 最大偏移量的注释是错误的。**xnu-4903.221.2**（iOS 12）将 `SHARED_REGION_SIZE_ARM64` 从 1 GiB 增加到 4 GiB，但注释中的值只增加了 1 GiB。

[2](#_footnoteref_2). 在 iOS 11 及更早版本中，共享区域的大小[固定为 1 GiB](https://github.com/apple-oss-distributions/xnu/blob/xnu-3789.1.32/osfmk/mach/shared_region.h#L77)。因此，只有 5 GiB 的虚拟地址空间不可供进程使用。而进程可用的地址空间量保持不变。
