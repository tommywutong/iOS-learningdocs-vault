---
title: MKAddressFilter
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkaddressfilter
source_url: 'https://developer.apple.com/documentation/mapkit/mkaddressfilter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkaddressfilter.json'
content_hash: 'sha256:474cdab690307073'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKAddressFilter

<sub>Class</sub>

An object that filters which address options to include or exclude in search results.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class MKAddressFilter
```

## Overview

Use this object to filter search results by criteria, such as country, region, and municipality. See [Options](mkaddressfilter/options.md) for more information.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Creating a filter

- [- initExcludingOptions:](<mkaddressfilter/init(excluding_).md>) — Creates an address filter with options for excluding results in a search.
- [- initIncludingOptions:](<mkaddressfilter/init(including_).md>) — Creates an address filter with options for including results in a search.

### Filtering results

- [Options](mkaddressfilter/options.md) — A structure that contains options for filtering results in a search.
- [filterExcludingAll](mkaddressfilter/excludingall.md) — A list of categories to exclude from a search.
- [filterIncludingAll](mkaddressfilter/includingall.md) — A list of categories to include in a search.
- [- excludesOptions:](<mkaddressfilter/excludes(__).md>) — Indicates whether options are excluded from filtering.
- [- includesOptions:](<mkaddressfilter/includes(__).md>) — Indicates whether options are included for filtering.

### Initializers

- [init(coder:)](<mkaddressfilter/init(coder_).md>)
- [init(excludingOptions:)](<mkaddressfilter/init(excludingoptions_).md>)
- [init(includingOptions:)](<mkaddressfilter/init(includingoptions_).md>)

## See Also

### Local search

- [Interacting with nearby points of interest](interacting-with-nearby-points-of-interest.md) — Provide automatic search completions for a partial search query, search the map for relevant locations nearby, and retrieve details for selected points of interest.
- [MKLocalSearchRegionPriority](mklocalsearchregionpriority.md) — A value that indicates the importance of the configured region.
- [ResultType](mklocalsearch/resulttype.md) — Options that indicate types of search results.
- [MKLocalSearch](mklocalsearch.md) — A utility object for initiating map-based searches and processing the results.
- [Options](mkaddressfilter/options.md) — A structure that contains options for filtering results in a search.
- [ResultType](mklocalsearchcompleter/resulttype.md) — Options that indicate types of search completions.
- [MKLocalSearchCompleter](mklocalsearchcompleter.md) — A utility object for generating a list of completion strings based on a partial search string that you provide.
- [MKLocalSearchCompletion](mklocalsearchcompletion.md) — A fully formed string that completes a partial string.
- [MKLocalPointsOfInterestRequest](mklocalpointsofinterestrequest.md) — A structured request to use when searching for points of interest.
