---
title: SecTrustResultType.otherError
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sectrustresulttype/othererror
source_url: 'https://developer.apple.com/documentation/security/sectrustresulttype/othererror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustresulttype/othererror.json'
content_hash: 'sha256:c50f01a6e069457c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecTrustResultType](../sectrustresulttype.md)

# SecTrustResultType.otherError

<sub>Case</sub>

A value that indicates a failure other than trust evaluation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case otherError
```

## Discussion

This value indicates that evaluation failed for some other reason. This can be caused by either a revoked certificate or by OS-level errors that are unrelated to the certificates themselves.

You might receive the [kSecTrustResultOtherError](othererror.md) value after an evaluation, but you can’t store the value as part of the user trust settings with a call to the [SecTrustSettingsSetTrustSettings](<../sectrustsettingssettrustsettings(______).md>) method.
