---
title: colors
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkgradientpolylinerenderer/colors
source_url: 'https://developer.apple.com/documentation/mapkit/mkgradientpolylinerenderer/colors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkgradientpolylinerenderer/colors.json'
content_hash: 'sha256:f2eaf27066b2c43e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKGradientPolylineRenderer](../mkgradientpolylinerenderer.md)

# colors

<sub>Instance Property</sub>

An array that represents the gradient’s color transition points.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var colors: [UIColor] { get }
```

<sub>macOS</sub>

```swift
var colors: [NSColor] { get }
```

## See Also

### Accessing the gradient colors

- [setColors(_:locations:)](<setcolors(__locations_)-3xrou.md>) — Sets the iOS colors and corresponding unit distance values to create gradients.
- [setColors(_:locations:)](<setcolors(__locations_)-1tuft.md>) — Sets the macOS colors and corresponding unit distance values to create gradients.
- [locations](locations-7k6qz.md) — An array of location indexes that correspond to their respective colors.
