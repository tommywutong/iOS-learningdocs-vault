---
title: instanceGreenOffset
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/careplicatorlayer/instancegreenoffset
source_url: 'https://developer.apple.com/documentation/quartzcore/careplicatorlayer/instancegreenoffset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/careplicatorlayer/instancegreenoffset.json'
content_hash: 'sha256:aa14ff602ddd36f6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAReplicatorLayer](../careplicatorlayer.md)

# instanceGreenOffset

<sub>Instance Property</sub>

Defines the offset added to the green component of the color for each replicated instance. Animatable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var instanceGreenOffset: Float { get set }
```

## Discussion

The `instanceGreenOffset` is added to the green color component of instance `k-1` to produce the modulation color of instance k.

Default is `0.0`.

## See Also

### Accessing Instance Color Values

- [instanceColor](instancecolor.md) — Defines the color used to multiply the source object. Animatable.
- [instanceRedOffset](instanceredoffset.md) — Defines the offset added to the red component of the color for each replicated instance. Animatable.
- [instanceBlueOffset](instanceblueoffset.md) — Defines the offset added to the blue component of the color for each replicated instance. Animatable.
- [instanceAlphaOffset](instancealphaoffset.md) — Defines the offset added to the alpha component of the color for each replicated instance. Animatable.
