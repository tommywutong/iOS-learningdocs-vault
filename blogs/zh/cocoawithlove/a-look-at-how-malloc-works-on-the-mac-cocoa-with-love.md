---
title: '一窥 Mac 上 malloc 的工作方式 | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2010/05/look-at-how-malloc-works-on-mac.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:3c889a4af525db24'
translated: true
---

> 原文：[A look at how malloc works on the Mac | Cocoa with Love](https://www.cocoawithlove.com/2010/05/look-at-how-malloc-works-on-mac.html)　·　Cocoa with Love (Matt Gallagher)

本文将从较高层次介绍 malloc 在 Mac 上的实现方式。我会讲解“tiny”“small”和“large”三种分配规模如何分配内存、Snow Leopard 引入的多核性能改进，以及一些可用于查找内存问题（包括缓冲区溢出）的内置调试功能。

## 引言

Mac OS X 中的所有内存都由内核分配给应用。内核通过将虚拟内存页（每页 4 KB）映射到应用的内存空间，为应用分配内存。

你可以在应用中使用 `mmap` 函数，以每次 4 KB 的粒度分配内存。也可以直接使用栈上的内存（默认大小为 64 KB），它会为每个线程自动映射。

但人们谈到分配内存时，大多数时候指的是使用 `malloc` 分配。

与直接请求虚拟内存页相比，`malloc` 的粒度更细（可以请求远小于 4 KB 的大小），速度也快得多（因为不必每次都调用 `mmap`）。

当然，`malloc` 内部仍然通过映射虚拟内存页从内核获取内存。它的优势来自将这些页（或页簇）划分为更小的区域，在请求小块分配时返回这些区域内地址的指针。

> 本文使用“`malloc`”这个术语，但内容同样适用于 Objective-C 的 `alloc` 和 `allocWithZone:`、所有 CoreFoundation 分配，以及 `calloc`、`realloc`、`valloc`、`malloc_zone_malloc`、`malloc_zone_calloc`、`malloc_zone_valloc`、`malloc_zone_realloc` 和 `malloc_zone_batch_malloc` 等相关 C 函数，因为这些函数在 Mac 上都经过同一套内部实现。

## 通用的 malloc 实现

malloc 实现会向内核请求少量虚拟内存页，并在收到内存请求时返回这些页中空闲区域的指针。为了随时知道页内哪些区域空闲，malloc 实现必须维护正在使用的每个已分配块的大小和位置，以及块之间所有空闲空间的元数据。

> malloc 管理的内存页合称“堆（heap）”，但需要注意，malloc 通常并不使用[堆数据结构](http://en.wikipedia.org/wiki/Heap_(data_structure))（一种有序树）来跟踪内存块；这两个“堆”是互不相关的概念。

随着程序需要更多内存，malloc 实现会请求更多虚拟内存页，从而增加应用的内存占用。应尽力在此前释放的块留下的空间中分配新块，以保持较低的内存占用。

对内存分配器来说，主要难点是同时降低元数据量和处理时间。当内存变成已分配块与空闲空间交错的斑驳图案时，这一点会非常困难。

如果内存分配器为每一次分配都保存一个数组，记录其位置和大小，那么元数据很容易占用与分配本身同样多的内存。为提高效率，大多数分配器不会跟踪内存中的每一个字节，而是使用 16 字节或更大的分辨率。这样只需较少元数据，就能跟踪已分配和已释放的连续区域。

此外，大多数分配器都会使用空闲列表；分配器不会在每次分配时遍历内存寻找大小合适的空闲空间，而是维护按近似大小分类的已释放区域列表。作为进一步优化，这些空闲列表并不总是记录一个块中的所有空闲区域（通常只记录有限数量的空闲区域）。

## Mac 的 malloc 实现

尽管所有 C 标准库实现都提供名为 `malloc` 的函数，但它们的内部实现各不相同。

Mac 的 malloc 实现是开源的，由两个关键实现文件组成：

- [malloc.c](http://www.opensource.apple.com/source/Libc/Libc-594.1.4/gen/malloc.c)
- [magazine_malloc.c](http://www.opensource.apple.com/source/Libc/Libc-594.1.4/gen/magazine_malloc.c)

_malloc.c_ 文件主要是对 _magazine_malloc.c_ 内部实现的包装。这个外部包装器使用默认 malloc zone，通过 `malloc_zone_malloc` 函数转发普通的 `malloc` 调用。因此，Mac 上所有 malloc 分配实际上都是分区分配，并共享 Objective-C `+[NSObject allocWithZone:]` 所使用的同一套实现。

在 Snow Leopard 之前，内部实现名为 [scalable_malloc.c](http://www.opensource.apple.com/source/Libc/Libc-594.1.4/gen/scalable_malloc.c)。它之所以可扩展，是因为会根据分配大小使用不同的代码路径。新版 magazine_malloc.c 保留了 scalable_malloc.c 的大量代码，但为较小分配增加了多线程改进，并移除了旧的“huge”规模（改为对“large”和“huge”规模分配使用相同的分配方式）。

## Mac 的 malloc 区域

Mac 上的 malloc 分配会根据以下分配大小使用不同的代码路径：

| 分配大小 | 代码路径名称 | 量子大小（分配分辨率） | 区域大小 |
|---|---|---|---|
| 32 位：1 字节至 496 字节 64 位：1 字节至 992 字节 | Tiny | 16 字节 | 32 位：1 MB 64 位：2 MB |
| 32 位：497 字节至“Large”阈值 64 位：993 字节至“Large”阈值 | Small | 512 字节 | 32 位：8 MB 64 位：16 MB |
| RAM 小于 1 GB：15 KB 或更大 RAM 大于等于 1 GB：127 KB 或更大 | Large | 4 KB | 不适用 |

Mac 的可扩展 malloc 实现有一个关键点：它并非只是将虚拟内存页切分后返回更小的块，而是从各自独立的区域中分配“tiny”和“small”分配（“large”分配则直接作为虚拟内存页分配）。

分配“tiny”大小的内存时，返回的内存来自一个 2 MB 的块（32 位程序中为 1 MB）。由于 tiny 区域只按 16 字节的分辨率跟踪分配，分配大小总会向上取整到最近的 16 字节边界。这样还可以确保所有内存分配都按 16 字节对齐（有助于 SSE/Altivec 指令）。

当然，用于 tiny 分配的 1 MB 或 2 MB 区域，在最小分配大小下也只能容纳约 64,000 次分配；分配越大，可容纳的次数越少。需要时会创建更多区域。

超过 15 KB（在 RAM 大于 1 GB 的系统上为 127 KB）后，Mac 的 malloc 纯粹按虚拟内存页分配内存，不再维护额外的跟踪信息或元数据（不过内核会为这些页维护跟踪信息）。

因此，层级结构可以总结如下：

- Malloc zone 分配“tiny”和“small”区域，或直接分配“large”块
- 区域从自身内容中返回块，作为“tiny”和“small” malloc 操作的结果

## 区域的重要性

为 tiny 和 small 分配使用独立区域，是因为这样可以更有效地调整区域元数据，以跟踪其中对象的大小。对于“tiny”分配，按 16 字节单位跟踪是值得的（能更好地回收释放的空间，也不会在已分配对象周围浪费大量内存）。但对于“small”大小的对象，以这种分辨率跟踪会在 CPU 时间（遍历已释放或已分配块的列表）和内存效率之间形成糟糕的权衡；更粗的 512 字节分辨率反而更高效。

tiny 区域还有助于减轻内存碎片的影响。将小分配和大分配分开，可以避免在原本较大的空闲区域中夹杂小分配而造成的内存碎片。当然，它不能消除碎片，但能有所帮助。

“tiny”区域的存在对 Objective-C 非常重要。由于 Objective-C 会在 malloc zone 中分配所有对象，而几乎所有 Objective-C 对象都处于“tiny”大小范围内，为这类分配提供优化的代码路径将带来很大好处。

## Mac OS X 10.6 中的线程改进

在 Snow Leopard 中，Apple 用新版 [magazine_malloc.c](http://www.opensource.apple.com/source/Libc/Libc-594.1.4/gen/magazine_malloc.c) 替换了旧的 [scalable_malloc.c](http://www.opensource.apple.com/source/Libc/Libc-594.1.4/gen/scalable_malloc.c)。新实现引入了一种方法，为每个线程创建特殊的“tiny”内存分配区域。

这种方法“受”[Hoard 内存分配器](http://www.cs.umass.edu/~emery/pubs/berger-asplos2000.pdf)启发，其中线程专属的集群和“superblock”在 Mac malloc 实现中对应 magazine 和区域。此前保存在“zone”结构中的大部分分配元数据，都移到了层级中的新“magazine”级别，以便按线程保存。这包括每次分配都需要更新的数据，例如已分配区域的数量、空闲列表和可用内存计数。

每个“tiny”区域本身由顶层分配器分配，然后分配给特定线程。由于区域随后变成线程专属，顶层共享分配器无需加锁，发生线程竞争的可能性非常低。

加入这些改动后，“tiny”分配的层级结构可以总结如下：

- Malloc zone 为“tiny”区域分配 magazine（每个线程一个），并在 magazine 请求时分配实际区域。
- Magazine 管理某个线程的区域
- 区域从自身内容中返回块

当然，从区域分配或释放内存时内部仍会使用锁（因为一个线程分配的内存仍可能由另一个线程释放），但两个线程争用同一把锁的可能性大幅降低。由于线程不会在同一区域分配内存，CPU 之间不必要共享缓存行的可能性也降低了。

最终结果是，Objective-C 中绝大多数内存分配（通常在某个线程中分配，并由该线程的自动释放池释放）几乎可以完全独立于其他线程。

## 两点小提示

释放内存后，应用的内存占用不会立即下降。释放区域分配的内存只会把空间加入区域的空闲列表，除非该区域中的最后一个块也被释放，否则不会释放整个区域。只有整个区域被释放、zone 可以解除虚拟内存页映射时，应用的内存占用才会下降。

`calloc` 接受两个参数：大小和元素数量。`malloc` 只接受大小，但这个大小通常通过元素数量乘以 `sizeof(SomeType)` 计算。最终结果是一样的：在内部，calloc 只是将两个参数相乘；除了会检查乘法是否溢出，`calloc(a, b)` 返回块的大小与 `malloc(a * b)` 返回的块完全相同。

## 调试信息

阅读 malloc.c 文件时需要注意的一点是，Mac 内存分配器可以在运行时配置为生成日志信息。设置以下环境变量，可以让内存分配器执行调试行为：

- **MallocLogFile** `<f>`：将消息创建或追加到文件 `<f>`，而不是 stderr
- **MallocGuardEdges**：为每个 large 块添加 2 个保护页
- **MallocDoNotProtectPrelude**：禁用保护（设置前一个标志时）
- **MallocDoNotProtectPostlude**：禁用保护（设置前一个标志时）
- **MallocStackLogging**：记录所有调用栈，然后可以使用 leaks 等工具
- **MallocStackLoggingNoCompact**：记录所有调用栈，malloc_history 需要此变量
- **MallocStackLoggingDirectory**：设置调用栈日志位置；日志可能很大，默认值为 /tmp
- **MallocScribble**：检测向已释放块写入以及缺少初始化的情况：释放时写入 0x55，分配时写入 0xaa
- **MallocCheckHeapStart** `<n>`：在执行 `<n>` 次操作后开始检查堆
- **MallocCheckHeapEach** `<s>`：每执行 `<s>` 次操作就重复检查堆
- **MallocCheckHeapSleep** `<t>`：堆损坏时休眠 `<t>` 秒
- **MallocCheckHeapAbort** `<b>`：如果 `<b>` 非零，堆损坏时中止
- **MallocCorruptionAbort**：发生 malloc 错误时中止，但 32 位进程内存不足时除外；在 64 位进程中始终设置 MallocCorruptionAbort
- **MallocErrorAbort**：发生任何 malloc 错误（包括内存不足）时中止
- **MallocHelp**：显示此帮助信息！

遗憾的是，Mac OS X 中 magazine_malloc.c 的常规构建存在一个限制：它不会为“small”或“tiny”分配应用保护页。要为所有数据应用保护页，需要使用 libgmalloc 库。设置以下环境变量即可：

```objc
export DYLD_INSERT_LIBRARIES=/usr/lib/libgmalloc.dylib
```

更多信息请参阅 [libgmalloc 手册页](http://developer.apple.com/mac/library/documentation/Darwin/Reference/ManPages/man3/libgmalloc.3.html)。

还可以在 Xcode 中设置环境变量：右键点按 Tree 视图中的可执行文件，选择“Get Info”，然后打开“Arguments”标签页。

## 结论

我不确定本文能否直接总结出大量可以立即用于程序的经验。出现需要时，了解这些调试选项会很有用，但本文主要是一次对 Mac 上使用频率很高的库函数进行探究的练习。

Mac 的内存分配器有许多与对齐、粒度和线程性能相关的操作系统特定行为。具体分配大小不同，甚至安装的内存量不同，这些行为都会随分配而变化。

从中可以得到一个令人安心的结论：典型 Cocoa 程序中成千上万次 tiny 级别的 Objective-C 对象分配，在 Mac 上确实走的是高度优化的路径。
