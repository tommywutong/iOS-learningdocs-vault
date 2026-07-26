---
title: '[objc explain]：类与元类'
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2009/04/14/objc_explain_Classes_and_metaclasses.html'
original_language: en
published: 2009-04-14
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:ea97b01aefaeb850'
translated: true
---

> 原文：[[objc explain]：类与元类](http://sealiesoftware.com/blog/archive/2009/04/14/objc_explain_Classes_and_metaclasses.html)　·　Hamster Emporium (Greg Parker)

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

\<\< [[objc explain]：单态派发](http://sealiesoftware.com/blog/archive/2009/05/14/objc_explain_Monomorphic_dispatch.html) | [归档](http://sealiesoftware.com/blog/archive/index.html) | [[objc explain]：非脆弱 ivar](http://sealiesoftware.com/blog/archive/2009/01/27/objc_explain_Non-fragile_ivars.html) \>\>

[![(链接)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2009/04/14/objc_explain_Classes_and_metaclasses.html)

**[objc explain]：类与元类** ([2009-04-14 08:35 PM](http://sealiesoftware.com/blog/archive/2009/04/14/objc_explain_Classes_and_metaclasses.html))

Objective-C 是一个基于类的对象系统。每个对象都是某个类的实例；对象的 `isa` 指针指向它的类。这个类描述了对象的数据：分配大小、ivar 的类型与布局。这个类还描述了对象的行为：它能响应的选择器、以及它实现的实例方法。

类的方法列表就是一组实例方法，也就是该对象能响应的那些选择器。当你向一个实例发送消息时，`objc_msgSend()` 会在该对象所属类（及其所有超类，如果有的话）的方法列表里查找，来决定该调用哪个方法。

每一个 Objective-C 类本身也是一个对象。它有一个 `isa` 指针和其他数据，也能响应选择器。当你调用一个"类方法"，比如 `[NSObject
	alloc]`，你实际上是在给那个类对象发消息。

[![](http://sealiesoftware.com/blog/class diagram.pdf)](http://sealiesoftware.com/blog/class diagram.pdf) 既然一个类是一个对象，它就必然是另一个类的实例：元类。元类是对类对象的描述，就好比类是对普通实例的描述一样。具体来说，元类的方法列表就是类方法，也就是那个类对象能响应的选择器。当你向一个类——也就是某个元类的一个实例——发送消息时，`objc_msgSend()` 会在元类（及其超类，如果有的话）的方法列表里查找，来决定该调用哪个方法。类方法是由元类代表类对象来描述的，正如实例方法是由类代表实例对象来描述的一样。

那元类本身又是怎么回事？难道是元类套元类，一路无穷下去？不是的。一个元类是根类的元类的实例；而根元类本身就是根元类的一个实例。`isa` 链条在这里形成了一个循环：实例指向类，类指向元类，元类指向根元类，根元类再指向它自己。元类的 `isa` 指针的行为很少会有实际意义，因为在现实世界里，几乎没有人会给元类对象发消息。

更重要的是元类的超类。元类的超类链条与类的超类链条是平行的，所以类方法会随着实例方法一起平行地被继承下去。而且根元类的超类就是根类本身，因此每个类对象都能响应根类的实例方法。归根结底，一个类对象就是（根类的某个子类的）一个实例，和其他任何对象没什么两样。

搞晕了？看看图示可能会有帮助。请记住，当一个消息被发送给任意对象时，方法查找是从该对象的 `isa` 指针开始的，然后沿着超类链条一路向上。"实例方法"是由类来定义的，而"类方法"则是由元类，加上那个根（非元）类共同来定义的。

在正统的计算机科学语言理论里，类和元类的层级结构本可以更自由，可以有更深的元类链条，也可以有多个类由同一个元类实例化而来。Objective-C 出于类方法这类实际目的而使用了元类，但在其他方面则倾向于把元类藏起来。举个例子，`[NSObject class]` 和 `[NSObject self]` 是完全一样的，尽管从形式上讲，它本该返回 `NSObject->isa` 所指向的那个元类。Objective-C 语言是一系列务实的折中方案；在这里，它把类的模式限定住了，免得它变得太……嗯，太*元*了。

[Sealie Software](http://sealiesoftware.com/index.html)
