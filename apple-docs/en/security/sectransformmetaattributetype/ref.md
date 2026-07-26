---
title: SecTransformMetaAttributeType.ref
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/sectransformmetaattributetype/ref
source_url: 'https://developer.apple.com/documentation/security/sectransformmetaattributetype/ref'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectransformmetaattributetype/ref.json'
content_hash: 'sha256:091d5cfb51a17a8a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecTransformMetaAttributeType](../sectransformmetaattributetype.md)

# SecTransformMetaAttributeType.ref

<sub>Case</sub>

A direct reference to an attribute’s value.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
case ref
```

## Discussion

This reference allows for direct access to an attribute without having to look up the attribute by name. If a transform commonly uses an attribute, using a reference speeds up the use of that attribute. Attribute references are not visible or valid from outside of the particular transform instance.
