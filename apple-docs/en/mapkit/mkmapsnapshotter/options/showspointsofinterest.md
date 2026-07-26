---
title: showsPointsOfInterest
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+（13.0 起废弃）, iPadOS 7.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.9+（10.15 起废弃）, tvOS 9.2+（13.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/mapkit/mkmapsnapshotter/options/showspointsofinterest
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/options/showspointsofinterest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapsnapshotter/options/showspointsofinterest.json'
content_hash: 'sha256:5c348c560e187e54'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKMapSnapshotter](../../mkmapsnapshotter.md) · [Options](../options.md)

# showsPointsOfInterest

<sub>Instance Property</sub>

A Boolean value that indicates whether the map displays point-of-interest information.

> [!warning] Deprecated
> Use [pointOfInterestFilter](pointofinterestfilter.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var showsPointsOfInterest: Bool { get set }
```

## Discussion

When this property is set to [true](../../../swift/true.md), the map displays icons and labels for restaurants, schools, and other relevant points of interest. The default value of this property is [true](../../../swift/true.md).

## See Also

### Properties

- [filterType](../../mklocalsearchcompleter/filtertype-swift.property.md) — The filter options for the search results. _(deprecated)_
- [pinColor](../../mkpinannotationview/pincolor.md) — The color of the pin head. _(deprecated)_
- [showsPointsOfInterest](../../mkmapview/showspointsofinterest.md) — A Boolean value that indicates whether the map displays point-of-interest information. _(deprecated)_
- [mapType](maptype.md) — The map’s visual style. _(deprecated)_
