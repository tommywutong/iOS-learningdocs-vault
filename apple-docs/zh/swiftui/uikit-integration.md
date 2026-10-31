---
title: UIKit 集成
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/uikit-integration
source_url: 'https://developer.apple.com/documentation/swiftui/uikit-integration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uikit-integration.json'
content_hash: 'sha256:cbacfc35dccf3bbc'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md)

# UIKit 集成

<sub>API 集合</sub>

向你的 SwiftUI App 添加 UIKit 视图，或在你的 UIKit App 中使用 SwiftUI 视图。

## 概述

使用托管控制器将 SwiftUI 与 App 的现有内容集成，把 SwiftUI 视图添加到 UIKit 界面中。托管控制器将一组 SwiftUI 视图封装成一种形式，然后你可以把它添加到基于 storyboard 的 App 中。

![](../../../attachments/74ee52cce15bcc5332715296b5d568d9/uikit-integration-hero@2x.png)

你还可以向你的 SwiftUI 界面添加 UIKit 视图和视图控制器。可表示对象会包装指定的视图或视图控制器，并促进被包装对象与你的 SwiftUI 视图之间的通信。

有关设计指引，请参阅《人机界面指南》中的以下部分：

- [Designing for iOS](../design/human-interface-guidelines/designing-for-ios.md)
- [Designing for iPadOS](../design/human-interface-guidelines/designing-for-ipados.md)
- [Designing for tvOS](../design/human-interface-guidelines/designing-for-tvos.md)

## 主题

### 在 UIKit 中显示 SwiftUI 视图

- [Using SwiftUI with UIKit](../uikit/using-swiftui-with-uikit.md) — 了解如何将 SwiftUI 视图融入 UIKit App。
- [Unifying your app’s animations](unifying-your-app-s-animations.md) — 在 SwiftUI、UIKit 和 AppKit 中打造一致的 UI 动画体验。
- [UIHostingController](uihostingcontroller.md) — 一个管理 SwiftUI 视图层级结构的 UIKit 视图控制器。
- [UIHostingControllerSizingOptions](uihostingcontrollersizingoptions.md) — 托管控制器跟踪其内容大小的方式选项。
- [UIHostingConfiguration](uihostingconfiguration.md) — 一种适合托管 SwiftUI 视图层级结构的内容配置。
- [UIHostingSceneDelegate](uihostingscenedelegate.md) — 扩展 `UIKit/UISceneDelegate` 以桥接 SwiftUI 场景。

### 将 UIKit 视图添加到 SwiftUI 视图层级结构

- [UIViewRepresentable](uiviewrepresentable.md) — 一个 UIKit 视图的包装器，用于将该视图集成到你的 SwiftUI 视图层级结构中。
- [UIViewRepresentableContext](uiviewrepresentablecontext.md) — 关于系统状态的上下文信息，用于创建和更新你的 UIKit 视图。
- [UIViewControllerRepresentable](uiviewcontrollerrepresentable.md) — 一个表示 UIKit 视图控制器的视图。
- [UIViewControllerRepresentableContext](uiviewcontrollerrepresentablecontext.md) — 关于系统状态的上下文信息，用于创建和更新你的 UIKit 视图控制器。

### 将 UIKit 手势识别器添加到 SwiftUI 视图层级结构

- [UIGestureRecognizerRepresentable](uigesturerecognizerrepresentable.md) — 一个 `UIGestureRecognizer` 的包装器，用于将该手势识别器集成到你的 SwiftUI 层级结构中。
- [UIGestureRecognizerRepresentableContext](uigesturerecognizerrepresentablecontext.md) — 关于系统状态的上下文信息，用于创建和更新被表示的手势识别器。
- [UIGestureRecognizerRepresentableCoordinateSpaceConverter](uigesturerecognizerrepresentablecoordinatespaceconverter.md) — 一个代理结构体，用于在与 [UIGestureRecognizerRepresentable](uigesturerecognizerrepresentable.md) 关联的 SwiftUI 视图层级结构中进行位置与坐标空间之间的相互转换。

### 共享配置信息

- [UITraitBridgedEnvironmentKey](uitraitbridgedenvironmentkey.md)

### 在 UIKit 中托管挂饰

- [UIHostingOrnament](uihostingornament.md) — 表示适合在 UIKit 中托管的挂饰的一个模型。
- [UIOrnament](uiornament.md) — 表示挂饰的抽象基类。

## 另请参阅

### 框架集成

- [AppKit integration](appkit-integration.md) — 向你的 SwiftUI App 添加 AppKit 视图，或在你的 AppKit App 中使用 SwiftUI 视图。
- [WatchKit integration](watchkit-integration.md) — 向你的 SwiftUI App 添加 WatchKit 视图，或在你的 WatchKit App 中使用 SwiftUI 视图。
- [Technology-specific views](technology-specific-views.md) — 使用其他 Apple 框架提供的 SwiftUI 视图。
