---
title: 'init(coordinate:postalAddress:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+（26.0 起废弃）, iPadOS 10.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, macOS 10.12+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）, watchOS 3.0+（26.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/mapkit/mkplacemark/init(coordinate:postaladdress:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkplacemark/init(coordinate:postaladdress:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkplacemark/init%28coordinate%3Apostaladdress%3A%29.json'
content_hash: 'sha256:339d6a29a11b6741'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKPlacemark](../mkplacemark.md)

# init(coordinate:postalAddress:)

<sub>Initializer</sub>

Creates and returns a placemark object with the specified coordinate and postal address from the user’s Contacts database.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
init(coordinate: CLLocationCoordinate2D, postalAddress: CNPostalAddress)
```

## Parameters

- `coordinate` — The geographic coordinate to associate with the placemark.

- `postalAddress` — An object containing the address information from the Contacts framework.

## Return Value

An initialized [MKPlacemark](../mkplacemark.md) object.

## See Also

### Creating a placemark object

- [- initWithCoordinate:](<init(coordinate_).md>) — Creates and returns a placemark object using the specified coordinate. _(deprecated)_
- [- initWithCoordinate:addressDictionary:](<init(coordinate_addressdictionary_).md>) — Creates and returns a placemark object using the specified coordinate and Address Book dictionary. _(deprecated)_
