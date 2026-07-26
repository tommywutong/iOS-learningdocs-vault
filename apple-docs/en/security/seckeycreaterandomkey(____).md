---
title: 'SecKeyCreateRandomKey(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/seckeycreaterandomkey(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeycreaterandomkey(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeycreaterandomkey%28_%3A_%3A%29.json'
content_hash: 'sha256:ffc70ab04305f94f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeyCreateRandomKey(_:_:)

<sub>Function</sub>

Generates a new public-private key pair.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecKeyCreateRandomKey(_ parameters: CFDictionary, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecKey?
```

## Parameters

- `parameters` — A dictionary you use to specify the attributes of the generated keys. See [Key Generation Attributes](key-generation-attributes.md) for details.

- `error` — An error reference pointer that [SecKeyCreateRandomKey](<seckeycreaterandomkey(____).md>) populates with a suitable error instance on failure.

## Return Value

The newly generated private key, or `NULL` on failure. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to free the key when you are done with it.

## Discussion

To get the associated public key, use [SecKeyCopyPublicKey](<seckeycopypublickey(__).md>). [SecKeyCreateRandomKey](<seckeycreaterandomkey(____).md>) fails and returns [errSecInteractionNotAllowed](errsecinteractionnotallowed.md) if you call it in the background on iPhone or iPad while the device is locked.
