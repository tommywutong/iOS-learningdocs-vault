---
title: drawsBeforeStartLocation
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cggradientdrawingoptions/drawsbeforestartlocation
source_url: 'https://developer.apple.com/documentation/coregraphics/cggradientdrawingoptions/drawsbeforestartlocation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cggradientdrawingoptions/drawsbeforestartlocation.json'
content_hash: 'sha256:34978cb3c545db24'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGGradientDrawingOptions](../cggradientdrawingoptions.md)

# drawsBeforeStartLocation

<sub>Type Property</sub>

The fill should extend beyond the starting location. The color that extends beyond the starting point is the solid color defined by the [CGGradient](../cggradient.md) object to be at location 0.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var drawsBeforeStartLocation: CGGradientDrawingOptions { get }
```

## See Also

### Constants

- [kCGGradientDrawsAfterEndLocation](drawsafterendlocation.md) — The fill should extend beyond the ending location. The color that extends beyond the ending point is the solid color defined by the [CGGradient](../cggradient.md) object to be at location 1.
