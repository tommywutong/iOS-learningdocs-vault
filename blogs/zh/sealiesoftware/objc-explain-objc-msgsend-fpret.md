---
title: '[objc explain]：objc_msgSend_fpret'
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2008/11/16/objc_explain_objc_msgSend_fpret.html'
original_language: en
published: 2008-11-16
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:79531377e20c0805'
translated: true
---

> 原文：[[objc explain]：objc_msgSend_fpret](http://sealiesoftware.com/blog/archive/2008/11/16/objc_explain_objc_msgSend_fpret.html)　·　Hamster Emporium (Greg Parker)

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

\<\< [无穷并没有你想的那么长](http://sealiesoftware.com/blog/archive/2008/11/30/Infinity_isnt_as_long_as_you_think.html) | [归档](http://sealiesoftware.com/blog/archive/index.html) | [[objc explain]：objc_msgSend_stret](http://sealiesoftware.com/blog/archive/2008/10/30/objc_explain_objc_msgSend_stret.html) \>\>

[![(链接)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2008/11/16/objc_explain_objc_msgSend_fpret.html)

**[objc explain]：objc_msgSend_fpret** ([2008-11-16 7:00 PM](http://sealiesoftware.com/blog/archive/2008/11/16/objc_explain_objc_msgSend_fpret.html))

`objc_msgSend` 是 Objective-C 的消息派发器。`objc_msgSend_stret` 和它完全一样，只不过是给那些返回 struct 类型值的方法用的。而 `objc_msgSend_fpret` 则是给那些在某些体系结构上返回浮点值的方法用的。

|  | `objc_msgSend_fpret` 的返回类型 |
|---|---|
| i386 | `float`、`double`、`long double` |
| x86_64 | `long double` |
| ppc | 无（与 `objc_msgSend` 完全相同） |
| ppc64 |  |
| arm |  |

`objc_msgSend_stret` 之所以存在，是因为对于返回 struct 的函数来说，参数是放在不同位置传递的。但这不是 `objc_msgSend_fpret` 要解决的问题。相反，`objc_msgSend_fpret` 的存在是为了正确处理返回值本身。具体来说，是为了处理在 i386 和 x86_64 上，发给 nil 的消息的返回值。

发给 nil 的消息会尽可能返回零。在 ppc 上，`objc_msgSend` 在接收者为 nil 时，会在返回前清空寄存器 r3、r4、f1 和 f2。这意味着任何指针、整数或浮点类型的返回值都会是零，而 struct 则是未定义的。在 ppc 上，`objc_msgSend_fpret` 是不必要的，因为如果调用者实际期望的值在 r3 或 r4 里，那清空 f1 和 f2 也是无害的。

i386 则不一样。那里的浮点寄存器历史上是从最初 8086 CPU 所用的 8087 FPU 衍生而来的。x87 单元是个古怪的家伙：它有八个浮点寄存器，但这些寄存器本身却被当作一个栈来使用。数值会在这个栈上被压入和弹出，尽管这个栈是存储在寄存器里的，最多只有八个位置。

对于返回值，被调用者会把值压入 x87 栈，调用者再把它弹出来。这对 C 函数来说没问题，但当 `objc_msgSend` 返回零的时候就不太妙了。`objc_msgSend` 并不知道调用者到底想要什么返回类型，所以除非调用者确实期望弹出一个浮点值，否则它绝不能往 x87 栈上压一个零。

解决办法就是 `objc_msgSend_fpret`。在 i386 上给 nil 发消息的过程中，`objc_msgSend_fpret` 会往 x87 栈上压一个零、供调用者弹出，而 `objc_msgSend` 则不会这么做。调用者知道自己期望的返回类型是什么，因此会用相应匹配的派发器。在 ppc、ppc64 和 arm 上，`objc_msgSend_fpret` 和 `objc_msgSend` 是完全一样的，通常也用不上。

那 x86_64 呢？这个体系结构是进一步、退两步。好消息是，`float` 和 `double` 类型的返回值是通过 XMM 寄存器返回的。`objc_msgSend` 就像在 ppc 上一样，自己就能处理好这个。坏消息是，`long double` 仍然要用到 x87 栈。所以 `objc_msgSend_fpret` 依然存在，但在 x86_64 上就只用于 `long double`。更糟的消息是，C99 的 `complex long double` 会在 x87 栈上返回两个值。所以现在还有一个专门为这种情况准备的 `objc_msgSend_fp2ret`。目前没有任何编译器实际会用到 `objc_msgSend_fp2ret`，所以但愿没有人会写出这样的代码：在 x86_64 上给 nil 发消息，还期望得到一个类型为 `complex long
	double` 的零返回值。

最后一点：Mac OS X 10.4 及更早版本，在 ppc 上给浮点方法发消息给 nil 时并不会返回零。如果你在为那些更老的系统写代码，请务必当心。其他所有体系结构一直都会返回浮点数的零值，包括 10.4 上的 i386。

[Sealie Software](http://sealiesoftware.com/index.html)
