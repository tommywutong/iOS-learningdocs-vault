---
title: 撤销架构
apple_id: 10000010i
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2011-06-03'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/UndoArchitecture/Articles/UndoNotifications.html
archived_at: '2026-07-15T07:21:00.821320Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [撤销架构](Introduction%20to%20Undo%20Architecture.md)


[下一页](Using%20Undo%20in%20AppKit-Based%20Applications.md)[上一页](Setting%20Action%20Names.md)

# 使用撤销通知

`NSUndoManager` 会定期发布检查点[通知](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Notification.html#//apple_ref/doc/uid/TP40008195-CH35)，以便同步撤销操作被纳入撤销组的时机。对象有时会因为各种原因延迟执行改动，这意味着它们也可能延迟为这些改动注册撤销操作。由于 `NSUndoManager` 会把单个操作收集成组，它必须确保客户端与这些组的创建保持同步，这样操作才会被记入正确的撤销组。为此，每当撤销管理器打开或关闭一个新的撤销组时（打开顶层组时除外），它都会发布一条 `NSUndoManagerCheckpointNotification`，让观察者能够把各自待处理的撤销操作应用到当前生效的组上。撤销管理器的客户端应该把自己注册为该通知的观察者，并在收到通知时为所有待处理的改动记录撤销操作。

`NSUndoManager` 还会在若干特定时机发布其他一些通知：创建组时、关闭组时，以及撤销和重做操作前后各一次。

[下一页](Using%20Undo%20in%20AppKit-Based%20Applications.md)[上一页](Setting%20Action%20Names.md)

