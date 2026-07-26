---
title: SecTrustResultType.fatalTrustFailure
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sectrustresulttype/fataltrustfailure
source_url: 'https://developer.apple.com/documentation/security/sectrustresulttype/fataltrustfailure'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustresulttype/fataltrustfailure.json'
content_hash: 'sha256:6c478dacf3084d51'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecTrustResultType](../sectrustresulttype.md)

# SecTrustResultType.fatalTrustFailure

<sub>Case</sub>

Trust is denied and no simple fix is available.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case fatalTrustFailure
```

## Discussion

This value indicates that evaluation failed because a certificate in the chain is defective. This usually represents a fundamental defect in the certificate data, such as an invalid encoding for a critical `subjectAltName` extension, an unsupported critical extension, or some other critical portion of the certificate that couldn’t be interpreted. Changing parameter values and reevaluating is unlikely to succeed unless you provide different certificates.

You might receive the [kSecTrustResultFatalTrustFailure](fataltrustfailure.md) value after an evaluation, but you can’t store the value as part of the user trust settings with a call to the [SecTrustSettingsSetTrustSettings](<../sectrustsettingssettrustsettings(______).md>) method.
