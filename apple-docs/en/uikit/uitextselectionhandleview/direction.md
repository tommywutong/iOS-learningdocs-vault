---
title: direction
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextselectionhandleview/direction
source_url: 'https://developer.apple.com/documentation/uikit/uitextselectionhandleview/direction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextselectionhandleview/direction.json'
content_hash: 'sha256:130ecd4b5b7c93fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSelectionHandleView](../uitextselectionhandleview.md)

# direction

<sub>Instance Property</sub>

The orientation of the selection handle.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var direction: NSDirectionalRectEdge { get set }
```

## Discussion

Specify [NSDirectionalRectEdgeLeading](../nsdirectionalrectedge/leading.md) if this view represents the leading selection handle or [NSDirectionalRectEdgeTrailing](../nsdirectionalrectedge/trailing.md) if it represents the trailing selection handle. The system uses this information to determine where to differentiate the selection handles visually.

## See Also

### Specifying the handle details

- [customShape](customshape.md) — The custom shape to draw for the stem of the selection handle.
- [vertical](isvertical.md) — Convenience accessor for @c direction calculations.
