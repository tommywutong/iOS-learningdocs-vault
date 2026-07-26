---
title: '[objc explain]：非脆弱 ivar'
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2009/01/27/objc_explain_Non-fragile_ivars.html'
original_language: en
published: 2009-01-27
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:bff9071576a2553c'
translated: true
---

> 原文：[[objc explain]：非脆弱 ivar](http://sealiesoftware.com/blog/archive/2009/01/27/objc_explain_Non-fragile_ivars.html)　·　Hamster Emporium (Greg Parker)

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

\<\< [[objc explain]：类与元类](http://sealiesoftware.com/blog/archive/2009/04/14/objc_explain_Classes_and_metaclasses.html) | [归档](http://sealiesoftware.com/blog/archive/index.html) | [无穷并没有你想的那么长](http://sealiesoftware.com/blog/archive/2008/11/30/Infinity_isnt_as_long_as_you_think.html) \>\>

[![(链接)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2009/01/27/objc_explain_Non-fragile_ivars.html)

**[objc explain]：非脆弱 ivar** ([2009-01-27 09:30 PM](http://sealiesoftware.com/blog/archive/2009/01/27/objc_explain_Non-fragile_ivars.html))

非脆弱实例变量（non-fragile instance variable）是 iPhone 和 64 位 Mac 上现代 Objective-C runtime 的一项头号特性。它们让框架开发者获得了更大的灵活性，同时又不失二进制兼容性，也为自动合成的属性 ivar、以及声明在类接口之外的 ivar 铺平了道路。

#### 脆弱基类问题

脆弱 ivar 是经典的*脆弱基类*问题的一个子集。在某些语言里，如果不重新编译该类的所有子类，超类就无法被改动。举例来说，给一个 C++ 超类添加数据成员或虚成员函数，会破坏与该类所有子类的二进制兼容性，哪怕新增的成员是私有的、对子类不可见也一样。

在经典 Objective-C 里，得益于动态消息派发，方法大多是非脆弱的。只要不产生名字冲突，你可以自由地给超类添加方法。但在 32 位 Mac 上，Objective-C 的 ivar 是脆弱的。

#### 32 位 Mac：脆弱的 Objective-C ivar

假设你正在为 Mac OS X Leopard 写下一款划时代的宠物店应用程序。你可能会有这样一个 `NSView` 的子类 `PetShopView`，里面用数组存着宠物店里的小狗和小猫。

| _`NSView (Leopard)`_ |  |
|---|---|
| `0` | `Class isa` |
| `4` | `NSRect bounds` |
| `20` | `NSView *superview` |
| `24` | `NSColor *bgColor` |

| _`PetShopView`_ |  |
|---|---|
| `0` | `Class isa` |
| `4` | `NSRect bounds` |
| `20` | `NSView *superview` |
| `24` | `NSColor *bgColor` |
| `28` | `NSArray *kittens` |
| `32` | `NSArray *puppies` |

然后 Mac OS X Def Leopard 发布了，带来了它全新的多爪界面技术。AppKit 的开发者给 `NSView` 加上了一些爪子追踪代码。

| _`NSView (Def Leopard)`_ |  |
|---|---|
| `0` | `Class isa` |
| `4` | `NSRect bounds` |
| `20` | `NSView *superview` |
| `24` | `NSColor *bgColor` |
| `28` | `NSSet *touchedPaws` |

| _`PetShopView`_ |  |
|---|---|
| `0` | `Class isa` |
| `4` | `NSRect bounds` |
| `20` | `NSView *superview` |
| `24` | `NSColor *bgColor` |
| `28` | `NSArray *kittens` |
| `32` | `NSArray *puppies` |

不幸的是，你的小猫们被脆弱 ivar 给害惨了。反过来说，AppKit 的开发者们也被困死在 Mac OS X 10.0 时代所选定的那些 ivar 里，动弹不得。

#### iPhone 和 64 位 Mac：非脆弱的 Objective-C ivar

你和 AppKit 的开发者们真正想要的是像这样的方案。

| _`NSView (Def Leopard)`_ |  |
|---|---|
| `0` | `Class isa` |
| `4` | `NSRect bounds` |
| `20` | `NSView *superview` |
| `24` | `NSColor *bgColor` |
| `28` | `NSSet *touchedPaws` |

| _`PetShopView`_ |  |
|---|---|
| `0` | `Class isa` |
| `4` | `NSRect bounds` |
| `20` | `NSView *superview` |
| `24` | `NSColor *bgColor` |
| `28` | `NSSet *touchedPaws` |
| `32` | `NSArray *kittens` |
| `36` | `NSArray *puppies` |

在这里，runtime 意识到 `NSView` 现在比 `PetShopView` 编译时更大了。子类的 ivar 会相应地滑动，而不需要重新编译任何代码，小猫们就这样被一个动态的 runtime 拯救了。

#### 原理

经典 Objective-C 中，ivar 访问所生成的代码就像访问 C `struct` 的字段一样。ivar 的偏移量是一个在编译期就确定的常量。而新的 ivar 代码则会为每个 ivar 创建一个变量，里面存着该 ivar 的偏移量，所有访问该 ivar 的代码都会使用这个变量。在启动时，如果 runtime 检测到超类的体积超出预期，它就可以改变任何一个 ivar 偏移量变量。

在宠物店这个例子里，`_OBJC_IVAR_PetShopView_kittens` 在编译期是 28，但当 runtime 看到 Def Leopard 版本的 `NSView` 时，会把它改成 32。不需要重新编译任何代码，而这个额外的 ivar 偏移量变量所带来的性能开销也很小。AppKit 开心了，你也开心了，小猫们也开心了。

[Sealie Software](http://sealiesoftware.com/index.html)
