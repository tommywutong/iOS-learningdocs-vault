---
title: '[objc explain]：objc_msgSend_vtable'
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2011/06/17/objc_explain_objc_msgSend_vtable.html'
original_language: en
published: 2011-06-17
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:1cf86dd029518248'
translated: true
---

> 原文：[[objc explain]：objc_msgSend_vtable](http://sealiesoftware.com/blog/archive/2011/06/17/objc_explain_objc_msgSend_vtable.html)　·　Hamster Emporium (Greg Parker)

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

\<\< [[objc explain]：发给 nil 的消息的返回值](http://sealiesoftware.com/blog/archive/2012/2/29/objc_explain_return_value_of_message_to_nil.html) | [归档](http://sealiesoftware.com/blog/archive/index.html) | [诊断工程系的 Gregory Parker 博士](http://sealiesoftware.com/blog/archive/2010/09/01/Dr_Gregory_Parker_Department_of_Diagnostic_Engineering.html) \>\>

[![(链接)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2011/06/17/objc_explain_objc_msgSend_vtable.html)

**[objc explain]：objc_msgSend_vtable** ([2011-06-17 4:42 PM](http://sealiesoftware.com/blog/archive/2011/06/17/objc_explain_objc_msgSend_vtable.html))

`objc_msgSend_vtable` 是 `objc_msgSend` 的一个版本，用来优化那几个被调用得最频繁的方法。

大多数 Objective-C 方法都是在 `objc_msgSend` 内部通过哈希表查找来派发的。在 x86_64 上，有少数几个选择器可以用类似 C++ 风格的虚函数表（virtual table）来派发：这是数组查找，而不是哈希表查找。

编译器知道哪些选择器会被 runtime 优化。它会用不同的方式编译这些调用点，通过一个函数指针去调用 `objc_msgSend_fixup`。在运行时，如果被调用的选择器正是那些被优化的选择器之一，`objc_msgSend_fixup` 就会把这个函数指针替换成某一个 `objc_msgSend_vtable` 函数。

C++ 的 vtable 是出了名的脆弱：每个虚方法的数组偏移量都被硬编码进了生成的代码里。Objective-C 的 vtable 则不脆弱。每个 vtable 都是在运行时构建的，并会在方法列表变化时更新。理论上甚至连"哪些方法要被优化"这个集合本身都可以改变。这种非脆弱的灵活性，代价是派发过程中要多一次内存读取。

通过 vtable 派发比哈希表更快，但如果到处都用的话会耗费大量内存。Objective-C 的 vtable 实现把使用范围限制在少数几个选择器上，这些选择器需要满足：(1) 在各处都有实现，但 (2) 很少被重写。这意味着大多数类都共享它们超类的 vtable，从而把内存开销压得很低。

任何一个 `objc_msgSend_vtable` 函数里的崩溃，都应该按照排查 `objc_msgSend` 本身崩溃的方式去调试。它们崩溃的原因完全一样，比如错误的内存管理或者内存破坏者。

目前，runtime 使用了十六个不同的 `objc_msgSend_vtable` 函数，对应这个十六项 vtable 里的每一个槽位。

| `objc_msgSend_vtable0` | `allocWithZone:` |
|---|---|
| `objc_msgSend_vtable1` | `alloc` |
| `objc_msgSend_vtable2` | `class` |
| `objc_msgSend_vtable3` | `self` |
| `objc_msgSend_vtable4` | `isKindOfClass:` |
| `objc_msgSend_vtable5` | `respondsToSelector:` |
| `objc_msgSend_vtable6` | `isFlipped` |
| `objc_msgSend_vtable7` | `length` |
| `objc_msgSend_vtable8` | `objectForKey:` |
| `objc_msgSend_vtable9` | `count` |
| `objc_msgSend_vtable10` | `objectAtIndex:` |
| `objc_msgSend_vtable11` | `isEqualToString:` |
| `objc_msgSend_vtable12` | `isEqual:` |
| `objc_msgSend_vtable13` | `retain`（非 GC 模式）`hash`（GC 模式） |
| `objc_msgSend_vtable14` | `release`（非 GC 模式）`addObject:`（GC 模式） |
| `objc_msgSend_vtable15` | `autorelease`（非 GC 模式）`countByEnumeratingWithState:objects:count:`（GC 模式） |

出于显而易见的原因，vtable 在 GC 和非 GC 下的内容是不一样的。`-isFlipped` 是 NSView 的一部分。`-countByEnumeratingWithState:objects:count:` 是快速枚举的实现，包括 `for (x in
       y)`。这些方法加在一起，大约占到一个典型 Objective-C 应用程序里 30% 到 50% 的调用量。

[Sealie Software](http://sealiesoftware.com/index.html)
