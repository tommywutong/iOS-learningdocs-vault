---
title: MKMapRect
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmaprect
source_url: 'https://developer.apple.com/documentation/mapkit/mkmaprect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmaprect.json'
content_hash: 'sha256:cc1082d1edc4aadd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKMapRect

<sub>Structure</sub>

A rectangular area on a two-dimensional map projection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MKMapRect
```

## Overview

If you project the curved surface of the globe onto a flat surface, what you get is a two-dimensional version of a map where longitude lines appear to be parallel. Such maps are often used to show the entire surface of the globe all at once. An `MKMapRect` data structure represents a rectangular area as seen on this two-dimensional map.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Creating a map rectangle

- [init()](<mkmaprect/init().md>) — Creates the rectangle with an empty region.
- [init(origin:size:)](<mkmaprect/init(origin_size_).md>) — Creates the map rectangle with the specified point and size.
- [MKMapRectMake](<mkmaprect/init(x_y_width_height_).md>) — Creates a new map rectangle structure from the specified values.
- [MKCoordinateRegionForMapRect](<mkcoordinateregion/init(__).md>) — Returns the region that corresponds to the specified map rectangle.

### Getting standard map rectangles

- [MKMapRectNull](mkmaprect/null.md) — The null map rectangle.
- [MKMapRectWorld](mkmaprect/world.md) — The map rectangle that represents the world in the two-dimensional map projection.

### Getting the rectangle coordinates

- [origin](mkmaprect/origin.md) — The origin point of the rectangle.
- [size](mkmaprect/size.md) — The width and height of the rectangle, starting from the origin point.

### Getting the boundaries

- [MKMapRectGetMinX](mkmaprect/minx.md) — Returns the minimum x-axis value of the specified rectangle.
- [MKMapRectGetMinY](mkmaprect/miny.md) — Returns the minimum y-axis value of the specified rectangle.
- [MKMapRectGetMidX](mkmaprect/midx.md) — Returns the mid-point along the x-axis of the specified rectangle.
- [MKMapRectGetMidY](mkmaprect/midy.md) — Returns the mid-point along the y-axis of the specified rectangle.
- [MKMapRectGetMaxX](mkmaprect/maxx.md) — Returns the maximum x-axis value of the specified rectangle.
- [MKMapRectGetMaxY](mkmaprect/maxy.md) — Returns the maximum y-axis value of the specified rectangle.
- [MKMapRectGetWidth](mkmaprect/width.md) — Returns the width of the map rectangle.
- [MKMapRectGetHeight](mkmaprect/height.md) — Returns the height of the map rectangle.

### Comparing rectangles

- [MKMapRectIsNull](mkmaprect/isnull.md) — A Boolean value that indicates whether the specified rectangle is null.
- [MKMapRectEqualToRect](<mkmaprectequaltorect(____).md>) — Returns a Boolean value that indicates whether two map rectangles are equal.
- [MKMapRectIsEmpty](mkmaprect/isempty.md) — A Boolean value that indicates whether the specified rectangle has no area.
- [MKMapRectSpans180thMeridian](mkmaprect/spans180thmeridian.md) — A Boolean value that indicates whether the specified map rectangle crosses the 180th meridian.
- [MKMapRectRemainder](mkmaprect/remainder.md) — A rectangle that represents the normalized portion of the specified rectangle that lies outside the world map boundaries.

### Intersecting the rectangle

- [MKMapRectContainsPoint](<mkmaprect/contains(__)-79tjt.md>) — Returns a Boolean value that indicates whether the specified map point lies within the rectangle.
- [MKMapRectContainsRect](<mkmaprect/contains(__)-1z5oa.md>) — Returns a Boolean value that indicates whether one rectangle contains another.
- [MKMapRectIntersectsRect](<mkmaprect/intersects(__).md>) — Returns a Boolean value that indicates whether two rectangles intersect each other.

### Modifying the rectangle

- [MKMapRectUnion](<mkmaprect/union(__).md>) — Returns a rectangle that represents the union of two rectangles.
- [MKMapRectIntersection](<mkmaprect/intersection(__).md>) — Returns the rectangle that represents the intersection of two rectangles.
- [MKMapRectInset](<mkmaprect/insetby(dx_dy_).md>) — Returns the specified rectangle with an inset by the specified amounts.
- [MKMapRectOffset](<mkmaprect/offsetby(dx_dy_).md>) — Returns a rectangle with an origin point that shifts by the specified amount.
- [MKMapRectDivide](<mkmaprectdivide(__________).md>) — Divides the specified rectangle into two smaller rectangles.

### Getting a description of the rectangle

- [MKStringFromMapRect](<mkstringfrommaprect(__).md>) — Returns a formatted string for the specified map rectangle.

## See Also

### Map coordinates

- [MKCoordinateRegion](mkcoordinateregion.md) — A rectangular geographic region that centers around a specific latitude and longitude.
- [MKCoordinateSpan](mkcoordinatespan.md) — The width and height of a map region.
- [MKMapPoint](mkmappoint.md) — A point on a two-dimensional map projection.
- [MKMapSize](mkmapsize.md) — Width and height information on a two-dimensional map projection.
- [MKDistanceFormatter](mkdistanceformatter.md) — A utility object that converts between a geographic distance and a string-based expression of that distance.
