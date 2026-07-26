---
title: 'init(top:left:bottom:right:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiedgeinsets/init(top:left:bottom:right:)-6ff7'
source_url: 'https://developer.apple.com/documentation/uikit/uiedgeinsets/init(top:left:bottom:right:)-6ff7'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiedgeinsets/init%28top%3Aleft%3Abottom%3Aright%3A%29-6ff7.json'
content_hash: 'sha256:b68bc42c0cf7d374'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIEdgeInsets](../uiedgeinsets.md)

# init(top:left:bottom:right:)

<sub>Initializer</sub>

Creates an edge insets structure with the specified edges.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
init(top: CGFloat, left: CGFloat, bottom: CGFloat, right: CGFloat)
```

## Parameters

- `top` — The inset on the top of an object.

- `left` — The inset on the left of an object.

- `bottom` — The inset on the bottom of an object.

- `right` — The inset on the right of an object.

## Return Value

An initialized inset structure.

## Discussion

An inset is a margin around a rectangle. Positive values represent margins closer to the center of the rectangle, while negative values represent margins further from the center.

## See Also

### Creating edge insets

- [init()](<init().md>) — Initializes the edge insets structure to default values.
