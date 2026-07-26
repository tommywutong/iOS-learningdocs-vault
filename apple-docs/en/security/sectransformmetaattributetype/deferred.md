---
title: SecTransformMetaAttributeType.deferred
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/sectransformmetaattributetype/deferred
source_url: 'https://developer.apple.com/documentation/security/sectransformmetaattributetype/deferred'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectransformmetaattributetype/deferred.json'
content_hash: 'sha256:02d0d738c8cd6578'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecTransformMetaAttributeType](../sectransformmetaattributetype.md)

# SecTransformMetaAttributeType.deferred

<sub>Case</sub>

The attribute defers notifications.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
case deferred
```

## Discussion

Determines if the AttributeSetNotification notification or the ProcessData blocks are deferred until [SecTransformExecute](<../sectransformexecute(____).md>) is called. This metadata value has a default value of [true](../../swift/true.md) for the input attribute but is [false](../../swift/false.md) for all other attributes.
