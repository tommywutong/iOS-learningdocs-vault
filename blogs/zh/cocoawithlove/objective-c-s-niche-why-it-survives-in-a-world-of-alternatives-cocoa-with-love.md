---
title: Objective-C 的利基：它为何能在众多替代语言中存活 | Cocoa with Love
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2009/10/objective-c-niche-why-it-survives-in.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:5f0d3a6a44ac303b'
translated: true
---

> 原文：[Objective-C's niche: why it survives in a world of alternatives | Cocoa with Love](https://www.cocoawithlove.com/2009/10/objective-c-niche-why-it-survives-in.html)　·　Cocoa with Love (Matt Gallagher)

对于许多初次接触 Mac 或 iPhone 平台的程序员来说，Objective-C 始终是一个障碍——在学习 Cocoa 之前，几乎没有人接触过它，这使得新 Cocoa 开发者不得不同时跨越两条学习曲线。Apple 为何最终采用了这样一门奇怪的语言？而对于一家以更换 CPU 架构和整个操作系统而闻名的公司来说，Apple 又为何坚持使用 Objective-C？答案就藏在那些方法之中。

## 虚方法（Virtual Method）

大多数编译型面向对象语言（如 C++、Java 和 C♯）都紧密遵循 [Simula 67](http://en.wikipedia.org/wiki/Simula) 首次引入的面向对象方法，特别是[虚方法](http://en.wikipedia.org/wiki/Virtual_function)的概念以及它们如何让方法可以被重写。

> **源于 Algol：** 就像 Objective-C 常被称为 C 语言的"纯超集"一样，Simula 67 是 [Algol 60](http://en.wikipedia.org/wiki/ALGOL) 的"纯超集"。虽然 [Fortran](http://en.wikipedia.org/wiki/Fortran) 有时被铭记为第一个流行（并遭人嫌弃）的高级语言，但 Algol 60 才是首个真正与现代语言相似的编程语言，它包含了 `for`、`if`/`else`、`while`（某种形式）以及其他现代编程语言中常见的程序结构。尽管 Algol 在 1970 年代之后就很少被使用，但 [Pascal](http://en.wikipedia.org/wiki/Pascal_(programming_language)) 及其后代在语法上与 Algol 非常相似。

在编译型语言中，一个[常规函数](http://en.wikipedia.org/wiki/Subroutine)（不可重写）最终体现为一个基本的内存地址。当函数被调用时，CPU 跳转到该内存地址。

Simula 67 引入了[虚方法表（virtual method table）](http://en.wikipedia.org/wiki/Virtual_table)来使其适应面向对象。方法不再对应基本的内存地址，而是被编译成表中的行号。为了获取内存地址，程序从对象的类中获取方法表，然后 CPU 跳转到指定行号对应的地址。

由于不同对象拥有不同的类，它们的方法表中也会有不同的地址，因而允许子类拥有与基类不同的方法实现，即[方法重写（method overriding）](http://en.wikipedia.org/wiki/Method_overriding)。

## 消息传递（Message Passing）

虽然虚方法表引入了一层间接性，允许方法行为随对象不同而变化，但表中的偏移量以及表本身都必须在编译时确定。

> **消息传递的历史：** 与面向对象本身一样，消息传递也受 Simula 67 启发，但 Simula 的"消息传递"（称为"Simulation"）并非用于方法调用，而是用于离散事件模拟（主要是队列和列表处理）。[Smalltalk](http://en.wikipedia.org/wiki/Smalltalk) 扩展了这一思想，将消息传递用于方法调用。Smalltalk 后来又启发了 [Actor Model](http://en.wikipedia.org/wiki/Actor_model)（用于分布式处理）和[远程过程调用（RPC）](http://en.wikipedia.org/wiki/Remote_procedure_call)。最初，Smalltalk 消息被设想携带大量元数据（更像电子邮件的完整标头），但最终被简化成一种在语法上与 Objective-C 当前实现相似的形式（去掉方括号）。

[消息传递](http://en.wikipedia.org/wiki/Message_passing)提供了解决[方法派发问题（method dispatch problem）](http://en.wikipedia.org/wiki/Dynamic_dispatch)的另一种途径。虚方法使用编译时确定的偏移量和表，这些并不查询对象本身（除了其类型）；而消息传递则将唯一的消息标识符发送给对象本身，由对象在运行时决定采取什么动作。

采用消息传递的方法可能仍然会在类的表示中保留虚方法表（vtable），但该结构在编译时是不可知的——它完全在运行时处理——并且类的实例有机会根据消息采取与虚方法表内容无关的不同动作。

这里有两个重要的区别：

- 运行时解析 —— 因此消息标识符与动作之间的连接可以在运行时更改。
- 对象本身（而不仅仅是其类）的参与。

在技术层面上，虚方法表与传递消息标识符之间的差异相对较小（因为两者本质上都是查表操作，并且实际上都在运行时执行）。差异归根结底在于概念层面：

- 使用虚方法表的语言通常很难或不可能在运行时更改虚方法表的内容或指针。
- 类型安全在使用虚方法表的语言中是至关重要的，因为编译器可能会根据类型改变查表操作，尤其是在多重继承的情况下。在消息传递系统中，类型安全与方法调用无关。

## 为什么这很重要

简短的回答是：Objective-C 中这种动态的消息处理机制，让你能够更容易地在一个自己并未创建的大型框架中工作，因为你可以在运行时即时检查、修补和修改该框架的元素。最常遇到这种情况的场景就是处理[应用程序框架（application framework）](http://en.wikipedia.org/wiki/Application_framework)。

其最大的原因是，你可以在现有对象上添加或修改方法，而无需派生它们的子类（subclass），且这一切都在它们运行过程中进行。实现这一目标的方法包括[分类（Categories）](http://developer.apple.com/mac/library/documentation/Cocoa/Conceptual/ObjectiveC/Articles/ocCategories.html#//apple_ref/doc/uid/TP30001163-CH20-TPXREF141)、[方法调配（method swizzling）](https://www.cocoawithlove.com/2008/03/supersequent-implementation.html)和 isa-swizzling。

这使得以下情况成为可能：

- 你想为其他人的对象添加一个便捷方法（快速搜索一下我自己的文章就会发现，约有十几篇涉及为 Cocoa 类添加便捷方法，例如[通过 URI 安全地获取 NSManagedObject](https://www.cocoawithlove.com/2008/08/safely-fetching-nsmanagedobject-by-uri.html)）。
- 你想要改变一个你没有（也无法）分配的类的行为，因为它是由其他人创建的（这就是 [Cocoa 中实现键值观察（Key-Value Observing）的方式](http://developer.apple.com/mac/library/documentation/Cocoa/Conceptual/KeyValueObserving/Concepts/KVOImplementation.html)）。
- 你想要泛化地处理对象，并通过运行时内省（runtime introspection）处理潜在的差异。
- 你想用一个完全不同的类的对象来替代预期的类（Cocoa 利用 [NSProxy](http://developer.apple.com/mac/library/documentation/Cocoa/Reference/Foundation/Classes/NSProxy_Class/Reference/Reference.html) 实现这一点，将普通对象转变为分布式对象）。

这些观点可能看起来有些平淡，但它们是在使用他人框架时最大化代码复用的核心：如果你需要现有代码以不同的方式工作，你不需要重新实现整个类，也不需要改变它的分配方式。

使用虚方法表的语言也可以采纳其中一些思想（例如 [boost::any](http://www.boost.org/doc/libs/1_40_0/doc/html/boost/any.html) 类或 [C♯ 4.0 的动态成员查找](http://en.wikipedia.org/wiki/C_Sharp_4.0)），但这些功能有额外的限制，并且不适用于所有对象，这意味着它们不能用于完全任意的对象（例如那些你无法控制或并未创建的对象），因此在与别人的框架交互时并无帮助。

简而言之：用动态消息传递替代虚方法调用，使得 Objective-C 成为使用别人编写的大型库或框架时更好用的语言。

## 权衡取舍

动态消息调用的缺点是，只有在消息查找被缓存时它才能达到与虚方法调用相同的速度，否则总是会更慢。

此外，为了保持纯粹动态消息传递系统的哲学，Objective-C 不使用模板或模板元编程，也没有非动态（即非虚）方法。这意味着使用这些技术时可能实现的编译器优化，Objective-C 方法将无法享受到。而且，由于现代 C++ 编程在很大程度上聚焦于这些特性，将采用这些思想的程序移植到 Objective-C 可能会很困难。

理论上，Objective-C 可以实现这些特性，但它们与 Objective-C 中灵活性和动态行为的基本理念相抵触——而且一旦使用，前一节中的所有优势都将消失。

## 结论

我写一个 Objective-C/Cocoa 博客并非巧合，我显然是 Objective-C 和 Cocoa 的拥护者。在我看来，在必须大量使用他人编写的框架（尤其是应用程序框架）的编程场景中，Objective-C 是最佳语言。Objective-C 在这种情况下取得成功，归功于以下两者的结合：

- 速度与精度（源于其编译型 C 的根源）
- 动态灵活性（归功于使用消息传递进行方法调用）

为了框定这一结论，我要说明我曾使用 C/WIN32、C++/PowerPlant、C++/MFC 和 Java/Swing/AWT 编写过大型项目。我也曾涉足使用 C♯/.Net 编写的小型项目。在所有以上案例中，我都发现那些应用程序框架的灵活性和可复用性较差，因为它们缺乏 Objective-C 那样的动态可修改性。

如我所述，我认为 Objective-C 在应用程序框架领域的优势确实是一个利基（niche）（虽然是一个非常庞大的利基）。如果我是在编写编译器、操作系统内核或底层/高性能库，我会使用 C++（我不会使用纯 C，因为我会怀念我的抽象能力）——但这些场景中，元编程、更强的内联以及更快的函数调用会盖过灵活性的考量。当然，如果你的项目需要满足所有这些标准：那么总有 Objective-C++ 可供选择。
