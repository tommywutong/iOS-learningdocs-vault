---
title: regionPriority
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mklocalsearchcompleter/regionpriority
source_url: 'https://developer.apple.com/documentation/mapkit/mklocalsearchcompleter/regionpriority'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklocalsearchcompleter/regionpriority.json'
content_hash: 'sha256:c4f9d38ec24f4cec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKLocalSearchCompleter](../mklocalsearchcompleter.md)

# regionPriority

<sub>Instance Property</sub>

A value that indicates the importance of the configured region.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var regionPriority: MKLocalSearchRegionPriority { get set }
```

## See Also

### Specifying the query attributes

- [addressFilter](addressfilter.md) — A filter that lists which address options to include or exclude in search results.
- [queryFragment](queryfragment.md) — The search string that you want completions for.
- [region](region.md) — The region that defines the geographic scope of the search.
- [resultTypes](resulttypes.md) — The types of search completions to include.
- [pointOfInterestFilter](pointofinterestfilter.md) — A filter that lists point of interest categories to include or exclude in the search.
- [filterType](filtertype-swift.property.md) — The filter options for the search results. _(deprecated)_
- [FilterType](filtertype-swift.enum.md) — Constants indicating the types of search completions to return. _(deprecated)_
- [ResultType](resulttype.md) — Options that indicate types of search completions.
