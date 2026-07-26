---
title: MKDirections.RoutePreference
framework: MapKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkdirections/routepreference
source_url: 'https://developer.apple.com/documentation/mapkit/mkdirections/routepreference'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkdirections/routepreference.json'
content_hash: 'sha256:ff1d9ab47c7a13c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKDirections](../mkdirections.md)

# MKDirections.RoutePreference

<sub>Enumeration</sub>

Options that modify how the framework selects routes when calculating directions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum RoutePreference
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Route selection options

- [MKDirectionsRoutePreferenceAny](routepreference/any.md) — The option that specifies any available route.
- [MKDirectionsRoutePreferenceAvoid](routepreference/avoid.md) — The option that requests the framework avoid certain routes.

### Initializers

- [init(rawValue:)](<routepreference/init(rawvalue_).md>)

## See Also

### Creating a directions object

- [- initWithRequest:](<init(request_).md>) — Creates and returns a directions object using the specified request.
- [Request](request.md) — The start and end points of a route, along with the planned mode of transportation.
