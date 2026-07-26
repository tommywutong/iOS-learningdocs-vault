---
title: 'SecKeyUnwrapSymmetric(_:_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeyunwrapsymmetric(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeyunwrapsymmetric(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeyunwrapsymmetric%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:69b9caf60ba5ccb3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeyUnwrapSymmetric(_:_:_:_:)

<sub>Function</sub>

Unwraps a wrapped symmetric key.

> [!warning] Deprecated
> No longer supported

<sub>macOS</sub>

```swift
func SecKeyUnwrapSymmetric(_ keyToUnwrap: UnsafeMutablePointer<Unmanaged<CFData>?>, _ unwrappingKey: SecKey, _ parameters: CFDictionary, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecKey?
```

## Parameters

- `keyToUnwrap` — The wrapped key to unwrap.

- `unwrappingKey` — The key that must be used to unwrap `keyToUnwrap`.

- `parameters` — A parameter list for the unwrapping process. This is usually either an empty dictionary or a dictionary containing a value for [kSecAttrSalt](ksecattrsalt.md).

- `error` — A pointer to a [CFError](../corefoundation/cferror.md) variable where an error object is stored upon failure. If not `NULL`, the caller is responsible for checking this variable and releasing the resulting object if it exists.

## Return Value

The unwrapped key, or `NULL` on failure. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to free the key’s memory when you are done with it.
