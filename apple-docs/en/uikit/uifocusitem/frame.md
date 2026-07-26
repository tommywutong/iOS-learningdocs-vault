---
title: frame
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocusitem/frame
source_url: 'https://developer.apple.com/documentation/uikit/uifocusitem/frame'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusitem/frame.json'
content_hash: 'sha256:2d283820f2ef6c21'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusItem](../uifocusitem.md)

# frame

<sub>Instance Property</sub>

The geometric frame of the item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var frame: CGRect { get }
```

## Discussion

The item’s frame must be expressed in the coordinate space of the [UIFocusItemContainer](../uifocusitemcontainer.md) that contains it.
