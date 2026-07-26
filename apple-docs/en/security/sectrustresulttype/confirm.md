---
title: SecTrustResultType.confirm
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+（7.0 起废弃）, iPadOS 2.0+（7.0 起废弃）, tvOS 9.0+, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/sectrustresulttype/confirm
source_url: 'https://developer.apple.com/documentation/security/sectrustresulttype/confirm'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustresulttype/confirm.json'
content_hash: 'sha256:295ee3e7e3fe6159'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecTrustResultType](../sectrustresulttype.md)

# SecTrustResultType.confirm

<sub>Case</sub>

User confirmation is required before proceeding.

<sub>tvOS, visionOS, watchOS</sub>

```swift
case confirm
```

## Discussion

This value indicates that the user previously chose to always be asked for permission before accepting one of the certificates in the chain. The Keychain Access utility refers to this value as “Ask Permission.” This return value is no longer used, but may occur in older versions of macOS.

Either ask the user what to do or reject the certificate. If you ask the user what to do in macOS, use an instance of the [SFCertificateTrustPanel](../../securityinterface/sfcertificatetrustpanel.md) class.
