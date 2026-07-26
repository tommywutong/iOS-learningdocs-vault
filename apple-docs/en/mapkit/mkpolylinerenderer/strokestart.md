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
doc_path: /documentation/mapkit/mkpolylinerenderer/strokestart
source_url: 'https://developer.apple.com/documentation/mapkit/mkpolylinerenderer/strokestart'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkpolylinerenderer/strokestart.json'
content_hash: 'sha256:102513c83796723c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKPolylineRenderer](../mkpolylinerenderer.md)

# strokeStart

<sub>Instance Property</sub>

The unit distance along the line where the stroke starts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var strokeStart: CGFloat { get set }
```

## Discussion

Use this property and [strokeEnd](strokeend.md) to render a portion of the line. Use [- locationAtPointIndex:](<../mkmultipoint/location(atpointindex_).md>) to get unit distance locations for point indices along the line.

## See Also

### Accessing the stroke

- [strokeEnd](strokeend.md) — The unit distance along the line where the stroke ends.
