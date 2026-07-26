---
title: showsCompass
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.9+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapview/showscompass
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/showscompass'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/showscompass.json'
content_hash: 'sha256:0996b69288c4738d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# showsCompass

<sub>Instance Property</sub>

A Boolean value that indicates whether the map displays a compass control.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var showsCompass: Bool { get set }
```

## Discussion

Use this property to show or hide a control that lets users change the heading orientation of the map.

## See Also

### Configuring the map display

- [- setCamera:animated:](<setcamera(__animated_).md>) — Changes the camera to use for determining the map’s viewing parameters, and optionally animates the change.
- [camera](camera.md) — The camera to use for determining the appearance of the map.
- [showsPitchControl](showspitchcontrol.md) — A Boolean value that indicates whether the map displays the pitch control.
- [showsScale](showsscale.md) — A Boolean value that indicates whether the map shows scale information.
- [showsZoomControls](showszoomcontrols.md) — A Boolean value that indicates whether the map displays zoom controls.
- [showsBuildings](showsbuildings.md) — A Boolean value that indicates whether the map displays extruded building information on supported map types. _(deprecated)_
- [showsPointsOfInterest](showspointsofinterest.md) — A Boolean value that indicates whether the map displays point-of-interest information. _(deprecated)_
- [pointOfInterestFilter](pointofinterestfilter.md) — The filter to use for determining the points of interest that appear on the map. _(deprecated)_
- [showsTraffic](showstraffic.md) — A Boolean value that indicates whether the map displays traffic information. _(deprecated)_
