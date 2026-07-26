---
title: SecTrustResultType.unspecified
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sectrustresulttype/unspecified
source_url: 'https://developer.apple.com/documentation/security/sectrustresulttype/unspecified'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustresulttype/unspecified.json'
content_hash: 'sha256:57939add18b1fb52'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecTrustResultType](../sectrustresulttype.md)

# SecTrustResultType.unspecified

<sub>Case</sub>

The user did not specify a trust setting.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case unspecified
```

## Discussion

This value indicates that evaluation reached an (implicitly trusted) anchor certificate without any evaluation failures, but never encountered any explicitly stated user-trust preference. This is the most common return value. The Keychain Access utility refers to this value as the “Use System Policy,” which is the default user setting.

When receiving this value, most apps should trust the chain. If you want to ask the user what to do in macOS, use an instance of the [SFCertificateTrustPanel](../../securityinterface/sfcertificatetrustpanel.md) class.

When you evaluate a trust, the evaluation starts with the leaf certificate and works through the chain down to the anchor. The [SecTrustSettingsCopyTrustSettings](<../sectrustsettingscopytrustsettings(______).md>) method returns the user trust settings of the first certificate for which the result code is other than [kSecTrustResultUnspecified](unspecified.md).
