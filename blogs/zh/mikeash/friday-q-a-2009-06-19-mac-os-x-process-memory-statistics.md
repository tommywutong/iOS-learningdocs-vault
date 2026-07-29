---
title: 'Friday Q&A 2009-06-19: Mac OS X 进程内存统计'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-06-19-mac-os-x-process-memory-statistics.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:86bbd14518b06bf4'
translated: true
---

> 原文：[Friday Q&A 2009-06-19: Mac OS X Process Memory Statistics](https://www.mikeash.com/pyblog/friday-qa-2009-06-19-mac-os-x-process-memory-statistics.html)　·　mikeash.com Friday Q&A

发布于 2009-06-19 13:48 | [RSS 源](https://www.mikeash.com/pyblog/rss.py) ([全文源](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇：[Friday Q&A 2009-06-26: C 语言中的类型限定符，第 1 部分](https://www.mikeash.com/pyblog/friday-qa-2009-06-26-type-qualifiers-in-c-part-1.html)  
上一篇：[Friday Q&A 2009-06-05: Valgrind 入门](https://www.mikeash.com/pyblog/friday-qa-2009-06-05-introduction-to-valgrind.html)  
标签：[fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [memory](https://www.mikeash.com/pyblog/?tag=memory) [performance](https://www.mikeash.com/pyblog/?tag=performance)

Friday Q&A 2009-06-19: Mac OS X 进程内存统计

作者：[Mike Ash](https://www.mikeash.com/)

**内存结构**  
在讨论这些统计数字的含义之前，我必须先讲解一下现代操作系统中内存的实际工作方式。如果你已经了解物理内存与虚拟地址空间之间的区别，并且理解文件映射（file mapping）的工作原理等，那么可以跳过这部分。

**硬件**  
在硬件层面，内存是通过总线访问的物理芯片。这些芯片中的每一字节内存都有一个离散的物理地址（尽管现代系统通常不是按字节寻址的，需要访问更大的数据块）。

CPU 的 MMU（内存管理单元）负责调解对物理芯片的访问。MMU 使得虚拟内存（virtual memory）成为可能。它在 CPU 发出的逻辑地址与物理 RAM 中的物理地址之间建立映射。

这让 CPU 拥有一个大型虚拟地址空间，该空间不一定与物理内存对应。（在 32 位下这个空间是 4GB，在 64 位下则是一个非常大的数字。）地址空间中的任意一段，要么可以映射到物理内存的任意一段，要么保持未映射状态。

**操作系统**  
当程序试图访问未映射的内存时会发生什么？会产生一个硬件异常，然后操作系统接管控制权。

一个设计巧妙的操作系统（比如，任何一个还算现代的 UNIX，甚至 Windows）可以利用这一点来做一些有趣的事情。例如，它可以在幕后维护自己更复杂的映射，表明硬件上未映射的内存段实际上映射到了磁盘上的某个文件。然后，当尝试访问该段引发硬件异常时，操作系统可以将文件的一个块读入该位置，然后让程序继续执行。这样你就有了文件映射，以及（如果自动 _取消映射_ 不常使用的内存段并将其内容写出到磁盘）交换（swap）。

另一个巧妙的做法是将两个不同进程地址空间的段映射到同一块物理内存上。这样就有了共享内存（shared memory）！

这些技术可以结合起来。例如，共享的 framework（框架）通常通过映射到内存中来加载（允许操作系统从磁盘延迟加载它们）。然后它们被同时映射到多个进程中，这样所有进程就可以使用同一块物理 RAM，而不需要保存多份副本。

**定义**  
现在我们对这些机制有了大致的了解，让我们定义一些与内存相关的术语：

- **常驻（Resident）：** 位于物理 RAM 中的内存。
- **私有（Private）：** 仅映射到一个进程中的内存。
- **共享（Shared）：** 映射到多个进程中的内存。
- **地址空间大小（Address space size）：** 虚拟内存中某个特定段占用的地址空间数量。
- **内存大小（Memory size）：** 占用的实际物理内存数量。

有了这些，我们现在可以通过查看 `top` 的手册页并使用这些定义来理解其中各个字段的含义：

- **RPRVT：** 本进程本地、与当前存在于物理 RAM 中的项相对应的地址空间量。
- **RSHRD：** 本进程与至少一个其他进程共享、与当前存在于物理 RAM 中的项相对应的地址空间量。
- **RSIZE：** 本进程使用的物理 RAM 总量。（它_不_等于 **RPRVT** + **RSHRD**，因为后两者衡量的是地址空间，而这个是衡量实际内存。）
- **VPRVT：** 进程中映射到未与其他进程共享的项的地址空间量。
- **VSIZE：** 进程中映射到任何内容的地址空间总量。

还应注意，这些数字源自一个并不总是与真实数字完全对应的统计系统，尤其是在区分共享内存和私有内存时。不过，它们通常足够准确，至少还是有用的。

**解读**  
到现在你可能正在挠头，想知道应该看哪个数字才能知道你的程序使用了多少内存。问题在于，并没有这样一个数字！

正如你所看到的，内存使用情况非常复杂，这些数字中的任何一个都无法回答这个问题。事实上，考虑到文件映射和共享内存等因素，这个问题本身甚至都不太有意义。

不过，这并不意味着这些数字毫无用处。即使没有哪个数字直接对应你真正想了解的信息，你仍然可以获得一些有趣的事实。

对于 32 位程序，**VSIZE** 可能非常重要。这是因为 32 位程序的虚拟地址空间严格限制在 4GB，而在当今世界，达到这个限制并不困难。一旦达到，内存分配将开始失败，你的程序很可能在之后不久就会崩溃。如果你的 **VSIZE** 接近 4GB 限制，说明你在某件事上消耗了过多的地址空间。

（对于 64 位程序，虚拟地址空间实际上是无限的，因此这一列意义不大。例如，64 位下使用垃圾回收（garbage collection）的 App 会立即分配一个 64GB 的虚拟地址空间块，仅仅是为了简化统计。这不会影响你的实际内存使用，也完全无害，尽管这往往会吓到那些在“活动监视器（Activity Monitor）”里仔细查看的用户。）

**RPRVT** 可以作为一个粗略的指标，用来观察你的程序分配的总内存量是上升还是下降。然而，依赖这个指标是危险的。因为它只跟踪常驻内存，如果你的程序开始交换，那么 **RPRVT** 将不再增加，即使你仍在分配越来越多的内存。（要检测这种情况，你可以观察 **VPRVT** 是否在上升，以及屏幕顶部列出的页出（pageout）数量是否在上升。）相反，内存分配器并不总是立即将内存归还给系统，因此如果你的程序正在释放内存，这个数字可能不会下降。

总的来说，要小心不要过分依赖这些统计信息。要更精确地追踪泄漏和过多的内存分配，像 `leaks` 命令和 ObjectAlloc 仪器这样的工具要好得多。

**结论**  
本期 Friday Q&A 到此结束。现在你应该理解了 `top` 中那些奇怪数字的含义（可能除了那些与内存无关的之外），以及如何最好地使用它们，避免误用。

欢迎下周（我希望）回来观看另一期精彩内容。请务必把你想要讨论的主题想法发送给我。没有你们的贡献，Friday Q&A 就无法存在。请在评论中发表，或者[直接发送电子邮件给我](mailto:mike@mikeash.com)。

Friday Q&A 在此鸣谢 Ed Wynne 为本周文章提供技术建议的重要贡献。

喜欢这篇文章吗？我正出售收录了这些文章的全套书籍！第二卷和第三卷现已出版！提供 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击此处了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[本页面的评论 RSS 源](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2009-06-19-mac-os-x-process-memory-statistics.html)

分享你的想法，发表评论：

垃圾评论和偏离主题的评论将被删除，恕不另行通知。违规者可能会由我自行决定公开羞辱。
