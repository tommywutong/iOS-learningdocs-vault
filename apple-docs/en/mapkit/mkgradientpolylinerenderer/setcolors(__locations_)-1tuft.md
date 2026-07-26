---
title: 'setColors(_:locations:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkgradientpolylinerenderer/setcolors(_:locations:)-1tuft'
source_url: 'https://developer.apple.com/documentation/mapkit/mkgradientpolylinerenderer/setcolors(_:locations:)-1tuft'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkgradientpolylinerenderer/setcolors%28_%3Alocations%3A%29-1tuft.json'
content_hash: 'sha256:2b01d8420db2a541'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKGradientPolylineRenderer](../mkgradientpolylinerenderer.md)

# setColors(_:locations:)

<sub>Instance Method</sub>

Sets the macOS colors and corresponding unit distance values to create gradients.

<sub>macOS</sub>

```swift
func setColors(_ colors: [NSColor], locations: [CGFloat])
```

## Parameters

- `colors` — An array of colors making up the transition points of the gradient.

- `locations` — An array of unit distance values that correspond to the provided colors.

## Discussion

The unit distance value of `0` represents the start of the polyline, and `1` represents the end of the polyline. A gradient may have any number of steps along the length of the polyline.

To determine a location along the polyline, use [- locationAtPointIndex:](<../mkmultipoint/location(atpointindex_).md>), or retrieve a set of locations using [locations](locations-7k6qz.md).

## See Also

### Accessing the gradient colors

- [setColors(_:locations:)](<setcolors(__locations_)-3xrou.md>) — Sets the iOS colors and corresponding unit distance values to create gradients.
- [colors](colors.md) — An array that represents the gradient’s color transition points.
- [locations](locations-7k6qz.md) — An array of location indexes that correspond to their respective colors.
