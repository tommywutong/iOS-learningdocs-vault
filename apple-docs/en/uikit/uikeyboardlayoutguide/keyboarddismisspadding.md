---
title: keyboardDismissPadding
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uikeyboardlayoutguide/keyboarddismisspadding
source_url: 'https://developer.apple.com/documentation/uikit/uikeyboardlayoutguide/keyboarddismisspadding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uikeyboardlayoutguide/keyboarddismisspadding.json'
content_hash: 'sha256:ecdce663aa46c544'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIKeyboardLayoutGuide](../uikeyboardlayoutguide.md)

# keyboardDismissPadding

<sub>Instance Property</sub>

A value that adds padding above the keyboard to increase the size of the touch area for the scrolling dismissal gesture.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var keyboardDismissPadding: CGFloat { get set }
```

## Discussion

Defaults to `0`. The system treats negative values as `0`.
