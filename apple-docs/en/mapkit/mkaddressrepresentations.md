---
title: MKAddressRepresentations
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkaddressrepresentations
source_url: 'https://developer.apple.com/documentation/mapkit/mkaddressrepresentations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkaddressrepresentations.json'
content_hash: 'sha256:49fd7e98c21efede'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKAddressRepresentations

<sub>Class</sub>

A class that provides formatted address strings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class MKAddressRepresentations
```

## Discussion

Use this class to obtain formatted address strings for a place’s full address, city, or region.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Getting parts of an address

- [cityName](mkaddressrepresentations/cityname.md) — The name of the city.
- [cityWithContext](mkaddressrepresentations/citywithcontext.md) — The city name along with the country name, to provide additional disambiguating context.
- [regionName](mkaddressrepresentations/regionname.md) — The region name, such as “United States”.
- [region](mkaddressrepresentations/region.md)

### Getting a full address and city name

- [- fullAddressIncludingRegion:singleLine:](<mkaddressrepresentations/fulladdress(includingregion_singleline_).md>) — Returns the the location’s full address, optionally including the country or on a single link without line breaks.
- [- cityWithContextUsingStyle:](<mkaddressrepresentations/citywithcontext(__).md>) — The city name and, optionally and if applicable, state and region to provide additional disambiguating context.

### Controlling the degree of disambiguation to include in an address representation

- [ContextStyle](mkaddressrepresentations/contextstyle.md) — Values that describe the degree of disambiguation context to include in an address representation.

## See Also

### Representing places and addresses

- [MKMapItem](mkmapitem.md) — A point of interest on the map.
- [MKAddress](mkaddress.md) — A class that contains a full address, and, optionally, a short address.
- [GeoToolbox](../geotoolbox.md) — Determine place descriptor information for map coordinates.
