---
title: reducedDirtyRectangleCount
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgscreenupdateoperation/reduceddirtyrectanglecount
source_url: 'https://developer.apple.com/documentation/coregraphics/cgscreenupdateoperation/reduceddirtyrectanglecount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgscreenupdateoperation/reduceddirtyrectanglecount.json'
content_hash: 'sha256:fc7fb5eadb83c7a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGScreenUpdateOperation](../cgscreenupdateoperation.md)

# reducedDirtyRectangleCount

<sub>Type Property</sub>

<sub>Mac Catalyst, macOS</sub>

```swift
static var reducedDirtyRectangleCount: CGScreenUpdateOperation { get }
```

## Discussion

When presented as part of the requested operations to the function [CGWaitForScreenUpdateRects](<../cgwaitforscreenupdaterects(__________).md>), specifies that the function should try to minimize the number of rectangles returned to represent the changed areas of the display.  The function may combine adjacent rectangles within a larger bounding rectangle, which may include unmodified areas of the display.

## See Also

### Constants

- [kCGScreenUpdateOperationRefresh](refresh.md) — A screen-refresh operation.
- [kCGScreenUpdateOperationMove](move.md) — A screen-move operation.
