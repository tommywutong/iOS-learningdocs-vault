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
doc_path: /documentation/mapkit/mkmapsnapshotter/options/showsbuildings
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/options/showsbuildings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapsnapshotter/options/showsbuildings.json'
content_hash: 'sha256:d0739d2a04ad6e15'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKMapSnapshotter](../../mkmapsnapshotter.md) · [Options](../options.md)

# showsBuildings

<sub>Instance Property</sub>

A Boolean that indicates whether the map displays extruded building information.

> [!warning] Deprecated
> MapKit no longer supports this option.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var showsBuildings: Bool { get set }
```

## Discussion

When you set this property to [true](../../../swift/true.md) and the camera has a pitch angle greater than 0, the map extrudes buildings so that they appear to extend above the map plane, creating a 3D effect. You need to set the [mapType](maptype.md) property must to [MKMapTypeStandard](../../mkmaptype/standard.md) for the map to display extruded buildings. The default value of this property is [true](../../../swift/true.md).

## See Also

### Configuring the map data

- [preferredConfiguration](preferredconfiguration.md) — The map configuration style to use for snapshots.
- [mapType](maptype.md) — The map’s visual style. _(deprecated)_
- [pointOfInterestFilter](pointofinterestfilter.md) — The filter to use for determining the points of interest that appear in the snapshot. _(deprecated)_
- [showsPointsOfInterest](showspointsofinterest.md) — A Boolean value that indicates whether the map displays point-of-interest information. _(deprecated)_
