---
title: showsTraffic
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+（27.0 起废弃）, iPadOS 9.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.11+（27.0 起废弃）, tvOS 9.2+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/mapkit/mkmapview/showstraffic
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/showstraffic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/showstraffic.json'
content_hash: 'sha256:0c7df419a96b8694'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# showsTraffic

<sub>Instance Property</sub>

A Boolean value that indicates whether the map displays traffic information.

> [!warning] Deprecated
> Use [MKStandardMapConfiguration](../mkstandardmapconfiguration.md) or [MKHybridMapConfiguration](../mkhybridmapconfiguration.md) and configure the `showsTraffic` property instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var showsTraffic: Bool { get set }
```

## Discussion

The [mapType](maptype.md) property must be set to [MKMapTypeStandard](../mkmaptype/standard.md) or [MKMapTypeHybrid](../mkmaptype/hybrid.md) for traffic information to be shown. The default value of this property is [false](../../swift/false.md).

## See Also

### Configuring the map display

- [- setCamera:animated:](<setcamera(__animated_).md>) — Changes the camera to use for determining the map’s viewing parameters, and optionally animates the change.
- [camera](camera.md) — The camera to use for determining the appearance of the map.
- [showsCompass](showscompass.md) — A Boolean value that indicates whether the map displays a compass control.
- [showsPitchControl](showspitchcontrol.md) — A Boolean value that indicates whether the map displays the pitch control.
- [showsScale](showsscale.md) — A Boolean value that indicates whether the map shows scale information.
- [showsZoomControls](showszoomcontrols.md) — A Boolean value that indicates whether the map displays zoom controls.
- [showsBuildings](showsbuildings.md) — A Boolean value that indicates whether the map displays extruded building information on supported map types. _(deprecated)_
- [showsPointsOfInterest](showspointsofinterest.md) — A Boolean value that indicates whether the map displays point-of-interest information. _(deprecated)_
- [pointOfInterestFilter](pointofinterestfilter.md) — The filter to use for determining the points of interest that appear on the map. _(deprecated)_
