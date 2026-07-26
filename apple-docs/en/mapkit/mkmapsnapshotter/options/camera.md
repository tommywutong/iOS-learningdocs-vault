---
title: camera
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapsnapshotter/options/camera
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/options/camera'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapsnapshotter/options/camera.json'
content_hash: 'sha256:da9debd650828d30'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKMapSnapshotter](../../mkmapsnapshotter.md) · [Options](../options.md)

# camera

<sub>Instance Property</sub>

The camera to use when taking the map snapshot.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying var camera: MKMapCamera { get set }
```

## Discussion

Specify a camera object if you want to change the pitch, altitude, or heading information applied to the map.

## See Also

### Configuring the snapshot region

- [region](region.md) — The area of the map that you want to capture.
- [mapRect](maprect.md) — The map rectangle that you want to capture.
