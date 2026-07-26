---
title: kSecTrustEvaluationDate
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksectrustevaluationdate
source_url: 'https://developer.apple.com/documentation/security/ksectrustevaluationdate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksectrustevaluationdate.json'
content_hash: 'sha256:bac34b2fa820b258'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecTrustEvaluationDate

<sub>Global Variable</sub>

A key whose value indicates the time that the trust evaluation took place.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecTrustEvaluationDate: CFString
```

## Discussion

This key is present after the results become available from performing the trust evaluation. The value is a [CFDate](../corefoundation/cfdate.md) object representing when the evaluation took place.
