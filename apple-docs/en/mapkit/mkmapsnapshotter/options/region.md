---
title: region
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapsnapshotter/options/region
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/options/region'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapsnapshotter/options/region.json'
content_hash: 'sha256:193633827a3529d8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKMapSnapshotter](../../mkmapsnapshotter.md) · [Options](../options.md)

# region

<sub>Instance Property</sub>

The area of the map that you want to capture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var region: MKCoordinateRegion { get set }
```

## Discussion

Use this property to specify the map using geographical coordinates. If you assign a value for this property, the snapshotter updates the value in the [mapRect](maprect.md) property to match the corresponding area as closely as possible.

The snapshotter sets the default value of this property to an area that encompasses the user’s country or region, based on the current locale information.

## See Also

### Configuring the snapshot region

- [mapRect](maprect.md) — The map rectangle that you want to capture.
- [camera](camera.md) — The camera to use when taking the map snapshot.
