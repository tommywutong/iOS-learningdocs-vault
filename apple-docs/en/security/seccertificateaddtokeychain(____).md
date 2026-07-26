---
title: 'SecCertificateAddToKeychain(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/seccertificateaddtokeychain(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seccertificateaddtokeychain(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccertificateaddtokeychain%28_%3A_%3A%29.json'
content_hash: 'sha256:80950f3e1c9b3001'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecCertificateAddToKeychain(_:_:)

<sub>Function</sub>

Adds a certificate to a keychain.

<sub>macOS</sub>

```swift
func SecCertificateAddToKeychain(_ certificate: SecCertificate, _ keychain: SecKeychain?) -> OSStatus
```

## Parameters

- `certificate` — The certificate object for the certificate to add to the keychain.

- `keychain` — The keychain object for the keychain to which you want to add the certificate. Pass `NULL` to add the certificate to the default keychain.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

> [!important] Important
> To add a certificate to the login keychain, use [SecItemAdd](<secitemadd(____).md>) instead.

This function requires a certificate object, which can, for example, be created with the [SecCertificateCreateFromData](seccertificatecreatefromdata.md) function or obtained over a network (see [Secure Transport](secure-transport.md)). If the certificate has already been added to the specified keychain, the function returns [errSecDuplicateItem](errsecduplicateitem.md) and does not add another copy to the keychain. The function looks at the certificate data, not at the certificate object, to determine whether the certificate is a duplicate. It considers two certificates to be duplicates if they have the same primary key attributes.

### Special Considerations

If the keychain is locked, the system asks the user for a password or other token to unlock it. This function can therefore block while waiting for user input.
