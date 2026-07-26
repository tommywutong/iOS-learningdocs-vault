---
title: CGDisplayStreamUpdateRectType.reducedDirtyRects
framework: Core Graphics
symbol_kind: case
role: symbol
role_heading: Case
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdisplaystreamupdaterecttype/reduceddirtyrects
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdisplaystreamupdaterecttype/reduceddirtyrects'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdisplaystreamupdaterecttype/reduceddirtyrects.json'
content_hash: 'sha256:25ad5fa99d4d8c00'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGDisplayStreamUpdateRectType](../cgdisplaystreamupdaterecttype.md)

# CGDisplayStreamUpdateRectType.reducedDirtyRects

<sub>Case</sub>

The union is calculated and then simplified. This reduces the number of rectangles returned to your app, but it may report some pixels that were not actually changed.

<sub>Mac Catalyst, macOS</sub>

```swift
case reducedDirtyRects
```

## See Also

### Constants

- [kCGDisplayStreamUpdateRefreshedRects](refreshedrects.md) — The rectangles for the portions of the display that were redrawn.
- [kCGDisplayStreamUpdateMovedRects](movedrects.md) — The rectangles for the portions of the display that were simply moved from one part of the display to another.
- [kCGDisplayStreamUpdateDirtyRects](dirtyrects.md) — The union of both rectangles that were redrawn and rectangles that were moved.
