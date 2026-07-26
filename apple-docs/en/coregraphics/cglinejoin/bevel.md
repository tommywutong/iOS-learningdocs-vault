---
title: CGLineJoin.bevel
framework: Core Graphics
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cglinejoin/bevel
source_url: 'https://developer.apple.com/documentation/coregraphics/cglinejoin/bevel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cglinejoin/bevel.json'
content_hash: 'sha256:5051c416d3995951'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGLineJoin](../cglinejoin.md)

# CGLineJoin.bevel

<sub>Case</sub>

A join with a squared-off end. Core Graphics draws the line to extend beyond the endpoint of the path, for a distance of 1/2 the line’s width.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case bevel
```

## See Also

### Constants

- [kCGLineJoinMiter](miter.md)
- [kCGLineJoinRound](round.md) — A join with a rounded end. Core Graphics draws the line to extend beyond the endpoint of the path. The line ends with a semicircular arc with a radius of 1/2 the line’s width, centered on the endpoint.
