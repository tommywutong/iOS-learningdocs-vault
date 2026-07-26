---
title: filterType
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.3+（13.0 起废弃）, iPadOS 9.3+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.11.4+（10.15 起废弃）, tvOS 9.2+（13.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/mapkit/mklocalsearchcompleter/filtertype-swift.property
source_url: 'https://developer.apple.com/documentation/mapkit/mklocalsearchcompleter/filtertype-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklocalsearchcompleter/filtertype-swift.property.json'
content_hash: 'sha256:5eebeb910349ec60'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKLocalSearchCompleter](../mklocalsearchcompleter.md)

# filterType

<sub>Instance Property</sub>

The filter options for the search results.

> [!warning] Deprecated
> Use [resultTypes](resulttypes.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var filterType: MKLocalSearchCompleter.FilterType { get set }
```

## Discussion

Use this property to determine whether you want completions that represent points-of-interest or whether completions might yield additional relevant query strings.

## See Also

### Properties

- [pinColor](../mkpinannotationview/pincolor.md) — The color of the pin head. _(deprecated)_
- [showsPointsOfInterest](../mkmapview/showspointsofinterest.md) — A Boolean value that indicates whether the map displays point-of-interest information. _(deprecated)_
- [showsPointsOfInterest](../mkmapsnapshotter/options/showspointsofinterest.md) — A Boolean value that indicates whether the map displays point-of-interest information. _(deprecated)_
- [mapType](../mkmapsnapshotter/options/maptype.md) — The map’s visual style. _(deprecated)_
