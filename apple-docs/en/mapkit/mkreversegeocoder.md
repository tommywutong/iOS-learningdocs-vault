---
title: MKReverseGeocoder
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+（5.0 起废弃）, iPadOS 3.0+（5.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/mapkit/mkreversegeocoder
source_url: 'https://developer.apple.com/documentation/mapkit/mkreversegeocoder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkreversegeocoder.json'
content_hash: 'sha256:838e1df5d0079c82'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKReverseGeocoder

<sub>Class</sub>

Provides services for converting a map coordinate (specified as a latitude/longitude pair) into information about that coordinate, such as the country or region, city, or street.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@interface MKReverseGeocoder : NSObject
```

## Overview

A reverse geocoder object is a single-shot object that works with a network-based map service to look up placemark information for its specified coordinate value.

The Google terms of service require that the reverse geocoding service be used in conjunction with a Google map; take this into account when designing your application’s user interface.

Each Map Kit application has a limited amount of reverse geocoding capacity, so it is to your advantage to use reverse geocode requests sparingly. Here are some rules of thumb for using this class most effectively:

- Send at most one reverse-geocoding request for any one user action.
- If the user performs multiple actions that involve reverse-geocoding the same location, reuse the results from the initial reverse-geocoding request instead of starting individual requests for each action.
- When you want to update the location automatically (such as when the user is moving), reissue the reverse-geocoding request only when the user’s location has moved a significant distance and after a reasonable amount of time has passed. For example, in a typical situation, you should not send more than one reverse-geocode request per minute.
- Do not start a reverse-geocoding request at a time when the user will not see the results immediately. For example, do not start a request if your application recently resigned the active state (possibly because of an interruption such as a phone call) and is waiting to become active again.

An iOS-based device must have access to the network in order for the reverse geocoder object to return valid information. The reverse geocoder returns information through its associated delegate object, which is an object that conforms to the [MKReverseGeocoderDelegate](mkreversegeocoderdelegate.md) protocol. If the reverse geocoder is unable to retrieve the requested information, it similarly reports the error to its delegate object. For more information on this protocol, see [MKReverseGeocoderDelegate](mkreversegeocoderdelegate.md).

This class is deprecated in iOS 5.0. Use the [CLGeocoder](../corelocation/clgeocoder.md) class instead.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

## Topics

### Initializing the Reverse Geocoder

- [initWithCoordinate:](mkreversegeocoder/initwithcoordinate_.md) — Initializes the reverse geocoder with the specified coordinate value. _(deprecated)_

### Accessing Reverse Geocoder Attributes

- [delegate](mkreversegeocoder/delegate.md) — The reverse geocoder’s delegate object. _(deprecated)_
- [coordinate](mkreversegeocoder/coordinate.md) — The coordinate whose placemark data you want to retrieve. _(deprecated)_
- [placemark](mkreversegeocoder/placemark.md) — The result of the reverse-geocoding operation. _(deprecated)_

### Managing the Search

- [start](mkreversegeocoder/start.md) — Starts the reverse-geocoding process asynchronously. _(deprecated)_
- [querying](mkreversegeocoder/querying.md) — A Boolean value indicating whether the receiver is in the middle of reverse-geocoding its coordinate. _(deprecated)_
- [cancel](mkreversegeocoder/cancel.md) — Cancels a pending reverse-geocoding request. _(deprecated)_

## See Also

### Classes

- [MKCircleView](mkcircleview.md) — Provides the visual representation for an [MKCircle](mkcircle.md) annotation object. _(deprecated)_
- [MKOverlayView](mkoverlayview.md) — Defines the basic behavior associated with all overlay views. _(deprecated)_
- [MKOverlayPathView](mkoverlaypathview.md) — Represents a generic overlay that draws its contents using a Core Graphics path data type. _(deprecated)_
- [MKPolygonView](mkpolygonview.md) — Provides the visual representation for an [MKPolygon](mkpolygon.md) annotation object. _(deprecated)_
- [MKPolylineView](mkpolylineview.md) — Provides the visual representation for an [MKPolyline](mkpolyline.md) annotation object. _(deprecated)_
- [MKPinAnnotationView](mkpinannotationview.md) — An annotation view that displays a pin image on the map. _(deprecated)_
