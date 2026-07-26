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
doc_path: /documentation/mapkit/mklocalsearchcompleter/pointofinterestfilter
source_url: 'https://developer.apple.com/documentation/mapkit/mklocalsearchcompleter/pointofinterestfilter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklocalsearchcompleter/pointofinterestfilter.json'
content_hash: 'sha256:c6b09dff4aa79d01'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKLocalSearchCompleter](../mklocalsearchcompleter.md)

# pointOfInterestFilter

<sub>Instance Property</sub>

A filter that lists point of interest categories to include or exclude in the search.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying var pointOfInterestFilter: MKPointOfInterestFilter? { get set }
```

## See Also

### Specifying the query attributes

- [addressFilter](addressfilter.md) — A filter that lists which address options to include or exclude in search results.
- [queryFragment](queryfragment.md) — The search string that you want completions for.
- [region](region.md) — The region that defines the geographic scope of the search.
- [regionPriority](regionpriority.md) — A value that indicates the importance of the configured region.
- [resultTypes](resulttypes.md) — The types of search completions to include.
- [filterType](filtertype-swift.property.md) — The filter options for the search results. _(deprecated)_
- [FilterType](filtertype-swift.enum.md) — Constants indicating the types of search completions to return. _(deprecated)_
- [ResultType](resulttype.md) — Options that indicate types of search completions.
