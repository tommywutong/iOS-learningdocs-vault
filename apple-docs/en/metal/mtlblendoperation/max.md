---
title: MTLBlendOperation.max
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlblendoperation/max
source_url: 'https://developer.apple.com/documentation/metal/mtlblendoperation/max'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblendoperation/max.json'
content_hash: 'sha256:0087e06221b0abe8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBlendOperation](../mtlblendoperation.md)

# MTLBlendOperation.max

<sub>Case</sub>

Maximum of the source and destination pixel values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case max
```

## Discussion

`RGB = max(Source.rgb, Dest.rgb)`

`A = max(Source.a, Dest.a)`

## See Also

### Blend operations

- [MTLBlendOperationAdd](add.md) — Add portions of both source and destination pixel values.
- [MTLBlendOperationSubtract](subtract.md) — Subtract a portion of the destination pixel values from a portion of the source.
- [MTLBlendOperationReverseSubtract](reversesubtract.md) — Subtract a portion of the source values from a portion of the destination pixel values.
- [MTLBlendOperationMin](min.md) — Minimum of the source and destination pixel values.
