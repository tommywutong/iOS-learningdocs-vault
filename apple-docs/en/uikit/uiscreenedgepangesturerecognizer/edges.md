---
title: edges
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscreenedgepangesturerecognizer/edges
source_url: 'https://developer.apple.com/documentation/uikit/uiscreenedgepangesturerecognizer/edges'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreenedgepangesturerecognizer/edges.json'
content_hash: 'sha256:1ae66ffbaccb8884'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScreenEdgePanGestureRecognizer](../uiscreenedgepangesturerecognizer.md)

# edges

<sub>Instance Property</sub>

The acceptable starting edges for the gesture.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var edges: UIRectEdge { get set }
```

## Discussion

The edges you specify are always relative to the app’s current interface orientation. This behavior ensures that the gestures always occur from the same place in your user interface, regardless of the device’s current orientation.

## See Also

### Specifying the starting edges

- [UIRectEdge](../uirectedge.md) — Constants that specify the edges of a rectangle.
