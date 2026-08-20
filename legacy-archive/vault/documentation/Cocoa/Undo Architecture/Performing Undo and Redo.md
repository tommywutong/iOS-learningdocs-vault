---
title: 撤销架构
apple_id: 10000010i
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2011-06-03'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/UndoArchitecture/Articles/PerformingUndo.html
archived_at: '2026-07-15T07:20:58.814647Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [撤销架构](Introduction%20to%20Undo%20Architecture.md)


[下一页](Clearing%20the%20Undo%20Stack.md)[上一页](Registering%20Undo%20Operations.md)

# 执行撤销与重做

执行撤销和重做通常就像向 [NSUndoManager](https://developer.apple.com/documentation/foundation/undomanager) 对象发送 [undo](https://developer.apple.com/documentation/foundation/nsundomanager/1412189-undo) 和 [redo](https://developer.apple.com/documentation/foundation/nsundomanager/1417030-redo) 消息那样简单。`undo` 消息会关闭最后一个尚未关闭的撤销组，然后应用该组中的所有撤销操作（同时把过程中产生的撤销操作记录为重做操作）。`redo` 消息同样会应用最顶层重做组中的所有重做操作。

`undo` 方法用于撤销顶层的组，不应该用于嵌套的撤销组。如果调用 `undo` 时栈上还有未关闭的嵌套撤销组，它会抛出[异常](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ExceptionHandling.html#//apple_ref/doc/uid/TP40008195-CH18)。要撤销嵌套的组，你必须先用 [endUndoGrouping](https://developer.apple.com/documentation/foundation/nsundomanager/1416490-endundogrouping) 消息显式关闭该组，然后用 [undoNestedGroup](https://developer.apple.com/documentation/foundation/nsundomanager/1410826-undonestedgroup) 撤销它。另请注意，如果你用 [setGroupsByEvent:](https://developer.apple.com/documentation/foundation/undomanager/1417407-groupsbyevent) 关闭了按事件自动分组的行为，那么在调用任一撤销方法之前，你必须用 `endUndoGrouping` 显式关闭当前的撤销组。

[下一页](Clearing%20the%20Undo%20Stack.md)[上一页](Registering%20Undo%20Operations.md)

