---
title: Objective-C 面向对象编程
apple_id: TP40005149
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Languages & Utilities
technology: Foundation
published: '2010-11-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/OOP_ObjC/Introduction/Introduction.html
archived_at: '2026-07-15T07:17:21.858374Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md)


[下一页](Why%20Objective-C.md)

# 简介

用面向对象的方式开发应用，可以让程序设计更符合直觉、开发速度更快、更便于修改，也更容易理解。大多数面向对象开发环境至少由三个部分组成：

- 一个对象库
- 一套开发工具
- 一门面向对象编程语言及其支持库

Objective-C 语言是一门为实现精巧的面向对象编程而设计的编程语言。它是标准 ANSI C 语言之上的一组扩展，规模不大，却很强大。这些相对于 C 新增的部分大多借鉴自 Smalltalk——最早的面向对象编程语言之一。Objective-C 的设计目标，是以简单直接的方式赋予 C 完整的面向对象编程能力。

每一门面向对象编程语言、每一个面向对象环境，对于“_面向对象_”究竟意味着什么、对象如何行事、程序该如何组织，都有各自的理解。本文档给出的是 Objective-C 的理解。

如果你从未用面向对象编程开发过应用，本文档可以帮你熟悉面向对象开发。它会讲清楚面向对象设计带来的一些影响，让你体会到编写一个面向对象程序究竟是怎样一种感受。

如果你已经用面向对象环境开发过应用，本文档能帮你理解那些基本概念——想要用好 Objective-C、想要组织好一个使用 Objective-C 的程序，这些概念必不可少。

由于本文档不是讲 C 的，它假定你对这门语言已有一定接触。不过这种接触不必很深入。Objective-C 中的面向对象编程与 ANSI C 中的过程式编程差别足够大，即使你不是经验丰富的 C 程序员，也不会因此举步维艰。

本文档分为以下几章：

- [为什么选择 Objective-C？](Why%20Objective-C.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcnbzfvbuqmznknltc)解释为什么 Objective-C 被选为 Cocoa 框架的开发语言。
- [面向对象编程](Object-Oriented%20Programming.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcnbzfvbuqobnknltc)讨论为什么需要面向对象编程语言，并引入大量术语。这一章会展开面向对象编程技术背后的思路。即便你已经熟悉面向对象编程，也建议读一读本章，以便体会 Objective-C 看待面向对象的视角，以及它对术语的用法。
- [对象模型](The%20Object%20Model.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcnbzfvbuqnjnknlti)描述如何把程序理解成一个个把状态与行为结合在一起的单元——也就是对象。接着解释你如何把这些对象归入某个特定的类、一个类如何从另一个类继承状态与行为，以及对象之间如何互相发送消息。
- [组织程序结构](Structuring%20Programs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcnbzfvbuqnbnknlte)解释如何通过在对象之间建立连接来构思一个面向对象程序的设计。这一章介绍聚合与分解这两种技术——它们把职责分派给不同类型的对象——以及框架在定义那些互相配合的对象库时所起的作用。
- [组织编程任务](Structuring%20the%20Programming%20Task.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcnbzfvbuqnrnknltc)讨论与程序员之间的协作和代码实现有关的项目管理问题。

_[Programming with Objective-C](../Programming%20with%20Objective-C/About%20Objective-C.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjq)_ 描述 Objective-C 编程语言本身。

_[Objective-C Runtime Programming Guide](../Objective-C%20Runtime%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danby)_ 描述如何与 Objective-C 运行时打交道。

_[Objective-C Runtime Reference](https://developer.apple.com/documentation/objectivec/objective_c_runtime)_ 描述 Objective-C 运行时支持库中的数据结构与函数。你的程序可以通过这些接口与 Objective-C 运行时系统交互。例如，你可以添加类或方法，也可以获取已加载类的全部类定义列表。

[下一页](Why%20Objective-C.md)

