---
title: CGDisplayStreamUpdateRectType.refreshedRects
framework: Core Graphics
symbol_kind: case
role: symbol
role_heading: Case
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdisplaystreamupdaterecttype/refreshedrects
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdisplaystreamupdaterecttype/refreshedrects'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdisplaystreamupdaterecttype/refreshedrects.json'
content_hash: 'sha256:3aa4a78d22a0e700'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGDisplayStreamUpdateRectType](../cgdisplaystreamupdaterecttype.md)

# CGDisplayStreamUpdateRectType.refreshedRects

<sub>Case</sub>

The rectangles for the portions of the display that were redrawn.

<sub>Mac Catalyst, macOS</sub>

```swift
case refreshedRects
```

## See Also

### Constants

- [kCGDisplayStreamUpdateMovedRects](movedrects.md) — The rectangles for the portions of the display that were simply moved from one part of the display to another.
- [kCGDisplayStreamUpdateDirtyRects](dirtyrects.md) — The union of both rectangles that were redrawn and rectangles that were moved.
- [kCGDisplayStreamUpdateReducedDirtyRects](reduceddirtyrects.md) — The union is calculated and then simplified. This reduces the number of rectangles returned to your app, but it may report some pixels that were not actually changed.
