---
title: boundingMapRect
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkoverlay/boundingmaprect
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlay/boundingmaprect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlay/boundingmaprect.json'
content_hash: 'sha256:759d6cbc2dfb07db'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKOverlay](../mkoverlay.md)

# boundingMapRect

<sub>Instance Property</sub>

The projected rectangle that encompasses the overlay.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var boundingMapRect: MKMapRect { get }
```

## Discussion

This property contains the smallest rectangle that completely encompasses the overlay. Implementers of this protocol need to set this area when implementing their overlay class, and after setting it, not change it. Specify the rectangle using projected coordinates — that is, coordinates you obtain by projecting the globe onto a two-dimensional surface.

## See Also

### Describing the overlay geometry

- [coordinate](coordinate.md) — The approximate center point of the overlay area.
