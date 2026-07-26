---
title: MKMapItemRequest
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapitemrequest
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapitemrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapitemrequest.json'
content_hash: 'sha256:3eefb38f337ef15e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKMapItemRequest

<sub>Class</sub>

A utility class you use to request additional information about a map feature.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class MKMapItemRequest
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a request

- [init(feature:)](<mkmapitemrequest/init(feature_).md>) — Creates a new map item request with the specified map feature.
- [- initWithMapItemIdentifier:](<mkmapitemrequest/init(mapitemidentifier_).md>) — Create a request with a map item identifier.
- [- initWithMapFeatureAnnotation:](<mkmapitemrequest/init(mapfeatureannotation_).md>) — Creates a new map item request with the specified feature annotation.

### Configuring the item request

- [mapFeature](mkmapitemrequest/mapfeature.md) — The map feature.
- [mapFeatureAnnotation](mkmapitemrequest/mapfeatureannotation.md) — The feature annotation.
- [mapItemIdentifier](mkmapitemrequest/mapitemidentifier.md) — The map item identifer.
- [feature](mkmapitemrequest/feature.md) — The map feature. _(deprecated)_
- [featureAnnotation](mkmapitemrequest/featureannotation.md) — The feature annotation. _(deprecated)_
- [placeDescriptor](mkmapitemrequest/placedescriptor.md) — The place descriptor that contains information that’s helpful in uniquely identifying this place.

### Starting and stopping requests

- [- cancel](<mkmapitemrequest/cancel().md>) — Cancels an in-progress map item request.
- [- getMapItemWithCompletionHandler:](<mkmapitemrequest/getmapitem(completionhandler_).md>) — Requests a map item and calls the provided completion handler.

### Checking the status of a request

- [cancelled](mkmapitemrequest/iscancelled.md) — A Boolean value that indicates if the cancellation of the request was successful.
- [loading](mkmapitemrequest/isloading.md) — A Boolean value that indicates if the request is loading.

### Initializers

- [init(placeDescriptor:)](<mkmapitemrequest/init(placedescriptor_).md>) — Creates a new map item request with the specified place descriptor

## See Also

### Points of interest

- [Identifying unique locations with Place IDs](identifying-unique-locations-with-place-ids.md) — Obtain information about a point of interest that persists over its lifetime.
- [MKMapFeatureAnnotation](mkmapfeatureannotation.md) — A class that describes an annotation element on the map’s display such as a point of interest, territorial boundary, or physical feature.
- [MKMapFeatureOptions](mkmapfeatureoptions.md) — A structure you use to tell the map which kinds of features users can interact with.
- [MKIconStyle](mkiconstyle.md) — A class you use to customize the annotation view icon of a point of interest (POI) on the map.
- [MKPointOfInterestFilter](mkpointofinterestfilter.md) — A filter that includes or excludes point of interest categories from a map view, local search, or local search completer.
- [MKPointOfInterestCategory](mkpointofinterestcategory.md) — A point of interest category.
