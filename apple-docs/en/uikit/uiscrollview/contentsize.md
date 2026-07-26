---
title: contentSize
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrollview/contentsize
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/contentsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/contentsize.json'
content_hash: 'sha256:ec8bef82bb54b04d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# contentSize

<sub>Instance Property</sub>

The size of the content view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var contentSize: CGSize { get set }
```

## Discussion

The unit of size is points. The default size is [CGSizeZero](../../coregraphics/cgsizezero.md).

## See Also

### Managing the content size and offset

- [contentOffset](contentoffset.md) — The point at which the origin of the content view is offset from the origin of the scroll view.
- [- setContentOffset:animated:](<setcontentoffset(__animated_).md>) — Sets the offset from the content view’s origin that corresponds to the scroll view’s origin.
