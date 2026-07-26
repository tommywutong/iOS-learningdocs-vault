---
title: CGEventMouseSubtype.tabletPoint
framework: Core Graphics
symbol_kind: case
role: symbol
role_heading: Case
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgeventmousesubtype/tabletpoint
source_url: 'https://developer.apple.com/documentation/coregraphics/cgeventmousesubtype/tabletpoint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgeventmousesubtype/tabletpoint.json'
content_hash: 'sha256:5af41dcfbb465d60'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGEventMouseSubtype](../cgeventmousesubtype.md)

# CGEventMouseSubtype.tabletPoint

<sub>Case</sub>

Specifies that the mouse event originated from a tablet device, and that the various `kCGTabletEvent` field selectors may be used to obtain tablet-specific data from the mouse event.

<sub>Mac Catalyst, macOS</sub>

```swift
case tabletPoint
```

## See Also

### Constants

- [kCGEventMouseSubtypeDefault](defaulttype.md) — Specifies that the event is an ordinary mouse event, and does not contain additional tablet device information.
- [kCGEventMouseSubtypeTabletProximity](tabletproximity.md)
