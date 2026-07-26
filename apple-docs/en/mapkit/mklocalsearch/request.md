---
title: MKLocalSearch.Request
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 6.1+, iPadOS 6.1+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mklocalsearch/request
source_url: 'https://developer.apple.com/documentation/mapkit/mklocalsearch/request'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklocalsearch/request.json'
content_hash: 'sha256:1a9b8ef53b99bdf2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKLocalSearch](../mklocalsearch.md)

# MKLocalSearch.Request

<sub>Class</sub>

The parameters to use when searching for points of interest on the map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class Request
```

## Overview

You create an [Request](request.md) object when you want to search for map locations based on a natural language string. For example, if your interface allows the user to type in addresses, place the typed text in this object and pass it to an [MKLocalSearch](../mklocalsearch.md) object to begin the search process. When specifying your search strings, include a map region to narrow the search results to the specified geographical area.

When creating an MKLocalSearch.Request object yourself, set the [naturalLanguageQuery](request/naturallanguagequery.md) property to an appropriate search string, as in the following example:

**Swift**

```swift
let searchRequest = MKLocalSearch.Request()
searchRequest.naturalLanguageQuery = "coffee"

// Set the region to an associated map view's region.
searchRequest.region = myMapView.region

let search = MKLocalSearch(request: searchRequest)
search.start { (response, error) in
    guard let response = response else {
        // Handle the error.
    }
    
    for item in response.mapItems {
        if let name = item.name,
            let location = item.placemark.location {
            print("\(name): \(location.coordinate.latitude),\(location.coordinate.longitude)")
        }
    }
}
```

**Objective-C**

```objc
MKLocalSearchRequest *searchRequest = [[MKLocalSearchRequest alloc] init];
searchRequest.naturalLanguageQuery = @"coffee";

// Set the region to an associated map view's region.
searchRequest.region = self.myMapView.region;

MKLocalSearch *search = [[MKLocalSearch alloc] initWithRequest:searchRequest];
[search startWithCompletionHandler:^(MKLocalSearchResponse *response, NSError *error) {
    if (response) {
        for (MKMapItem *item in response.mapItems) {
            CLLocationCoordinate2D coordinate = item.placemark.coordinate;
            NSLog(@"%@: %f,%f", item.name, coordinate.latitude, coordinate.longitude);
        }
    } else if (error) {
        // Handle the error.
    }
}];
```

If your app uses an [MKLocalSearchCompleter](../mklocalsearchcompleter.md) object to implement autocomplete support for user-supplied search strings, initialize your search request using the search completion that the user selects. In that case, use the [- initWithCompletion:](<request/init(completion_).md>) method instead of the [init()](<../../objectivec/nsobject-swift.class/init().md>) method to initialize your search request object. The completion object automatically provides the value for the [naturalLanguageQuery](request/naturallanguagequery.md) property.

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSCopying](../../foundation/nscopying.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md)

## Topics

### Creating a local search request

- [- init](<request/init().md>) — Creates a local search request.
- [- initWithCompletion:](<request/init(completion_).md>) — Creates and returns a search request based on the specified search completion data.

### Initializing a natural language search request

- [- initWithNaturalLanguageQuery:](<request/init(naturallanguagequery_).md>) — Initializes and returns a local search request based on the provided string.
- [- initWithNaturalLanguageQuery:region:](<request/init(naturallanguagequery_region_).md>) — Initializes and returns a local search request based on the provided string and region.

### Configuring the search parameters

- [addressFilter](request/addressfilter.md) — A filter that lists which address options to include or exclude in search results.
- [naturalLanguageQuery](request/naturallanguagequery.md) — A string containing the desired search item.
- [region](request/region.md) — A map region that provides a hint as to where to search.
- [MKLocalSearchResultTypePhysicalFeature](resulttype/physicalfeature.md) — A value that indicates that search results include physical features.
- [pointOfInterestFilter](request/pointofinterestfilter.md) — A filter that lists point-of-interest categories to include or exclude in search results.
- [regionPriority](request/regionpriority.md) — A value that indicates the importance of the configured region.
- [resultTypes](request/resulttypes.md) — The types of items to include in the search results.
- [ResultType](request/resulttype.md) — Options that indicate types of search results.

## See Also

### Creating a search request

- [- initWithRequest:](<init(request_)-12tf0.md>) — Creates and returns a search object with the specified parameters.
- [- initWithPointsOfInterestRequest:](<init(request_)-9x8kn.md>) — Creates and returns a search object for fetching points of interest.
- [ResultType](resulttype.md) — Options that indicate types of search results.
