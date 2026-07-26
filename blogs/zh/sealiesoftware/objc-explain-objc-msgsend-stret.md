---
title: '[objc explain]：objc_msgSend_stret'
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2008/10/30/objc_explain_objc_msgSend_stret.html'
original_language: en
published: 2008-10-30
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:02edf4fbe2132af4'
translated: true
---

> 原文：[[objc explain]：objc_msgSend_stret](http://sealiesoftware.com/blog/archive/2008/10/30/objc_explain_objc_msgSend_stret.html)　·　Hamster Emporium (Greg Parker)

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

\<\< [[objc explain]：objc_msgSend_fpret](http://sealiesoftware.com/blog/archive/2008/11/16/objc_explain_objc_msgSend_fpret.html) | [归档](http://sealiesoftware.com/blog/archive/index.html) | [更新：Mac OS X 版 Valgrind](http://sealiesoftware.com/blog/archive/2008/10/27/updated_Valgrind_for_Mac_OS_X.html) \>\>

[![(链接)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2008/10/30/objc_explain_objc_msgSend_stret.html)

**[objc explain]：objc_msgSend_stret** ([2008-10-30 10:28 PM](http://sealiesoftware.com/blog/archive/2008/10/30/objc_explain_objc_msgSend_stret.html))

`objc_msgSend` 是 Objective-C 的消息派发器。它是那个"调用函数的函数"，靠选择器和接收者对象的类来决定要跳转到哪里。`objc_msgSend_stret` 和它完全一样，只不过是给那些返回 struct 类型值的方法用的。为什么 `objc_msgSend_stret` 会存在呢？因为 C 语言机器层面的底层机制要求如此，而 Objective-C 的方法说到底就是 C 函数，只要你稍微歪着头眯起眼睛看就能看出来。

在大多数处理器上，函数最初的几个参数是通过 CPU 寄存器传递的，返回值也是通过 CPU 寄存器传回的。Objective-C 方法也是如此，只不过前两个参数固定是 `id self` 和 `SEL
	_cmd`。这是一个 PowerPC 的例子：

```
    -(int) method:(id)arg;
        r3 = self
        r4 = _cmd, @selector(method:)
        r5 = arg
	(on exit) r3 = returned int
```

CPU 寄存器对于 int 和指针这类小的返回值来说没问题，但 struct 类型的值可能大到装不下。对于 struct，调用者会在自己的栈上分配好用来存放返回值的空间，把这块存储空间的地址传给函数，函数再把返回值写进这块空间。struct 的地址就像 `self` 和 `_cmd` 一样，是一个隐式的第一参数：

```
    -(struct st) method:(id)arg;
        r3 = &struct_var (in caller's stack frame)
        r4 = self
        r5 = _cmd, @selector(method:)
        r6 = arg
        (on exit) return value written into struct_var
```

现在来看看 `objc_msgSend` 的任务。它要用 `_cmd` 和 `self->isa` 来选择跳转目标。但如果方法要返回一个 struct，`self` 和 `_cmd` 就会在不同的寄存器里，而 `objc_msgSend` 事先没法知道这一点。于是就有了 `objc_msgSend_stret`：和 `objc_msgSend` 一样，只是从不同的寄存器里读取它的值。

但这里面有个陷阱。

在大多数体系结构上，有一些小的 C struct 终归还是会通过寄存器返回，而不是像 `objc_msgSend_stret` 所预期的那样，使用那个 struct 地址的第一参数。如果 struct 类型属于这一类，那就会改用 `objc_msgSend`。所以 `objc_msgSend_stret` 里"struct return"指的是该体系结构对"栈上返回的 struct"这一定义，而这未必和 C 语言里的 struct 相吻合。

关于哪些 struct 类型会通过寄存器返回，这些规则总是很晦涩，有时候简直莫名其妙。ppc32 很简单：struct 永远不会通过寄存器返回。i386 也很直接：`sizeof` 恰好等于 1、2、4 或 8 的 struct 会通过寄存器返回。x86_64 就复杂多了，包括把浮点 struct 字段通过 FPU 寄存器返回的规则，而 ppc64 的规则和例外足以让你头晕目眩。这些繁琐的细节都记录在 [Mac OS X ABI Guide](http://developer.apple.com/documentation/DeveloperTools/Conceptual/LowLevelABI) 里，不过和往常一样，如果文档和编译器对不上，那多半是文档错了。

如果你要直接调用 `objc_msgSend`，需要知道某个特定 struct 类型是否该用 `objc_msgSend_stret`，我建议采用实证的办法：写一行调用你那个方法的代码，在你关心的每个体系结构上编译它，然后看看汇编代码里编译器用的是哪个派发函数。

[Sealie Software](http://sealiesoftware.com/index.html)
