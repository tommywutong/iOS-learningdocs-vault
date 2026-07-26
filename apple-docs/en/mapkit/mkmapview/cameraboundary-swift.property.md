---
title: cameraBoundary
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapview/cameraboundary-swift.property
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/cameraboundary-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/cameraboundary-swift.property.json'
content_hash: 'sha256:af6d38b652f241de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# cameraBoundary

<sub>Instance Property</sub>

The boundary of the area within which the map view’s center needs to remain.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@NSCopying var cameraBoundary: MKMapView.CameraBoundary? { get set }
```

## See Also

### Constraining the map view

- [- setCameraBoundary:animated:](<setcameraboundary(__animated_).md>) — Sets the camera boundary for the map view, specifying whether to use animation.
- [- setCameraZoomRange:animated:](<setcamerazoomrange(__animated_).md>) — Sets the camera zoom range for the map view, specifying whether to use animation.
- [cameraZoomRange](camerazoomrange-swift.property.md) — The zoom range to apply to the map view.
- [CameraBoundary](cameraboundary-swift.class.md) — A boundary of an area within which the map’s center needs to remain.
- [CameraZoomRange](camerazoomrange-swift.class.md) — A camera zoom range that limits the distances to which the user can zoom.
