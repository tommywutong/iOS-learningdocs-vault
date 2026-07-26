---
title: SecExternalFormat
framework: Security
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secexternalformat
source_url: 'https://developer.apple.com/documentation/security/secexternalformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secexternalformat.json'
content_hash: 'sha256:b755320ebb1d8723'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecExternalFormat

<sub>Enumeration</sub>

The external format of a keychain item.

<sub>macOS</sub>

```swift
enum SecExternalFormat
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kSecFormatUnknown](secexternalformat/formatunknown.md)
- [kSecFormatOpenSSL](secexternalformat/formatopenssl.md) — Format for asymmetric (public/private) keys. OpenSSL is an open source toolkit for Secure Sockets Layer (SSL) and Transport Layer Security (TLS). Also known as X.509 for public keys.
- [kSecFormatSSH](secexternalformat/formatssh.md) — OpenSSH 1 format for asymmetric (public/private) keys. OpenSSH is an OpenBSD implementation of the Secure Shell (SSH) protocol.
- [kSecFormatBSAFE](secexternalformat/formatbsafe.md) — Format for asymmetric keys. BSAFE is a standard from RSA Security for encryption, digital signatures, and privacy.
- [kSecFormatSSHv2](secexternalformat/formatsshv2.md) — OpenSSH 2 format for public keys. OpenSSH version 2 private keys are in format `kSecFormatOpenSSL` or `kSecFormatWrappedOpenSSL`. OpenSSH is an OpenBSD implementation of the Secure Shell (SSH) protocol.
- [kSecFormatRawKey](secexternalformat/formatrawkey.md) — Format for symmetric keys. Raw, unformatted key bits. This is the default for symmetric keys.
- [kSecFormatWrappedPKCS8](secexternalformat/formatwrappedpkcs8.md) — Format for wrapped symmetric and private keys. PKCS8 is the Private-Key Information Syntax Standard from RSA Security.
- [kSecFormatWrappedOpenSSL](secexternalformat/formatwrappedopenssl.md) — Format for wrapped symmetric and private keys. OpenSSL is an open-source toolkit for Secure Sockets Layer (SSL) and Transport Layer Security (TLS).
- [kSecFormatWrappedSSH](secexternalformat/formatwrappedssh.md) — OpenSSH 1 format for wrapped symmetric and private keys.  OpenSSH is an OpenBSD implementation of the Secure Shell (SSH) protocol.
- [kSecFormatWrappedLSH](secexternalformat/formatwrappedlsh.md) — Not supported.
- [kSecFormatX509Cert](secexternalformat/formatx509cert.md) — Format for certificates. DER (distinguished encoding rules) encoded. X.509 is a standard for digital certificates from the International Telecommunication Union (ITU). This is the default for certificates.
- [kSecFormatPEMSequence](secexternalformat/formatpemsequence.md) — Sequence of certificates and keys with PEM armor. PEM armor refers to a way of expressing binary data as an ASCII string so that it can be transferred over text-only channels such as email. This is the default format for multiple items.
- [kSecFormatPKCS7](secexternalformat/formatpkcs7.md) — Sequence of certificates, no PEM armor. PKCS7 is the Cryptographic Message Syntax Standard from RSA Security, Inc.
- [kSecFormatPKCS12](secexternalformat/formatpkcs12.md) — Set of certificates and private keys. PKCS12 is the Personal Information Exchange Syntax from RSA Security, Inc.
- [kSecFormatNetscapeCertSequence](secexternalformat/formatnetscapecertsequence.md) — Set of certificates in the Netscape Certificate Sequence format.

### Initializers

- [init(rawValue:)](<secexternalformat/init(rawvalue_).md>)
