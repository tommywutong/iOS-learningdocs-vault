---
title: '[objc explain]：弱导入类（weak-import classes）'
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2009/09/09/objc_explain_Weak-import_classes.html'
original_language: en
published: 2009-09-09
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:636c59a750b11ccf'
translated: true
---

> 原文：[[objc explain]：弱导入类（weak-import classes）](http://sealiesoftware.com/blog/archive/2009/09/09/objc_explain_Weak-import_classes.html)　·　Hamster Emporium (Greg Parker)

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

\<\< [自己动手实现 Objective-C weak import](http://sealiesoftware.com/blog/archive/2010/4/8/Do-it-yourself_Objective-C_weak_import.html) | [归档](http://sealiesoftware.com/blog/archive/index.html) | [键盘背光变色](http://sealiesoftware.com/blog/archive/2009/09/05/Colorized_keyboard_backlight.html) \>\>

[![(链接)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2009/09/09/objc_explain_Weak-import_classes.html)

**[objc explain]：弱导入类（weak-import classes）** ([2009-09-09 1:30 PM](http://sealiesoftware.com/blog/archive/2009/09/09/objc_explain_Weak-import_classes.html))

弱导入类是一个很实用的 Objective-C 新特性，但你现在还用不上。

当你想使用框架里的某样东西，但又得兼容那些还不支持它的旧版本框架时，weak import 就是解决办法。用上 weak import，你就能在真正使用某个特性之前，先在运行时检测它是否存在。

Objective-C 此前一直不支持对类的 weak import。你只能用笨拙的运行时内省来检查某个类是否可用，把指向那个类的指针存到一个变量里，然后在想给这个类发消息时使用那个变量。更糟的是，也没有什么合理的办法能让你创建自己的子类，去继承一个可能不可用的超类。有些开发者会把子类放进一个单独的库里，等确认超类存在之后才加载这个库，但即便是这个技巧，在 iPhone OS 上也是不被允许的。

C 函数的 weak import 是这样工作的：在调用之前先检查这个弱导入函数指针的值：

```
    if (NSNewFunction != NULL) {
        NSNewFunction(...);
    } else {
        // NSNewFunction not supported on this system
    }
```

同样的机制天然适配 Objective-C 的类，以及 Objective-C 对发给 nil 的消息的处理方式。这些写法比 `NSClassFromString()` 或者一个单独的 `NSBundle` 要好用得多。

```
    if ([NSNewClass class] != nil) {
        [NSNewClass doSomething];
    } else {
        // NSNewClass is unavailable on this system
    }
```

```
    @interface MySubclass : NSNewClass ... @end
    MySubclass *obj = [[MySubclass alloc] init];
    if (!obj) {
        // MySubclass (or a superclass thereof) is unavailable on this system
    }
```

Objective-C 类的 weak import 现在已经可用了。但你现在还用不上。首先，目前它只在 iPhone OS 3.1 上受支持；预计将来会在某个 Mac OS 版本中登场。

其次，在 iPhone OS 3.1 之后的第一次系统更新到来之前，weak import 也没什么你能做的事。到那时你才能写一个采用那个未来版本新特性的 App，同时用 weak import 保持对 3.1 的兼容。（它仍然无法运行在 3.0 或 2.x 上，因为那些系统缺少处理弱导入引用所需的 runtime 机制。）

由于排期原因，Objective-C 的 weak import 没能赶上 Snow Leopard。假设它会在 Mac OS X 10.7（暂名 Cat Name Forthcoming）中发布，那你要等到 Mac OS X 10.8（LOLcat）才能用上它。

[Sealie Software](http://sealiesoftware.com/index.html)
