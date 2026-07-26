---
title: 'SecIdentityCreate(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 11.2+, iPadOS 11.2+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 11.2+, visionOS 1.0+, watchOS 4.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/secidentitycreate(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/secidentitycreate(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secidentitycreate%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:4fd8d75cf00d7183'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecIdentityCreate(_:_:_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecIdentityCreate(_ allocator: CFAllocator?, _ certificate: SecCertificate, _ privateKey: SecKey) -> SecIdentity?
```

## Parameters

- `allocator` — CFAllocator to allocate the identity object. Pass NULL to use the default allocator.

- `certificate` — A certificate reference.

- `privateKey` — A private key reference.

## Return Value

An identity reference.

## Discussion

Create a new identity object from the provided certificate and its associated private key.

This interface returns null if the private does not key correspond to the public key in the certifcate.
