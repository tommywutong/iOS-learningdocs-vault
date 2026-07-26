---
title: SecKeyUsage
framework: Security
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seckeyusage
source_url: 'https://developer.apple.com/documentation/security/seckeyusage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeyusage.json'
content_hash: 'sha256:c7006052f3bb5f8d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeyUsage

<sub>Structure</sub>

The flags that indicate key usage in the `KeyUsage` extension of a certificate.

<sub>macOS</sub>

```swift
struct SecKeyUsage
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<seckeyusage/init(rawvalue_).md>) — Initializes a key usage structure.

### Flags

- [kSecKeyUsageCRLSign](seckeyusage/crlsign.md) — The `CRLSign` bit is set in KeyUsage extension.
- [kSecKeyUsageContentCommitment](seckeyusage/contentcommitment.md) — The `ContentCommitment` bit is set in KeyUsage extension.
- [kSecKeyUsageCritical](seckeyusage/critical.md) — The KeyUsage extension is marked critical.
- [kSecKeyUsageDataEncipherment](seckeyusage/dataencipherment.md) — The `DataEncipherment` bit is set in KeyUsage extension.
- [kSecKeyUsageDecipherOnly](seckeyusage/decipheronly.md) — The `DecipherOnly` bit is set in KeyUsage extension.
- [kSecKeyUsageDigitalSignature](seckeyusage/digitalsignature.md) — The `DigitalSignature` bit is set in KeyUsage extension.
- [kSecKeyUsageEncipherOnly](seckeyusage/encipheronly.md) — The `EncipherOnly` bit is set in KeyUsage extension.
- [kSecKeyUsageKeyAgreement](seckeyusage/keyagreement.md) — The `KeyAgreement` bit is set in KeyUsage extension.
- [kSecKeyUsageKeyCertSign](seckeyusage/keycertsign.md) — The `KeyCertSign` bit is set in KeyUsage extension.
- [kSecKeyUsageKeyEncipherment](seckeyusage/keyencipherment.md) — The `KeyEncipherment` bit is set in KeyUsage extension.
- [kSecKeyUsageNonRepudiation](seckeyusage/nonrepudiation.md) — The `NonRepudiation` bit is set in KeyUsage extension.
- [kSecKeyUsageAll](seckeyusage/all.md) — All flags set.
