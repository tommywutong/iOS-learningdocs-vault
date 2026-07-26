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
doc_path: /documentation/mapkit/mkpolylinerenderer/strokeend
source_url: 'https://developer.apple.com/documentation/mapkit/mkpolylinerenderer/strokeend'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkpolylinerenderer/strokeend.json'
content_hash: 'sha256:161b5a7553268511'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKPolylineRenderer](../mkpolylinerenderer.md)

# strokeEnd

<sub>Instance Property</sub>

The unit distance along the line where the stroke ends.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var strokeEnd: CGFloat { get set }
```

## Discussion

Use this property and [strokeStart](strokestart.md) to render a portion of the line. Use [- locationAtPointIndex:](<../mkmultipoint/location(atpointindex_).md>) to get unit distance locations for point indices along the line.

## See Also

### Accessing the stroke

- [strokeStart](strokestart.md) — The unit distance along the line where the stroke starts.
