---
title: strokeStart
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkcirclerenderer/strokestart
source_url: 'https://developer.apple.com/documentation/mapkit/mkcirclerenderer/strokestart'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkcirclerenderer/strokestart.json'
content_hash: 'sha256:ef10fa6bce43f51a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKCircleRenderer](../mkcirclerenderer.md)

# strokeStart

<sub>Instance Property</sub>

The unit distance along the circle where the stroke starts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var strokeStart: CGFloat { get set }
```

## Discussion

Use this property and [strokeEnd](strokeend.md) to render a portion of the line. As a unit distance, [strokeStart](strokestart.md) must be a value between 0 and 1. A unit distance of 0 represents the top of the circle and the stroke draws in a clockwise direction.

## See Also

### Accessing the stroke

- [strokeEnd](strokeend.md) — The unit distance along the circle where the stroke ends.
