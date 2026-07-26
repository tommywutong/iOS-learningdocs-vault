---
title: 'SecEncodeTransformCreate(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/secencodetransformcreate(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/secencodetransformcreate(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secencodetransformcreate%28_%3A_%3A%29.json'
content_hash: 'sha256:78bee293cd6ba73d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecEncodeTransformCreate(_:_:)

<sub>Function</sub>

Creates an encode transform object.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
func SecEncodeTransformCreate(_ encodeType: CFTypeRef, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform?
```

## Parameters

- `encodeType` — The type of digest to compute. You may pass `NULL` for this parameter, in which case an appropriate algorithm will be chosen for you. See `Encoding Types` for a list of valid values.

- `error` — A pointer to a [CFError](../corefoundation/cferror.md). This pointer will be set if an error occurred. This value may be `nil` if you do not want an error returned.

## Return Value

A pointer to a new transform or `NULL` on error. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to free this object’s memory when you are done with it.

## Discussion

This function creates a transform which computes an encode.
