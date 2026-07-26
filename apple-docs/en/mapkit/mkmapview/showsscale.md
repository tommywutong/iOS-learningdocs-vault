---
title: showsScale
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapview/showsscale
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/showsscale'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/showsscale.json'
content_hash: 'sha256:ec9549e911d038a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# showsScale

<sub>Instance Property</sub>

A Boolean value that indicates whether the map shows scale information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var showsScale: Bool { get set }
```

## Discussion

The default value of this property is [false](../../swift/false.md).

## See Also

### Configuring the map display

- [- setCamera:animated:](<setcamera(__animated_).md>) — Changes the camera to use for determining the map’s viewing parameters, and optionally animates the change.
- [camera](camera.md) — The camera to use for determining the appearance of the map.
- [showsCompass](showscompass.md) — A Boolean value that indicates whether the map displays a compass control.
- [showsPitchControl](showspitchcontrol.md) — A Boolean value that indicates whether the map displays the pitch control.
- [showsZoomControls](showszoomcontrols.md) — A Boolean value that indicates whether the map displays zoom controls.
- [showsBuildings](showsbuildings.md) — A Boolean value that indicates whether the map displays extruded building information on supported map types. _(deprecated)_
- [showsPointsOfInterest](showspointsofinterest.md) — A Boolean value that indicates whether the map displays point-of-interest information. _(deprecated)_
- [pointOfInterestFilter](pointofinterestfilter.md) — The filter to use for determining the points of interest that appear on the map. _(deprecated)_
- [showsTraffic](showstraffic.md) — A Boolean value that indicates whether the map displays traffic information. _(deprecated)_
