---
title: 'setColors:atLocations:'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkgradientpolylinerenderer/setcolors:atlocations:'
source_url: 'https://developer.apple.com/documentation/mapkit/mkgradientpolylinerenderer/setcolors:atlocations:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkgradientpolylinerenderer/setcolors%3Aatlocations%3A.json'
content_hash: 'sha256:ff2965f12b7d5aa1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKGradientPolylineRenderer](../mkgradientpolylinerenderer.md)

# setColors:atLocations:

<sub>Instance Method</sub>

Sets the colors and corresponding unit distance values to create gradients.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) setColors:(NSArray<UIColor *> *) colors atLocations:(NSArray<NSNumber *> *) locations;
```

<sub>macOS</sub>

```objc
- (void) setColors:(NSArray<NSColor *> *) colors atLocations:(NSArray<NSNumber *> *) locations;
```

## Parameters

- `colors` — An array of colors making up the transition points of the gradient.

- `locations` — An array of unit distance values that correspond to the provided colors.

## Discussion

The unit distance value of `0` represents the start of the polyline, and `1` represents the end of the polyline. A gradient may have any number of steps along the length of the polyline.

To determine a location along the polyline, use [- locationAtPointIndex:](<../mkmultipoint/location(atpointindex_).md>), or retrieve a set of locations using [locationsAtPointIndexes:](../mkmultipoint/locationsatpointindexes_.md).

## See Also

### Accessing the gradient colors

- [colors](colors.md) — An array that represents the gradient’s color transition points.
- [locations](locations-50knt.md) — An array of location indices corresponding to their respective colors.
