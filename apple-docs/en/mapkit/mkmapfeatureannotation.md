---
title: MKMapFeatureAnnotation
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapfeatureannotation
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapfeatureannotation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapfeatureannotation.json'
content_hash: 'sha256:9b087ee25e190148'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKMapFeatureAnnotation

<sub>Class</sub>

A class that describes an annotation element on the map’s display such as a point of interest, territorial boundary, or physical feature.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class MKMapFeatureAnnotation
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [MKAnnotation](mkannotation.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Customizing the annotation

- [featureType](mkmapfeatureannotation/featuretype-swift.property.md) — The type of map feature this annotation represents.
- [FeatureType](mkmapfeatureannotation/featuretype-swift.enum.md) — Values that describe the kinds of features visible on the map.
- [iconStyle](mkmapfeatureannotation/iconstyle.md) — The icon style of a feature annotation.
- [pointOfInterestCategory](mkmapfeatureannotation/pointofinterestcategory.md) — The feature annotation’s point of interest category.

## See Also

### Points of interest

- [Identifying unique locations with Place IDs](identifying-unique-locations-with-place-ids.md) — Obtain information about a point of interest that persists over its lifetime.
- [MKMapFeatureOptions](mkmapfeatureoptions.md) — A structure you use to tell the map which kinds of features users can interact with.
- [MKMapItemRequest](mkmapitemrequest.md) — A utility class you use to request additional information about a map feature.
- [MKIconStyle](mkiconstyle.md) — A class you use to customize the annotation view icon of a point of interest (POI) on the map.
- [MKPointOfInterestFilter](mkpointofinterestfilter.md) — A filter that includes or excludes point of interest categories from a map view, local search, or local search completer.
- [MKPointOfInterestCategory](mkpointofinterestcategory.md) — A point of interest category.
