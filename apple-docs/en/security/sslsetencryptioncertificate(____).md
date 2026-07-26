---
title: 'SSLSetEncryptionCertificate(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+（9.0 起废弃）, iPadOS 5.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.2+（10.11 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslsetencryptioncertificate(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslsetencryptioncertificate(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslsetencryptioncertificate%28_%3A_%3A%29.json'
content_hash: 'sha256:8299f8343250f593'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLSetEncryptionCertificate(_:_:)

<sub>Function</sub>

Specifies the encryption certificates used for this connection.

> [!warning] Deprecated
> Using separate RSA certificates for encryption and signing is no longer supported.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLSetEncryptionCertificate(_ context: SSLContext, _ certRefs: CFArray) -> OSStatus
```

## Parameters

- `context` — An SSL session context reference.

- `certRefs` — A value of type `CFArrayRef` referring to an array of certificate references. The references are type `SecCertificateRef`, except for `certRefs[0]`, which is of type `SecIdentityRef`.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

Use this function in one of the following cases:

- The leaf certificate specified in the [SSLSetCertificate](<sslsetcertificate(____).md>) function is not capable of encryption.
- The leaf certificate specified in the [SSLSetCertificate](<sslsetcertificate(____).md>) function contains a key that is too large or strong for legal encryption in this session. In this case, a weaker certificate is specified here and is used for server-initiated key exchange.

The following assumptions are made:

- The `certRefs` parameter’s references remain valid for the lifetime of the connection.
- The specified `certRefs[0]` value is capable of encryption.

This function can be called only when no session is active.

SSL servers that enforce the SSL3 or TLS1 specification to the letter do not accept encryption certificates with key sizes larger than 512 bits for exportable ciphers (that is, for SSL sessions with 40-bit session keys). Therefore, if you wish to support exportable ciphers and your certificate has a key larger than 512 bits, you must specify a separate encryption certificate.
