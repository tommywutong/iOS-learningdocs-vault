---
title: 'SecDecodeTransformCreate(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/secdecodetransformcreate(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/secdecodetransformcreate(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secdecodetransformcreate%28_%3A_%3A%29.json'
content_hash: 'sha256:dc004cec096f923a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecDecodeTransformCreate(_:_:)

<sub>Function</sub>

Creates a decode transform object.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
func SecDecodeTransformCreate(_ DecodeType: CFTypeRef, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform?
```

## Parameters

- `DecodeType` — The type of digest to decode. You may pass `NULL` for this parameter, in which case an appropriate algorithm will be chosen for you. See `Encoding Types` for a list of valid values.

- `error` — A pointer to a [CFError](../corefoundation/cferror.md). This pointer will be set if an error occurred. This value may be `NULL` if you do not want an error returned.

## Return Value

A pointer to a new transform or `NULL` on error. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to free this object’s memory when you are done with it.

## Discussion

This function creates a transform which computes a decode.
