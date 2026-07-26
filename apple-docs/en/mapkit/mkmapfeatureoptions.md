---
title: MKMapFeatureOptions
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapfeatureoptions
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapfeatureoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapfeatureoptions.json'
content_hash: 'sha256:21b32d54049b641a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKMapFeatureOptions

<sub>Structure</sub>

A structure you use to tell the map which kinds of features users can interact with.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
struct MKMapFeatureOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<mkmapfeatureoptions/init(rawvalue_).md>) — Creates a new feature option structure with the specified value.

### Selecting interactive map features

- [MKMapFeatureOptionPhysicalFeatures](mkmapfeatureoptions/physicalfeatures.md) — The option that represents physical map features such as mountain ranges, rivers, and ocean basins.
- [MKMapFeatureOptionPointsOfInterest](mkmapfeatureoptions/pointsofinterest.md) — The option that represents points of interest such as museums, cafes, parks, or schools.
- [MKMapFeatureOptionTerritories](mkmapfeatureoptions/territories.md) — The option that represents territorial boundaries such as a national border, a state boundary, or a neighborhood.

## See Also

### Points of interest

- [Identifying unique locations with Place IDs](identifying-unique-locations-with-place-ids.md) — Obtain information about a point of interest that persists over its lifetime.
- [MKMapFeatureAnnotation](mkmapfeatureannotation.md) — A class that describes an annotation element on the map’s display such as a point of interest, territorial boundary, or physical feature.
- [MKMapItemRequest](mkmapitemrequest.md) — A utility class you use to request additional information about a map feature.
- [MKIconStyle](mkiconstyle.md) — A class you use to customize the annotation view icon of a point of interest (POI) on the map.
- [MKPointOfInterestFilter](mkpointofinterestfilter.md) — A filter that includes or excludes point of interest categories from a map view, local search, or local search completer.
- [MKPointOfInterestCategory](mkpointofinterestcategory.md) — A point of interest category.
