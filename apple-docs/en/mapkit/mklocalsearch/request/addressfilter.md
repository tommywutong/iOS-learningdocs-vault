---
title: addressFilter
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mklocalsearch/request/addressfilter
source_url: 'https://developer.apple.com/documentation/mapkit/mklocalsearch/request/addressfilter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklocalsearch/request/addressfilter.json'
content_hash: 'sha256:0732425ac2b576f0'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKLocalSearch](../../mklocalsearch.md) · [Request](../request.md)

# addressFilter

<sub>Instance Property</sub>

A filter that lists which address options to include or exclude in search results.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying var addressFilter: MKAddressFilter? { get set }
```

## See Also

### Configuring the search parameters

- [naturalLanguageQuery](naturallanguagequery.md) — A string containing the desired search item.
- [region](region.md) — A map region that provides a hint as to where to search.
- [MKLocalSearchResultTypePhysicalFeature](../resulttype/physicalfeature.md) — A value that indicates that search results include physical features.
- [pointOfInterestFilter](pointofinterestfilter.md) — A filter that lists point-of-interest categories to include or exclude in search results.
- [regionPriority](regionpriority.md) — A value that indicates the importance of the configured region.
- [resultTypes](resulttypes.md) — The types of items to include in the search results.
- [ResultType](resulttype.md) — Options that indicate types of search results.
