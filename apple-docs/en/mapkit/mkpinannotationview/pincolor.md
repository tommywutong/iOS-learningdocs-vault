---
title: pinColor
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+（9.0 起废弃）, iPadOS 3.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.9+（10.11 起废弃）]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/mapkit/mkpinannotationview/pincolor
source_url: 'https://developer.apple.com/documentation/mapkit/mkpinannotationview/pincolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkpinannotationview/pincolor.json'
content_hash: 'sha256:fbce719546c1e904'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKPinAnnotationView](../mkpinannotationview.md)

# pinColor

<sub>Instance Property</sub>

The color of the pin head.

> [!warning] Deprecated
> Use [pinTintColor](pintintcolor.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var pinColor: MKPinAnnotationColor { get set }
```

## Discussion

The Maps application uses different pin colors for different types of map annotations. Your own map annotation should use the available pin colors in the same way. For a description of when to use each type of pin, see the constants of [MKPinAnnotationColor](../mkpinannotationcolor.md).

## See Also

### Properties

- [filterType](../mklocalsearchcompleter/filtertype-swift.property.md) — The filter options for the search results. _(deprecated)_
- [showsPointsOfInterest](../mkmapview/showspointsofinterest.md) — A Boolean value that indicates whether the map displays point-of-interest information. _(deprecated)_
- [showsPointsOfInterest](../mkmapsnapshotter/options/showspointsofinterest.md) — A Boolean value that indicates whether the map displays point-of-interest information. _(deprecated)_
- [mapType](../mkmapsnapshotter/options/maptype.md) — The map’s visual style. _(deprecated)_
