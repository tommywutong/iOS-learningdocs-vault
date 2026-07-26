---
title: strokeEnd
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkcirclerenderer/strokeend
source_url: 'https://developer.apple.com/documentation/mapkit/mkcirclerenderer/strokeend'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkcirclerenderer/strokeend.json'
content_hash: 'sha256:6d436d9d79531aa6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKCircleRenderer](../mkcirclerenderer.md)

# strokeEnd

<sub>Instance Property</sub>

The unit distance along the circle where the stroke ends.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var strokeEnd: CGFloat { get set }
```

## Discussion

Use this property and [strokeStart](strokestart.md) to render a portion of the line. As a unit distance, [strokeEnd](strokeend.md) must be a value between 0 and 1. A unit distance of 0 represents the top of the circle and the stroke draws in a clockwise direction.

## See Also

### Accessing the stroke

- [strokeStart](strokestart.md) — The unit distance along the circle where the stroke starts.
