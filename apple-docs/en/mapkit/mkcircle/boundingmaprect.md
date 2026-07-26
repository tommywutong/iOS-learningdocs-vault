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
doc_path: /documentation/mapkit/mkcircle/boundingmaprect
source_url: 'https://developer.apple.com/documentation/mapkit/mkcircle/boundingmaprect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkcircle/boundingmaprect.json'
content_hash: 'sha256:aef190d08b039c1a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKCircle](../mkcircle.md)

# boundingMapRect

<sub>Instance Property</sub>

The bounding rectangle of the circular area.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var boundingMapRect: MKMapRect { get }
```

## Discussion

As latitude values move away from the equator and toward the poles, the physical distance between map points gets smaller. This means that the map needs more map points to represent the same distance. As a result, the bounding rectangle of a circle overlay gets larger as the center point of that circle moves away from the equator and toward the poles.

## See Also

### Accessing the overlay’s attributes

- [coordinate](coordinate.md) — The center point of the circular area, specified as a latitude and longitude.
- [radius](radius.md) — The radius of the circular area, in meters.
