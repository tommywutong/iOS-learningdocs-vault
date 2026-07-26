---
title: 'SecIdentityCreateWithCertificate(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/secidentitycreatewithcertificate(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/secidentitycreatewithcertificate(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secidentitycreatewithcertificate%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:44437cc8cb9a7e3a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecIdentityCreateWithCertificate(_:_:_:)

<sub>Function</sub>

Creates a new identity for a certificate and its associated private key.

<sub>macOS</sub>

```swift
func SecIdentityCreateWithCertificate(_ keychainOrArray: CFTypeRef?, _ certificateRef: SecCertificate, _ identityRef: UnsafeMutablePointer<SecIdentity?>) -> OSStatus
```

## Parameters

- `keychainOrArray` — A reference to a keychain or an array of keychains to search for the associated private key. Specify `NULL` to search the user’s default keychain search list.

- `certificateRef` — The certificate for which you want to create an identity.

- `identityRef` — On return, an identity object for the certificate and its associated private key. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to release this object when you are finished with it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

If the associated private key is not found in one of the specified keychains, this function fails with an appropriate error code (usually [errSecItemNotFound](errsecitemnotfound.md)), and does not return anything in the `identityRef` parameter.
