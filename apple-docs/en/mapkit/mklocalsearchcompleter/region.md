---
title: region
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.3+, iPadOS 9.3+, Mac Catalyst 13.1+, macOS 10.11.4+, tvOS 9.2+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mklocalsearchcompleter/region
source_url: 'https://developer.apple.com/documentation/mapkit/mklocalsearchcompleter/region'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklocalsearchcompleter/region.json'
content_hash: 'sha256:e066a7b2a3511492'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKLocalSearchCompleter](../mklocalsearchcompleter.md)

# region

<sub>Instance Property</sub>

The region that defines the geographic scope of the search.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var region: MKCoordinateRegion { get set }
```

## Discussion

Use this property to limit search results to the specified geographic area. The default value of this property is a region that spans the entire world.

## See Also

### Specifying the query attributes

- [addressFilter](addressfilter.md) — A filter that lists which address options to include or exclude in search results.
- [queryFragment](queryfragment.md) — The search string that you want completions for.
- [regionPriority](regionpriority.md) — A value that indicates the importance of the configured region.
- [resultTypes](resulttypes.md) — The types of search completions to include.
- [pointOfInterestFilter](pointofinterestfilter.md) — A filter that lists point of interest categories to include or exclude in the search.
- [filterType](filtertype-swift.property.md) — The filter options for the search results. _(deprecated)_
- [FilterType](filtertype-swift.enum.md) — Constants indicating the types of search completions to return. _(deprecated)_
- [ResultType](resulttype.md) — Options that indicate types of search completions.
