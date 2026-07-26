---
title: contentLayoutGuide
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrollview/contentlayoutguide
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/contentlayoutguide'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/contentlayoutguide.json'
content_hash: 'sha256:7271cbfa26e94ada'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# contentLayoutGuide

<sub>Instance Property</sub>

The layout guide based on the untranslated content rectangle of the scroll view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var contentLayoutGuide: UILayoutGuide { get }
```

## Discussion

Use this layout guide when you want to create Auto Layout constraints related to the content area of a scroll view.

## See Also

### Getting the layout guides

- [frameLayoutGuide](framelayoutguide.md) — The layout guide based on the untransformed frame rectangle of the scroll view.
