---
title: toValue
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cabasicanimation/tovalue
source_url: 'https://developer.apple.com/documentation/quartzcore/cabasicanimation/tovalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cabasicanimation/tovalue.json'
content_hash: 'sha256:27184376418e1d64'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CABasicAnimation](../cabasicanimation.md)

# toValue

<sub>Instance Property</sub>

Defines the value the receiver uses to end interpolation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var toValue: Any? { get set }
```

## Discussion

See [Setting Interpolation Values](../cabasicanimation.md#Setting-Interpolation-Values) for details on how `toValue` interacts with the other interpolation values.

## See Also

### Interpolation values

- [fromValue](fromvalue.md) — Defines the value the receiver uses to start interpolation.
- [byValue](byvalue.md) — Defines the value the receiver uses to perform relative interpolation.
