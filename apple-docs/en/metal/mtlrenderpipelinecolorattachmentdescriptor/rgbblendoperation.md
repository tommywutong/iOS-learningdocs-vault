---
title: rgbBlendOperation
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpipelinecolorattachmentdescriptor/rgbblendoperation
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinecolorattachmentdescriptor/rgbblendoperation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinecolorattachmentdescriptor/rgbblendoperation.json'
content_hash: 'sha256:746e43be03d0123f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineColorAttachmentDescriptor](../mtlrenderpipelinecolorattachmentdescriptor.md)

# rgbBlendOperation

<sub>Instance Property</sub>

The blend operation assigned for the RGB data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var rgbBlendOperation: MTLBlendOperation { get set }
```

## Discussion

The default value is [MTLBlendOperationAdd](../mtlblendoperation/add.md).

## See Also

### Controlling blend operations

- [blendingEnabled](isblendingenabled.md) — A Boolean value that determines whether blending is enabled.
- [alphaBlendOperation](alphablendoperation.md) — The blend operation assigned for the alpha data.
- [MTLBlendOperation](../mtlblendoperation.md) — For every pixel, `MTLBlendOperation` determines how to combine and weight the source fragment values with the destination values. Some blend operations multiply the source values by a source blend factor (SBF), multiply the destination values by a destination blend factor (DBF), and then combine the results using addition or subtraction. Other blend operations use either a minimum or maximum function to determine the result.
