---
title: MKAddress
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkaddress
source_url: 'https://developer.apple.com/documentation/mapkit/mkaddress'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkaddress.json'
content_hash: 'sha256:e13c0a83ef8f1602'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKAddress

<sub>Class</sub>

A class that contains a full address, and, optionally, a short address.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class MKAddress
```

## Discussion

MapKit capabilities, such as Search and Reverse geocoding, populate the [MKAddress](mkaddress.md) of a [MKMapItem](mkmapitem.md) with a full address, and a short address, if the framework has one.

When presenting a Place Card using an [MKMapItemDetailViewController](mkmapitemdetailviewcontroller.md) or a selection accessory on an annotation you created using an [MKMapItem](mkmapitem.md), MapKit uses the full address provided if you create the `MKMapitem` using [- initWithLocation:address:](<mkmapitem/init(location_address_).md>).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating an address

- [- initWithFullAddress:shortAddress:](<mkaddress/init(fulladdress_shortaddress_).md>) — Initializes a new address with a location’s full address using a string and a short address that provides an abbreviated form of the address such as a street address.

### Getting the full and short addresses

- [fullAddress](mkaddress/fulladdress.md) — A string that represents a place’s full address
- [shortAddress](mkaddress/shortaddress.md) — A  string that represents the short address of a location, such as it’s street address and city.

## See Also

### Representing places and addresses

- [MKMapItem](mkmapitem.md) — A point of interest on the map.
- [MKAddressRepresentations](mkaddressrepresentations.md) — A class that provides formatted address strings.
- [GeoToolbox](../geotoolbox.md) — Determine place descriptor information for map coordinates.
