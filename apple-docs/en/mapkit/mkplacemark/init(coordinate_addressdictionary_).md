---
title: 'init(coordinate:addressDictionary:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.0+（26.0 起废弃）, iPadOS 3.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, macOS 10.9+（26.0 起废弃）, tvOS 9.2+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）, watchOS 2.0+（26.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/mapkit/mkplacemark/init(coordinate:addressdictionary:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkplacemark/init(coordinate:addressdictionary:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkplacemark/init%28coordinate%3Aaddressdictionary%3A%29.json'
content_hash: 'sha256:375deae14a080444'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKPlacemark](../mkplacemark.md)

# init(coordinate:addressDictionary:)

<sub>Initializer</sub>

Creates and returns a placemark object using the specified coordinate and Address Book dictionary.

> [!warning] Deprecated
> Use MKMapItem's location, address and addressRepresentations properties instead. Use MKAddressRepresentations for formatted address strings for MapKit provided MKMapItems

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(coordinate: CLLocationCoordinate2D, addressDictionary: [String : Any]?)
```

## Parameters

- `coordinate` — The geographic coordinate to associate with the placemark.

- `addressDictionary` — A dictionary containing keys and values from an Address Book record. For a list of strings that you can use for the keys of this dictionary, see the “Address Property” constants in `ABPerson`. All of the keys in should be at the top level of the dictionary.

## Return Value

An initialized `MKPlacemark` object.

## Discussion

You can create placemark objects manually for entities for which you already have address information, such as contacts in the Address Book. Creating a placemark object explicitly avoids the need to query the reverse geocoder object for the same information.

## See Also

### Related Documentation

- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)

### Creating a placemark object

- [- initWithCoordinate:](<init(coordinate_).md>) — Creates and returns a placemark object using the specified coordinate. _(deprecated)_
- [- initWithCoordinate:postalAddress:](<init(coordinate_postaladdress_).md>) — Creates and returns a placemark object with the specified coordinate and postal address from the user’s Contacts database. _(deprecated)_
