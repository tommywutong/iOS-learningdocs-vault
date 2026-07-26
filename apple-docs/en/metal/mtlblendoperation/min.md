---
title: MTLBlendOperation.min
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlblendoperation/min
source_url: 'https://developer.apple.com/documentation/metal/mtlblendoperation/min'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblendoperation/min.json'
content_hash: 'sha256:8b8ab0e15d82f2c9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBlendOperation](../mtlblendoperation.md)

# MTLBlendOperation.min

<sub>Case</sub>

Minimum of the source and destination pixel values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case min
```

## Discussion

`RGB = min(Source.rgb, Dest.rgb)`

`A = min(Source.a, Dest.a)`

## See Also

### Blend operations

- [MTLBlendOperationAdd](add.md) — Add portions of both source and destination pixel values.
- [MTLBlendOperationSubtract](subtract.md) — Subtract a portion of the destination pixel values from a portion of the source.
- [MTLBlendOperationReverseSubtract](reversesubtract.md) — Subtract a portion of the source values from a portion of the destination pixel values.
- [MTLBlendOperationMax](max.md) — Maximum of the source and destination pixel values.
