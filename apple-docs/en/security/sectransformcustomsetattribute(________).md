---
title: 'SecTransformCustomSetAttribute(_:_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sectransformcustomsetattribute(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectransformcustomsetattribute(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectransformcustomsetattribute%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:02983280285a825c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTransformCustomSetAttribute(_:_:_:_:)

<sub>Function</sub>

Sets an attribute value on a custom transform.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
func SecTransformCustomSetAttribute(_ ref: SecTransformImplementationRef, _ attribute: SecTransformStringOrAttribute, _ type: SecTransformMetaAttributeType, _ value: CFTypeRef?) -> CFTypeRef?
```

## Parameters

- `ref` — A [SecTransformImplementationRef](sectransformimplementationref.md) that is bound to an instance of a custom transform.

- `attribute` — The name or the attribute handle of the attribute whose value is to be set. When using a name, see [Transform Attributes](transform-attributes.md) for a list of valid key names.

- `type` — The type of data to be retrieved for the attribute. See the discussion on [SecTransformMetaAttributeType](sectransformmetaattributetype.md) for details.

- `value` — The new value for the attribute

## Return Value

An error on failure, or `NULL` on success. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to free the error’s memory when you are done with it.

## Discussion

Unlike the [SecTransformSetAttribute](<sectransformsetattribute(________).md>) function this function can set attribute values while a transform is executing. These values are limited to the custom transform instance that is bound to the `ref` parameter.
