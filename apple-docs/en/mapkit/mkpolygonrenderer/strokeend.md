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
doc_path: /documentation/mapkit/mkpolygonrenderer/strokeend
source_url: 'https://developer.apple.com/documentation/mapkit/mkpolygonrenderer/strokeend'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkpolygonrenderer/strokeend.json'
content_hash: 'sha256:39940eff01a05b01'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKPolygonRenderer](../mkpolygonrenderer.md)

# strokeEnd

<sub>Instance Property</sub>

The unit distance along the polygon where the stroke ends.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var strokeEnd: CGFloat { get set }
```

## Discussion

Use this property and [strokeStart](strokestart.md) to render a portion of the polygon. Use [- locationAtPointIndex:](<../mkmultipoint/location(atpointindex_).md>) to get unit distance locations for point indices along the polygon.

## See Also

### Accessing the stroke

- [strokeStart](strokestart.md) — The unit distance along the polygon where the stroke starts.
