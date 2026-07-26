---
title: naturalLanguageQuery
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.1+, iPadOS 6.1+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mklocalsearch/request/naturallanguagequery
source_url: 'https://developer.apple.com/documentation/mapkit/mklocalsearch/request/naturallanguagequery'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklocalsearch/request/naturallanguagequery.json'
content_hash: 'sha256:96e0ad5026293dbf'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKLocalSearch](../../mklocalsearch.md) · [Request](../request.md)

# naturalLanguageQuery

<sub>Instance Property</sub>

A string containing the desired search item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var naturalLanguageQuery: String? { get set }
```

## Discussion

You specify this parameter as a string describing the map-based item you want to look for. The text is equivalent to what the user would type in a search field in the Maps app. For example, the text might contain all or part of an address or it might contain the name of a point of interest.

## See Also

### Configuring the search parameters

- [addressFilter](addressfilter.md) — A filter that lists which address options to include or exclude in search results.
- [region](region.md) — A map region that provides a hint as to where to search.
- [MKLocalSearchResultTypePhysicalFeature](../resulttype/physicalfeature.md) — A value that indicates that search results include physical features.
- [pointOfInterestFilter](pointofinterestfilter.md) — A filter that lists point-of-interest categories to include or exclude in search results.
- [regionPriority](regionpriority.md) — A value that indicates the importance of the configured region.
- [resultTypes](resulttypes.md) — The types of items to include in the search results.
- [ResultType](resulttype.md) — Options that indicate types of search results.
