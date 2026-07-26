---
title: MTLBlendOperation
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlblendoperation
source_url: 'https://developer.apple.com/documentation/metal/mtlblendoperation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblendoperation.json'
content_hash: 'sha256:950abd4ec0bebc0d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLBlendOperation

<sub>Enumeration</sub>

For every pixel, `MTLBlendOperation` determines how to combine and weight the source fragment values with the destination values. Some blend operations multiply the source values by a source blend factor (SBF), multiply the destination values by a destination blend factor (DBF), and then combine the results using addition or subtraction. Other blend operations use either a minimum or maximum function to determine the result.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLBlendOperation
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Blend operations

- [MTLBlendOperationAdd](mtlblendoperation/add.md) — Add portions of both source and destination pixel values.
- [MTLBlendOperationSubtract](mtlblendoperation/subtract.md) — Subtract a portion of the destination pixel values from a portion of the source.
- [MTLBlendOperationReverseSubtract](mtlblendoperation/reversesubtract.md) — Subtract a portion of the source values from a portion of the destination pixel values.
- [MTLBlendOperationMin](mtlblendoperation/min.md) — Minimum of the source and destination pixel values.
- [MTLBlendOperationMax](mtlblendoperation/max.md) — Maximum of the source and destination pixel values.

### Enumeration Cases

- [MTLBlendOperationUnspecialized](mtlblendoperation/unspecialized.md) — Defers assigning the blend operation.

### Initializers

- [init(rawValue:)](<mtlblendoperation/init(rawvalue_).md>)

## See Also

### Controlling blend operations

- [blendingEnabled](mtlrenderpipelinecolorattachmentdescriptor/isblendingenabled.md) — A Boolean value that determines whether blending is enabled.
- [alphaBlendOperation](mtlrenderpipelinecolorattachmentdescriptor/alphablendoperation.md) — The blend operation assigned for the alpha data.
- [rgbBlendOperation](mtlrenderpipelinecolorattachmentdescriptor/rgbblendoperation.md) — The blend operation assigned for the RGB data.
