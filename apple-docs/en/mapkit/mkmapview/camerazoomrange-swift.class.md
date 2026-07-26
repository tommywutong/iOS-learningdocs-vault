---
title: MKMapView.CameraZoomRange
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapview/camerazoomrange-swift.class
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/camerazoomrange-swift.class'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/camerazoomrange-swift.class.json'
content_hash: 'sha256:ddc03fa31687926f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# MKMapView.CameraZoomRange

<sub>Class</sub>

A camera zoom range that limits the distances to which the user can zoom.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class CameraZoomRange
```

## Overview

Create a camera zoom range to limit the distance to which the user can zoom. After you create the camera zoom range, you can apply it to multiple map views. If you don’t create a camera zoom range, your map view allows the user to zoom to MapKit’s capabilities.

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSCoding](../../foundation/nscoding.md), [NSCopying](../../foundation/nscopying.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md), [NSSecureCoding](../../foundation/nssecurecoding.md)

## Topics

### Creating a camera zoom range

- [- initWithMinCenterCoordinateDistance:maxCenterCoordinateDistance:](<camerazoomrange-swift.class/init(mincentercoordinatedistance_maxcentercoordinatedistance_).md>) — Create a camera zoom range by specifying a minimum and maximum distance from your map view’s center coordinates, measured in meters.
- [- initWithMinCenterCoordinateDistance:](<camerazoomrange-swift.class/init(mincentercoordinatedistance_).md>) — Create a camera zoom range by specifying the minimum distance from your map view’s center coordinate, measured in meters.
- [- initWithMaxCenterCoordinateDistance:](<camerazoomrange-swift.class/init(maxcentercoordinatedistance_).md>) — Create a camera zoom range by specifying the maximum distance from your map view’s center coordinate, measured in meters.
- [MKMapCameraZoomDefault](../mkmapcamerazoomdefault.md) — A constant value used to represent the default value for zooming in or out on a map.

### Accessing zoom range values

- [maxCenterCoordinateDistance](camerazoomrange-swift.class/maxcentercoordinatedistance.md) — The maximum distance of the camera to the center of the map, measured in meters.
- [minCenterCoordinateDistance](camerazoomrange-swift.class/mincentercoordinatedistance.md) — The minimum distance of the camera to the center of the map, measured in meters.

### Initializers

- [init(coder:)](<camerazoomrange-swift.class/init(coder_).md>)

## See Also

### Constraining the map view

- [- setCameraBoundary:animated:](<setcameraboundary(__animated_).md>) — Sets the camera boundary for the map view, specifying whether to use animation.
- [cameraBoundary](cameraboundary-swift.property.md) — The boundary of the area within which the map view’s center needs to remain.
- [- setCameraZoomRange:animated:](<setcamerazoomrange(__animated_).md>) — Sets the camera zoom range for the map view, specifying whether to use animation.
- [cameraZoomRange](camerazoomrange-swift.property.md) — The zoom range to apply to the map view.
- [CameraBoundary](cameraboundary-swift.class.md) — A boundary of an area within which the map’s center needs to remain.
