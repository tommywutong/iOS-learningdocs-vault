---
title: SecTransformMetaAttributeType.canCycle
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/sectransformmetaattributetype/cancycle
source_url: 'https://developer.apple.com/documentation/security/sectransformmetaattributetype/cancycle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectransformmetaattributetype/cancycle.json'
content_hash: 'sha256:c5086f2390c76c3f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecTransformMetaAttributeType](../sectransformmetaattributetype.md)

# SecTransformMetaAttributeType.canCycle

<sub>Case</sub>

The transform allows cyclic behavior.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
case canCycle
```

## Discussion

A transform group is a directed graph which is typically acyclic. Some transforms need to work with cycles. For example, a transform that emits a header and trailer around the data of another transform must create a cycle. If this metadata set to [true](../../swift/true.md), no error is returned if a cycle is detected for this attribute.
