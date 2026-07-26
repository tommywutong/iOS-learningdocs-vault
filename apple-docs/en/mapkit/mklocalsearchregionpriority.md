---
title: MKLocalSearchRegionPriority
framework: MapKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mklocalsearchregionpriority
source_url: 'https://developer.apple.com/documentation/mapkit/mklocalsearchregionpriority'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklocalsearchregionpriority.json'
content_hash: 'sha256:ae816e30c9ab39ab'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKLocalSearchRegionPriority

<sub>Enumeration</sub>

A value that indicates the importance of the configured region.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum MKLocalSearchRegionPriority
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Setting region priority

- [MKLocalSearchRegionPriorityDefault](mklocalsearchregionpriority/default.md) — A value indicating that the results can originate from outside the specified region.
- [MKLocalSearchRegionPriorityRequired](mklocalsearchregionpriority/required.md) — A value indicating that no results can originate from outside the specified region.

### Initializers

- [init(rawValue:)](<mklocalsearchregionpriority/init(rawvalue_).md>)

## See Also

### Local search

- [Interacting with nearby points of interest](interacting-with-nearby-points-of-interest.md) — Provide automatic search completions for a partial search query, search the map for relevant locations nearby, and retrieve details for selected points of interest.
- [ResultType](mklocalsearch/resulttype.md) — Options that indicate types of search results.
- [MKLocalSearch](mklocalsearch.md) — A utility object for initiating map-based searches and processing the results.
- [Options](mkaddressfilter/options.md) — A structure that contains options for filtering results in a search.
- [MKAddressFilter](mkaddressfilter.md) — An object that filters which address options to include or exclude in search results.
- [ResultType](mklocalsearchcompleter/resulttype.md) — Options that indicate types of search completions.
- [MKLocalSearchCompleter](mklocalsearchcompleter.md) — A utility object for generating a list of completion strings based on a partial search string that you provide.
- [MKLocalSearchCompletion](mklocalsearchcompletion.md) — A fully formed string that completes a partial string.
- [MKLocalPointsOfInterestRequest](mklocalpointsofinterestrequest.md) — A structured request to use when searching for points of interest.
