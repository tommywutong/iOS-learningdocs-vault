---
title: region
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.1+, iPadOS 6.1+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mklocalsearch/request/region
source_url: 'https://developer.apple.com/documentation/mapkit/mklocalsearch/request/region'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklocalsearch/request/region.json'
content_hash: 'sha256:c7ce38eacd1ee176'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKLocalSearch](../../mklocalsearch.md) · [Request](../request.md)

# region

<sub>Instance Property</sub>

A map region that provides a hint as to where to search.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var region: MKCoordinateRegion { get set }
```

## Discussion

You can use this parameter to narrow the list of search results to those inside or close to the specified region. Specifying a region doesn’t ensure that the results are all inside the region. It’s merely a hint to the search engine.

## See Also

### Configuring the search parameters

- [addressFilter](addressfilter.md) — A filter that lists which address options to include or exclude in search results.
- [naturalLanguageQuery](naturallanguagequery.md) — A string containing the desired search item.
- [MKLocalSearchResultTypePhysicalFeature](../resulttype/physicalfeature.md) — A value that indicates that search results include physical features.
- [pointOfInterestFilter](pointofinterestfilter.md) — A filter that lists point-of-interest categories to include or exclude in search results.
- [regionPriority](regionpriority.md) — A value that indicates the importance of the configured region.
- [resultTypes](resulttypes.md) — The types of items to include in the search results.
- [ResultType](resulttype.md) — Options that indicate types of search results.
