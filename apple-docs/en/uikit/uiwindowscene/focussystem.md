---
title: focusSystem
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindowscene/focussystem
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene/focussystem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene/focussystem.json'
content_hash: 'sha256:3c44a54aab1b6dc3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindowScene](../uiwindowscene.md)

# focusSystem

<sub>Instance Property</sub>

The focus system that’s responsible for the window scene.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var focusSystem: UIFocusSystem? { get }
```

## Discussion

The value of this property is `nil` if the window scene doesn’t support focus.
