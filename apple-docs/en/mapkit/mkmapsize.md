---
title: MKMapSize
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapsize
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapsize.json'
content_hash: 'sha256:80786e7f9926eae0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKMapSize

<sub>Structure</sub>

Width and height information on a two-dimensional map projection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MKMapSize
```

## Overview

If you project the curved surface of the globe onto a flat surface, what you get is a two-dimensional version of a map where longitude lines appear to be parallel. Such maps are often used to show the entire surface of the globe all at once. An `MKMapSize` data structure represents a horizontal and vertical distance as measured on this two-dimensional map.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Creating a map size

- [init()](<mkmapsize/init().md>) — Creates a map size that represents an empty area on a two-dimensional projection of a map.
- [init(width:height:)](<mkmapsize/init(width_height_).md>) — Creates a map size that represents an area on a two-dimensional projection of a map with the specified width and height.

### Getting standard map sizes

- [MKMapSizeWorld](mkmapsize/world.md) — The width and height, in map points, of the world in a two-dimensional map projection.

### Getting the width and height

- [height](mkmapsize/height.md) — The height of the specified area, measured in map points.
- [width](mkmapsize/width.md) — The width of the specified area, measured in map points.

### Comparing map sizes

- [MKMapSizeEqualToSize](<mkmapsizeequaltosize(____).md>) — Returns a Boolean value that indicates whether two map sizes are equal.

### Getting a description of the size

- [MKStringFromMapSize](<mkstringfrommapsize(__).md>) — Returns a formatted string for the specified map size.

## See Also

### Map coordinates

- [MKCoordinateRegion](mkcoordinateregion.md) — A rectangular geographic region that centers around a specific latitude and longitude.
- [MKCoordinateSpan](mkcoordinatespan.md) — The width and height of a map region.
- [MKMapRect](mkmaprect.md) — A rectangular area on a two-dimensional map projection.
- [MKMapPoint](mkmappoint.md) — A point on a two-dimensional map projection.
- [MKDistanceFormatter](mkdistanceformatter.md) — A utility object that converts between a geographic distance and a string-based expression of that distance.
