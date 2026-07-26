---
title: CGLineCap.butt
framework: Core Graphics
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cglinecap/butt
source_url: 'https://developer.apple.com/documentation/coregraphics/cglinecap/butt'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cglinecap/butt.json'
content_hash: 'sha256:9442981e110c9f7f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGLineCap](../cglinecap.md)

# CGLineCap.butt

<sub>Case</sub>

A line with a squared-off end. Core Graphics draws the line to extend only to the exact endpoint of the path. This is the default.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case butt
```

## See Also

### Constants

- [kCGLineCapRound](round.md) — A line with a rounded end. Core Graphics draws the line to extend beyond the endpoint of the path. The line ends with a semicircular arc with a radius of 1/2 the line’s width, centered on the endpoint.
- [kCGLineCapSquare](square.md) — A line with a squared-off end. Core Graphics extends the line beyond the endpoint of the path for a distance equal to half the line width.
