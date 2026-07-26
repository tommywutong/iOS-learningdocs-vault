---
title: 'init(latitudeDelta:longitudeDelta:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkcoordinatespan/init(latitudedelta:longitudedelta:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkcoordinatespan/init(latitudedelta:longitudedelta:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkcoordinatespan/init%28latitudedelta%3Alongitudedelta%3A%29.json'
content_hash: 'sha256:591c06566ad0aca7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKCoordinateSpan](../mkcoordinatespan.md)

# init(latitudeDelta:longitudeDelta:)

<sub>Initializer</sub>

Creates a new [MKCoordinateSpan](../mkcoordinatespan.md) from the specified values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(latitudeDelta: CLLocationDegrees, longitudeDelta: CLLocationDegrees)
```

## Parameters

- `latitudeDelta` — The amount of north-to-south distance (measured in degrees) to use for the span. Unlike longitudinal distances, which vary based on the latitude, one degree of latitude is approximately 111 kilometers (69 miles) at all times.

- `longitudeDelta` — The amount of east-to-west distance (measured in degrees) to use for the span. The number of kilometers spanned by a longitude range varies based on the current latitude. For example, one degree of longitude spans a distance of approximately 111 kilometers (69 miles) at the equator but shrinks to 0 kilometers at the poles.

## Return Value

A span with the specified delta values.

## See Also

### Creating a coordinate span

- [init()](<init().md>) — Creates a coordinate span that represents a width and height on a map.
