---
title: SecTransformAttributeActionBlock
framework: Security
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/sectransformattributeactionblock
source_url: 'https://developer.apple.com/documentation/security/sectransformattributeactionblock'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectransformattributeactionblock.json'
content_hash: 'sha256:e19357f11f39223f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTransformAttributeActionBlock

<sub>Type Alias</sub>

A block used to override the default attribute handling for when an attribute is set.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
typealias SecTransformAttributeActionBlock = (SecTransformAttribute, CFTypeRef) -> Unmanaged<CFTypeRef>?
```

## Parameters

- `attribute` — The attribute whose default is being overridden or NULL if this is a generic notification override

- `value` — Proposed new value for the attribute.

## Return Value

The new value of the attribute if successful or a [CFError](../corefoundation/cferror.md) object on failure. If a transform needs to have a [CFError](../corefoundation/cferror.md) as the value of an attribute, then place the object in a container, such as a [CFArray](../corefoundation/cfarray.md) or [CFDictionary](../corefoundation/cfdictionary.md) object.
