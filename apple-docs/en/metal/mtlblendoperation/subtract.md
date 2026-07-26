---
title: MTLBlendOperation.subtract
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlblendoperation/subtract
source_url: 'https://developer.apple.com/documentation/metal/mtlblendoperation/subtract'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblendoperation/subtract.json'
content_hash: 'sha256:3ab498f1672fd791'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBlendOperation](../mtlblendoperation.md)

# MTLBlendOperation.subtract

<sub>Case</sub>

Subtract a portion of the destination pixel values from a portion of the source.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case subtract
```

## Discussion

`RGB = Source.rgb * SBF - Dest.rgb * DBF`

`A = Source.a * SBF - Dest.a * DBF`

## See Also

### Blend operations

- [MTLBlendOperationAdd](add.md) — Add portions of both source and destination pixel values.
- [MTLBlendOperationReverseSubtract](reversesubtract.md) — Subtract a portion of the source values from a portion of the destination pixel values.
- [MTLBlendOperationMin](min.md) — Minimum of the source and destination pixel values.
- [MTLBlendOperationMax](max.md) — Maximum of the source and destination pixel values.
