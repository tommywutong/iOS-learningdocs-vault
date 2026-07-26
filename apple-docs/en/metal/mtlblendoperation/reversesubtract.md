---
title: MTLBlendOperation.reverseSubtract
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlblendoperation/reversesubtract
source_url: 'https://developer.apple.com/documentation/metal/mtlblendoperation/reversesubtract'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblendoperation/reversesubtract.json'
content_hash: 'sha256:5ea45aaa587af578'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBlendOperation](../mtlblendoperation.md)

# MTLBlendOperation.reverseSubtract

<sub>Case</sub>

Subtract a portion of the source values from a portion of the destination pixel values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case reverseSubtract
```

## Discussion

`RGB = Dest.rgb * DBF - Source.rgb * SBF`

`A = Dest.a * DBF - Source.a * SBF`

## See Also

### Blend operations

- [MTLBlendOperationAdd](add.md) — Add portions of both source and destination pixel values.
- [MTLBlendOperationSubtract](subtract.md) — Subtract a portion of the destination pixel values from a portion of the source.
- [MTLBlendOperationMin](min.md) — Minimum of the source and destination pixel values.
- [MTLBlendOperationMax](max.md) — Maximum of the source and destination pixel values.
