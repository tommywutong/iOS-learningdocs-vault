---
title: MKMapItem
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapitem
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapitem.json'
content_hash: 'sha256:197d9618bd853865'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKMapItem

<sub>Class</sub>

A point of interest on the map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class MKMapItem
```

## Overview

A map item includes a geographic location and any interesting data that might apply to that location, such as the address at that location and the name of a business at that address. You can also create a special `MKMapItem` object representing the user’s location.

Use this class to do the following:

- Share map-related data with the Maps app.
- Handle requests for directions that originate from the Maps app.

To display information in the Maps app, create an `MKMapItem` object with the information you want to display and call the [+ openMapsWithItems:launchOptions:](<mkmapitem/openmaps(with_launchoptions_).md>) method. The Maps app displays that location on the map and shows the information you provide.

If you implement a routing app, the Maps app provides two `MKMapItem` objects representing the start and end points. Use the information in those two objects to plot the route and generate directions.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSItemProviderReading](../foundation/nsitemproviderreading.md), [NSItemProviderWriting](../foundation/nsitemproviderwriting.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Creating map items

- [- initWithPlacemark:](<mkmapitem/init(placemark_).md>) — Creates and returns a map item object using the specified placemark object. _(deprecated)_
- [+ mapItemForCurrentLocation](<mkmapitem/forcurrentlocation().md>) — Creates and returns a singleton map item object representing the user’s location.

### Accessing the map item attributes

- [Identifier](mkmapitem/identifier-swift.class.md) — A unique identifier for a place.
- [alternateIdentifiers](mkmapitem/alternateidentifiers.md) — A set of alternative identifiers for a place.
- [identifier](mkmapitem/identifier-swift.property.md) — A unique identifier for a place.
- [isCurrentLocation](mkmapitem/iscurrentlocation.md) — A Boolean value that indicates whether the map item represents the user’s location.
- [name](mkmapitem/name.md) — The descriptive name associated with the map item.
- [placemark](mkmapitem/placemark.md) — The placemark object containing the location information. _(deprecated)_
- [pointOfInterestCategory](mkmapitem/pointofinterestcategory.md) — The point-of-interest category for the map item.
- [phoneNumber](mkmapitem/phonenumber.md) — The phone number associated with a business at the specified location.
- [timeZone](mkmapitem/timezone.md) — The time zone of the specified location.
- [url](mkmapitem/url.md) — The URL associated with the specified location.

### Launching the Maps app

- [+ openMapsWithItems:launchOptions:](<mkmapitem/openmaps(with_launchoptions_).md>) — Opens the Maps app and displays the specified map items.
- [+ openMapsWithItems:launchOptions:completionHandler:](<mkmapitem/openmaps(with_launchoptions_completionhandler_).md>) — Opens the Maps app using the specified map items and options.
- [+ openMapsWithItems:launchOptions:fromScene:completionHandler:](<mkmapitem/openmaps(with_launchoptions_from_completionhandler_).md>) — Opens the Maps app from a particular scene using the specified map items and options.
- [- openInMapsWithLaunchOptions:](<mkmapitem/openinmaps(launchoptions_).md>) — Opens the Maps app and displays the map item.
- [- openInMapsWithLaunchOptions:completionHandler:](<mkmapitem/openinmaps(launchoptions_completionhandler_).md>) — Opens the Maps app and displays the map item.
- [- openInMapsWithLaunchOptions:fromScene:completionHandler:](<mkmapitem/openinmaps(launchoptions_from_completionhandler_).md>) — Opens the Maps app from a particular scene using the specified options.

### Serializing a map item

- [MKMapItemTypeIdentifier](mkmapitemtypeidentifier.md) — A constant that indicates the type of a serialized map item.

### Opening items at launch time

- [Launch options dictionary keys](launch-options-dictionary-keys.md) — Launch options to specify when opening map items in the Maps app.
- [Directions mode values](directions-mode-values.md) — Strings that represent the possible values of the launch options direction mode key.

### Initializers

- [- initWithLocation:address:](<mkmapitem/init(location_address_).md>) — Creates and returns a map item object using the specified location and address objects.

### Instance Properties

- [address](mkmapitem/address.md) — The address object.
- [addressRepresentations](mkmapitem/addressrepresentations.md) — The address representations object that contains various address representations useful for display purposes.
- [location](mkmapitem/location.md) — The location object.

### Default Implementations

- [MKMapItem Implementations](mkmapitem/mkmapitem-implementations.md)

## See Also

### Essentials

- [Enabling Maps capability in Xcode](enabling-maps-capability-in-xcode.md) — Configure your routing app to support providing directions.
- [Identifying unique locations with Place IDs](identifying-unique-locations-with-place-ids.md) — Obtain information about a point of interest that persists over its lifetime.
- [MKMapView](mkmapview.md) — An embeddable map interface, similar to the one that the Maps app provides.
