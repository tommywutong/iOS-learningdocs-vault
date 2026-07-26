---
title: showsZoomControls
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.9+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapview/showszoomcontrols
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/showszoomcontrols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/showszoomcontrols.json'
content_hash: 'sha256:b8032858b83816c9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# showsZoomControls

<sub>Instance Property</sub>

A Boolean value that indicates whether the map displays zoom controls.

<sub>Mac Catalyst, macOS</sub>

```swift
var showsZoomControls: Bool { get set }
```

## Discussion

In macOS, use this property to show or hide the controls that let users change the zoom level of the map.

## See Also

### Configuring the map display

- [- setCamera:animated:](<setcamera(__animated_).md>) — Changes the camera to use for determining the map’s viewing parameters, and optionally animates the change.
- [camera](camera.md) — The camera to use for determining the appearance of the map.
- [showsCompass](showscompass.md) — A Boolean value that indicates whether the map displays a compass control.
- [showsPitchControl](showspitchcontrol.md) — A Boolean value that indicates whether the map displays the pitch control.
- [showsScale](showsscale.md) — A Boolean value that indicates whether the map shows scale information.
- [showsBuildings](showsbuildings.md) — A Boolean value that indicates whether the map displays extruded building information on supported map types. _(deprecated)_
- [showsPointsOfInterest](showspointsofinterest.md) — A Boolean value that indicates whether the map displays point-of-interest information. _(deprecated)_
- [pointOfInterestFilter](pointofinterestfilter.md) — The filter to use for determining the points of interest that appear on the map. _(deprecated)_
- [showsTraffic](showstraffic.md) — A Boolean value that indicates whether the map displays traffic information. _(deprecated)_
