---
title: pointOfInterestFilter
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/mapkit/mkmapview/pointofinterestfilter
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/pointofinterestfilter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/pointofinterestfilter.json'
content_hash: 'sha256:ace5328e7b79ea45'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# pointOfInterestFilter

<sub>Instance Property</sub>

The filter to use for determining the points of interest that appear on the map.

> [!warning] Deprecated
> Use one of the map configurations that support an [MKPointOfInterestFilter](../mkpointofinterestfilter.md), such as  [MKStandardMapConfiguration](../mkstandardmapconfiguration.md) or [MKHybridMapConfiguration](../mkhybridmapconfiguration.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@NSCopying var pointOfInterestFilter: MKPointOfInterestFilter? { get set }
```

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
- [showsTraffic](showstraffic.md) — A Boolean value that indicates whether the map displays traffic information. _(deprecated)_
