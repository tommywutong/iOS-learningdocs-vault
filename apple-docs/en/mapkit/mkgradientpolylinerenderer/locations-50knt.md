---
title: locations
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkgradientpolylinerenderer/locations-50knt
source_url: 'https://developer.apple.com/documentation/mapkit/mkgradientpolylinerenderer/locations-50knt'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkgradientpolylinerenderer/locations-50knt.json'
content_hash: 'sha256:df93dab3cd8f47b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKGradientPolylineRenderer](../mkgradientpolylinerenderer.md)

# locations

<sub>Instance Property</sub>

An array of location indices corresponding to their respective colors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, copy, readonly) NSArray<NSNumber *> * locations;
```

## See Also

### Accessing the gradient colors

- [setColors:atLocations:](setcolors_atlocations_.md) — Sets the colors and corresponding unit distance values to create gradients.
- [colors](colors.md) — An array that represents the gradient’s color transition points.
