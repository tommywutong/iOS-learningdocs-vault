---
title: camera
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapview/camera
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/camera'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/camera.json'
content_hash: 'sha256:6d1ab3b402aac038'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# camera

<sub>Instance Property</sub>

The camera to use for determining the appearance of the map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@NSCopying var camera: MKMapCamera { get set }
```

## Discussion

A camera object defines a point above the map’s surface from which to view the map. Applying a camera to a map can have the effect of giving the map a 3D-like appearance. You can use a camera to rotate the map so that it orients to match the user’s heading or to apply a pitch angle to tilt the plane of the map. You can check the map’s [pitchEnabled](ispitchenabled.md) property to determine whether the map can use pitch.

Assigning a new camera to this property updates the map immediately and without animating the change. If you want to animate changes in camera position, use the [- setCamera:animated:](<setcamera(__animated_).md>) method instead.

Don’t set this property to `nil`. To restore the map to a flat appearance, apply a camera with a pitch angle of `0`, which yields a camera looking straight down onto the map surface.

## See Also

### Configuring the map display

- [- setCamera:animated:](<setcamera(__animated_).md>) — Changes the camera to use for determining the map’s viewing parameters, and optionally animates the change.
- [showsCompass](showscompass.md) — A Boolean value that indicates whether the map displays a compass control.
- [showsPitchControl](showspitchcontrol.md) — A Boolean value that indicates whether the map displays the pitch control.
- [showsScale](showsscale.md) — A Boolean value that indicates whether the map shows scale information.
- [showsZoomControls](showszoomcontrols.md) — A Boolean value that indicates whether the map displays zoom controls.
- [showsBuildings](showsbuildings.md) — A Boolean value that indicates whether the map displays extruded building information on supported map types. _(deprecated)_
- [showsPointsOfInterest](showspointsofinterest.md) — A Boolean value that indicates whether the map displays point-of-interest information. _(deprecated)_
- [pointOfInterestFilter](pointofinterestfilter.md) — The filter to use for determining the points of interest that appear on the map. _(deprecated)_
- [showsTraffic](showstraffic.md) — A Boolean value that indicates whether the map displays traffic information. _(deprecated)_
