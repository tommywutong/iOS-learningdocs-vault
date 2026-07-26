---
title: MKLocalPointsOfInterestRequest
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mklocalpointsofinterestrequest
source_url: 'https://developer.apple.com/documentation/mapkit/mklocalpointsofinterestrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklocalpointsofinterestrequest.json'
content_hash: 'sha256:3a0c5d8177a70c5c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKLocalPointsOfInterestRequest

<sub>Class</sub>

A structured request to use when searching for points of interest.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class MKLocalPointsOfInterestRequest
```

## Overview

You create an [MKLocalPointsOfInterestRequest](mklocalpointsofinterestrequest.md) to fetch points of interest within a rectangular bounding box or circular area.

To leverage the phone’s viewport to request points of interest, create a request with a rectangular bounding box using an [MKCoordinateRegion](mkcoordinateregion.md). The request fetches points of interest within the rectangular region.

To retrieve points of interest nearby or “around the user,” create a request with a circular area defined by [CLLocationCoordinate2D](../corelocation/cllocationcoordinate2d.md) and a [CLLocationDistance](../corelocation/cllocationdistance.md) in meters. The fetch returns points of interest up to the maximum distance defined by [MKPointsOfInterestRequestMaxRadius](mklocalpointsofinterestrequest/maxradius.md).

You may optionally specifying an [MKPointOfInterestFilter](mkpointofinterestfilter.md) describing categories to include or exclude. The default behavior of the fetch returns all points of interest.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a point of interest request

- [- initWithCenterCoordinate:radius:](<mklocalpointsofinterestrequest/init(center_radius_).md>) — Creates a points of interest search request centered on the provided coordinate with the provided radius.
- [- initWithCoordinateRegion:](<mklocalpointsofinterestrequest/init(coordinateregion_).md>) — Creates a points of interest search request based on existing region.

### Configuring the request parameters

- [region](mklocalpointsofinterestrequest/region.md) — The region of the bounding box of the request provided or the derived bounding box of the circle created by the radius.
- [coordinate](mklocalpointsofinterestrequest/coordinate.md) — The center of the point of request as latitude and longitude.
- [radius](mklocalpointsofinterestrequest/radius.md) — The distance provided in meters or the longest distance derived from the center point to the region’s bounding box.
- [pointOfInterestFilter](mklocalpointsofinterestrequest/pointofinterestfilter.md) — A filter that lists points of interest categories to include or exclude.

### Getting the maximum radius

- [MKPointsOfInterestRequestMaxRadius](mklocalpointsofinterestrequest/maxradius.md) — The maximum distance respected for fetching points of interest from the center of the region.

### Initializers

- [init(centerCoordinate:radius:)](<mklocalpointsofinterestrequest/init(centercoordinate_radius_).md>)

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
- [MKLocalSearchCompletion](mklocalsearchcompletion.md) — A fully formed string that completes a partial string.
