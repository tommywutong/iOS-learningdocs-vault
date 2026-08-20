---
title: 撤销架构
apple_id: 10000010i
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2011-06-03'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/UndoArchitecture/Articles/AppKitUndo.html
archived_at: '2026-07-15T07:20:57.822476Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [撤销架构](Introduction%20to%20Undo%20Architecture.md)


[下一页](Using%20Undo%20on%20iPhone.md)[上一页](Using%20Undo%20Notifications.md)

# 在基于 AppKit 的应用程序中使用撤销

Application Kit 从几个方面补充了 [NSUndoManager](https://developer.apple.com/documentation/foundation/undomanager) 的行为：

- 它为文本提供了默认的撤销和重做行为。
- 它包含用于管理动作名称的 API，这些名称会与应用程序菜单中的“撤销”和“重做”一起显示。
- 它建立了一套在应用程序中分发和选取撤销管理器的机制。

一个应用程序可以有一个或多个撤销客户端——即在各自的局部上下文中注册和执行撤销操作的对象。这些对象各自拥有自己的 `NSUndoManager` 对象以及与之关联的撤销栈和重做栈。这种情形的一个例子是自定义视图，每个视图都是某个撤销管理器的客户端。举例来说，你可以有一个包含两个自定义视图的窗口；每个视图都能以可变的[属性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectModeling.html#//apple_ref/doc/uid/TP40008195-CH41)（如字体、颜色和字号）显示文本，而用户可以撤销（或重做）任一视图中对任一属性的每一次改动。`NSResponder` 和 `NSWindow` 定义了一些方法，帮助你在视图层级中控制撤销操作的上下文。

`NSResponder` 为大多数继承自它的对象（也就是窗口和视图）声明了 `undoManager` 方法。当应用程序的第一响应者（first responder）收到 `undo` 或 `redo` 消息时，`NSResponder` 会沿响应者链向上查找，寻找一个能从 `undoManager` 返回 `NSUndoManager` 对象的下一个响应者。凡是返回的撤销管理器都会被用于该撤销或重做操作。

如果 `undoManager` 消息一路沿响应者链向上传到了窗口，`NSWindow` 对象会用 `windowWillReturnUndoManager:` 询问它的[委托](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)，看委托是否有撤销管理器。如果委托没有实现这个方法，窗口就会为自己以及它的所有视图创建一个 `NSUndoManager` 对象。

基于文档的应用程序常常把自己的 `NSDocument` 对象作为窗口的委托，并让它响应 `windowWillReturnUndoManager:` 消息，返回该文档所使用的撤销管理器。这类应用程序也可以把每个 `NSWindowController` 对象作为其窗口的委托——窗口控制器实现 `windowWillReturnUndoManager:`，从它的文档那里取得撤销管理器并返回：

```objc
return [[self document] undoManager];
```


`NSTextView` 的实例提供了撤销和重做行为。这是一个可选特性，你必须确保在创建文本视图时，要么在 Interface Builder 中勾选了相应的复选框，要么向它发送了参数为 `YES` 的 `setAllowsUndo:`。如果你希望某个文本视图使用它自己的撤销管理器（而不是窗口的），就为该文本视图提供一个[委托](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)；委托随后可以在 `undoManagerForTextView:` 委托方法中返回一个 `NSUndoManager` 实例。

只要文本字段或单元格是第一响应者（也就是键盘动作的焦点所在），默认的撤销和重做行为就会作用于文本字段和单元格中的文本。一旦插入点离开了该字段或单元格，之前的操作就无法再撤销了。

如果你使用文档架构，撤销处理的某些方面会自动完成。默认情况下，每个 `NSDocument` 对象都有一个 `NSUndoManager` 对象。（如果你不想让应用程序支持撤销，可以用 `NSDocument` 的 `setHasUndoManager:` 方法阻止撤销管理器的创建。）如果你需要使用某个子类，或者出于其他原因需要更换文档所用的撤销管理器，可以使用 `setUndoManager:` 方法。

当一个 `NSDocument` 对象拥有 `NSUndoManager` 对象时，文档会通过监听撤销管理器发出的通知来自动保持其已编辑状态是最新的——这些通知会告诉它改动何时被执行、撤销或重做。在这种情况下，你完全不需要直接调用 `NSDocument` 的 `updateChangeCount:` 方法，因为它会在恰当的时机自动被调用。

关于在基于文档的应用程序中支持撤销，最需要记住的一点是：所有影响文档持久化状态的改动都必须是可撤销的。在多级撤销架构下，这一点非常重要。如果有可能对文档做出某些无法撤销的改动，那么 `NSUndoManager` 为该文档维护的编辑链就可能与文档的实际状态不一致。例如，设想你有一个绘图程序，它能撤销缩放但不能撤销删除。如果用户选中一个图形并将其缩放，`NSUndoManager` 会得到一个能撤销该缩放操作的调用。接着用户删除了这个图形（这一步没有被记录以供撤销）。此时如果用户尝试撤销，那么（至少）什么都不会发生，因为被缩放的那个图形已经不存在了，撤销缩放不可能产生任何视觉效果。最糟的情况是，应用程序可能因为试图向一个已释放的对象发送消息而崩溃。所以在实现撤销时，请记住：一切会导致文档发生改动的操作都应该是可撤销的。

支持撤销最重要的代码应该位于你的模型层。应用程序中的每个模型对象都应该能够为所有会改变该对象的原始（primitive）方法注册撤销调用。

把模型对象的 API 划分为原始方法和扩展方法往往很有用。这类划分的例子在 Foundation 框架中随处可见（包括 `NSString`、`NSArray` 和 `NSDictionary`），Sketch 示例工程中也有。如果你的模型对象采用了这样的划分，请记住只有原始方法才应该注册撤销，因为按定义，扩展方法就是用原始方法实现的。

某些场景下你可能需要为特定动作临时挂起撤销注册。例如，Sketch 应用程序允许用户抓住缩放手柄并拖动来缩放图形。在这个拖动过程中，被选中图形的边界矩形可能会被改动成百上千次。改变图形的边界是一个原始操作，正常情况下会导致一次撤销注册。但在用户正在主动缩放的过程中，最好不要产生这成千上万次撤销注册。这类情况下，你的模型对象可以提供 API，用于临时挂起和恢复它的部分或全部撤销注册。具体如何处理由你决定。当然，即使真的产生了那成千上万次撤销注册，功能上也是可行的，但既然你永远不需要恢复到那些中间状态，却要记住所有这些中间矩形，就会造成巨大的内存浪费。

尽管撤销支持中最重要的部分应该在模型层，但有两种情况下你需要在控制器对象或视图对象中编写一些与撤销相关的代码。第一种情况是你希望“撤销”和“重做”菜单项拥有更具体的标题。你可以用 `NSUndoManager` 的 `setActionName:` 方法为当前撤销组指定名称。一个事件周期内最后一次调用 `setActionName:` 才是生效的那次。这些名称应该反映用户动作的意图，而不是该动作最终引发的原始操作。因此，你应该在自己的动作方法中设置动作名称。

给撤销组命名并非绝对必要。菜单项只会显示“撤销”和“重做”，不会具体说明要撤销或重做什么。但当你确实注册了名称时，它能帮助用户了解将要被撤销或重做的内容。在视图或控制器的动作消息里零星加上几处 `setActionName:` 调用并不算难，所以建议你尽量给出有意义的动作名称。

第二种可能需要在控制器层或视图层编写撤销代码的情况是：有些改动并不影响文档的实际状态，但仍然需要可撤销。撤销选择状态的改变常常就属于这种情况。例如，Sketch 应用程序可能并不把选择状态视为文档的一部分。事实上，如果一个文档可以打开多个视图，你可能在每个视图中都有不同的选择状态。不过，为了方便用户、也为了用户真正执行撤销时的视觉连贯性，你可能希望选择状态的改变也能被撤销。在这种情况下，显示图形的那个视图可以自己跟踪选择状态，并在选择状态改变时注册撤销调用。

在一个文档对象的生命周期中，控制器对象和视图对象可能会不断产生和消失，当控制器层或视图层的事件需要可撤销时，就必须考虑这一点。你的模型对象通常与文档同寿，而文档又拥有撤销管理器，所以一般不必担心模型消失后会发生什么。但你可能需要担心控制器对象和视图对象消失后会发生什么。如果你的控制器或视图对象注册了任何撤销调用，就应该确保在该控制器或视图被释放时，这些调用会从撤销管理器中被清除。为此你可以使用 `NSUndoManager` 的 `removeAllActionsWithTarget:` 方法。一旦文档上的某个视图被关闭，再为该视图保留诸如选择状态改变之类的撤销信息就没有意义了。

[下一页](Using%20Undo%20on%20iPhone.md)[上一页](Using%20Undo%20Notifications.md)

