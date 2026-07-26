---
title: 'SecDigestTransformCreate(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/secdigesttransformcreate(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/secdigesttransformcreate(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secdigesttransformcreate%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:449a1682cbe228e6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecDigestTransformCreate(_:_:_:)

<sub>Function</sub>

Creates a digest transform object.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
func SecDigestTransformCreate(_ digestType: CFTypeRef?, _ digestLength: CFIndex, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform
```

## Parameters

- `digestType` — The type of digest to compute. You may pass `NULL` for this parameter, in which case an appropriate algorithm will be chosen for you. Otherwise, use one of the values listed in `Digest Constants`.

- `digestLength` — The desired digest length. Note that certain algorithms may only support certain sizes. You may pass `0` for this parameter, in which case an appropriate length will be chosen for you.

- `error` — A pointer to a [CFError](../corefoundation/cferror.md). This pointer will be set if an error occurred. This value may be `nil` if you do not want an error returned.

## Return Value

A pointer to a new transform or `NULL` on error. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to free this object’s memory when you are done with it.

## Discussion

This function creates a transform which computes a cryptographic digest.
