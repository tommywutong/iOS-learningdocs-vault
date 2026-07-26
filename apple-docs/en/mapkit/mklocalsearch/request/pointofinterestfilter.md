---
title: pointOfInterestFilter
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mklocalsearch/request/pointofinterestfilter
source_url: 'https://developer.apple.com/documentation/mapkit/mklocalsearch/request/pointofinterestfilter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklocalsearch/request/pointofinterestfilter.json'
content_hash: 'sha256:b0f3e3b7e95e43c9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKLocalSearch](../../mklocalsearch.md) · [Request](../request.md)

# pointOfInterestFilter

<sub>Instance Property</sub>

A filter that lists point-of-interest categories to include or exclude in search results.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying var pointOfInterestFilter: MKPointOfInterestFilter? { get set }
```

## See Also

### Configuring the search parameters

- [addressFilter](addressfilter.md) — A filter that lists which address options to include or exclude in search results.
- [naturalLanguageQuery](naturallanguagequery.md) — A string containing the desired search item.
- [region](region.md) — A map region that provides a hint as to where to search.
- [MKLocalSearchResultTypePhysicalFeature](../resulttype/physicalfeature.md) — A value that indicates that search results include physical features.
- [regionPriority](regionpriority.md) — A value that indicates the importance of the configured region.
- [resultTypes](resulttypes.md) — The types of items to include in the search results.
- [ResultType](resulttype.md) — Options that indicate types of search results.
