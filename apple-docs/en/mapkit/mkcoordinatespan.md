---
title: MKCoordinateSpan
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkcoordinatespan
source_url: 'https://developer.apple.com/documentation/mapkit/mkcoordinatespan'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkcoordinatespan.json'
content_hash: 'sha256:da83eb0fbd9e7ffe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKCoordinateSpan

<sub>Structure</sub>

The width and height of a map region.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MKCoordinateSpan
```

## Overview

You use the delta values in this structure to indicate the desired zoom level of the map, with smaller delta values corresponding to a higher zoom level.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [Sendable](../swift/sendable.md)

## Topics

### Creating a coordinate span

- [init()](<mkcoordinatespan/init().md>) — Creates a coordinate span that represents a width and height on a map.
- [init(latitudeDelta:longitudeDelta:)](<mkcoordinatespan/init(latitudedelta_longitudedelta_).md>) — Creates a new [MKCoordinateSpan](mkcoordinatespan.md) from the specified values.

### Getting the span coordinates

- [latitudeDelta](mkcoordinatespan/latitudedelta.md) — The amount of north-to-south distance (measured in degrees) to display on the map.
- [longitudeDelta](mkcoordinatespan/longitudedelta.md) — The amount of east-to-west distance (measured in degrees) to display for the map region.

## See Also

### Map coordinates

- [MKCoordinateRegion](mkcoordinateregion.md) — A rectangular geographic region that centers around a specific latitude and longitude.
- [MKMapRect](mkmaprect.md) — A rectangular area on a two-dimensional map projection.
- [MKMapPoint](mkmappoint.md) — A point on a two-dimensional map projection.
- [MKMapSize](mkmapsize.md) — Width and height information on a two-dimensional map projection.
- [MKDistanceFormatter](mkdistanceformatter.md) — A utility object that converts between a geographic distance and a string-based expression of that distance.
