---
title: Block 编程主题
apple_id: TP40007502
resource_type: Guide
platform: watchOS|iOS|macOS
topic: Languages & Utilities
technology: null
published: '2011-03-08'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Blocks/Articles/bxOverview.html
archived_at: '2026-07-15T07:11:19.252171Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [Block 编程主题](Introduction.md)


[下一页](Declaring%20and%20Creating%20Blocks.md)[上一页](Getting%20Started%20with%20Blocks.md)

# 概念概览

block 对象让你能够在 C 以及 [Objective-C](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectiveC.html#//apple_ref/doc/uid/TP40008195-CH43)、C++ 这类从 C 派生出来的语言中，以表达式的形式创建一段临时的函数体。在其他语言和环境里，block 对象有时也被称为“闭包（closure）”。在本文中，除非可能与 C 语言中“代码块”这一标准术语产生混淆，一般都俗称它们为“block”。

一个 block 是一段匿名的内联代码集合，它具有以下特点：

- 像函数一样拥有带类型的参数列表
- 拥有推断出来的或者显式声明的返回类型
- 能够捕获其定义所在的词法作用域（lexical scope）中的状态
- 可以选择性地修改该词法作用域中的状态
- 可以与同一词法作用域中定义的其他 block 共享这种修改能力
- 即使词法作用域（栈帧）已经被销毁，仍然可以继续共享并修改在该词法作用域（栈帧）中定义的状态

你可以拷贝一个 block，甚至把它传给其他线程以延后执行（或者在它自己的线程内传给某个运行循环）。编译器和运行时会做好安排，让 block 中引用到的所有变量在该 block 的所有副本的生命周期内都保持有效。虽然纯 C 和 C++ 中也能使用 block，但一个 block 同时也永远是一个 Objective-C 对象。

block 通常代表小而自成一体的代码片段。因此，它们特别适合用来封装那些可能被并发执行、需要作用于集合中各个元素、或者要在另一项操作完成后作为回调（callback）执行的工作单元。

相比传统的回调函数，block 是一种很有用的替代方案，主要有两个原因：

1. 它们让你可以在调用点处编写代码，而这段代码稍后会在方法实现的上下文中执行。

   因此 block 常常作为框架方法的参数出现。
2. 它们允许访问局部变量。

   传统回调需要一个数据结构来承载执行操作所需的全部上下文信息，而使用 block 时你只需直接访问局部变量即可。

[下一页](Declaring%20and%20Creating%20Blocks.md)[上一页](Getting%20Started%20with%20Blocks.md)

