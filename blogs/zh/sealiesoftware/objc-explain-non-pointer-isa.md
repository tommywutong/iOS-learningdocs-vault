---
title: '[objc explain]：非指针 isa'
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2013/09/24/objc_explain_Non-pointer_isa.html'
original_language: en
published: 2013-09-24
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:c74d10bd60d32670'
translated: true
---

> 原文：[[objc explain]：非指针 isa](http://sealiesoftware.com/blog/archive/2013/09/24/objc_explain_Non-pointer_isa.html)　·　Hamster Emporium (Greg Parker)

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

\<\< [macOS 10.13 中的 Objective-C 与 fork()](http://sealiesoftware.com/blog/archive/2017/6/5/Objective-C_and_fork_in_macOS_1013.html) | [归档](http://sealiesoftware.com/blog/archive/index.html) | [[objc explain]：你在 objc_msgSend() 里崩溃了：iPhone 5s 篇](http://sealiesoftware.com/blog/archive/2013/09/12/objc_explain_So_you_crashed_in_objc_msgSend_iPhone_5s_Edition.html) \>\>

[![(链接)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2013/09/24/objc_explain_Non-pointer_isa.html)

**[objc explain]：非指针 isa** ([2013-09-24 1:27 AM](http://sealiesoftware.com/blog/archive/2013/09/24/objc_explain_Non-pointer_isa.html))

在 arm64 架构的 iOS 上，Objective-C 对象的 isa 字段不再是一个指针了。

#### 你说什么？

在 arm64 架构的 iOS 上，Objective-C 对象的 isa 字段不再是一个指针了。

#### 如果它不再是指针了，那它是什么？

其中一部分位仍然编码着指向该对象所属类的指针。但无论是 OS X 还是 iOS，实际上都没有用满 64 位的全部虚拟地址空间。Objective-C runtime 可以利用这些多出来的位，来存储每个对象各自的数据，比如它的保留计数（retain count），或者它是否曾经被弱引用过。

#### 为什么要改成这样？

为了性能。把这些原本用不上的位重新利用起来，能提升速度、减小内存占用。在 iOS 7 上，重点放在了优化 retain/release 和 alloc/dealloc 上。

#### 这对我的代码意味着什么？

不要直接读取 `obj->isa`。如果你这么做，编译器会报错。相信编译器。编译器是你的朋友。改用 `[obj class]` 或 `object_getClass(obj)`。

不要直接写 `obj->isa`。改用 `object_setClass()`。

如果你重写了 `+allocWithZone:`，你可能会把对象的 isa 字段初始化成一个"原始的"（raw）isa 指针。如果你这样做，就不会有额外的数据被存进那个 isa 字段，而且你可能会因此在 retain/release 这类代码路径上走慢速路径。要启用这些优化，应该改成把 isa 字段设为零（如果它还不是零的话），然后调用 `object_setClass()`。

如果你重写了 retain/release 来实现一个自定义的内联保留计数，可以考虑把那段代码去掉，改用 runtime 自身的实现。

64 位 iOS 模拟器目前并不使用非指针 isa。请在真实的 arm64 设备上测试你的代码。

#### 这对调试意味着什么？

调试器知道如何从 isa 字段里解码出类信息。大多数情况下，你应该不需要直接去查看它。

你可以在运行代码时设置环境变量 `OBJC_DISABLE_NONPOINTER_ISA=YES`，来为所有类禁用非指针 isa。如果你的代码在设置了这个环境变量之后能正常工作、不设置就出问题，那你可能在某处不正确地直接访问了 isa 字段。

如果你在写一个类似调试器的工具，Objective-C runtime 导出了一些变量，可以帮你解码 isa 字段。`objc_debug_isa_class_mask` 描述了哪些位是类指针：`(isa & class_mask) == `类指针。`objc_debug_isa_magic_mask` 和 `objc_debug_isa_magic_value` 描述了一些位，用来帮助区分有效的 isa 字段和其他无效的值：对于不是原始类指针的 isa 字段，`(isa & magic_mask) == magic_value`。这些变量未来可能会发生变化，所以不要在应用程序代码里使用它们。

#### 不，说真的，每一位到底都代表什么？

纯粹是为了好玩。这些数值在未来的操作系统版本里会发生变化。我觉得它们其实已经变过了。

| (LSB) |  |  |  |
|---|---|---|---|
| 1 | bit | `indexed` | `0` 表示原始 isa，`1` 表示非指针 isa。 |
| 1 | bit | `has_assoc` | 对象有过、或曾经有过关联引用。没有关联引用的对象可以更快地被释放。 |
| 1 | bit | `has_cxx_dtor` | 对象有一个 C++ 或 ARC 析构函数。没有析构函数的对象可以更快地被释放。 |
| 30 | bits | `shiftcls` | 类指针中非零的那些位。 |
| 9 | bits | `magic` | 等于 `0xd2`。供调试器用来区分真实对象和尚未初始化的垃圾数据。 |
| 1 | bit | `weakly_referenced` | 对象是、或曾经是某个 ARC 弱变量所指向的对象。没有被弱引用过的对象可以更快地被释放。 |
| 1 | bit | `deallocating` | 对象当前正在被释放。 |
| 1 | bit | `has_sidetable_rc` | 对象的保留计数太大，无法内联存储。 |
| 19 | bits | `extra_rc` | 对象超出 1 的那部分保留计数。（举例来说，如果 `extra_rc` 是 5，那么该对象真实的保留计数就是 6。） |
| (MSB) |  |  |  |

[Sealie Software](http://sealiesoftware.com/index.html)
