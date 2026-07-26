---
title: 'SecIdentityCopyCertificate(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/secidentitycopycertificate(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/secidentitycopycertificate(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secidentitycopycertificate%28_%3A_%3A%29.json'
content_hash: 'sha256:a5209bca133bc9a2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecIdentityCopyCertificate(_:_:)

<sub>Function</sub>

Retrieves a certificate associated with an identity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecIdentityCopyCertificate(_ identityRef: SecIdentity, _ certificateRef: UnsafeMutablePointer<SecCertificate?>) -> OSStatus
```

## Parameters

- `identityRef` — The identity object for the identity whose certificate you wish to retrieve.

- `certificateRef` — On return, points to the certificate object associated with the specified identity. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to release this object when you are finished with it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

An identity is a digital certificate together with its associated private key.

For a certificate in a keychain, you can cast the `SecCertificateRef` data type to a `SecKeychainItemRef` for use with Keychain Services functions.
