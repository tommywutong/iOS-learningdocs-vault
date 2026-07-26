---
title: 'SecTransformPushbackAttribute(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sectransformpushbackattribute(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectransformpushbackattribute(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectransformpushbackattribute%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:b52b5030d6d9faba'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTransformPushbackAttribute(_:_:_:)

<sub>Function</sub>

Pushes a single value back for a specific attribute.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
func SecTransformPushbackAttribute(_ ref: SecTransformImplementationRef, _ attribute: SecTransformStringOrAttribute, _ value: CFTypeRef) -> CFTypeRef?
```

## Parameters

- `ref` — A [SecTransformImplementationRef](sectransformimplementationref.md) that is bound to an instance of a custom transform.

- `attribute` — The name or the attribute handle of the attribute whose value is to be pushed back. When using a name, see [Transform Attributes](transform-attributes.md) for a list of valid key names.

- `value` — The value being pushed back.

## Return Value

An error on failure, or `NULL` on success. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to free the error’s memory when you are done with it.

## Discussion

Calling this function stops the flow of data into the specified attribute until any attribute is changed for the transform instance bound to the `ref` parameter.
