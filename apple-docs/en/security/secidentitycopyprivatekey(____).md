---
title: 'SecIdentityCopyPrivateKey(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/secidentitycopyprivatekey(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/secidentitycopyprivatekey(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secidentitycopyprivatekey%28_%3A_%3A%29.json'
content_hash: 'sha256:2290c691af1f8c1e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecIdentityCopyPrivateKey(_:_:)

<sub>Function</sub>

Retrieves the private key associated with an identity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecIdentityCopyPrivateKey(_ identityRef: SecIdentity, _ privateKeyRef: UnsafeMutablePointer<SecKey?>) -> OSStatus
```

## Parameters

- `identityRef` — The identity object for the identity whose private key you wish to retrieve.

- `privateKeyRef` — On return, points to the private key object for the specified identity. The private key must be of class type [kSecPrivateKeyItemClass](secitemclass/privatekeyitemclass.md). In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to release this object when you are finished with it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

An identity is a digital certificate together with its associated private key.
