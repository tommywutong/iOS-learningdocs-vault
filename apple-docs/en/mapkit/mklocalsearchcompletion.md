---
title: MKLocalSearchCompletion
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.3+, iPadOS 9.3+, Mac Catalyst 13.1+, macOS 10.11.4+, tvOS 9.2+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mklocalsearchcompletion
source_url: 'https://developer.apple.com/documentation/mapkit/mklocalsearchcompletion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklocalsearchcompletion.json'
content_hash: 'sha256:edd630de56642f99'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKLocalSearchCompletion

<sub>Class</sub>

A fully formed string that completes a partial string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class MKLocalSearchCompletion
```

## Overview

You don’t create instances of this class directly. Instead, you use an [MKLocalSearchCompleter](mklocalsearchcompleter.md) to initiate a search based on a set of partial search strings. That object stores any matches in its results property. Retrieve any `MKLocalSearchCompletion` objects from that property and display the search terms in your interface, or use one to initiate a search for content based on that search term.

When displaying text completions for a partial search term in your user interface, you might want to use a bold version of a font or add some other highlighting to the portion of the completion string that causes it to match the partial search term. To help you add this styling, the completion object includes highlight ranges for the title and subtitle strings.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Getting the search completions

- [title](mklocalsearchcompletion/title.md) — The title string associated with the point of interest.
- [subtitle](mklocalsearchcompletion/subtitle.md) — The subtitle (if any) associated with the point of interest.
- [titleHighlightRanges](mklocalsearchcompletion/titlehighlightranges.md) — The ranges of characters to highlight in the title string.
- [subtitleHighlightRanges](mklocalsearchcompletion/subtitlehighlightranges.md) — The ranges of characters to highlight in the subtitle string.

## See Also

### Local search

- [Interacting with nearby points of interest](interacting-with-nearby-points-of-interest.md) — Provide automatic search completions for a partial search query, search the map for relevant locations nearby, and retrieve details for selected points of interest.
- [MKLocalSearchRegionPriority](mklocalsearchregionpriority.md) — A value that indicates the importance of the configured region.
- [ResultType](mklocalsearch/resulttype.md) — Options that indicate types of search results.
- [MKLocalSearch](mklocalsearch.md) — A utility object for initiating map-based searches and processing the results.
- [Options](mkaddressfilter/options.md) — A structure that contains options for filtering results in a search.
- [MKAddressFilter](mkaddressfilter.md) — An object that filters which address options to include or exclude in search results.
- [ResultType](mklocalsearchcompleter/resulttype.md) — Options that indicate types of search completions.
- [MKLocalSearchCompleter](mklocalsearchcompleter.md) — A utility object for generating a list of completion strings based on a partial search string that you provide.
- [MKLocalPointsOfInterestRequest](mklocalpointsofinterestrequest.md) — A structured request to use when searching for points of interest.
