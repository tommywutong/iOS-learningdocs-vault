---
title: 自己动手实现 Objective-C weak import
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2010/4/8/Do-it-yourself_Objective-C_weak_import.html'
original_language: en
published: 2010-04-08
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:42b4d22e565427b6'
translated: true
---

> 原文：[自己动手实现 Objective-C weak import](http://sealiesoftware.com/blog/archive/2010/4/8/Do-it-yourself_Objective-C_weak_import.html)　·　Hamster Emporium (Greg Parker)

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

\<\< [TargetConditionals.h 速查表](http://sealiesoftware.com/blog/archive/2010/8/16/TargetConditionalsh.html) | [归档](http://sealiesoftware.com/blog/archive/index.html) | [[objc explain]：弱导入类（weak-import classes）](http://sealiesoftware.com/blog/archive/2009/09/09/objc_explain_Weak-import_classes.html) \>\>

[![(链接)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2010/4/8/Do-it-yourself_Objective-C_weak_import.html)

**自己动手实现 Objective-C weak import** ([2010-4-8 10:23 PM](http://sealiesoftware.com/blog/archive/2010/4/8/Do-it-yourself_Objective-C_weak_import.html))

#### 警告 危险 有害 小心 呃啊

下面描述的方案是**未经测试的**，多半还有 **bug**。使用风险自负。

#### 内容摘要

Objective-C runtime 支持[弱导入类（weak-imported classes）](http://sealiesoftware.com/blog/archive/2009/09/09/objc_explain_Weak-import_classes.html)，最早可以追溯到 iPhone OS 3.1。一个 App 可以使用某个在 iPhone OS 3.2 或 4.0 中新增的类，同时依然能在 3.1 上运行。App 会检查 `[SomeClass
	class]` 是否为 `nil`，然后据此采取相应行动。

不幸的是，编译器和框架头文件里的类声明目前还不支持 weak import。但你或许还是能用上弱链接，只要你自己加上正确的"咒语"。

要**使用**某个在你 App 的部分部署目标上不可用的类 `SomeClass`，就在**每一个**用到该类的文件里写下这行：

```
    asm(".weak_reference _OBJC_CLASS_$_SomeClass");
```

要**继承**某个在你 App 的部分部署目标上不可用的类 `SomeClass`，就在包含你子类 `@implementation` 的那个文件里写下：

```
    asm(".weak_reference _OBJC_CLASS_$_SomeClass");
    asm(".weak_reference _OBJC_METACLASS_$_SomeClass");
```

这个办法在运行于 iPhone OS 3.0 或更旧系统上的 App 里是不会起作用的。只有 iPhone OS 3.1 及更新的系统才有希望成功。当然了，既然这是**未经测试的**，那在那些系统上也未必能成。

#### 原理

假设你正在写下一款伟大的宠物店应用，想用上 iPhone OS 3.2 里新增的那个假想类 `UIDancePad`。（请勿在 iPad 上跳舞。）当你在代码里用到 `UIDancePad` 这个类时，编译器会生成一个指向该类的 C 符号：

```
    .long _OBJC_CLASS_$_UIDancePad
```

由于 `UIDancePad` 是在一个框架里而不是你自己的代码里，这个符号在你的可执行文件中就保持未定义状态，正如 ``nm -m`` 所显示的那样：

```
    (undefined) external _OBJC_CLASS_$_UIDancePad (from DanceKit)
```

当你运行在 iPhone OS 3.2 上时，一切都很顺利：动态加载器打开你的可执行文件和 DanceKit，并把你那个未定义的符号绑定到它们的类定义上。

但在 iPhone OS 3.1 上事情就没那么顺利了。DanceKit 存在，但没有定义 `UIDancePad`。动态加载器无法解析你那个未定义的符号，于是进程就停止了：

```
    dyld: Symbol not found: _OBJC_CLASS_$_UIDancePad
        Referenced from: /path/to/YourApp
        Expected in: /path/to/DanceKit
```

Weak import 解决了这个问题。编译出来的符号引用现在变成了一个弱引用：

```
    .weak_reference _OBJC_CLASS_$_UIDancePad
    .long _OBJC_CLASS_$_UIDancePad

    (undefined) weak external _OBJC_CLASS_$_UIDancePad (from DanceKit)
```

如果一个弱引用无法解析，动态加载器会耸耸肩，把指针设为 `NULL`。Objective-C runtime 看到这个 `NULL` 指针后，就会修正其余的元数据，就好像 `UIDancePad` 从未存在过一样。

正如上面提到的，编译器和框架头文件的支持目前还没到位。这些"咒语"只是简单地添加了编译器目前还不知道该如何生成的汇编指令：

```
    asm(".weak_reference _OBJC_CLASS_$_UIDancePad");
```

大功告成：Objective-C 类的 weak import。呃，也许吧。我只在一些玩具级的例子上测试过这个方法，其中没有一个真正接近过任何版本的 iPhone OS。写代码的人小心了！

（你可能会问 `_OBJC_METACLASS` 符号是怎么回事？当你继承一个类时，你子类的元类的超类指针，指向的是你子类的超类的元类。换句话说，你子类的 `@implementation` 同时指向它的超类，以及超类的[元类](http://sealiesoftware.com/blog/archive/2009/04/14/objc_explain_Classes_and_metaclasses.html)。这就需要两个符号：一个给类，一个给元类。当你只是单纯使用一个类而不去继承它时，你就不需要那个元类指针。）

[Sealie Software](http://sealiesoftware.com/index.html)
