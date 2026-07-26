---
title: MKDirections.Request
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkdirections/request
source_url: 'https://developer.apple.com/documentation/mapkit/mkdirections/request'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkdirections/request.json'
content_hash: 'sha256:277e4dceac8f031f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKDirections](../mkdirections.md)

# MKDirections.Request

<sub>Class</sub>

The start and end points of a route, along with the planned mode of transportation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class Request
```

## Overview

You use an [Request](request.md) object when requesting or providing directions. If your app provides directions, use this class to decode the URL that the Maps app sends to you. If you need to request directions from Apple, pass an instance of this class to an [MKDirections](../mkdirections.md) object. For example, an app that provides subway directions might request walking directions to and from relevant subway stations.

Prior to iOS 14, for apps that provide directions, you receive direction-related URLs in your app delegate’s [application(_:open:options:)](<../../uikit/uiapplicationdelegate/application(__open_options_).md>)method. Upon receiving a URL, call the [+ isDirectionsRequestURL:](<request/isdirectionsrequest(__).md>) method of this class to determine whether the URL relates to routing directions. If it does, create an instance of this class using the provided URL and extract the map items associated with the start and end points.

> [!note] Note
> Prior to iOS 14, to provide routing directions, your app needs to include special keys in its `Info.plist` file and be able to handle URLs that the Maps app sends to it. These keys indicate a special URL type that you app needs to handle. For information about how to implement this support, see [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497).

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md)

## Topics

### Creating a directions request object

- [+ isDirectionsRequestURL:](<request/isdirectionsrequest(__).md>) — Returns a Boolean value that indicates whether the specified URL contains a directions request.
- [init(contentsOfURL:)](<request/init(contentsofurl_).md>) — Creates and returns a directions request object using the specified URL.

### Accessing the start and end points

- [source](request/source.md) — The starting point for routing directions.
- [destination](request/destination.md) — The end point for routing directions.

### Specifying transportation options

- [transportType](request/transporttype.md) — The type of conveyance that the directions apply to.
- [highwayPreference](request/highwaypreference.md) — The value that indicates whether the framework uses or avoids highways when providing directions.
- [tollPreference](request/tollpreference.md) — The value that indicates whether the framework avoids routes that have tolls when providing directions.
- [RoutePreference](routepreference.md) — Options that modify how the framework selects routes when calculating directions.
- [requestsAlternateRoutes](request/requestsalternateroutes.md) — A Boolean value that indicates whether your app requests multiple routes when they’re available.
- [departureDate](request/departuredate.md) — The departure date for the trip.
- [arrivalDate](request/arrivaldate.md) — The arrival date for the trip.

### Constants

- [MKDirectionsTransportType](../mkdirectionstransporttype.md) — Constants that specify the type of conveyance to use.

### Launch options

- [MKLaunchOptionsCameraKey](../mklaunchoptionscamerakey.md) — The virtual camera to use for viewing the map.
- [MKLaunchOptionsDirectionsModeCycling](../mklaunchoptionsdirectionsmodecycling.md) — Cycling directions between the specified start and end points.
- [MKLaunchOptionsDirectionsModeDefault](../mklaunchoptionsdirectionsmodedefault.md) — Directions that match the user’s preferred transportation type.
- [MKLaunchOptionsDirectionsModeDriving](../mklaunchoptionsdirectionsmodedriving.md) — Driving directions between the specified start and end points.
- [MKLaunchOptionsDirectionsModeKey](../mklaunchoptionsdirectionsmodekey.md) — The mode of transportation.
- [MKLaunchOptionsDirectionsModeTransit](../mklaunchoptionsdirectionsmodetransit.md) — Public transit directions between the specified start and end points.
- [MKLaunchOptionsDirectionsModeWalking](../mklaunchoptionsdirectionsmodewalking.md) — Walking directions between the specified start and end points.
- [MKLaunchOptionsMapCenterKey](../mklaunchoptionsmapcenterkey.md) — The coordinate value on which to center the map.
- [MKLaunchOptionsMapSpanKey](../mklaunchoptionsmapspankey.md) — The amount of the map to display.
- [MKLaunchOptionsMapTypeKey](../mklaunchoptionsmaptypekey.md) — The type of map (standard, satellite, or hybrid) to display.
- [MKLaunchOptionsShowsTrafficKey](../mklaunchoptionsshowstraffickey.md) — A Boolean value that indicates whether to display traffic information.

### Initializers

- [- initWithContentsOfURL:](<request/init(contentsof_).md>)

### Default Implementations

- [Request Implementations](request/request-implementations.md)

## See Also

### Directions

- [MKDirections](../mkdirections.md) — A utility object that computes directions and travel-time information based on the route information you provide.
- [Response](response.md) — The route information that Apple servers return in response to your request for directions.
- [ETAResponse](etaresponse.md) — The travel-time information that Apple servers return.
- [MKRoute](../mkroute.md) — A single route between a requested start and end point.
- [Step](../mkroute/step.md) — One portion of an overall route.
