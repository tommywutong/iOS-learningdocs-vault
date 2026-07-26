---
title: CGEventMouseSubtype.tabletProximity
framework: Core Graphics
symbol_kind: case
role: symbol
role_heading: Case
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgeventmousesubtype/tabletproximity
source_url: 'https://developer.apple.com/documentation/coregraphics/cgeventmousesubtype/tabletproximity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgeventmousesubtype/tabletproximity.json'
content_hash: 'sha256:f01e97d9afe29240'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGEventMouseSubtype](../cgeventmousesubtype.md)

# CGEventMouseSubtype.tabletProximity

<sub>Case</sub>

<sub>Mac Catalyst, macOS</sub>

```swift
case tabletProximity
```

## Discussion

Specifies that the mouse event originated from a tablet device with the pen in proximity but not necessarily touching the tablet, and that the various `kCGTabletProximity` field selectors may be used to obtain tablet-specific data from the mouse event. This is often used with mouse move events originating from a tablet.

## See Also

### Constants

- [kCGEventMouseSubtypeDefault](defaulttype.md) — Specifies that the event is an ordinary mouse event, and does not contain additional tablet device information.
- [kCGEventMouseSubtypeTabletPoint](tabletpoint.md) — Specifies that the mouse event originated from a tablet device, and that the various `kCGTabletEvent` field selectors may be used to obtain tablet-specific data from the mouse event.
