---
title: isBlendingEnabled
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpipelinecolorattachmentdescriptor/isblendingenabled
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinecolorattachmentdescriptor/isblendingenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinecolorattachmentdescriptor/isblendingenabled.json'
content_hash: 'sha256:0d92a3bd987be163'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineColorAttachmentDescriptor](../mtlrenderpipelinecolorattachmentdescriptor.md)

# isBlendingEnabled

<sub>Instance Property</sub>

A Boolean value that determines whether blending is enabled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isBlendingEnabled: Bool { get set }
```

## Discussion

The default value is [false](../../swift/false.md), meaning blending is disabled and pixel values are unaffected by blending. Disabled blending is effectively the same as the `MTLBlendOperationAdd` blend operation with a source blend factor of `1.0` and a destination blend factor of `0.0` for both RGB and alpha.

If the value is [true](../../swift/true.md), blending is enabled and the blend descriptor property values are used to determine how source and destination color values are combined.

## See Also

### Controlling blend operations

- [alphaBlendOperation](alphablendoperation.md) — The blend operation assigned for the alpha data.
- [rgbBlendOperation](rgbblendoperation.md) — The blend operation assigned for the RGB data.
- [MTLBlendOperation](../mtlblendoperation.md) — For every pixel, `MTLBlendOperation` determines how to combine and weight the source fragment values with the destination values. Some blend operations multiply the source values by a source blend factor (SBF), multiply the destination values by a destination blend factor (DBF), and then combine the results using addition or subtraction. Other blend operations use either a minimum or maximum function to determine the result.
