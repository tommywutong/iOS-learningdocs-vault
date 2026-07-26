---
title: distance
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkroute/step/distance
source_url: 'https://developer.apple.com/documentation/mapkit/mkroute/step/distance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkroute/step/distance.json'
content_hash: 'sha256:b031d3d235abc761'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKRoute](../../mkroute.md) · [Step](../step.md)

# distance

<sub>Instance Property</sub>

The step distance, in meters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var distance: CLLocationDistance { get }
```

## Discussion

This property reflects the distance that the user covers while traversing the path of the step. It isn’t a lilnear distance between the start and end points of the step.

## See Also

### Getting additional step details

- [instructions](instructions.md) — The written instructions for following the path that the step represents.
- [notice](notice.md) — Additional notices that apply to the step.
- [transportType](transporttype.md) — The transport type of the step.
