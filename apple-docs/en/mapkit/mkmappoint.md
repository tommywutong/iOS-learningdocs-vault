---
title: MKMapPoint
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmappoint
source_url: 'https://developer.apple.com/documentation/mapkit/mkmappoint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmappoint.json'
content_hash: 'sha256:7e460e16cf0d7025'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKMapPoint

<sub>Structure</sub>

A point on a two-dimensional map projection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MKMapPoint
```

## Overview

If you project the curved surface of the globe onto a flat surface, you get a two-dimensional version of a map where longitude lines appear to be parallel. An `MKMapPoint` data structure represents a point on this two-dimensional map.

The underlying units that MapKit uses to draw the contents of an [MKMapView](mkmapview.md) define the actual units of a map point, but you don’t need to worry about these units directly. You use map points primarily to simplify computations that are complex to do using coordinate values on a curved surface. By converting to map points, you can perform those calculations on a flat surface, which is generally much simpler, and then convert back as necessary. You can map between coordinate values and map points using the [MKMapPointForCoordinate](<mkmappoint/init(__).md>) and [MKCoordinateForMapPoint](mkmappoint/coordinate.md) functions.

When saving map-related data to a file, save coordinate values (latitude and longitude) rather than map points.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Creating a map point

- [init()](<mkmappoint/init().md>) — Creates a map point at an unspecified point.
- [init(x:y:)](<mkmappoint/init(x_y_).md>) — Creates a new map point structure from the specified values.
- [MKMapPointForCoordinate](<mkmappoint/init(__).md>) — Creates the map point data structure that corresponds to the specified coordinate.

### Getting the point coordinates

- [x](mkmappoint/x.md) — The location of the point along the x-axis of the map.
- [y](mkmappoint/y.md) — The location of the point along the y-axis of the map.
- [MKCoordinateForMapPoint](mkmappoint/coordinate.md) — A 2D coordinate that corresponds to the latitude and longitude of the specified map point.

### Comparing map points

- [MKMapPointEqualToPoint](<mkmappointequaltopoint(____).md>) — Returns a Boolean value that indicates whether two map points are equal.

### Getting the distance between points

- [MKMetersBetweenMapPoints](<mkmappoint/distance(to_).md>) — Returns the number of meters between two map points.
- [MKMetersPerMapPointAtLatitude](<mkmeterspermappointatlatitude(__).md>) — Returns the distance that one map point spans at the specified latitude.
- [MKMapPointsPerMeterAtLatitude](<mkmappointspermeteratlatitude(__).md>) — Returns the number of map points that represent one meter at the specified latitude.

### Getting a description of the point

- [MKStringFromMapPoint](<mkstringfrommappoint(__).md>) — Returns a formatted string for the specified map point.

## See Also

### Map coordinates

- [MKCoordinateRegion](mkcoordinateregion.md) — A rectangular geographic region that centers around a specific latitude and longitude.
- [MKCoordinateSpan](mkcoordinatespan.md) — The width and height of a map region.
- [MKMapRect](mkmaprect.md) — A rectangular area on a two-dimensional map projection.
- [MKMapSize](mkmapsize.md) — Width and height information on a two-dimensional map projection.
- [MKDistanceFormatter](mkdistanceformatter.md) — A utility object that converts between a geographic distance and a string-based expression of that distance.
