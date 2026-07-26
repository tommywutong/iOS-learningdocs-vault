---
title: SecTransformMetaAttributeType.required
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/sectransformmetaattributetype/required
source_url: 'https://developer.apple.com/documentation/security/sectransformmetaattributetype/required'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectransformmetaattributetype/required.json'
content_hash: 'sha256:d3d3dd5884ddb313'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecTransformMetaAttributeType](../sectransformmetaattributetype.md)

# SecTransformMetaAttributeType.required

<sub>Case</sub>

Indicates whether the attribute value is optional.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
case required
```

## Discussion

Specifies if an attribute must have a non `NULL` value set or have an incoming connection before the transform starts to execute. This metadata has a default value of [true](../../swift/true.md) for the input attribute, but [false](../../swift/false.md) for all other attributes.
