---
title: steps
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkroute/steps
source_url: 'https://developer.apple.com/documentation/mapkit/mkroute/steps'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkroute/steps.json'
content_hash: 'sha256:1a054052422fa926'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKRoute](../mkroute.md)

# steps

<sub>Instance Property</sub>

The array of steps that create the overall route.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var steps: [MKRoute.Step] { get }
```

## Discussion

The array contains one or more [Step](step.md) objects representing distinct portions of the route. Each step corresponds to a single direction that must be followed along the route.

## See Also

### Getting the route geometry

- [polyline](polyline.md) — The detailed route geometry.
- [Step](step.md) — One portion of an overall route.
