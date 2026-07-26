---
title: '[objc explain]：线程本地垃圾回收'
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2009/08/28/objc_explain_Thread-local_garbage_collection.html'
original_language: en
published: 2009-08-28
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:bc1d47e90874a320'
translated: true
---

> 原文：[[objc explain]：线程本地垃圾回收](http://sealiesoftware.com/blog/archive/2009/08/28/objc_explain_Thread-local_garbage_collection.html)　·　Hamster Emporium (Greg Parker)

[![](http://sealiesoftware.com/hamster.jpg)](http://sealiesoftware.com/blog/index.html)  
  
 **博客**  
 [最近](http://sealiesoftware.com/blog/index.html)  
 [归档](http://sealiesoftware.com/blog/archive/index.html)  
 [twitter](http://twitter.com/gparker)  
   
 **项目**  
 [Mac OS X](http://www.apple.com/macosx/)  
 [Keyboard](http://sealiesoftware.com/keyboard/index.html)  
 [backlight](http://sealiesoftware.com/keyboard/index.html)  
 [CSC Menu](http://sealiesoftware.com/cscmenu/index.html)  
 [Valgrind](http://sealiesoftware.com/valgrind/index.html)  
 [Fringe Player](http://sealiesoftware.com/fringe/index.html)  
 [pssh](http://sealiesoftware.com/pssh/index.html)  
 [Peal](http://sealiesoftware.com/peal/index.html)  
 [Frankenmouse](http://sealiesoftware.com/frankenmouse/index.html)

## Hamster Emporium 归档

\<\< [[objc explain]：dyld 共享缓存中的选择器唯一化](http://sealiesoftware.com/blog/archive/2009/09/01/objc_explain_Selector_uniquing_in_the_dyld_shared_cache.html) | [归档](http://sealiesoftware.com/blog/archive/index.html) | [[objc explain]：你在 objc_msgSend() 里崩溃了：iPhone 篇](http://sealiesoftware.com/blog/archive/2009/06/08/objc_explain_So_you_crashed_in_objc_msgSend_iPhone_Edition.html) \>\>

[![(链接)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2009/08/28/objc_explain_Thread-local_garbage_collection.html)

**[objc explain]：线程本地垃圾回收** ([2009-08-28 1:00 PM](http://sealiesoftware.com/blog/archive/2009/08/28/objc_explain_Thread-local_garbage_collection.html))

Mac OS X Snow Leopard 引入了线程本地回收（thread-local collection），这是对 Objective-C 垃圾回收器的一项重大增强。线程本地回收是一种更高效的方式，能回收大多数程序里的大部分垃圾。相比 Objective-C GC 所用的其他算法，它在线程和核心数增多时的伸缩性也更好。

#### 垃圾回收简史

Objective-C GC 所用的最简单的算法是**全量回收**（full collection）。GC 会扫描整个堆里所有存活的对象，（近似地）找出所有已死亡的对象，并将它们回收。这个过程很慢，尤其是当你有大量并未死亡的对象时，但它确实能找出所有可能的垃圾。从历史上看，这基本上是 1960 年代的技术，唯一的例外是那套能让其他线程在扫描完成前基本不受阻碍地继续运行的机制。

Objective-C GC 所用的第二种算法是**分代回收**（generational collection）。它利用了*分代假设*：大多数对象都"英年早逝"。堆被划分成至少两代：新对象和老对象。在分配了一定量的新对象之后，回收器会执行一次分代回收。首先，它只扫描"新"对象，以及任何被写入了指向"新"对象的指针的"老"对象。然后，那些如今已经死亡的"新"对象会被回收，而存活下来的"新"对象则会被"老化"，移到下一代里。分代 GC 的优点在于，它能用少得多的工作量（不需要扫描大多数"老"对象），回收掉大量垃圾（因为大多数对象都会早夭）。全量回收仍然是必要的，用来回收那些熬过了"婴儿期"、之后才死亡的对象，但运行频率会低一些。分代回收是 1980 年代的技术。

#### 线程本地回收

第三种算法就是全新的**线程本地回收**（TLC）。TLC 和分代回收有点像：它扫描并回收一部分对象子集，力图让回收器的每一分投入都物有所值。这里用到的假设是*线程本地*假设：大多数对象死亡时都还没有被任何其他线程触及过。新分配的对象会被标记为该分配线程的线程本地对象。如果一个线程本地对象变得能被另一个线程访问到（比如说，指向它的一个指针被写入了某个全局变量），那么它就"逃逸"了，会被移出线程本地集合。在一次线程本地回收中，一个线程会扫描自己的栈以及自己那组线程本地对象，并回收其中已经死亡的对象。

线程本地回收的优点在于，它不需要和其他线程做任何同步。通常，执行 GC 工作的线程需要和其他线程协调。举例来说，可能是其他线程在 GC 线程查看过某个指针变量之后又改变了它，或者开始指向一个 GC 线程原本以为已经死亡的对象。线程本地回收避免了这些复杂情况。线程本地对象按定义只能被一个线程访问到。其他线程没有任何办法获取指向这些对象的指针，也没法改变其内部的指针值。执行线程本地回收的线程可以独自快速工作，不受其他线程的干扰。

让每个线程"自己收拾自己的摊子"，能缓解回收器里的瓶颈，而这个瓶颈只会随着线程和核心数的增加而变得更糟。在多个线程上同时运行线程本地回收是很轻松的一件事。而且它非常快，因为唯一需要扫描的内存就是该线程自己的栈，以及它存活下来的那些线程本地对象。一个线程在分代或全量 GC 期间的暂停时间，几乎和它运行一次线程本地回收的暂停时间一样长——但 TLC 能立刻回收掉一些垃圾，而其他算法则需要先做更多工作、和所有其他线程协调好，才能真正开始回收任何东西。

#### 你能帮上什么忙

当对象始终不被其他线程触及时，线程本地回收的效果最好。在 Objective-C 回收器里，这意味着要尽量避免对临时对象调用 CFRetain()。一个被 CFRetain 过的指针，可能会绕过回收器用来追踪逃逸对象的写屏障（write barrier），跑到任何地方去。（这正是 Snow Leopard 还有改进空间的一处：系统框架经常会分配一个 CF 保留计数为 1 的对象，然后立刻释放它，这就使得这些对象没法参与线程本地回收。）一个对象逃出线程本地回收的其他方式还包括：把一个指针存进某个全局变量；把一个指针存进某个本身并非线程本地的其他对象；以及对该对象建立弱引用或关联引用。

如果你的线程刚刚创建并丢弃了大量临时对象，你可以给回收器一个提示，告诉它现在可能是运行的好时机。`-[NSGarbageCollector
	collectIfNeeded]` 和 `-[NSAutoreleasePool
	drain]` 就是这样的两个提示。它们可能会先运行一次线程本地回收，然后再视情况跟进一次分代回收或全量回收。

[Sealie Software](http://sealiesoftware.com/index.html)
