---
title: 撤销架构
apple_id: 10000010i
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2011-06-03'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/UndoArchitecture/Articles/RegisteringUndo.html
archived_at: '2026-07-15T07:20:59.328595Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [撤销架构](Introduction%20to%20Undo%20Architecture.md)


[下一页](Performing%20Undo%20and%20Redo.md)[上一页](Undo%20Manager.md)

# 注册撤销操作

本文介绍向撤销管理器注册撤销操作的两种方式。

要把一个撤销操作添加到撤销栈中，你必须把它注册到执行该撤销操作的对象上。[NSUndoManager](https://developer.apple.com/documentation/foundation/undomanager) 支持两种注册撤销操作的方式：

- “简单撤销”，基于一个带单个对象参数的简单选择器。

  采用这种方式时，当某个对象发生改变，该对象本身（或代表它行事的另一个对象）会把这次改动注册到撤销管理器，并传入一个保存了该对象改动前[属性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectModeling.html#//apple_ref/doc/uid/TP40008195-CH41)的参数。（这个参数常常是一个 `NSDictionary` 对象，但也可以是任何对象。）执行撤销时，就是用这些属性把对象重置回去。
- “基于调用的撤销”，使用一个 [NSInvocation](https://developer.apple.com/documentation/foundation/nsinvocation) 对象。

  由于这种方式使用调用（invocation）对象，它可以使用参数数量和类型任意的方法。基于调用的撤销适合用来注册特定的状态变更方法，例如 `setWidth:height:` 这样的方法。

在大多数应用程序中，`NSUndoManager` 的单个实例归属于某个包含或管理其他对象的对象。基于文档的桌面应用程序尤其如此，其中每个 `NSDocument` 对象负责一个文档的所有撤销和重做操作。这样的对象通常被称为撤销管理器的客户端。每个客户端对象都有自己的 `NSUndoManager`。客户端声明自己独占修改其可撤销对象的权利，从而可以为所有改动记录撤销操作。就文档这个具体场景而言，这种方案让每一对撤销栈和重做栈彼此独立，因此执行撤销时，它只作用于应用程序中当前聚焦的那个文档（通常是显示在主窗口（key window）中的那一个）。它还免去了文档中各个独立对象必须知道自己的撤销管理器是谁、或者必须自己跟踪自身改动的负担。

不过，发生改变的对象也可以拥有自己的撤销管理器，并执行自己的撤销和重做操作。例如，你可以有一个自定义视图，用来显示被拖入其中的图片；每完成一次拖放操作，它就注册一个新的撤销组。如果这个视图随后被选中（也就是成为第一响应者）并应用了“撤销”命令，之前显示的图片就会重新显示出来。

下面很多代码示例为撤销和重做注册了同一个方法。虽然在撤销和重做只是让一个简单数据值在两个状态之间来回切换时，这种做法很方便，但你并不一定要为撤销和重做注册同一个方法。当被撤销和重做的内容更复杂时——例如在数组中插入和删除对象——你可以交替调用一对方法，其中一个知道如何构建某个状态，另一个知道如何拆解它。当你把一个选择器注册为撤销动作时，一旦用户请求撤销某个上下文中发生的事情，该选择器所标识的方法就会被调用。这个方法不必与注册发生所在的方法是同一个。而且该方法本身也可以注册自己的撤销选择器。要点在于：注册撤销和重做操作时，数据状态和选择器都是可以变化的。

要记录一个简单的撤销操作，你只需调用 [registerUndoWithTarget:selector:object:](https://developer.apple.com/documentation/foundation/nsundomanager/1414001-registerundowithtarget)，给出撤销操作[选择器](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Selector.html#//apple_ref/doc/uid/TP40008195-CH48)要发送给的对象、要调用的选择器，以及随该消息一起传递的参数。目标对象不一定是状态真正发生改变的那个对象；它也可以是客户端对象，即持有许多可撤销对象的文档或容器。参数是一个捕获了对象改动前状态的对象，如下例所示：

```objc
- (void)setMyObjectTitle:(NSString *)newTitle {

    NSString *currentTitle = [myObject title];
    if (newTitle != currentTitle) {
        [undoManager registerUndoWithTarget:self
                selector:@selector(setMyObjectTitle:)
                object:currentTitle];
        [undoManager setActionName:NSLocalizedString(@"Title Change", @"title undo")];
        [myObject setTitle:newTitle];
    }
}
```

在撤销操作中，`setMyObjectTitle:` 会以之前的值被调用。请注意，这又会调用 `registerUndoWithTarget:selector:object:` 方法——这一次传入的是 `myObject` 标题的“新”值。由于撤销管理器正处于撤销的过程中，它会被记录为一个_重做_操作。

对于涉及特定方法、或参数不是对象的其他改动，你可以使用基于调用的撤销，它记录的是一条能够还原目标对象状态的真实消息。与简单撤销一样，你记录的是一条能把对象还原到改动前状态的消息。不过在这种方式下，你是把消息直接发送给撤销管理器，并且事先用一条特殊的消息（[prepareWithInvocationTarget:](https://developer.apple.com/documentation/foundation/nsundomanager/1409564-preparewithinvocationtarget)）告知它目标是谁，如下例所示：

```objc
- (void)setMyObjectWidth:(CGFloat)newWidth height:(CGFloat)newHeight{

    float currentWidth = [myObject size].width;
    float currentHeight = [myObject size].height;
    if ((newWidth != currentWidth) || (newHeight != currentHeight)) {
        [[undoManager prepareWithInvocationTarget:self]
                setMyObjectWidth:currentWidth height:currentHeight];
        [undoManager setActionName:NSLocalizedString(@"Size Change", @"size undo")];
        [myObject setSize:NSMakeSize(newWidth, newHeight)];
    }
}
```

`prepareWithInvocationTarget:` 方法会把传入的参数记录为即将建立的撤销操作的目标。紧接着，你发送那条用于还原目标状态的消息——本例中是 `setMyObjectWidth:height:`。由于 `NSUndoManager` 并不响应这个方法，`forwardInvocation:` 会被调用；`NSUndoManager` 对它的实现会记录下包含目标、[选择器](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Selector.html#//apple_ref/doc/uid/TP40008195-CH48)和所有参数的 [NSInvocation](https://developer.apple.com/documentation/foundation/nsinvocation) 对象。这样，执行撤销的结果就是 _self_ 收到一条带原始值的 `setMyObjectWidth:height:` 消息。

[下一页](Performing%20Undo%20and%20Redo.md)[上一页](Undo%20Manager.md)

