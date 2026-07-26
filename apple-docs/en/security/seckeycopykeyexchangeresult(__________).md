---
title: 'SecKeyCopyKeyExchangeResult(_:_:_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/seckeycopykeyexchangeresult(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeycopykeyexchangeresult(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeycopykeyexchangeresult%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:1fbc4b6c4222397d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeyCopyKeyExchangeResult(_:_:_:_:_:)

<sub>Function</sub>

Performs the Diffie-Hellman style of key exchange with optional key-derivation steps.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecKeyCopyKeyExchangeResult(_ privateKey: SecKey, _ algorithm: SecKeyAlgorithm, _ publicKey: SecKey, _ parameters: CFDictionary, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?
```

## Return Value

A data object representing the result of the key exchange operation or `NULL` on failure. In Objective-C, call [CFRelease](../corefoundation/cfrelease.md) to free the data object’s memory when you are done with it.
