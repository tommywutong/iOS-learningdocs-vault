---
title: contentOffset
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocusitemscrollablecontainer/contentoffset
source_url: 'https://developer.apple.com/documentation/uikit/uifocusitemscrollablecontainer/contentoffset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusitemscrollablecontainer/contentoffset.json'
content_hash: 'sha256:682a0d14282b3eaf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusItemScrollableContainer](../uifocusitemscrollablecontainer.md)

# contentOffset

<sub>Instance Property</sub>

The current content offset for the scrollable container.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var contentOffset: CGPoint { get set }
```

## Discussion

If the scrollable container contains `bounds`, then `bounds.origin` must be equal to the content offset. The system repeatedly sets this property to simulate animated scrolling.

## See Also

### Retrieving the content size

- [contentSize](contentsize.md) — The total size of the content contained by this container.
- [visibleSize](visiblesize.md) — The visible size of the scrollable container.
