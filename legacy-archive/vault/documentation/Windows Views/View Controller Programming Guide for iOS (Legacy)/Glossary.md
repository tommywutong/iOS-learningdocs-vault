---
title: iOS View Controller 编程指南（旧版）
apple_id: TP40011381
resource_type: Guide
platform: iOS
topic: User Experience
technology: UIKit
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/ViewControllerPGforiOSLegacy/Glossary/Glossary.html
archived_at: '2026-07-18T02:23:49.500892Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [iOS View Controller 编程指南（旧版）](About%20View%20Controllers.md)


[上一页](Document%20Revision%20History.md)

# 术语表

- __container view controller__

  一种协调其他 View Controller 之间交互、以呈现特定类型用户界面的 View Controller。

- __custom view controller__

  你出于在屏幕上显示特定内容这一明确目的而自行定义的 View Controller。

- __detached nib file__

  一种 nib 文件，其中包含某个 View Controller 的视图，但不包含该 View Controller 对象本身。该 View Controller 改为从另一个单独的 nib 文件加载，或以编程方式创建。

- __integrated nib file__

  同时包含 View Controller 及其关联视图的 nib 文件。

- __modal view controller__

  一种以特殊过渡方式呈现在当前 View Controller 之上的 View Controller。模态 View Controller 常用于从用户处收集信息，但也可用于其他用途。

- __More view controller__

  系统提供的一种 View Controller，用于管理 tab bar 界面中额外标签页的呈现。仅当标签数量超过屏幕上能同时显示的数量时，才会显示该 View Controller。

- __navigation interface__

  navigation controller 的视图所呈现的界面样式。navigation 界面在屏幕顶部包含一个导航栏，便于在不同屏幕之间导航。

- __navigation stack__

  当前由某个 navigation controller 管理的 View Controller 列表。栈中的 View Controller 代表 navigation 界面当前正在显示的内容。

- __root view controller__

  navigation 界面中呈现的第一个 View Controller，或 tab bar 界面中与某个标签关联的第一个 View Controller。根 View Controller 充当对应界面的锚点。navigation 或 tab bar 界面中的大多数 View Controller 都是动态添加和移除的，而某个界面的根 View Controller 是在初始化时添加的，永远不会被移除。

- __tab bar interface__

  tab bar controller 的视图所呈现的界面样式。tab bar 界面在屏幕底部包含一个或多个标签。点按某个标签会切换当前显示的屏幕内容。

- __view controller__

  一种派生自 [UIViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller) 类的对象。View Controller 负责协调一组视图与这些视图所呈现的自定义数据之间的交互。

[上一页](Document%20Revision%20History.md)

