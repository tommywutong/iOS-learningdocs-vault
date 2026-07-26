---
title: CGLineJoin.miter
framework: Core Graphics
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cglinejoin/miter
source_url: 'https://developer.apple.com/documentation/coregraphics/cglinejoin/miter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cglinejoin/miter.json'
content_hash: 'sha256:a71f7bd021a9d0d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGLineJoin](../cglinejoin.md)

# CGLineJoin.miter

<sub>Case</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case miter
```

## Discussion

A join with a sharp (angled) corner. Core Graphics draws the outer sides of the lines beyond the endpoint of the path, until they meet. If the length of the miter divided by the line width is greater than the miter limit, a bevel join is used instead. This is the default. To set the miter limit, see [CGContextSetMiterLimit](<../cgcontext/setmiterlimit(__).md>).

## See Also

### Constants

- [kCGLineJoinRound](round.md) — A join with a rounded end. Core Graphics draws the line to extend beyond the endpoint of the path. The line ends with a semicircular arc with a radius of 1/2 the line’s width, centered on the endpoint.
- [kCGLineJoinBevel](bevel.md) — A join with a squared-off end. Core Graphics draws the line to extend beyond the endpoint of the path, for a distance of 1/2 the line’s width.
