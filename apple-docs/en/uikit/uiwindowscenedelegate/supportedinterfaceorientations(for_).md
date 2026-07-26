---
title: 'supportedInterfaceOrientations(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, swift, swift, occ, occ, occ]
beta: true
deprecated: false
doc_path: '/documentation/uikit/uiwindowscenedelegate/supportedinterfaceorientations(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscenedelegate/supportedinterfaceorientations(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscenedelegate/supportedinterfaceorientations%28for%3A%29.json'
content_hash: 'sha256:c974dbf13ee21b77'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindowSceneDelegate](../uiwindowscenedelegate.md)

# supportedInterfaceOrientations(for:)

<sub>Instance Method</sub>

Returns the interface orientations supported by the window scene. The returned value replaces the app’s UISupportedInterfaceOrientations Info.plist value for this scene. If not implemented, the Info.plist value is used.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func supportedInterfaceOrientations(for windowScene: UIWindowScene) -> UIInterfaceOrientationMask
```
