---
title: MKLocalSearchCompleter
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.3+, iPadOS 9.3+, Mac Catalyst 13.1+, macOS 10.11.4+, tvOS 9.2+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mklocalsearchcompleter
source_url: 'https://developer.apple.com/documentation/mapkit/mklocalsearchcompleter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklocalsearchcompleter.json'
content_hash: 'sha256:e6e684e3872c8e4f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKLocalSearchCompleter

<sub>Class</sub>

A utility object for generating a list of completion strings based on a partial search string that you provide.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class MKLocalSearchCompleter
```

## Overview

You use an [MKLocalSearchCompleter](mklocalsearchcompleter.md) object to retrieve auto-complete suggestions for your own map-based search controls. As the user types text, you feed the current text string into the search completer object, which delivers possible string completions that match locations or points of interest.

You create and configure [MKLocalSearchCompleter](mklocalsearchcompleter.md) objects yourself. You must always assign a delegate object to the search completer so that you can receive the search results that it generates. Specify a search region to restrict results to a designated area. The following code shows a simple example of a view controller that stores the [MKLocalSearchCompleter](mklocalsearchcompleter.md) object in a property. The view controller itself acts as the delegate for the completer and the view controller uses the region associated with an [MKMapView](mkmapview.md) object that’s part of the view controller’s interface. Completer objects are long-lived objects, so you can store strong references to them and reuse them later in your code.

Listing 1. Creating and configuring a search completer

**Swift**

```swift
override func viewDidLoad() {
    super.viewDidLoad()

    completer = MKLocalSearchCompleter()
    completer.delegate = self
      
    // Limit search results to the map view's current region.
    completer.region = myMapView.region
}
```

**Objective-C**

```objc
- (void)viewDidLoad {
   [super viewDidLoad];
 
   self.completer = [[MKLocalSearchCompleter alloc] init];
   self.completer.delegate = self;
 
   // Limit search results to the map view's current region.
   self.completer.region = self.myMapView.region;
}
```

Update the value of the completer’s [queryFragment](mklocalsearchcompleter/queryfragment.md) property to begin a search query. You can update this property in real time as the user types new characters into a text field because the completer object waits a short amount of time for the query string to stabilize. When modifications to the query string stop, the completer initiates a new search and returns the results to your delegate as an array of [MKLocalSearchCompletion](mklocalsearchcompletion.md) objects.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Receiving the search results

- [delegate](mklocalsearchcompleter/delegate.md) — The object that receives the completion results.
- [MKLocalSearchCompleterDelegate](mklocalsearchcompleterdelegate.md) — Methods the delegate calls with search completion data.

### Specifying the query attributes

- [addressFilter](mklocalsearchcompleter/addressfilter.md) — A filter that lists which address options to include or exclude in search results.
- [queryFragment](mklocalsearchcompleter/queryfragment.md) — The search string that you want completions for.
- [region](mklocalsearchcompleter/region.md) — The region that defines the geographic scope of the search.
- [regionPriority](mklocalsearchcompleter/regionpriority.md) — A value that indicates the importance of the configured region.
- [resultTypes](mklocalsearchcompleter/resulttypes.md) — The types of search completions to include.
- [pointOfInterestFilter](mklocalsearchcompleter/pointofinterestfilter.md) — A filter that lists point of interest categories to include or exclude in the search.
- [filterType](mklocalsearchcompleter/filtertype-swift.property.md) — The filter options for the search results. _(deprecated)_
- [FilterType](mklocalsearchcompleter/filtertype-swift.enum.md) — Constants indicating the types of search completions to return. _(deprecated)_
- [ResultType](mklocalsearchcompleter/resulttype.md) — Options that indicate types of search completions.

### Canceling the query

- [- cancel](<mklocalsearchcompleter/cancel().md>) — Cancels an in-progress search operation.
- [searching](mklocalsearchcompleter/issearching.md) — A Boolean value that indicates whether a search operation is in progress.

### Getting the current query results

- [results](mklocalsearchcompleter/results.md) — The most recently received search completions.

## See Also

### Local search

- [Interacting with nearby points of interest](interacting-with-nearby-points-of-interest.md) — Provide automatic search completions for a partial search query, search the map for relevant locations nearby, and retrieve details for selected points of interest.
- [MKLocalSearchRegionPriority](mklocalsearchregionpriority.md) — A value that indicates the importance of the configured region.
- [ResultType](mklocalsearch/resulttype.md) — Options that indicate types of search results.
- [MKLocalSearch](mklocalsearch.md) — A utility object for initiating map-based searches and processing the results.
- [Options](mkaddressfilter/options.md) — A structure that contains options for filtering results in a search.
- [MKAddressFilter](mkaddressfilter.md) — An object that filters which address options to include or exclude in search results.
- [ResultType](mklocalsearchcompleter/resulttype.md) — Options that indicate types of search completions.
- [MKLocalSearchCompletion](mklocalsearchcompletion.md) — A fully formed string that completes a partial string.
- [MKLocalPointsOfInterestRequest](mklocalpointsofinterestrequest.md) — A structured request to use when searching for points of interest.
