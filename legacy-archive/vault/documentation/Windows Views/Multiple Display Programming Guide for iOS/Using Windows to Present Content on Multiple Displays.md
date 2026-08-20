---
title: iOS 多显示屏编程指南
apple_id: TP40012555
resource_type: Guide
platform: iOS
topic: User Experience
technology: UIKit
published: '2012-12-13'
source_url: https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/WindowAndScreenGuide/Introduction/Introduction.html
archived_at: '2026-07-18T02:24:16.496949Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md)


[下一页](Understanding%20Windows%20and%20Screens.md)

# 使用窗口在多个显示屏上呈现内容

每个 iOS 应用都有一个窗口（window），负责呈现应用的用户界面。尽管窗口提供了至关重要的功能，但大多数应用从不需要访问它。通常只有支持外接显示屏（external display）的应用才需要与窗口打交道。

在 iOS 中，窗口对象容纳应用的视图，并管理它们在设备显示屏上的呈现。窗口所关联的屏幕（screen）对象代表当前正在使用的那块具体设备显示屏。如果你的应用允许用户在外接显示屏上查看内容，你就要创建另一个窗口对象，来管理内容在那块显示屏上的呈现。

### 窗口为你的应用提供重要功能

除了容纳应用的可见内容之外，窗口还参与向你的视图派发触摸事件以及响应方向变化。窗口所关联的屏幕对象提供了当前所用设备显示屏的信息。当你使用 storyboard 定义应用的用户界面时，主 storyboard 会自动为你设置好那个管理设备显示屏内容的窗口。

### 支持外接显示屏需要额外一个窗口

如果你的应用支持外接设备显示屏，你需要创建一个单独的窗口对象来表示要在其上显示的内容。你可以在两块显示屏上显示相同的内容——这个特性叫做_镜像_（mirroring），并且默认就是这样——也可以在每块显示屏上显示不同的内容。

_[App Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007072)_ 描述了 iOS 应用的基础架构，并提供了帮助你开发出优秀应用的编码准则与最佳实践。

_[AirPlay Overview](../../Audio%20Video/AirPlay%20Overview/About%20AirPlay.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytanbv)_ 描述了如何向 iOS 设备提供兼容 AirPlay 的媒体内容。

_[UIWindow Class Reference](https://developer.apple.com/documentation/uikit/uiwindow)_ 描述了 `UIWindow` 类的编程接口。

_[UIScreen Class Reference](https://developer.apple.com/documentation/uikit/uiscreen)_ 描述了 `UIScreen` 类的编程接口。

[下一页](Understanding%20Windows%20and%20Screens.md)

