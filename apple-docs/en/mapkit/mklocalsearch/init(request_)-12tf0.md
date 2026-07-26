---
title: 'init(request:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 6.1+, iPadOS 6.1+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mklocalsearch/init(request:)-12tf0'
source_url: 'https://developer.apple.com/documentation/mapkit/mklocalsearch/init(request:)-12tf0'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklocalsearch/init%28request%3A%29-12tf0.json'
content_hash: 'sha256:de91d91123d76ca9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKLocalSearch](../mklocalsearch.md)

# init(request:)

<sub>Initializer</sub>

Creates and returns a search object with the specified parameters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(request: MKLocalSearch.Request)
```

## Parameters

- `request` — The search request information. This parameter can’t be `nil`.

## Return Value

An initialized search object.

## Discussion

This method stores a copy of the object in the `request` parameter. So, the object ignores any changes you make to your request object after calling this method.

## See Also

### Related Documentation

- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)

### Creating a search request

- [- initWithPointsOfInterestRequest:](<init(request_)-9x8kn.md>) — Creates and returns a search object for fetching points of interest.
- [Request](request.md) — The parameters to use when searching for points of interest on the map.
- [ResultType](resulttype.md) — Options that indicate types of search results.
