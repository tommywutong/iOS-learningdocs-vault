---
title: '[objc explain]：单态派发'
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2009/05/14/objc_explain_Monomorphic_dispatch.html'
original_language: en
published: 2009-05-14
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:cf2206dd21885e21'
translated: true
---

> 原文：[[objc explain]：单态派发](http://sealiesoftware.com/blog/archive/2009/05/14/objc_explain_Monomorphic_dispatch.html)　·　Hamster Emporium (Greg Parker)

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

\<\< [Mac OS X 版 Valgrind 并入主线](http://sealiesoftware.com/blog/archive/2009/06/03/Valgrind_for_Mac_OS_X_goes_mainline.html) | [归档](http://sealiesoftware.com/blog/archive/index.html) | [[objc explain]：类与元类](http://sealiesoftware.com/blog/archive/2009/04/14/objc_explain_Classes_and_metaclasses.html) \>\>

[![(链接)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2009/05/14/objc_explain_Monomorphic_dispatch.html)

**[objc explain]：单态派发** ([2009-05-14 8:04 PM](http://sealiesoftware.com/blog/archive/2009/05/14/objc_explain_Monomorphic_dispatch.html))

多态派发是指同一个调用点可能会跳转到几个不同实现中的某一个。C 语言的函数调用不是多态的；Objective-C 的方法和 C++ 的虚方法则是多态的。

当一个调用点在原理上可能调用不同的实现，但在现实中却只会调用某一个特定实现时，就会用到单态派发这一优化。这样优化器就能消除多态派发器的开销，直接跳转到正确的位置，甚至能把被调用者就地内联进来。这是从 Smalltalk 到 Java 再到 JavaScript，各种动态编译 runtime 里的一个经典优化手段。

这里存在一些复杂情况。首先是像共享库或 eval() 操作这样的动态加载代码。如果你的新代码给一个此前是单态的调用提供了第二种实现，你就需要能够即时撤销之前的那个优化，重新编译它，或者退回到解释执行。如今任何一个够格的动态编译器都能做到这一点。

其次，搜索其他实现的范围有多大，取决于你所用语言的类型严格程度。如果接收者的编译期类型严格限定了运行时允许的类型，那么这项优化只需要在层级结构的那一部分里保证实现唯一即可。在一个接收者类型为 `Employee`（或其子类）、类型严格的调用点上，`Window.title` 和 `Employee.title` 是不会互相干扰的。

那 Objective-C 在这里处于什么位置呢？总的来说，它并不适用。单态优化很难应用到 Objective-C 上。由于这门语言自身的定义，上述两个问题的影响都很大，哪怕它明天突然获得了一个运行时重编译器也一样。

Objective-C 的调用点不是类型严格的。代码里可能写着接收者是某个类型，但在运行时它实际上可能是一个 Distributed Objects 代理，或者一个单元测试的 mock 对象，又或者一个脚本桥接的垫片。你得去看所有的类，才能判断某个选择器是否有多个实现，而不能只搜索类层级结构里的一个子树。

更糟的是，根本没有哪个选择器只有唯一一个实现。它们至少都有两个：某个类里实际存在的那一个，以及来自其他每一个调用 -forwardInvocation: 的类的那一个。你永远无法直接跳转到任何一个实现，因为如果你的接收者对象类型不对，你就需要转而调用转发（forwarding）机制。而快速检查接收者的类型，很快就会把优化带来的收益吃光；你只能做有限的几次检查，成本就会和 `objc_msgSend()` 打平。

在 Objective-C 里，仍有一些重要的场景，单态派发依然能起作用。容器类尤其只有一两种真正的实现，所以对接收者类型的检查可能就足够快了。而在其他地方，你可以做一次相对昂贵的类型检查，然后多次复用这个结果，比如一连串的 `[self ...]` 调用。棘手的地方在于，要找出哪些选择器和调用点值得做这种优化，同时又不能花太多时间或内存去判断。

单态派发这项优化，未来会出现在某个动态重编译的 Objective-C runtime 里，但它不会像在其他动态性更弱的语言里那样好用。

[Sealie Software](http://sealiesoftware.com/index.html)
