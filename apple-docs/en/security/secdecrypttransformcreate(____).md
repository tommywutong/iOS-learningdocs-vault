---
title: 'SecDecryptTransformCreate(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/secdecrypttransformcreate(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/secdecrypttransformcreate(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secdecrypttransformcreate%28_%3A_%3A%29.json'
content_hash: 'sha256:918fd25ce99dd967'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecDecryptTransformCreate(_:_:)

<sub>Function</sub>

Creates a decryption transform object.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
func SecDecryptTransformCreate(_ keyRef: SecKey, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform
```

## Parameters

- `keyRef` — The key for the operation

- `error` — A pointer to a [CFError](../corefoundation/cferror.md). This pointer will be set if an error occurred. This value may be `NULL` if you do not want an error returned.

## Return Value

A pointer to a new transform or `nil` on error. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to free this object’s memory when you are done with it.

## Discussion

This function creates a transform which decrypts data.
