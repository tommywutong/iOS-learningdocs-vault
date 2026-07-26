---
title: MKLocalSearchCompleter.ResultType
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mklocalsearchcompleter/resulttype
source_url: 'https://developer.apple.com/documentation/mapkit/mklocalsearchcompleter/resulttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklocalsearchcompleter/resulttype.json'
content_hash: 'sha256:18bdd6e62a23e7ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKLocalSearchCompleter](../mklocalsearchcompleter.md)

# MKLocalSearchCompleter.ResultType

<sub>Structure</sub>

Options that indicate types of search completions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ResultType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Type properties

- [MKLocalSearchCompleterResultTypeAddress](resulttype/address.md) — A value that indicates that the search completer includes address completions in the result.
- [MKLocalSearchCompleterResultTypePointOfInterest](resulttype/pointofinterest.md) — A value that indicates that the search completer includes point-of-interest completions in the result.
- [MKLocalSearchCompleterResultTypePhysicalFeature](resulttype/physicalfeature.md) — A value that indicates that the search completer includes physical feature completions in the result.
- [MKLocalSearchCompleterResultTypeQuery](resulttype/query.md) — A value that indicates that the search completer includes query completions in the result.

### Initializers

- [init(rawValue:)](<resulttype/init(rawvalue_).md>) — Creates a direction transport type using a raw unsigned integer value.
- [MKLocalSearchCompleterResultTypeAddress](resulttype/address.md) — A value that indicates that the search completer includes address completions in the result.
- [MKLocalSearchCompleterResultTypePointOfInterest](resulttype/pointofinterest.md) — A value that indicates that the search completer includes point-of-interest completions in the result.
- [MKLocalSearchCompleterResultTypePhysicalFeature](resulttype/physicalfeature.md) — A value that indicates that the search completer includes physical feature completions in the result.
- [MKLocalSearchCompleterResultTypeQuery](resulttype/query.md) — A value that indicates that the search completer includes query completions in the result.

## See Also

### Local search

- [Interacting with nearby points of interest](../interacting-with-nearby-points-of-interest.md) — Provide automatic search completions for a partial search query, search the map for relevant locations nearby, and retrieve details for selected points of interest.
- [MKLocalSearchRegionPriority](../mklocalsearchregionpriority.md) — A value that indicates the importance of the configured region.
- [ResultType](../mklocalsearch/resulttype.md) — Options that indicate types of search results.
- [MKLocalSearch](../mklocalsearch.md) — A utility object for initiating map-based searches and processing the results.
- [Options](../mkaddressfilter/options.md) — A structure that contains options for filtering results in a search.
- [MKAddressFilter](../mkaddressfilter.md) — An object that filters which address options to include or exclude in search results.
- [MKLocalSearchCompleter](../mklocalsearchcompleter.md) — A utility object for generating a list of completion strings based on a partial search string that you provide.
- [MKLocalSearchCompletion](../mklocalsearchcompletion.md) — A fully formed string that completes a partial string.
- [MKLocalPointsOfInterestRequest](../mklocalpointsofinterestrequest.md) — A structured request to use when searching for points of interest.
