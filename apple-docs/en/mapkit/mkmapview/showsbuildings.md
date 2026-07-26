---
title: showsBuildings
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+（27.0 起废弃）, iPadOS 7.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.9+（27.0 起废弃）, tvOS 9.2+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/mapkit/mkmapview/showsbuildings
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/showsbuildings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/showsbuildings.json'
content_hash: 'sha256:9a56596c77d76675'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# showsBuildings

<sub>Instance Property</sub>

A Boolean value that indicates whether the map displays extruded building information on supported map types.

> [!warning] Deprecated
> Use [MKStandardMapConfiguration](../mkstandardmapconfiguration.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var showsBuildings: Bool { get set }
```

## Discussion

> [!note] Note
> In iOS 16 and macOS 13, and later, when overlay content is present, this property has no effect and the map renders buildings and trees as transparent. This enables content to be clearly visible while preserving the context of the surroundings.

When this property is [true](../../swift/true.md) and the camera has a pitch angle greater than zero, the map extrudes buildings so that they extend above the map plane, creating a 3D effect. The default value of this property is [true](../../swift/true.md).

To display extruded buildings, set the [mapType](maptype.md) property to [MKMapTypeStandard](../mkmaptype/standard.md) or [MKMapTypeMutedStandard](../mkmaptype/mutedstandard.md).

## See Also

### Configuring the map display

- [- setCamera:animated:](<setcamera(__animated_).md>) — Changes the camera to use for determining the map’s viewing parameters, and optionally animates the change.
- [camera](camera.md) — The camera to use for determining the appearance of the map.
- [showsCompass](showscompass.md) — A Boolean value that indicates whether the map displays a compass control.
- [showsPitchControl](showspitchcontrol.md) — A Boolean value that indicates whether the map displays the pitch control.
- [showsScale](showsscale.md) — A Boolean value that indicates whether the map shows scale information.
- [showsZoomControls](showszoomcontrols.md) — A Boolean value that indicates whether the map displays zoom controls.
- [showsPointsOfInterest](showspointsofinterest.md) — A Boolean value that indicates whether the map displays point-of-interest information. _(deprecated)_
- [pointOfInterestFilter](pointofinterestfilter.md) — The filter to use for determining the points of interest that appear on the map. _(deprecated)_
- [showsTraffic](showstraffic.md) — A Boolean value that indicates whether the map displays traffic information. _(deprecated)_
