---
title: identifier
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapitem/identifier-swift.property
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapitem/identifier-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapitem/identifier-swift.property.json'
content_hash: 'sha256:fb07a2fd9aced332'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapItem](../mkmapitem.md)

# identifier

<sub>Instance Property</sub>

A unique identifier for a place.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var identifier: MKMapItem.Identifier? { get }
```

## Discussion

An identifier uniquely identifies a place, such as a business or a landmark. You can persist an identifier and use it later to recall information about place.

## See Also

### Accessing the map item attributes

- [Identifier](identifier-swift.class.md) — A unique identifier for a place.
- [alternateIdentifiers](alternateidentifiers.md) — A set of alternative identifiers for a place.
- [isCurrentLocation](iscurrentlocation.md) — A Boolean value that indicates whether the map item represents the user’s location.
- [name](name.md) — The descriptive name associated with the map item.
- [placemark](placemark.md) — The placemark object containing the location information. _(deprecated)_
- [pointOfInterestCategory](pointofinterestcategory.md) — The point-of-interest category for the map item.
- [phoneNumber](phonenumber.md) — The phone number associated with a business at the specified location.
- [timeZone](timezone.md) — The time zone of the specified location.
- [url](url.md) — The URL associated with the specified location.
