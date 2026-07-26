---
title: CLGeocoder
framework: Core Location
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 5.0+（26.0 起废弃）, iPadOS 5.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, macOS 10.8+（26.0 起废弃）, tvOS 9.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）, watchOS 2.0+（26.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/corelocation/clgeocoder
source_url: 'https://developer.apple.com/documentation/corelocation/clgeocoder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clgeocoder.json'
content_hash: 'sha256:6096b835091149f3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLGeocoder

<sub>Class</sub>

An interface for converting between geographic coordinates and place names.

> [!warning] Deprecated
> Use MapKit

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CLGeocoder
```

## Overview

The [CLGeocoder](clgeocoder.md) class provides services for converting between a coordinate (specified as a latitude and longitude) and the user-friendly representation of that coordinate. A user-friendly representation of the coordinate typically consists of the street, city, state, and country or region information corresponding to the given location, but it may also contain a relevant point of interest, landmarks, or other identifying information. A geocoder object is a single-shot object that works with a network-based service to look up placemark information for its specified coordinate value.

To use a geocoder object, you create it and call one of its forward- or reverse-geocoding methods to begin the request. _Reverse-geocoding_ requests take a latitude and longitude value and find a user-readable address. _Forward-geocoding_ requests take a user-readable address and find the corresponding latitude and longitude value. Forward-geocoding requests may also return additional information about the specified location, such as a point of interest or building at that location. For both types of request, the results are returned using a [CLPlacemark](clplacemark.md) object. In the case of forward-geocoding requests, multiple placemark objects may be returned if the provided information yielded multiple possible locations.

To make smart decisions about what types of information to return, the geocoder server uses all the information provided to it when processing the request. For example, if the user is moving quickly along a highway, it might return the name of the overall region, and not the name of a small park that the user is passing through.

### Tips for Using a Geocoder Object

Apps must be conscious of how they use geocoding. Geocoding requests are rate-limited for each app, so making too many requests in a short period of time may cause some of the requests to fail. (When the maximum rate is exceeded, the geocoder returns an error object with the [kCLErrorNetwork](clerror-swift.struct/code/network.md) error to the associated completion handler.) Here are some rules of thumb for using this class effectively:

- Send at most one geocoding request for any one user action.
- If the user performs multiple actions that involve geocoding the same location, reuse the results from the initial geocoding request instead of starting individual requests for each action.
- When you want to update the user’s current location automatically (such as when the user is moving), issue new geocoding requests only when the user has moved a significant distance and after a reasonable amount of time has passed. For example, in a typical situation, you should not send more than one geocoding request per minute.
- Do not start a geocoding request at a time when the user will not see the results immediately. For example, do not start a request if your application is inactive or in the background.

The computer or device must have access to the network in order for the geocoder object to return detailed placemark information. Although, the geocoder stores enough information locally to report the localized country or region name and ISO country code for many locations. If this information isn’t available for a specific location, the geocoder may still report an error to your completion block.

You can use geocoder objects either in conjunction with, or independent of, the classes of the [MapKit](../mapkit.md) framework.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Reverse geocoding a location

- [- reverseGeocodeLocation:preferredLocale:completionHandler:](<clgeocoder/reversegeocodelocation(__preferredlocale_completionhandler_).md>) — Submits a reverse-geocoding request for the specified location and locale. _(deprecated)_
- [- reverseGeocodeLocation:completionHandler:](<clgeocoder/reversegeocodelocation(__completionhandler_).md>) — Submits a reverse-geocoding request for the specified location. _(deprecated)_
- [CLGeocodeCompletionHandler](clgeocodecompletionhandler.md) — A block to be called when a geocoding request is complete.

### Geocoding an address

- [- geocodeAddressString:inRegion:preferredLocale:completionHandler:](<clgeocoder/geocodeaddressstring(__in_preferredlocale_completionhandler_).md>) — Submits a forward-geocoding requesting using the specified address string and locale information. _(deprecated)_
- [- geocodeAddressString:completionHandler:](<clgeocoder/geocodeaddressstring(__completionhandler_).md>) — Submits a forward-geocoding request using the specified string. _(deprecated)_
- [- geocodeAddressString:inRegion:completionHandler:](<clgeocoder/geocodeaddressstring(__in_completionhandler_).md>) — Submits a forward-geocoding request using the specified string and region information. _(deprecated)_
- [- geocodePostalAddress:completionHandler:](<clgeocoder/geocodepostaladdress(__completionhandler_).md>) — Submits a forward-geocoding requesting using the specified Contacts framework information. _(deprecated)_
- [- geocodePostalAddress:preferredLocale:completionHandler:](<clgeocoder/geocodepostaladdress(__preferredlocale_completionhandler_).md>) — Submits a forward-geocoding requesting using the specified locale and Contacts framework information. _(deprecated)_
- [- geocodeAddressDictionary:completionHandler:](<clgeocoder/geocodeaddressdictionary(__completionhandler_).md>) — Submits a forward-geocoding request using the specified address dictionary. _(deprecated)_

### Managing geocoding requests

- [- cancelGeocode](<clgeocoder/cancelgeocode().md>) — Cancels a pending geocoding request. _(deprecated)_
- [geocoding](clgeocoder/isgeocoding.md) — A Boolean value indicating whether the receiver is in the middle of geocoding its value. _(deprecated)_

### Instance Methods

- [- geocodeAddressString:inRegionCenteredAt:inRegionRadius:preferredLocale:completionHandler:](<clgeocoder/geocodeaddressstring(__inregioncenteredat_inregionradius_preferredlocale_completionhandler_).md>) _(deprecated)_

## See Also

### Geocoding

- [Converting between coordinates and user-friendly place names](converting-between-coordinates-and-user-friendly-place-names.md) — Convert between a latitude and longitude pair and a more user-friendly description of that location.
- [Converting a user’s location to a descriptive placemark](converting-a-user-s-location-to-a-descriptive-placemark.md) — Transform the user’s location that displays on a map into an informative textual description by reverse geocoding.
- [CLPlacemark](clplacemark.md) — A user-friendly description of a geographic coordinate, often containing the name of the place, its address, and other relevant information. _(deprecated)_
