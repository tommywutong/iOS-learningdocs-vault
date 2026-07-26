---
title: preferredConfiguration
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapsnapshotter/options/preferredconfiguration
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/options/preferredconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapsnapshotter/options/preferredconfiguration.json'
content_hash: 'sha256:ad9d4dfb61486ba3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKMapSnapshotter](../../mkmapsnapshotter.md) · [Options](../options.md)

# preferredConfiguration

<sub>Instance Property</sub>

The map configuration style to use for snapshots.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying var preferredConfiguration: MKMapConfiguration { get set }
```

## Discussion

Set this property to one of the [MKMapConfiguration](../../mkmapconfiguration.md) subclasses to configure the map style to use when making map snapshots.

## See Also

### Configuring the map data

- [mapType](maptype.md) — The map’s visual style. _(deprecated)_
- [showsBuildings](showsbuildings.md) — A Boolean that indicates whether the map displays extruded building information. _(deprecated)_
- [pointOfInterestFilter](pointofinterestfilter.md) — The filter to use for determining the points of interest that appear in the snapshot. _(deprecated)_
- [showsPointsOfInterest](showspointsofinterest.md) — A Boolean value that indicates whether the map displays point-of-interest information. _(deprecated)_
