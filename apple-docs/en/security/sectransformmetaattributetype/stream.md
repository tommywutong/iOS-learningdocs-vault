---
title: SecTransformMetaAttributeType.stream
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/sectransformmetaattributetype/stream
source_url: 'https://developer.apple.com/documentation/security/sectransformmetaattributetype/stream'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectransformmetaattributetype/stream.json'
content_hash: 'sha256:b1bf8c65ab28689f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecTransformMetaAttributeType](../sectransformmetaattributetype.md)

# SecTransformMetaAttributeType.stream

<sub>Case</sub>

The attribute expects stream operation.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
case stream
```

## Discussion

Specifies if the attribute should expect a series of values ending with a `NULL` to specify the end of the data stream. This metadata has a default value of [true](../../swift/true.md) for the input and output attributes, but is [false](../../swift/false.md) for all other attributes.
