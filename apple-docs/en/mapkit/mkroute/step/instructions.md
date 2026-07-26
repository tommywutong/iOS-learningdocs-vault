---
title: instructions
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkroute/step/instructions
source_url: 'https://developer.apple.com/documentation/mapkit/mkroute/step/instructions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkroute/step/instructions.json'
content_hash: 'sha256:572560f00e6d81c0'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKRoute](../../mkroute.md) · [Step](../step.md)

# instructions

<sub>Instance Property</sub>

The written instructions for following the path that the step represents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var instructions: String { get }
```

## Discussion

The framework localizes the string in this property according to the user’s language preferences. You can present this string to the user from your app’s interface.

## See Also

### Getting additional step details

- [notice](notice.md) — Additional notices that apply to the step.
- [distance](distance.md) — The step distance, in meters.
- [transportType](transporttype.md) — The transport type of the step.
