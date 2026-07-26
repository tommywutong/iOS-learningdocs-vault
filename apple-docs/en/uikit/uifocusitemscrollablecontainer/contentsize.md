---
title: contentSize
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocusitemscrollablecontainer/contentsize
source_url: 'https://developer.apple.com/documentation/uikit/uifocusitemscrollablecontainer/contentsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusitemscrollablecontainer/contentsize.json'
content_hash: 'sha256:c25a476824fc4526'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusItemScrollableContainer](../uifocusitemscrollablecontainer.md)

# contentSize

<sub>Instance Property</sub>

The total size of the content contained by this container.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var contentSize: CGSize { get }
```

## Discussion

If the value of this property is larger than [visibleSize](visiblesize.md) then the content is scrollable.

## See Also

### Retrieving the content size

- [contentOffset](contentoffset.md) — The current content offset for the scrollable container.
- [visibleSize](visiblesize.md) — The visible size of the scrollable container.
