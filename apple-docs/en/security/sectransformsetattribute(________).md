---
title: 'SecTransformSetAttribute(_:_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sectransformsetattribute(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectransformsetattribute(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectransformsetattribute%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:35458ef36133dc56'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTransformSetAttribute(_:_:_:_:)

<sub>Function</sub>

Sets a static value for an attribute in a transform.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
func SecTransformSetAttribute(_ transformRef: SecTransform, _ key: CFString, _ value: CFTypeRef, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool
```

## Parameters

- `transformRef` — The transform whose attribute is to be set.

- `key` — The name of the attribute to be set. See [Transform Attributes](transform-attributes.md) for a list of valid keys and possible values.

- `value` — The static value to set for the named attribute.

- `error` — A pointer that the function uses to provide an error object with details if an error occurs. The caller becomes responsible for the object’s memory. Pass `NULL` to ignore the error.

## Return Value

A Boolean set to [true](../swift/true.md) if the call succeeds. Otherwise, the `error` parameter contains information about the failure.

## Discussion

This function is useful for things like iteration counts and other non-changing values. It returns an error and the named attribute is not changed if [SecTransformExecute](<sectransformexecute(____).md>) has already been called on the transform.

Compare this function with the [SecTransformConnectTransforms](<sectransformconnecttransforms(____________).md>) function which sets derived data.
