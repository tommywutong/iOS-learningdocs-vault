---
title: contentOffset
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrollview/contentoffset
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/contentoffset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/contentoffset.json'
content_hash: 'sha256:185eef0bc2967af6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# contentOffset

<sub>Instance Property</sub>

The point at which the origin of the content view is offset from the origin of the scroll view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var contentOffset: CGPoint { get set }
```

## Discussion

The default value is [CGPointZero](../../coregraphics/cgpointzero.md).

## See Also

### Managing the content size and offset

- [contentSize](contentsize.md) — The size of the content view.
- [- setContentOffset:animated:](<setcontentoffset(__animated_).md>) — Sets the offset from the content view’s origin that corresponds to the scroll view’s origin.
