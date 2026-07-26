---
title: CLPlacemark
framework: Core Location
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 5.0+（27.0 起废弃）, iPadOS 5.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.8+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/corelocation/clplacemark
source_url: 'https://developer.apple.com/documentation/corelocation/clplacemark'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clplacemark.json'
content_hash: 'sha256:0ca3916279cc04f3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLPlacemark

<sub>Class</sub>

A user-friendly description of a geographic coordinate, often containing the name of the place, its address, and other relevant information.

> [!warning] Deprecated
> Use either GeoToolbox.PlaceDescriptor or MapKit

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CLPlacemark
```

## Overview

A `CLPlacemark` object stores placemark data for a given latitude and longitude. Placemark data includes information such as the country or region, state, city, and street address associated with the specified coordinate. It can also include points of interest and geographically related data.

When you reverse geocode a geographic coordinate using a [CLGeocoder](clgeocoder.md) object, you receive a [CLPlacemark](clplacemark.md) object containing the descriptive information for that location. You can also create [CLPlacemark](clplacemark.md) object and fill it with address information yourself, which you might do when you want to determine the geographic coordinate associated with the location.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomLocalizedStringResourceConvertible](../foundation/customlocalizedstringresourceconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [DisplayRepresentable](../appintents/displayrepresentable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [InstanceDisplayRepresentable](../appintents/instancedisplayrepresentable.md), [IntentValueConvertible](../appintents/intentvalueconvertible.md), [IntentValueExpressing](../appintents/intentvalueexpressing.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [TypeDisplayRepresentable](../appintents/typedisplayrepresentable.md)

## Topics

### Creating a placemark object

- [- initWithPlacemark:](<clplacemark/init(placemark_).md>) — Initializes and returns a placemark object from another placemark object. _(deprecated)_

### Getting the placemark’s location

- [location](clplacemark/location.md) — The location object containing latitude and longitude information. _(deprecated)_
- [region](clplacemark/region.md) — The geographic region associated with the placemark. _(deprecated)_

### Getting the placemark name

- [name](clplacemark/name.md) — The name of the placemark. _(deprecated)_

### Getting the placemark details

- [thoroughfare](clplacemark/thoroughfare.md) — The street address associated with the placemark. _(deprecated)_
- [subThoroughfare](clplacemark/subthoroughfare.md) — Additional street-level information for the placemark. _(deprecated)_
- [locality](clplacemark/locality.md) — The city associated with the placemark. _(deprecated)_
- [subLocality](clplacemark/sublocality.md) — Additional city-level information for the placemark. _(deprecated)_
- [administrativeArea](clplacemark/administrativearea.md) — The state or province associated with the placemark. _(deprecated)_
- [subAdministrativeArea](clplacemark/subadministrativearea.md) — Additional administrative area information for the placemark. _(deprecated)_
- [postalCode](clplacemark/postalcode.md) — The postal code associated with the placemark. _(deprecated)_

### Getting the placemark’s country

- [ISOcountryCode](clplacemark/isocountrycode.md) — The abbreviated country or region name. _(deprecated)_
- [country](clplacemark/country.md) — The name of the country or region associated with the placemark. _(deprecated)_

### Getting the associated contact details

- [postalAddress](clplacemark/postaladdress.md) — The postal address associated with the location, formatted for use with the Contacts framework. _(deprecated)_
- [addressDictionary](clplacemark/addressdictionary.md) — A dictionary containing the Address Book keys and values for the placemark. _(deprecated)_

### Getting landscape information

- [inlandWater](clplacemark/inlandwater.md) — The name of the inland water body associated with the placemark. _(deprecated)_
- [ocean](clplacemark/ocean.md) — The name of the ocean associated with the placemark. _(deprecated)_

### Getting points of interest

- [areasOfInterest](clplacemark/areasofinterest.md) — The relevant areas of interest associated with the placemark. _(deprecated)_

### Getting the placemark’s time zone

- [timeZone](clplacemark/timezone.md) — The time zone associated with the placemark. _(deprecated)_

### Type Aliases

- [Specification](clplacemark/specification.md) _(deprecated)_
- [UnwrappedType](clplacemark/unwrappedtype.md) _(deprecated)_
- [ValueType](clplacemark/valuetype.md) _(deprecated)_

### Type Properties

- [defaultResolverSpecification](clplacemark/defaultresolverspecification.md)

### Initializers

- [init(coder:)](<clplacemark/init(coder_).md>) _(deprecated)_
- [+ placemarkWithLocation:name:postalAddress:](<clplacemark/init(location_name_postaladdress_).md>)

## See Also

### Geocoding

- [Converting between coordinates and user-friendly place names](converting-between-coordinates-and-user-friendly-place-names.md) — Convert between a latitude and longitude pair and a more user-friendly description of that location.
- [Converting a user’s location to a descriptive placemark](converting-a-user-s-location-to-a-descriptive-placemark.md) — Transform the user’s location that displays on a map into an informative textual description by reverse geocoding.
- [CLGeocoder](clgeocoder.md) — An interface for converting between geographic coordinates and place names. _(deprecated)_
