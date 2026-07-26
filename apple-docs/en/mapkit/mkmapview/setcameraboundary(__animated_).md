---
title: 'setCameraBoundary(_:animated:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapview/setcameraboundary(_:animated:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/setcameraboundary(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/setcameraboundary%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:e24e0c74674a0ed5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# setCameraBoundary(_:animated:)

<sub>Instance Method</sub>

Sets the camera boundary for the map view, specifying whether to use animation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setCameraBoundary(_ cameraBoundary: MKMapView.CameraBoundary?, animated: Bool)
```

## Parameters

- `cameraBoundary` — The new [CameraBoundary](cameraboundary-swift.class.md).

- `animated` — A Boolean value that indicates whether the framework animates the transition of the map view to the new boundary.

## See Also

### Constraining the map view

- [cameraBoundary](cameraboundary-swift.property.md) — The boundary of the area within which the map view’s center needs to remain.
- [- setCameraZoomRange:animated:](<setcamerazoomrange(__animated_).md>) — Sets the camera zoom range for the map view, specifying whether to use animation.
- [cameraZoomRange](camerazoomrange-swift.property.md) — The zoom range to apply to the map view.
- [CameraBoundary](cameraboundary-swift.class.md) — A boundary of an area within which the map’s center needs to remain.
- [CameraZoomRange](camerazoomrange-swift.class.md) — A camera zoom range that limits the distances to which the user can zoom.
