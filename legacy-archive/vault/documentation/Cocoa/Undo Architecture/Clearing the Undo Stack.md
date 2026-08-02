---
title: 撤销架构
apple_id: 10000010i
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2011-06-03'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/UndoArchitecture/Articles/CleaningUndoStack.html
archived_at: '2026-07-15T07:20:58.309407Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [撤销架构](Introduction%20to%20Undo%20Architecture.md)


[下一页](Setting%20Action%20Names.md)[上一页](Performing%20Undo%20and%20Redo.md)

# 清空撤销栈

如果你在引用计数环境中使用撤销管理器，就必须小心处理与[内存管理](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MemoryManagement.html#//apple_ref/doc/uid/TP40008195-CH27)相关的问题。[NSUndoManager](https://developer.apple.com/documentation/foundation/undomanager) 对象不会保留（retain）撤销操作的目标。客户端——即执行撤销操作的那个对象——通常拥有撤销管理器，所以如果撤销管理器反过来又保留它的目标，就会频繁地造成保留循环。但这也意味着，撤销管理器有可能持有一个已经被释放的对象的引用。如果目标对象已被释放，而撤销消息又发给了它，就会导致运行时[异常](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ExceptionHandling.html#//apple_ref/doc/uid/TP40008195-CH18)。

为了防范这一点，你必须留意清除那些正在被释放的目标所对应的撤销操作。根据客户端的具体配置方式，通常有以下三种做法：

- 客户端是撤销管理器的唯一拥有者，同时也是所有撤销操作的目标。

  在这种情况下，客户端只需在它的 [dealloc](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/instm/NSObject/dealloc) 方法中释放撤销管理器即可。
- 客户端与其他客户端共用撤销管理器。

  为处理这种情况，客户端应该在它的 `dealloc` 方法中释放撤销管理器之前，先向撤销管理器发送 [removeAllActionsWithTarget:](https://developer.apple.com/documentation/foundation/undomanager/1409896-removeallactions)（并把 `self` 作为参数传入）。
- 客户端为自身之外的其他对象注册了撤销操作。

  此时，要么客户端必须监视其他对象何时被释放，以便发送 `removeAllActionsWithTarget:`；要么这些对象必须在自己被释放时自行发送该消息（这要求它们持有撤销管理器的引用）。使用基于调用的撤销时，很可能需要这么做。

在更一般的意义上，有时清除所有撤销和重做操作是合理的。例如，某些应用程序可能希望在保存文档时这么做。为此，`NSUndoManager` 定义了 [removeAllActions](https://developer.apple.com/documentation/foundation/nsundomanager/1407442-removeallactions) 方法，它会把两个栈都清空。

[下一页](Setting%20Action%20Names.md)[上一页](Performing%20Undo%20and%20Redo.md)

