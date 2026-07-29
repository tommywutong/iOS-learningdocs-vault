---
title: '适配器接口在 Objective-C 中通过分类实现。 | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/05/adapter-interfaces-in-objective-c-using.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:c41fc4be79894981'
translated: true
---

> 原文：[Adapter interfaces in Objective-C, using categories. | Cocoa with Love](https://www.cocoawithlove.com/2008/05/adapter-interfaces-in-objective-c-using.html)　·　Cocoa with Love (Matt Gallagher)

Objective-C 的分类（Category）特性让程序员在编译之后还能为类添加额外的方法集，这在大多数编译型语言中是无法做到的。利用这一特性，这里呈现经典适配器（Adapter）设计模式的一个 Objective-C 变体，它让两个类可以紧密协作，而不会产生双向耦合依赖问题。

## 连接两个类：简单版本

本文讨论的是如何让两个（或多个）类协同工作。传统的做法如下：

1. 用一组给定的方法实现「类 A」
2. 实现「类 B」，调用「类 A」已提供的方法

显然，这正是几乎所有类交互的工作方式。并且这种方法效果很好，尤其是在「类 B」依赖「类 A」，而「类 A」保持独立的情况下。

## 紧密协作会产生问题

当两个类需要紧密协作时，保持它们接口和操作的干净清晰就会变得困难。

### 当第二个类需要第一个类没有提供的信息时，我们能做什么？

我们可以持续为「类 A」添加方法，为「类 B」提供所需的一切，但将两个类耦合在一起（纯粹为了另一个类而给一个类添加额外的设计特性）通常被认为不利于维护。

如果额外方法在更通用的意义上是有用的，那就没有问题；但如果这些额外方法只对「类 B」有用，那么我们就真的打破了两个类之间的抽象，因为「类 A」现在知道了「类 B」内部需要的一切。因此，类的非层次耦合通常被认为是一种反面模式（anti-pattern）（即不良的设计选择）。

### 如何优雅地执行需要两个类内部数据的计算？

如果我们要执行一个聚合计算，其中部分计算需要在两个类各自内部完成，那么该算法可能会因为分散在多个模块中而难以阅读和维护。

我们可以创建第三个类或模块，在统一的地方执行计算，但这可能会产生上一节中描述的相同耦合问题：第三方类现在需要针对「类 A」和「类 B」定制专门的接口，才能访问其工作所需的数据。

## 使用分类的解决方案

在大多数情况下，Objective-C 的分类用于在单独的库中为某个类定义额外的方法——当类的原始方法集无法更改时。分类也可以用于根据关注点（areas of concern）来拆分一个类。这正是我们在此解决方案中使用它的方式：通过根据关注点划分类，来打破类之间的耦合问题。

我们的问题包含以下约束：

1. 「类 B」需要来自「类 A」的一些详细信息
2. 「类 A」不应该去关心「类 B」在做什么

我们可以通过在「类 B」的源文件中创建额外的「类 A」方法来解决这个问题。具体来说，我们在「类 B」的源文件中创建一个「类 A」的分类。

这使得「类 A」的源文件可以保持独立于「类 B」，同时仍然允许「类 B」获取为其量身定制的信息。结果是，「类 A」源文件中的方法是任何类都可以使用的公开「类 A」方法，而「类 B」则定义了自己的私有接口——如此私密，以至于基础的「类 A」定义完全不知晓它的存在。这也允许原本可能分散在两个类中的计算完全在一个源文件中完成，从而保证整洁和清晰。

本文标题中提到的适配器（Adapter）接口指的是适配器设计模式。通常，适配器是一个第三方类，用于连接两个不兼容的类。在本例中，Objective-C 的分类让我们能够将适配器接口创建为「类 A」的扩展（extension），但位于「类 B」的实现文件内。

## 总结

适配器接口的结构如下。

类 A 的实现：

```objc
@implementation Class_A
// Class_A 的方法
@end
```

类 B 的实现：

```objc
@ implementation Class_A (Class_B_Adapter)
// 允许 Class_B 连接 Class_A 的方法
// Class_B 可以用来计算同时依赖 Class_A 和 Class_B
//   的值的方法
@end

@ implementation Class_B
// Class_B 的方法
@end
```

请注意，这些是「实现」文件，而不是「接口」文件。由于这是「类 B」与「类 A」交互的私有接口，`Class_A (ClassBAdapter)` 不应出现在接口文件中。

这种设计允许「类 B」与「类 A」紧密协作，而无需强制改变「类 A」的默认实现来仅仅迎合「类 B」，并且进一步允许 `ClassBAdapter` 方法的实现与其使用位置相邻。
