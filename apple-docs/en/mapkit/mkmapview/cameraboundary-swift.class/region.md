---
title: region
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapview/cameraboundary-swift.class/region
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/cameraboundary-swift.class/region'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/cameraboundary-swift.class/region.json'
content_hash: 'sha256:b89fb0719cf5f0b5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKMapView](../../mkmapview.md) · [CameraBoundary](../cameraboundary-swift.class.md)

# region

<sub>Instance Property</sub>

The coordinate region that describes the camera boundary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var region: MKCoordinateRegion { get }
```

## Discussion

Both the [mapRect](maprect.md) and the [region](region.md) represent the same camera boundary.

## See Also

### Accessing the boundary

- [mapRect](maprect.md) — The map rectangle that describes the camera boundary.
