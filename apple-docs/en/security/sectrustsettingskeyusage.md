---
title: SecTrustSettingsKeyUsage
framework: Security
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sectrustsettingskeyusage
source_url: 'https://developer.apple.com/documentation/security/sectrustsettingskeyusage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustsettingskeyusage.json'
content_hash: 'sha256:c38b3061274a0957'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustSettingsKeyUsage

<sub>Structure</sub>

Allowed uses for the encryption key in a certificate.

<sub>Mac Catalyst, macOS</sub>

```swift
struct SecTrustSettingsKeyUsage
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<sectrustsettingskeyusage/init(rawvalue_).md>) — Initializes a trust settings key usage structure.

### Constants

- [kSecTrustSettingsKeyUseSignature](sectrustsettingskeyusage/usesignature.md) — The key can be used to sign data or verify a signature.
- [kSecTrustSettingsKeyUseEnDecryptData](sectrustsettingskeyusage/useendecryptdata.md) — The key can be used to encrypt or decrypt data.
- [kSecTrustSettingsKeyUseEnDecryptKey](sectrustsettingskeyusage/useendecryptkey.md) — The key can be used to encrypt or decrypt (wrap or unwrap) a key.
- [kSecTrustSettingsKeyUseSignCert](sectrustsettingskeyusage/usesigncert.md) — The key can be used to sign a certificate or verify a signature.
- [kSecTrustSettingsKeyUseSignRevocation](sectrustsettingskeyusage/usesignrevocation.md) — The key can be used to sign an OCSP (online certificate status protocol) message or CRL (certificate verification list), or to verify a signature.
- [kSecTrustSettingsKeyUseKeyExchange](sectrustsettingskeyusage/usekeyexchange.md) — The key is a private key that has been shared using a key exchange protocol, such as Diffie-Hellman key exchange.
- [kSecTrustSettingsKeyUseAny](sectrustsettingskeyusage/useany.md) — The key can be used for any purpose.
