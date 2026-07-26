---
title: cycling
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkdirectionstransporttype/cycling
source_url: 'https://developer.apple.com/documentation/mapkit/mkdirectionstransporttype/cycling'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkdirectionstransporttype/cycling.json'
content_hash: 'sha256:089047589f9ca6ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKDirectionsTransportType](../mkdirectionstransporttype.md)

# cycling

<sub>Type Property</sub>

Directions suitable for use while cycling.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var cycling: MKDirectionsTransportType { get }
```

## Discussion

Use this transportation type to request cycling directions between locations.

The following example shows a task that requests directions between two locations.

```swift
  // Bethesda Terrace in Central Park, New York, NY, United States
  let origin = MKMapItem(location: .init(latitude: 40.77396, longitude: -73.97097), address: nil)

  // Grand Central Terminal, New York, NY, United States
  let destination = MKMapItem(location: .init(latitude: 40.7528, longitude: -73.97715), address: nil)

  Task {
      let request = MKDirections.Request()
      request.transportType = .cycling
      request.source = origin
      request.destination = destination
      directions = try? await MKDirections(request: request).calculate()
  }
```

## See Also

### Transport types

- [MKDirectionsTransportTypeAny](any.md) — Directions suitable for any transportation option.
- [MKDirectionsTransportTypeAutomobile](automobile.md) — Directions suitable for use while driving.
- [MKDirectionsTransportTypeTransit](transit.md) — Directions suitable for public transportation.
- [MKDirectionsTransportTypeWalking](walking.md) — Directions suitable for a pedestrian.
