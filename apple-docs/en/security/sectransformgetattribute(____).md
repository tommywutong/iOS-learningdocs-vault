---
title: 'SecTransformGetAttribute(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sectransformgetattribute(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectransformgetattribute(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectransformgetattribute%28_%3A_%3A%29.json'
content_hash: 'sha256:f9531d2eb8cc36eb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTransformGetAttribute(_:_:)

<sub>Function</sub>

Gets the current value of a transform attribute.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
func SecTransformGetAttribute(_ transformRef: SecTransform, _ key: CFString) -> CFTypeRef?
```

## Parameters

- `transformRef` — The transform whose attribute value will be retrieved.

- `key` — The name of the attribute to retrieve. See [Transform Attributes](transform-attributes.md)  for a list of valid keys.

## Return Value

The value of an attribute. If this attribute is being set as the output of another transform and [SecTransformExecute](<sectransformexecute(____).md>) has not been called on the transform or if the attribute does not exists then `NULL` will be returned.

## Discussion

This may be called after [SecTransformExecute](<sectransformexecute(____).md>).
