---
title: frameLayoutGuide
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrollview/framelayoutguide
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/framelayoutguide'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/framelayoutguide.json'
content_hash: 'sha256:54352db2c7330d26'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# frameLayoutGuide

<sub>Instance Property</sub>

The layout guide based on the untransformed frame rectangle of the scroll view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var frameLayoutGuide: UILayoutGuide { get }
```

## Discussion

Use this layout guide when you want to create Auto Layout constraints that explicitly involve the frame rectangle of the scroll view itself, as opposed to its content rectangle.

## See Also

### Getting the layout guides

- [contentLayoutGuide](contentlayoutguide.md) — The layout guide based on the untranslated content rectangle of the scroll view.
