---
title: timeZone
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapitem/timezone
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapitem/timezone'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapitem/timezone.json'
content_hash: 'sha256:6b458511024bd4ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapItem](../mkmapitem.md)

# timeZone

<sub>Instance Property</sub>

The time zone of the specified location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var timeZone: TimeZone? { get set }
```

## Discussion

When you search for map items, MapKit populates this field with the time zone information as a convenience. You may also set the time zone for any map items you create.

## See Also

### Accessing the map item attributes

- [Identifier](identifier-swift.class.md) — A unique identifier for a place.
- [alternateIdentifiers](alternateidentifiers.md) — A set of alternative identifiers for a place.
- [identifier](identifier-swift.property.md) — A unique identifier for a place.
- [isCurrentLocation](iscurrentlocation.md) — A Boolean value that indicates whether the map item represents the user’s location.
- [name](name.md) — The descriptive name associated with the map item.
- [placemark](placemark.md) — The placemark object containing the location information. _(deprecated)_
- [pointOfInterestCategory](pointofinterestcategory.md) — The point-of-interest category for the map item.
- [phoneNumber](phonenumber.md) — The phone number associated with a business at the specified location.
- [url](url.md) — The URL associated with the specified location.
