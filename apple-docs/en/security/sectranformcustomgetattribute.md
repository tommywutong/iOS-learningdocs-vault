---
title: SecTranformCustomGetAttribute
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（10.8 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/sectranformcustomgetattribute
source_url: 'https://developer.apple.com/documentation/security/sectranformcustomgetattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectranformcustomgetattribute.json'
content_hash: 'sha256:e72eeaff717bbb46'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTranformCustomGetAttribute

<sub>Function</sub>

Gets an attribute value from a custom transform.

> [!warning] Deprecated
> Use [SecTransformCustomGetAttribute](<sectransformcustomgetattribute(______).md>) instead.

<sub>Mac Catalyst, macOS</sub>

```objc
extern CFTypeRefSecTranformCustomGetAttribute(SecTransformImplementationRef ref, SecTransformStringOrAttributeRef attribute, SecTransformMetaAttributeType type);
```

## Parameters

- `ref` — A [SecTransformImplementationRef](sectransformimplementationref.md) that is bound to an instance of a custom transform.

- `attribute` — The name or the attribute handle of the attribute whose value is to be retrieved. When using a name, see [Transform Attributes](transform-attributes.md) for a list of valid key names.

- `type` — The type of data to be retrieved for the attribute. See the discussion on [SecTransformMetaAttributeType](sectransformmetaattributetype.md) for details.

## Return Value

The value of the attribute.

## Discussion

> [!important] Important
> This function is deprecated. Use [SecTransformCustomGetAttribute](<sectransformcustomgetattribute(______).md>) instead.
