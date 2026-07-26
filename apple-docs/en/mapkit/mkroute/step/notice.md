---
title: notice
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkroute/step/notice
source_url: 'https://developer.apple.com/documentation/mapkit/mkroute/step/notice'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkroute/step/notice.json'
content_hash: 'sha256:22adea691972b094'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKRoute](../../mkroute.md) · [Step](../step.md)

# notice

<sub>Instance Property</sub>

Additional notices that apply to the step.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var notice: String? { get }
```

## Discussion

Notices may include legal information or warning notices that apply to the step. For example, if the step crosses railroad tracks, it might contain a notice that warns the user not to cross the tracks when the lights are flashing.

## See Also

### Getting additional step details

- [instructions](instructions.md) — The written instructions for following the path that the step represents.
- [distance](distance.md) — The step distance, in meters.
- [transportType](transporttype.md) — The transport type of the step.
