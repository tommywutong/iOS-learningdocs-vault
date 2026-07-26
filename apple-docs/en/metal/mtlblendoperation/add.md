---
title: MTLBlendOperation.add
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlblendoperation/add
source_url: 'https://developer.apple.com/documentation/metal/mtlblendoperation/add'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblendoperation/add.json'
content_hash: 'sha256:b4c922a259d286a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBlendOperation](../mtlblendoperation.md)

# MTLBlendOperation.add

<sub>Case</sub>

Add portions of both source and destination pixel values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case add
```

## Discussion

`RGB = Source.rgb * SBF + Dest.rgb * DBF`

`A = Source.a * SBF + Dest.a * DBF`

## See Also

### Blend operations

- [MTLBlendOperationSubtract](subtract.md) — Subtract a portion of the destination pixel values from a portion of the source.
- [MTLBlendOperationReverseSubtract](reversesubtract.md) — Subtract a portion of the source values from a portion of the destination pixel values.
- [MTLBlendOperationMin](min.md) — Minimum of the source and destination pixel values.
- [MTLBlendOperationMax](max.md) — Maximum of the source and destination pixel values.
