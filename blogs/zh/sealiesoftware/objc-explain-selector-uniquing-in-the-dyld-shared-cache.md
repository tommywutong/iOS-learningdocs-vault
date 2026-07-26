---
title: '[objc explain]：dyld 共享缓存中的选择器唯一化'
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2009/09/01/objc_explain_Selector_uniquing_in_the_dyld_shared_cache.html'
original_language: en
published: 2009-09-01
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:1f9de33b42489426'
translated: true
---

> 原文：[[objc explain]：dyld 共享缓存中的选择器唯一化](http://sealiesoftware.com/blog/archive/2009/09/01/objc_explain_Selector_uniquing_in_the_dyld_shared_cache.html)　·　Hamster Emporium (Greg Parker)

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

\<\< [键盘背光变色](http://sealiesoftware.com/blog/archive/2009/09/05/Colorized_keyboard_backlight.html) | [归档](http://sealiesoftware.com/blog/archive/index.html) | [[objc explain]：线程本地垃圾回收](http://sealiesoftware.com/blog/archive/2009/08/28/objc_explain_Thread-local_garbage_collection.html) \>\>

[![(链接)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2009/09/01/objc_explain_Selector_uniquing_in_the_dyld_shared_cache.html)

**[objc explain]：dyld 共享缓存中的选择器唯一化** ([2009-09-01 2:10 AM](http://sealiesoftware.com/blog/archive/2009/09/01/objc_explain_Selector_uniquing_in_the_dyld_shared_cache.html))

Mac OS X Snow Leopard 把启动 Objective-C runtime 时的启动期开销砍掉了一半，同时还为每个 App 节省了几百 KB 的内存。这一切都是每个 App 白得的好处，多亏了比 Objective-C runtime 本身还要底层的那几块 Mac OS X 组件之一：dyld。

#### dyld 与共享缓存

dyld 是动态加载器和链接器。当你的进程启动时，dyld 会把你的可执行文件及其共享库加载进内存，把跨库的 C 函数和变量引用链接到一起，然后开始朝着 `main()` 执行。

理论上，每次运行你的程序时，共享库都可能是不一样的。但在实践中，几乎每次运行时你拿到的都是同一个版本的共享库，系统上的其他每个进程也是如此。系统利用这一点，构建出了 dyld 共享缓存。这个共享缓存包含了许多系统库的副本，其中大部分 dyld 的链接和加载工作都提前做好了。这样每个进程就都能共享这个共享缓存，从而节省内存和启动时间。

（顺带一提，这个共享缓存把 Leopard 之前那套本该实现同样优化的预绑定（prebinding）系统甩开了老远。还记得安装后那个"正在优化系统性能"的步骤吗？它花的时间常常比安装本身还长。那就是在更新预绑定。而重建共享缓存快得惊人，快到安装程序都懒得再去报告这一步了。）

#### Objective-C 选择器唯一化

Leopard 的 dyld 共享缓存对 C 代码很友好，但它对 Objective-C 的启动开销毫无帮助。Objective-C 最大的一项启动开销就是选择器唯一化。App 和每个共享库都各自带着一份自己的选择器名字副本，比如 "alloc" 和 "init"。runtime 需要为每个选择器名字选出一个单一的、规范的 SEL 指针值，然后更新每个调用点和方法列表的元数据，让它们都使用这个"钦定"的唯一值。这就意味着要建一张很大的哈希表（耗内存）、要频繁调用 `strcmp()`（耗时间），还要修改写时复制（copy-on-write）的元数据（更耗内存）。

一个典型进程里存在着数以万计的唯一选择器。如果你在 Leopard 上运行 ``strings
	/usr/lib/libobjc.dylib``，你能看到那张三万行的[内置选择器表](http://www.opensource.apple.com/source/objc4/objc4-371/runtime/objc-sel-table.h)，那是此前为降低内存开销而做的一次尝试。即便如此，随着 Cocoa.framework 里每新增一个类和方法，这项开销还是会往上涨；如果放任不管，同一个 App 每经历一次系统升级，启动就会变得更慢，占用的内存也会更多。

那显而易见的解决办法是什么？把选择器唯一化的工作放到 dyld 共享缓存里去做。在共享缓存本身里构建一张选择器表，并更新共享库缓存副本里的选择器引用。这样你既能省内存，因为每个进程共享同一张选择器表；又能省时间，因为 runtime 不需要在每次 App 启动时都重建这张表。runtime 只需要修正来自 App 自身的那些选择器引用。问题在哪？选择器太动态了，没法作为 C 符号来实现，所以共享缓存构建工具得学会读写 Objective-C 的元数据才行。

#### 优化的胜利

Snow Leopard 的 dyld 共享缓存对 Objective-C 选择器做了唯一化，而 Snow Leopard 的 Objective-C runtime 能识别出，某个共享库里的选择器是不是已经借助共享缓存被唯一化过了。runtime 初始化时间的大约一半被省了下来，让热启动的 App 快上几十分之一秒。典型的内存节省是每个进程 200 到 500 KB，累积到全系统层面就是好几个 MB。等这项优化在 iPhone OS 那边上线时，据估计能在一台 128 MB 的设备上省下 1 MB。iPhone 性能团队为了这种量级的收益，什么代价都愿意付。

你可以通过各种调试开关，亲眼看到这套系统的运作。

```
$ sudo /usr/bin/update_dyld_shared_cache -debug -verify

[...]

update_dyld_shared_cache: for x86_64, uniquing objc selectors

update_dyld_shared_cache: for x86_64, found 68761 unique objc selectors

update_dyld_shared_cache: for x86_64, 541736/590908 bytes (91%) used in	libobjc unique selector section

update_dyld_shared_cache: for x86_64, updated 205230 selector references
```

```
$ OBJC_PRINT_PREOPTIMIZATION=YES /usr/bin/defaults

objc[424]: PREOPTIMIZATION: selector preoptimization ENABLED (version 3)

objc[424]: PREOPTIMIZATION: honoring preoptimized selectors in /usr/lib/libobjc.A.dylib

objc[424]: PREOPTIMIZATION: honoring preoptimized selectors in /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

objc[424]: PREOPTIMIZATION: honoring preoptimized selectors in /System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/A/Metadata

objc[424]: PREOPTIMIZATION: honoring preoptimized selectors in /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
```

你可以用 `allmemory` 工具来估算内存节省量。记录一下 App 在设置和不设置环境变量 `OBJC_DISABLE_PREOPTIMIZATION=YES` 这两种情况下、启动后的内存占用。看一下脏页（dirty page）的数量，每个脏页会吃掉该进程 4 KB 内存。以 64 位的 TextEdit 为例，禁用这项优化后，脏页数量从 725 跳到了 1069。这是一个偏高的估计——其中许多页在 Leopard 上因为那张旧的内置选择器表本来就不会是脏页——但这依然能说明这项优化的收益有多大。

Objective-C runtime 在启动期做的事情不只是选择器唯一化。未来对 dyld 共享缓存的改进，或许会把其他那些工作也预先算好，从而进一步缩短启动时间、节省内存，并降低链接到那些你实际上并不会用到的 Objective-C 代码所带来的成本。但就目前来看，Snow Leopard 里的选择器唯一化，依然是投入产出比最高的一项优化。

[Sealie Software](http://sealiesoftware.com/index.html)
