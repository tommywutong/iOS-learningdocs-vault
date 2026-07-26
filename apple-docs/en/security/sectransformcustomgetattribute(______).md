---
title: 'SecTransformCustomGetAttribute(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sectransformcustomgetattribute(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectransformcustomgetattribute(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectransformcustomgetattribute%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:4e247d364bae92cd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTransformCustomGetAttribute(_:_:_:)

<sub>Function</sub>

Gets an attribute value from a custom transform.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
func SecTransformCustomGetAttribute(_ ref: SecTransformImplementationRef, _ attribute: SecTransformStringOrAttribute, _ type: SecTransformMetaAttributeType) -> CFTypeRef?
```

## Parameters

- `ref` — A [SecTransformImplementationRef](sectransformimplementationref.md) that is bound to an instance of a custom transform.

- `attribute` — The name or the attribute handle of the attribute whose value is to be retrieved. When using a name, see [Transform Attributes](transform-attributes.md) for a list of valid key names.

- `type` — The type of data to be retrieved for the attribute. See the discussion on [SecTransformMetaAttributeType](sectransformmetaattributetype.md) for details.

## Return Value

The value of the attribute.
