---
title: MKMapCameraZoomDefault
framework: MapKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapcamerazoomdefault
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapcamerazoomdefault'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapcamerazoomdefault.json'
content_hash: 'sha256:92f49972884e17f2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKMapCameraZoomDefault

<sub>Global Variable</sub>

A constant value used to represent the default value for zooming in or out on a map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let MKMapCameraZoomDefault: CLLocationDistance
```

## Discussion

Use [MKMapCameraZoomDefault](mkmapcamerazoomdefault.md) for the minimum or maximum zoom range when you create an instance of [CameraZoomRange](mkmapview/camerazoomrange-swift.class.md) to allow the user to zoom to any level that MapKit supports.

## See Also

### Creating a camera zoom range

- [- initWithMinCenterCoordinateDistance:maxCenterCoordinateDistance:](<mkmapview/camerazoomrange-swift.class/init(mincentercoordinatedistance_maxcentercoordinatedistance_).md>) — Create a camera zoom range by specifying a minimum and maximum distance from your map view’s center coordinates, measured in meters.
- [- initWithMinCenterCoordinateDistance:](<mkmapview/camerazoomrange-swift.class/init(mincentercoordinatedistance_).md>) — Create a camera zoom range by specifying the minimum distance from your map view’s center coordinate, measured in meters.
- [- initWithMaxCenterCoordinateDistance:](<mkmapview/camerazoomrange-swift.class/init(maxcentercoordinatedistance_).md>) — Create a camera zoom range by specifying the maximum distance from your map view’s center coordinate, measured in meters.
