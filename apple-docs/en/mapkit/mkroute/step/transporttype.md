---
title: transportType
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkroute/step/transporttype
source_url: 'https://developer.apple.com/documentation/mapkit/mkroute/step/transporttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkroute/step/transporttype.json'
content_hash: 'sha256:9361cc73fe9ec531'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKRoute](../../mkroute.md) · [Step](../step.md)

# transportType

<sub>Instance Property</sub>

The transport type of the step.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var transportType: MKDirectionsTransportType { get }
```

## Discussion

This property reflects the transport type employed by the step and may differ from the transport type of the overall route.

## See Also

### Getting additional step details

- [instructions](instructions.md) — The written instructions for following the path that the step represents.
- [notice](notice.md) — Additional notices that apply to the step.
- [distance](distance.md) — The step distance, in meters.
