---
title: 撤销架构
apple_id: 10000010i
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2011-06-03'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/UndoArchitecture/UndoArchitecture.html
archived_at: '2026-07-15T07:21:01.823036Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md)


[下一页](Undo%20Manager.md)

# 撤销架构简介

本主题介绍如何用 [NSUndoManager](https://developer.apple.com/documentation/foundation/undomanager) 记录操作，使用户能够撤销某个操作产生的效果。撤销（undo）与重做（redo）操作以及 `NSUndoManager` 类在 iOS 和 OS X 上均可使用。

如果你想学习如何在应用程序中使用撤销管理器（undo manager），就应该阅读本文档。

本文档包含以下文章：

- [撤销管理器](Undo%20Manager.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgiydklkdjjbeissdinfa) 从概念上介绍负责记录撤销和重做操作的那个对象。
- [注册撤销操作](Registering%20Undo%20Operations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgiydmlkcifbesq2gircq) 说明如何把操作添加到撤销栈中。
- [执行撤销与重做](Performing%20Undo%20and%20Redo.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgiydolkcijbuesscijba) 说明如何执行撤销和重做操作。
- [清空撤销栈](Clearing%20the%20Undo%20Stack.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgiydqlkcijbuersii5fa) 说明如何从撤销栈中移除操作。
- [设置动作名称](Setting%20Action%20Names.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgiydslkciffeusccjfbq) 说明如何为“撤销”和“重做”菜单项提供自定义名称。
- [在基于 AppKit 的应用程序中使用撤销](Using%20Undo%20in%20AppKit-Based%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgiytglkdjjbeuqsfjfeq) 介绍 Application Kit 对撤销机制的补充。
- [使用撤销通知](Using%20Undo%20Notifications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgiytalkcineuersfi5dq) 说明如何利用通知进行同步。

[下一页](Undo%20Manager.md)

