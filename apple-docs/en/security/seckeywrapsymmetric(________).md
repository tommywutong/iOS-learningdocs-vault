---
title: 'SecKeyWrapSymmetric(_:_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeywrapsymmetric(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeywrapsymmetric(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeywrapsymmetric%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:46087d3f569d8a51'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeyWrapSymmetric(_:_:_:_:)

<sub>Function</sub>

Wraps a symmetric key with another key.

> [!warning] Deprecated
> No longer supported

<sub>macOS</sub>

```swift
func SecKeyWrapSymmetric(_ keyToWrap: SecKey, _ wrappingKey: SecKey, _ parameters: CFDictionary, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?
```

## Parameters

- `keyToWrap` — The key to wrap.

- `wrappingKey` — The key to use when wrapping `keyToWrap`.

- `parameters` — A parameter list for the unwrapping process. This is usually either an empty dictionary or a dictionary containing a value for [kSecAttrSalt](ksecattrsalt.md).

- `error` — A pointer to a [CFError](../corefoundation/cferror.md) variable where an error object is stored upon failure. If not `NULL`, the caller is responsible for checking this variable and releasing the resulting object if it exists.

## Return Value

The wrapped key, or `NULL` on error. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to free the data’s memory when you are done with it.
