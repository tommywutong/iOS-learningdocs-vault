---
title: CGLineCap.square
framework: Core Graphics
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cglinecap/square
source_url: 'https://developer.apple.com/documentation/coregraphics/cglinecap/square'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cglinecap/square.json'
content_hash: 'sha256:fca2dc565012a47d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGLineCap](../cglinecap.md)

# CGLineCap.square

<sub>Case</sub>

A line with a squared-off end. Core Graphics extends the line beyond the endpoint of the path for a distance equal to half the line width.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case square
```

## See Also

### Constants

- [kCGLineCapButt](butt.md) — A line with a squared-off end. Core Graphics draws the line to extend only to the exact endpoint of the path. This is the default.
- [kCGLineCapRound](round.md) — A line with a rounded end. Core Graphics draws the line to extend beyond the endpoint of the path. The line ends with a semicircular arc with a radius of 1/2 the line’s width, centered on the endpoint.
