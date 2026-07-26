---
title: 'preferredWindowingControlStyle(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiwindowscenedelegate/preferredwindowingcontrolstyle(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscenedelegate/preferredwindowingcontrolstyle(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscenedelegate/preferredwindowingcontrolstyle%28for%3A%29.json'
content_hash: 'sha256:3f112bfc718579d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindowSceneDelegate](../uiwindowscenedelegate.md)

# preferredWindowingControlStyle(for:)

<sub>Instance Method</sub>

Called by the system to determine the windowing control style for the provided scene. `automaticStyle` will be used if this method is not implemented.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func preferredWindowingControlStyle(for windowScene: UIWindowScene) -> UIWindowScene.WindowingControlStyle
```
