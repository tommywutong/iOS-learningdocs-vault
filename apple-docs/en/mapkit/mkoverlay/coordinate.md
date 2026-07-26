---
title: coordinate
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkoverlay/coordinate
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlay/coordinate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlay/coordinate.json'
content_hash: 'sha256:cd5e18734880f050'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKOverlay](../mkoverlay.md)

# coordinate

<sub>Instance Property</sub>

The approximate center point of the overlay area.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var coordinate: CLLocationCoordinate2D { get }
```

## Discussion

This point is typically set to the center point of the map’s bounding rectangle. The overlay uses it as the anchor point for any callouts that display for the annotation.

## See Also

### Related Documentation

- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)

### Describing the overlay geometry

- [boundingMapRect](boundingmaprect.md) — The projected rectangle that encompasses the overlay.
