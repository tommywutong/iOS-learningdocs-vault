---
title: MKMapView.CameraBoundary
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapview/cameraboundary-swift.class
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/cameraboundary-swift.class'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/cameraboundary-swift.class.json'
content_hash: 'sha256:c0b174b94909ec69'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# MKMapView.CameraBoundary

<sub>Class</sub>

A boundary of an area within which the map’s center needs to remain.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class CameraBoundary
```

## Overview

The constraints of the camera boundary restrict the center point of your map.

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSCoding](../../foundation/nscoding.md), [NSCopying](../../foundation/nscopying.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md), [NSSecureCoding](../../foundation/nssecurecoding.md)

## Topics

### Creating a camera boundary

- [- initWithCoder:](<cameraboundary-swift.class/init(coder_).md>) — Creates a camera boundary using the provided coder.
- [- initWithCoordinateRegion:](<cameraboundary-swift.class/init(coordinateregion_).md>) — Creates a camera boundary using the provided coordinate region.
- [- initWithMapRect:](<cameraboundary-swift.class/init(maprect_).md>) — Creates a camera boundary using the provided map rectangle.

### Accessing the boundary

- [mapRect](cameraboundary-swift.class/maprect.md) — The map rectangle that describes the camera boundary.
- [region](cameraboundary-swift.class/region.md) — The coordinate region that describes the camera boundary.

## See Also

### Constraining the map view

- [- setCameraBoundary:animated:](<setcameraboundary(__animated_).md>) — Sets the camera boundary for the map view, specifying whether to use animation.
- [cameraBoundary](cameraboundary-swift.property.md) — The boundary of the area within which the map view’s center needs to remain.
- [- setCameraZoomRange:animated:](<setcamerazoomrange(__animated_).md>) — Sets the camera zoom range for the map view, specifying whether to use animation.
- [cameraZoomRange](camerazoomrange-swift.property.md) — The zoom range to apply to the map view.
- [CameraZoomRange](camerazoomrange-swift.class.md) — A camera zoom range that limits the distances to which the user can zoom.
