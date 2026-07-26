---
title: '空间就是时间：你的计算机理论课骗了你'
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2008/10/14/Space_is_time_how_your_CS_theory_class_lied_to_you.html'
original_language: en
published: 2008-10-14
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:b0fffecc6b15c2c3'
translated: true
---

> 原文：[空间就是时间：你的计算机理论课骗了你](http://sealiesoftware.com/blog/archive/2008/10/14/Space_is_time_how_your_CS_theory_class_lied_to_you.html)　·　Hamster Emporium (Greg Parker)

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

\<\< [更新：Mac OS X 版 Valgrind](http://sealiesoftware.com/blog/archive/2008/10/27/updated_Valgrind_for_Mac_OS_X.html) | [归档](http://sealiesoftware.com/blog/archive/index.html) | [更新：Mac OS X 版 Valgrind](http://sealiesoftware.com/blog/archive/2008/10/01/updated_Valgrind_for_Mac_OS_X.html) \>\>

[![(链接)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2008/10/14/Space_is_time_how_your_CS_theory_class_lied_to_you.html)

**空间就是时间：你的计算机理论课骗了你** ([2008-10-14 1:04 AM](http://sealiesoftware.com/blog/archive/2008/10/14/Space_is_time_how_your_CS_theory_class_lied_to_you.html))

在你的计算机科学算法课上，你学到了空间与时间的权衡。一个需要大量时间的算法，往往可以改造成占用更多空间、但耗时更少。从缓存到记忆化（memoization）再到循环展开，一大批性能优化都是这么干的。

但这种"权衡"是个谎言。空间*就是*时间。

每一次空间的使用都会带来时间上的代价。在你的理论课上，空间的时间代价被大 O 记号这块遮羞布盖住了。在你那台跑单一计算任务或 CPU 跑分测试的高端机器上，空间的时间代价相对于其他时间开销来说微不足道。但在真实世界里，面对内存和电力都有限的消费级设备，空间的时间代价是巨大的。一项试图用更多空间换取更少时间的性能优化，最后往往会变成既耗更多时间、又耗更多空间。

`gcc` 编译器用垃圾回收器来管理它的内存。为了省时间，`gcc` 要等到自己的内存占用相当大之后，才会开始回收任何垃圾。"没关系"，你可能会说，"我的新机器有好几个 GB 的内存"。但内核光是为了记录其余内存的状态，就需要占用一大块内存。而你还在同时跑着一个网页浏览器、一个邮件客户端、一个 IDE，还有音乐、聊天、时钟、搜索、同步、备份，以及十几二十年前你根本没有的一大堆其他东西。而且你的构建系统还会因为你的机器有多个核心，而并行跑好几个 `gcc` 命令。这下你的内存容量其实也没那么充裕了，系统开始向磁盘换页，你的编译器性能一落千丈，网页浏览器也跟着变卡。在这种内存吃紧的环境里，试图少花时间（跳过 GC）、多占空间（堆积垃圾）的做法，狠狠地弄巧成拙了。

空间*就是*时间。一项在配置优越的设备上更快的优化，在其他地方可能要慢得多。假设你客户的机器内存比你的少，据此去设计和测试。

在现代的一个极端例子上，iPhone 只有 128 MB 内存。你有没有见过 iPhone 上的 Safari"忘记"一个网页、在你切换标签页或应用之后又重新下载一遍的情况？那是系统内存耗尽了，Safari 不得不把这个页面扔掉。在 iPhone 上，你自己程序里那个心爱的空间换时间的权衡，可能会牺牲用户的网页，逼着他们在一个慢速网络上重新下载一遍。对你的程序来说或许是好事，但对用户来说是坏事。

空间*就是*时间。一项让*你的程序*更快的优化，可能会让*用户的系统*整体上变慢。要和其他程序好好相处。

Mac OS X 的大部分代码是用 `-Os` 而不是 `-O3` 编译的，为的是减小代码体积。Mac OS X 的内存分配器在某些工作负载下比其他分配器要慢，因为它试图避免囤积那些其他进程用不到的空闲内存。Mac OS X 完全使用动态共享库，再把多个共享库合并成一个共享缓存，然后再仔细地重新处理这个共享缓存，这一切都是为了在多个进程之间节省空间。许多本可以让跨库调用更快、或加速 Objective-C 方法派发、或基于 JIT 做优化的想法，都因为占用空间太多、省下的时间又不够多而被放弃了。

只盯着 CPU 的优化，可能和那个臭名昭著的"过早优化"一样有害。空间*就是*时间。

[Sealie Software](http://sealiesoftware.com/index.html)
