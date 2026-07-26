---
title: MKPlacemark
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+（26.0 起废弃）, iPadOS 3.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, macOS 10.9+（26.0 起废弃）, tvOS 9.2+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）, watchOS 2.0+（26.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/mapkit/mkplacemark
source_url: 'https://developer.apple.com/documentation/mapkit/mkplacemark'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkplacemark.json'
content_hash: 'sha256:b7c7641d10c38407'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKPlacemark

<sub>Class</sub>

A user-friendly description of a location on the map.

> [!warning] Deprecated
> Use MKMapItem's location, address and addressRepresentations properties instead. Use MKAddressRepresentations for formatted address strings for MapKit provided MKMapItems

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class MKPlacemark
```

## Overview

Placemark data includes information like the country or region, state, city, and street address associated with the specified coordinate. A placemark is a concrete annotation object and conforms to the [MKAnnotation](mkannotation.md) protocol. Because it’s an annotation, you can add a placemark directly to the map view’s list of annotations.

## Relationships

- **Inherits From**: [CLPlacemark](../corelocation/clplacemark.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [MKAnnotation](mkannotation.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a placemark object

- [- initWithCoordinate:](<mkplacemark/init(coordinate_).md>) — Creates and returns a placemark object using the specified coordinate. _(deprecated)_
- [- initWithCoordinate:postalAddress:](<mkplacemark/init(coordinate_postaladdress_).md>) — Creates and returns a placemark object with the specified coordinate and postal address from the user’s Contacts database. _(deprecated)_
- [- initWithCoordinate:addressDictionary:](<mkplacemark/init(coordinate_addressdictionary_).md>) — Creates and returns a placemark object using the specified coordinate and Address Book dictionary. _(deprecated)_

### Accessing the placemark attributes

- [countryCode](mkplacemark/countrycode.md) — The abbreviated country or region name. _(deprecated)_

## See Also

### Shared behavior

- [MKAnnotation](mkannotation.md) — An interface for associating your content with a specific map location.
- [MKAnnotationView](mkannotationview.md) — The visual representation of one of your annotation objects.
