---
title: MKLocalSearch
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 6.1+, iPadOS 6.1+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mklocalsearch
source_url: 'https://developer.apple.com/documentation/mapkit/mklocalsearch'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklocalsearch.json'
content_hash: 'sha256:aa9ab927178ad6fd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKLocalSearch

<sub>Class</sub>

A utility object for initiating map-based searches and processing the results.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class MKLocalSearch
```

## Overview

Use an [MKLocalSearch](mklocalsearch.md) object to execute a single search request. You might use this class to search for addresses or points of interest on the map. Upon completion of the request, the object delivers the results to the completion handler that you provide.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a search request

- [- initWithRequest:](<mklocalsearch/init(request_)-12tf0.md>) — Creates and returns a search object with the specified parameters.
- [- initWithPointsOfInterestRequest:](<mklocalsearch/init(request_)-9x8kn.md>) — Creates and returns a search object for fetching points of interest.
- [Request](mklocalsearch/request.md) — The parameters to use when searching for points of interest on the map.
- [ResultType](mklocalsearch/resulttype.md) — Options that indicate types of search results.

### Performing the search

- [- startWithCompletionHandler:](<mklocalsearch/start(completionhandler_).md>) — Starts the search and delivers the results to the specified completion handler.
- [CompletionHandler](mklocalsearch/completionhandler.md) — A completion handler block for a search operation.
- [searching](mklocalsearch/issearching.md) — A Boolean value that indicates whether the search is in progress.
- [- cancel](<mklocalsearch/cancel().md>) — Cancels an in-progress search operation.

### Getting search results

- [Response](mklocalsearch/response.md) — The results from a map-based search.

### Initializers

- [init(pointsOfInterestRequest:)](<mklocalsearch/init(pointsofinterestrequest_).md>)

## See Also

### Local search

- [Interacting with nearby points of interest](interacting-with-nearby-points-of-interest.md) — Provide automatic search completions for a partial search query, search the map for relevant locations nearby, and retrieve details for selected points of interest.
- [MKLocalSearchRegionPriority](mklocalsearchregionpriority.md) — A value that indicates the importance of the configured region.
- [ResultType](mklocalsearch/resulttype.md) — Options that indicate types of search results.
- [Options](mkaddressfilter/options.md) — A structure that contains options for filtering results in a search.
- [MKAddressFilter](mkaddressfilter.md) — An object that filters which address options to include or exclude in search results.
- [ResultType](mklocalsearchcompleter/resulttype.md) — Options that indicate types of search completions.
- [MKLocalSearchCompleter](mklocalsearchcompleter.md) — A utility object for generating a list of completion strings based on a partial search string that you provide.
- [MKLocalSearchCompletion](mklocalsearchcompletion.md) — A fully formed string that completes a partial string.
- [MKLocalPointsOfInterestRequest](mklocalpointsofinterestrequest.md) — A structured request to use when searching for points of interest.
