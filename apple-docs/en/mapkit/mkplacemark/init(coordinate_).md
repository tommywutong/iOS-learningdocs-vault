---
title: 'init(coordinate:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+（26.0 起废弃）, iPadOS 10.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, macOS 10.12+（26.0 起废弃）, tvOS 10.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）, watchOS 3.0+（26.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/mapkit/mkplacemark/init(coordinate:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkplacemark/init(coordinate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkplacemark/init%28coordinate%3A%29.json'
content_hash: 'sha256:0d35c035f0da9d1d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKPlacemark](../mkplacemark.md)

# init(coordinate:)

<sub>Initializer</sub>

Creates and returns a placemark object using the specified coordinate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(coordinate: CLLocationCoordinate2D)
```

## Parameters

- `coordinate` — The geographic coordinate to associate with the placemark.

## Return Value

An initialized [MKPlacemark](../mkplacemark.md) object.

## Discussion

This method doesn’t fill in any of the other inherited properties describing the location.

## See Also

### Creating a placemark object

- [- initWithCoordinate:postalAddress:](<init(coordinate_postaladdress_).md>) — Creates and returns a placemark object with the specified coordinate and postal address from the user’s Contacts database. _(deprecated)_
- [- initWithCoordinate:addressDictionary:](<init(coordinate_addressdictionary_).md>) — Creates and returns a placemark object using the specified coordinate and Address Book dictionary. _(deprecated)_
