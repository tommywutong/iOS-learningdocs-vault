---
title: 为你的 iOS App 选择特定的界面风格
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

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [Appearance customization](appearance-customization.md) · [Supporting Dark Mode in your interface](supporting-dark-mode-in-your-interface.md)

# 为你的 iOS App 选择特定的界面风格

<sub>文章</sub>

当完全支持浅色与深色变体不合适时，为你的视图、视图控制器或 App 采用特定的界面风格。

## 概述

支持浅色与深色外观是良好实践，但你可能有充分理由在 App 中整体或部分退出外观更改。包含用户创建内容的视图应始终反映用户的选择。同样，你可能为打印相关视图选择特定外观，以便它们反映用户在打印页面上看到的内容。

系统假设链接到 iOS 13 或更高版本 SDK 的 App 支持浅色与深色外观。在 iOS 中，你通过把特定的界面风格分配给你的窗口、视图或视图控制器来指定想要的特定外观。你还可以使用 `Info.plist` 键完全禁用深色模式支持。

有关如何支持深色模式的一般信息，参见 [Supporting Dark Mode in your interface](supporting-dark-mode-in-your-interface.md)。

### 为窗口、视图或视图控制器覆盖界面风格

当你的界面无论系统设置如何都必须始终以浅色或深色风格显示时，把相应窗口、视图或视图控制器的 [overrideUserInterfaceStyle](uiview/overrideuserinterfacestyle.md) 属性设为该风格。覆盖界面风格会影响你的界面中的其他对象，如下所示：

- 视图控制器——视图控制器的视图和子视图控制器采用该风格。
- 视图——该视图及其所有子视图采用该风格。
- 窗口——窗口中的所有内容都采用该风格，包括根视图控制器以及在该窗口中显示内容的所有呈现控制器。

下面的代码示例为视图控制器及其所有视图启用浅色外观。

```swift
    override func viewDidLoad() {
        super.viewDidLoad()

        // Always adopt a light interface style.    
        overrideUserInterfaceStyle = .light
    }
```

### 为子视图控制器覆盖界面风格

父视图控制器控制其包含的子视图控制器的外观。要为子视图控制器覆盖界面风格，请使用 [- setOverrideTraitCollection:forChildViewController:](<uiviewcontroller/setoverridetraitcollection(__forchild_).md>) 方法为该视图控制器分配新特性。对于自定呈现，你可以通过把新特性分配给 [UIPresentationController](uipresentationcontroller.md) 对象的 [overrideTraitCollection](uipresentationcontroller/overridetraitcollection.md) 属性，类似地覆盖被呈现视图控制器的界面风格。

### 完全退出深色模式

系统自动把链接到 iOS 13.0 或更高版本 SDK 的任何 App 选择加入浅色与深色外观。如果你需要更多时间来处理 App 的深色模式支持，可以通过在 App 的 `Info.plist` 文件中包含 [UIUserInterfaceStyle](../bundleresources/information-property-list/uiuserinterfacestyle.md) 键（值为 `Light`）来临时退出。把此键设为 `Light` 会导致系统忽略用户的偏好，并始终对你的 App 应用浅色外观。

> [!important] 重要
> 强烈建议支持深色模式。仅在你改进 App 的深色模式支持时，使用 [UIUserInterfaceStyle](../bundleresources/information-property-list/uiuserinterfacestyle.md) 键暂时退出。

## 另请参阅

### 外观支持

- [Choosing a Specific Appearance for Your macOS App](../appkit/choosing-a-specific-appearance-for-your-macos-app.md) — 当完全支持浅色与深色变体不合适时，为你的窗口、视图或 App 采用特定外观。
