---
title: mapRect
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapsnapshotter/options/maprect
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/options/maprect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapsnapshotter/options/maprect.json'
content_hash: 'sha256:528dd5a56cf0095b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKMapSnapshotter](../../mkmapsnapshotter.md) · [Options](../options.md)

# mapRect

<sub>Instance Property</sub>

The map rectangle that you want to capture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var mapRect: MKMapRect { get set }
```

## Discussion

Use this property to specify the map using map view points. If you assign a value for this property, the snapshotter updates the value in the [region](region.md) property to match the corresponding map rectangle as closely as possible.

The snapshotter sets the default value of this property to a map rectangle that encompasses the user’s country or region, based on the current locale information.

## See Also

### Configuring the snapshot region

- [region](region.md) — The area of the map that you want to capture.
- [camera](camera.md) — The camera to use when taking the map snapshot.
