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
doc_path: /documentation/mapkit/mkmapsnapshotter/options/pointofinterestfilter
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/options/pointofinterestfilter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapsnapshotter/options/pointofinterestfilter.json'
content_hash: 'sha256:25db52008928d99b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKMapSnapshotter](../../mkmapsnapshotter.md) · [Options](../options.md)

# pointOfInterestFilter

<sub>Instance Property</sub>

The filter to use for determining the points of interest that appear in the snapshot.

> [!warning] Deprecated
> Use preferredConfiguration

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@NSCopying var pointOfInterestFilter: MKPointOfInterestFilter? { get set }
```

## See Also

### Configuring the map data

- [preferredConfiguration](preferredconfiguration.md) — The map configuration style to use for snapshots.
- [mapType](maptype.md) — The map’s visual style. _(deprecated)_
- [showsBuildings](showsbuildings.md) — A Boolean that indicates whether the map displays extruded building information. _(deprecated)_
- [showsPointsOfInterest](showspointsofinterest.md) — A Boolean value that indicates whether the map displays point-of-interest information. _(deprecated)_
