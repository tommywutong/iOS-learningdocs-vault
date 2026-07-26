---
title: SecTransformMetaAttributeType.externalize
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/sectransformmetaattributetype/externalize
source_url: 'https://developer.apple.com/documentation/security/sectransformmetaattributetype/externalize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectransformmetaattributetype/externalize.json'
content_hash: 'sha256:fd4263ca4e85b7b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecTransformMetaAttributeType](../sectransformmetaattributetype.md)

# SecTransformMetaAttributeType.externalize

<sub>Case</sub>

The attribute is exportable.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
case externalize
```

## Discussion

Specifies if this attribute should be written out when creating the external representation of this transform. This metadata has a default value of [true](../../swift/true.md).
