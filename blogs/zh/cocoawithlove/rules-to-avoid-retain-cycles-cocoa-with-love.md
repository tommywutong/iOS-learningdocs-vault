---
title: '避免保留循环的规则 | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2009/07/rules-to-avoid-retain-cycles.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:652643d39e7a57fd'
translated: true
---

> 原文：[Rules to avoid retain cycles | Cocoa with Love](https://www.cocoawithlove.com/2009/07/rules-to-avoid-retain-cycles.html)　·　Cocoa with Love (Matt Gallagher)

在 Objective-C 中，通常情况下，只要你遵循以下基本规则——为所有你需要持有的对象保持正的保留计数，并在使用完成后释放——内存管理就会“正常工作”——直到你创建了一个保留循环，突然循环中的所有对象都永远不会被释放。在这篇文章中，我将解释保留循环、它们发生的常见情况以及这些问题的解决方案。

## 内存管理

计算机程序中的所有内存必须在被使用之前分配，如果你稍后想将该内存用于其他目的，则必须在用完后解除分配。

在垃圾回收环境中，程序员不需要自己处理分配和解除分配；分配、保留、释放和解除分配是自动处理的——但这些步骤仍然会发生。不幸的是，这种自动工作会消耗大量 CPU 和内存；垃圾回收比手动内存管理更慢，占用更多内存。

因此，在 iPhone 和对性能要求苛刻的 Mac OS X 应用程序中，我们仍然需要自己处理内存管理，这意味着要系统地遵循 Objective-C 内存管理的规则：

1. 如果你想“拥有”一个对象，你必须 `alloc`、`copy` 或 `retain` 它。
2. 当你对一个对象操作完成后，总是要 `release` 或 `autorelease` 它。

不幸的是，如果发生保留循环，这些规则不足以确保内存被正确释放。

## 对象层级结构与保留循环

要快速解释保留循环，我需要先简要总结一下对象层级结构是如何关联在一起的。具体来说：在层级结构中，对象沿着层级链被创建、拥有和释放。

![](https://www.cocoawithlove.com/assets/objc-era/retaincycle1.png)

在这个例子中，“某个对象”拥有 Parent，而 Parent 又拥有 Child。

当不再需要该层级结构时，“某个对象”向 Parent 发送 `release`。Parent 的 `retainCount` 降至零，导致其 `dealloc` 方法运行。在其 `dealloc` 方法中，它向 Child 发送 `release`，从而成功释放该链。这是*正确*的行为。

当 Child 出于任何原因需要一个指向 Parent 的指针，并且它选择保留 Parent 时，就会出现保留循环的问题。这将图表修改为如下所示：

![](https://www.cocoawithlove.com/assets/objc-era/retaincycle2.png)

在这个图表中，当“某个对象”向 Parent 发送 `release` 时，`retainCount` 并没有降到零（因为 Child 对 Parent 的保留已经增加了 Parent 自己的 `retainCount`）。由于 Parent 的 `retainCount` 没有降到零，其 `dealloc` 方法永远不会被调用，因此它也永远不会向 Child 发送 `release`。

这就是一个保留循环：Parent 保留 Child，Child 又保留 Parent，它们继续存在，与程序中的其他对象隔绝，但却保持彼此存活。它们泄露了。

## 避免保留循环的规则#1：对象绝不能保留其父对象

避免保留循环的第一条规则是，对象绝不能保留其父对象。这将前面的图表修改为如下所示：

![](https://www.cocoawithlove.com/assets/objc-era/retaincycle3.png)

这是一个简单的情况：对象在创建指向父对象的指针时，绝不应保留该父对象。

请注意，这里使用了术语“弱指针（weak pointer）”。弱指针是指不会保留其目标的指针。

当然，既然子对象不再保留父对象，子对象必须意识到父对象变得无效（被释放）的任何情况，并在那种情况下不使用指向父对象的指针。

因此，要么：

- 当关系中断时，父对象必须将子对象中的 `parent` 指针设置为 `nil`。
- 设计必须保证在子对象的生命周期内父指针始终有效（或者，如果父对象使用 `autorelease` 来释放子对象，则在子对象的 `dealloc` 方法之外，父指针始终有效）。

这两个选项通常适用于弱指针：一旦目标变得无效，必须将指针设置为 `nil`，或者设计必须以其他方式防止无效使用。

一般来说，设置为 `nil` 的选项要安全得多。唯一的缺点是，它需要一种方法来检测目标即将被释放，并指定一个对象，其职责是进行检测并相应更新指针。在父对象（弱指针的目标）知道子对象并且也是子对象的层级结构管理者的情况下，这很容易实现，但并非所有的保留循环都像这样一对一。

## 避免保留循环的规则#2：不能保留任何层级结构祖先

这可能看起来显而易见，但这正是保留循环可能变得微妙的地方：对象不得保留其父对象的任何父对象，或它们的任何父对象。

![](https://www.cocoawithlove.com/assets/objc-era/retaincycle4.png)

此规则适用于许多不同的情况。在 Cocoa 中一些重要的考虑因素：

- 如果一个对象保留了一个 `NSArray`、`NSDictionary` 或 `NSSet`，那么该集合不得保留该对象或其任何父对象。
- 如果一个对象保留了一个 `NSInvocation`，而其中一个参数是该对象或其祖先之一，那么该 `NSInvocation` 不得保留其参数。

如果你想要存储一个可能包含一个或多个父对象的对象集合，你可能需要考虑一种能够处理非保留指针的集合（“弱”集合）：

- 使用 `NULL` 作为回调结构的 `CFArray`、`CFDictionary` 或 `CFSet`。例如：`CFArrayCreateMutable(NULL, 0, NULL);`。
- `+[NSPointerArray pointerArrayWithWeakObjects]`（仅限 Mac OS X）
- `+[NSMapTable mapTableWithWeakToWeakObjects]`（仅限 Mac OS X）
- `+[NSMapTable hashTableWithWeakObjects]`（仅限 Mac OS X）

在极少数情况下，你必须将一个父对象放入一个保留其内容的集合（如 `NSArray`）中，你可以将内容包装在一个非保留对象 `NSValue` 中。例如：

```objc
[arrayOfParents addObject:[NSValue valueWithNonretainedObject:aParent]];
```

尽管对直接祖先有这样的非保留要求，但保留非直接祖先是可以的。然而，一旦一个对象保留了一个非直接祖先，它就成为它所保留的对象的直接祖先。

例如，考虑一个父对象的一个子对象保留另一个子对象的情况：

![](https://www.cocoawithlove.com/assets/objc-era/retaincycle5.png)

在“高级”子对象保留另一个子对象之前，它们都是同级别的兄弟对象。一旦一个子对象保留了另一个子对象，它就成为了另一个子对象的直接祖先。现在这个“初级”子对象不能保留其高级兄弟对象，否则会形成一个循环。从这个“初级”子对象回到“高级”子对象的任何连接都必须遵循“弱指针”规则。

如果你有很多兄弟节点，并且希望以复杂的方式连接它们，最好将所有权留给父对象，并使用非保留指针连接所有兄弟节点。

## 避免保留循环的规则#3：“连接”对象不得保留其目标

任何连接到任意目标对象，但不知晓它们之间关系的对象，都不得保留其目标。

连接对象包括：

- 具有 target 和 action 的对象（例如按钮）
- 采用委托（delegate）的对象
- 被观察者（被添加了观察者的对象）

让我们通过查看用户界面中按钮的例子来考虑这一点。按钮将视图层级结构（通过按钮的 `superview`）连接到其 action 的 target（当被点击时，它在 target 上调用 action 方法）。

按钮不得保留其 target。当你考虑到一个连接可能需要指向一个父对象时，原因就变得清晰了：

![](https://www.cocoawithlove.com/assets/objc-era/retaincycle6.png)

此图表模拟了按钮在控制器上调用方法的常见情况。“Parent”是视图控制器，“Child”是包含按钮的视图，“具有连接的对象”是按钮。

显然，如果按钮保留了它的 target，就会形成一个保留循环。

不过，这显然产生了一个管理问题：按钮的控制器必须确保，如果 target 消失，其 target 会被更新（因为按钮对象本身不会注意到）。

维护连接的责任总是落在该对象的拥有者（manager）身上——遵循你的代码设计，你必须决定哪个对象负责管理该连接，并且它必须检测连接何时变得无效，并将其设置为 `nil` 或完全删除该连接。

幸运的是，在大多数情况下，解决方案很简单：target 最终是连接对象的所有者和控制器，因此当 target 被释放时，它只需要正确地释放其子对象，并且连接永远不会在 target 的生命周期之后持续存在。

## 避免保留循环的规则#4：使用“close（关闭）”方法打破循环

如果你有一个难以理清的层级结构，那么保留任何你想要的对象的做法可能更容易，并实现一个“close”方法来解决循环问题。“close”方法是指在对象的主要功能完成后，能够保证发送给该对象的方法。

两个 `NSView` 之间的保留循环就是一个例子。如果你想在两个视图之间创建保留循环，那么请便。你需要记住的只是在每个视图的 `willRemoveSubview:` 方法中断开它们的连接。

`willRemoveSubview:` 的作用是向每个视图发出即将从显示中移除的警告（其主要功能的结束），并且无论保留计数如何，都会发送该方法——因此你可以用它来打破任何可能的保留循环，这样当它的父对象释放它时，该对象可以像平常一样被 `dealloc`。

## 避免保留循环的规则#5：临时保留必须是临时的

在短时间内可以打破上述任何规则——但必须在没有进一步干预的情况下自动“恢复”规则的遵守，例如：当动画或其他触发过程完成时。

这对于预期会临时删除、中断、排序或重新排列层级结构的操作特别有用。你必须记住，如果保留时间过长，这可能会增加内存使用量，因此请谨慎使用此方法。

临时打破规则的一个例子是 `NSURLConnection` 的 `delegate`。默认情况下，`delegate` 不应被保留，因为它是任意连接的目标（参见规则#3）。然而，`NSURLConnection` 对其 `delegate` 的使用会保证自动完成（无论是通过连接完成还是超时），因此这个对象可以安全地保留其 `delegate`。为了在这种情况下表现得更好，`NSURLConnection` 还提供了 `cancel` 方法，它充当了“close（关闭）”的作用，如果需要，可以更早地释放 `delegate`（尽管释放通过运行循环（run loop）推迟；它不是与方法调用同步的）。

## 结论

你可能因为担心使用的对象会消失，而倾向于保留你使用的每个对象。不幸的是，你不能简单地保留所有东西——你必须注意层级结构，并思考你在保留什么以及为什么保留。

我在这里列出了 5 条规则，但如果你想记住一个更简单的信息：一个对象只有在层级结构中层级更高时，才能无限期地保留某个东西。如果你不知道哪个对象层级更高，你必须在保留之前弄清楚。如果没有明确的更高级对象——你应该重新设计，使之存在。
