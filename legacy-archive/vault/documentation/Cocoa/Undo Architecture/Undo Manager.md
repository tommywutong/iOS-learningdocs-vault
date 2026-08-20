---
title: 撤销架构
apple_id: 10000010i
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2011-06-03'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/UndoArchitecture/Articles/UndoManager.html
archived_at: '2026-07-15T07:21:00.323615Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [撤销架构](Introduction%20to%20Undo%20Architecture.md)


[下一页](Registering%20Undo%20Operations.md)[上一页](Introduction%20to%20Undo%20Architecture.md)

# 撤销管理器

本文从_概念_层面讲解撤销管理器（undo manager）的基本特性和行为。基于代码的实用示例会在后面的文章中给出。

`NSUndoManager` 是一个通用的撤销栈（undo stack），客户端可以在其中注册回调，以便在需要执行撤销时被调用。当你执行某个改变对象[属性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectModeling.html#//apple_ref/doc/uid/TP40008195-CH41)值的动作时（例如调用某个 set [存取方法](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/AccessorMethod.html#//apple_ref/doc/uid/TP40008195-CH2)），你还可以向撤销管理器注册一个能够反转该动作的操作。

撤销管理器会把发生在单个运行循环（run loop）周期内的所有撤销操作收集在一起，这样执行一次撤销就能还原该周期内发生的全部改动。此外，撤销管理器在执行撤销时会保存被还原的那些操作，使你可以重做这些撤销。

`NSUndoManager` 之所以实现为 Foundation 框架中的一个类，是因为除应用程序之外的可执行文件也可能希望还原自身状态的改动。举例来说，你可能有一个带撤销和重做命令的交互式命令行工具；也可能存在能够“通过网络”还原操作的分布式对象（Distributed Object）实现。不过，用户通常把撤销和重做视为应用程序级别的功能。Application Kit 在它的 `NSTextView` 对象中实现了撤销和重做，并让你可以很方便地在响应者链（responder chain）上的对象中实现该功能。关于 Application Kit 在撤销和重做中扮演的角色，参见[在基于 AppKit 的应用程序中使用撤销](Using%20Undo%20in%20AppKit-Based%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgiytglkdjjbeuqsfjfeq)。

_撤销操作_是指用于还原某个对象上的一次改动的方法，以及还原该改动所需的参数。操作要指明：

- 当请求撤销时接收消息的对象。

  它可以是发生改变的那个对象，也可以是持有发生改变的对象的另一个对象。
- 要发送的消息。
- 随消息一起传递的参数。

  通常你至少需要传递一个参数——也就是原来的值。

由于 `NSUndoManager` 同时支持重做，这些操作通常应该是可反转的。在撤销操作期间被调用的方法本身也应该注册一个撤销操作，这个操作随后就成为重做动作。

撤销操作通常被收集到_撤销组_（undo group）中，一个撤销组代表一次完整的可还原动作，并被存放在栈上。撤销管理器执行撤销或重做时，实际上是在撤销或重做一整组操作。例如，用户可能同时修改了某段文本的字体和字号。应用程序可以把这两次[属性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13)设置操作打包成一个组，这样当用户选择“撤销”时，字体和字号会一起被还原。即便只想撤销一个操作，它也仍然必须被打包在一个组里。

重做操作和重做组其实就是存放在另一个栈（下面会介绍）上的撤销操作。

`NSUndoManager` 通常会在运行循环期间自动创建撤销组。在一次运行循环中，它第一次被要求记录撤销操作时会新建一个组；然后在这次循环结束时关闭该组。你可以用 [beginUndoGrouping](https://developer.apple.com/documentation/foundation/undomanager/1409894-beginundogrouping) 和 [enableUndoRegistration](https://developer.apple.com/documentation/foundation/nsundomanager/1408957-enableundoregistration) 方法在这些默认的组内部创建额外的嵌套撤销组。你也可以用 [setGroupsByEvent:](https://developer.apple.com/documentation/foundation/undomanager/1417407-groupsbyevent) 关闭默认的分组行为。

撤销组存放在一个栈上，最旧的组在栈底，最新的组在栈顶。撤销栈默认是不限长度的，但你可以用 [setLevelsOfUndo:](https://developer.apple.com/documentation/foundation/nsundomanager/1409753-levelsofundo) 方法把它限制为最多容纳若干个组。当栈超出上限时，最旧的撤销组会从栈底被丢弃。

一开始，两个栈都是空的。记录撤销操作会向撤销栈中添加内容，但在执行撤销之前，重做栈始终是空的。执行撤销会把最新一组中的还原操作应用到它们各自的对象上。由于这些操作会改变对象的状态，这些对象想必又会向撤销管理器注册新的操作，只不过这次的方向与原来的操作相反。由于撤销管理器正处于执行撤销的过程中，它会把这些操作作为重做操作记录到重做栈上。连续多次撤销会不断向重做栈中添加内容。之后的重做操作会把这些操作从重做栈上取出、应用到对象上，再把它们压回撤销栈。

只要撤销和重做是接连执行的，重做栈的内容就会一直保留。但是，由于对一个对象施加新的改动会使之前的改动失效，所以一旦有新的撤销操作被注册，已有的重做栈就会被清空。这样可以防止重做把对象恢复到一个不合适的先前状态。你可以用 [canUndo](https://developer.apple.com/documentation/foundation/nsundomanager/1412394-canundo) 和 [canRedo](https://developer.apple.com/documentation/foundation/nsundomanager/1415212-canredo) 方法检查当前是否能够撤销和重做。

[下一页](Registering%20Undo%20Operations.md)[上一页](Introduction%20to%20Undo%20Architecture.md)

