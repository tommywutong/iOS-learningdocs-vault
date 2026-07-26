---
title: CGDisplayStreamUpdateRectType.movedRects
framework: Core Graphics
symbol_kind: case
role: symbol
role_heading: Case
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdisplaystreamupdaterecttype/movedrects
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdisplaystreamupdaterecttype/movedrects'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdisplaystreamupdaterecttype/movedrects.json'
content_hash: 'sha256:ce123a57f8a066ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGDisplayStreamUpdateRectType](../cgdisplaystreamupdaterecttype.md)

# CGDisplayStreamUpdateRectType.movedRects

<sub>Case</sub>

The rectangles for the portions of the display that were simply moved from one part of the display to another.

<sub>Mac Catalyst, macOS</sub>

```swift
case movedRects
```

## See Also

### Constants

- [kCGDisplayStreamUpdateRefreshedRects](refreshedrects.md) — The rectangles for the portions of the display that were redrawn.
- [kCGDisplayStreamUpdateDirtyRects](dirtyrects.md) — The union of both rectangles that were redrawn and rectangles that were moved.
- [kCGDisplayStreamUpdateReducedDirtyRects](reduceddirtyrects.md) — The union is calculated and then simplified. This reduces the number of rectangles returned to your app, but it may report some pixels that were not actually changed.
