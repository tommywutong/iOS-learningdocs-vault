---
title: window
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipress/window
source_url: 'https://developer.apple.com/documentation/uikit/uipress/window'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipress/window.json'
content_hash: 'sha256:1f58248398d5e224'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPress](../uipress.md)

# window

<sub>Instance Property</sub>

The window in which the press initially occurred.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var window: UIWindow? { get }
```

## Discussion

The value of this property is the window in which the press originally occurred. This object might not be the window in which the press is currently located.
