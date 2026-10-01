---
title: 为你的 iOS App 选择特定的界面样式
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/choosing-a-specific-interface-style-for-your-ios-app
source_url: 'https://developer.apple.com/documentation/uikit/choosing-a-specific-interface-style-for-your-ios-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/choosing-a-specific-interface-style-for-your-ios-app.json'
content_hash: 'sha256:aa78e7d1cf43e732'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [外观自定义](appearance-customization.md) · [在界面中支持深色模式](supporting-dark-mode-in-your-interface.md)

# 为你的 iOS App 选择特定的界面样式

<sub>文章</sub>

当同时支持浅色和深色变体并不合适时，为你的视图、视图控制器或 App 采用特定的界面样式（interface style）。

## 概述

同时支持浅色和深色外观是一种良好实践，但你也可能有充分的理由让你的 App 完全或部分地不参与外观变化。包含用户创建内容的视图应始终反映用户的选择。同样，你可能会为与打印相关的视图选择特定的外观，让它们反映出用户在打印页面上看到的内容。

系统假定链接到 iOS 13 或更高版本 SDK 的 App 同时支持浅色和深色外观。在 iOS 中，你可以通过为窗口、视图或视图控制器指定特定的界面样式来确定你想要的外观。你还可以使用 `Info.plist` 键完全禁用对深色模式（Dark Mode）的支持。

有关如何支持深色模式的一般信息，请参阅[在界面中支持深色模式](supporting-dark-mode-in-your-interface.md)。

### 为窗口、视图或视图控制器覆盖界面样式

当你的界面必须始终以浅色或深色样式显示、不受系统设置影响时，把相应窗口、视图或视图控制器的 [overrideUserInterfaceStyle](uiview/overrideuserinterfacestyle.md) 属性设置为该样式。覆盖界面样式会按以下方式影响你界面中的其他对象：

- 视图控制器——该视图控制器的视图和子视图控制器会采用此样式。
- 视图——该视图及其所有子视图会采用此样式。
- 窗口——窗口中的一切都会采用此样式，包括根视图控制器以及在该窗口中显示内容的所有呈现控制器（presentation controller）。

以下代码示例为一个视图控制器及其所有视图启用浅色外观。

```swift
    override func viewDidLoad() {
        super.viewDidLoad()

        // 始终采用浅色界面样式。
        overrideUserInterfaceStyle = .light
    }
```

### 为子视图控制器覆盖界面样式

父视图控制器控制其所包含的子视图控制器的外观。要覆盖某个子视图控制器的界面样式，请使用 [- setOverrideTraitCollection:forChildViewController:](<uiviewcontroller/setoverridetraitcollection(__forchild_).md>) 方法为该视图控制器指定新的特性（trait）。对于自定义呈现方式，你同样可以通过为你的 [UIPresentationController](uipresentationcontroller.md) 对象的 [overrideTraitCollection](uipresentationcontroller/overridetraitcollection.md) 属性指定新的特性，来覆盖被呈现视图控制器的界面样式。

### 完全退出深色模式

系统会自动让链接到 iOS 13.0 或更高版本 SDK 的 App 同时支持浅色和深色外观。如果你需要额外的时间来完善你的 App 的深色模式支持，可以在你的 App 的 `Info.plist` 文件中加入 [UIUserInterfaceStyle](../bundleresources/information-property-list/uiuserinterfacestyle.md) 键（值为 `Light`）来暂时退出。把这个键设置为 `Light` 会使系统忽略用户的偏好，并始终对你的 App 应用浅色外观。

> [!important] 重要
> 强烈建议支持深色模式。在你改进你的 App 的深色模式支持期间，只应临时使用 [UIUserInterfaceStyle](../bundleresources/information-property-list/uiuserinterfacestyle.md) 键来退出。

## 另请参阅

### 外观支持

- [为你的 macOS App 选择特定外观](../appkit/choosing-a-specific-appearance-for-your-macos-app.md) — 当同时支持浅色和深色变体并不合适时，为你的窗口、视图或 App 采用特定的外观。
