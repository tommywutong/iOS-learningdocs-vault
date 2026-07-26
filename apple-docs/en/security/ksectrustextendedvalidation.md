---
title: kSecTrustExtendedValidation
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksectrustextendedvalidation
source_url: 'https://developer.apple.com/documentation/security/ksectrustextendedvalidation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksectrustextendedvalidation.json'
content_hash: 'sha256:df441df600d3d6df'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecTrustExtendedValidation

<sub>Global Variable</sub>

A key whose value is a Boolean used to indicate Extended Validation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecTrustExtendedValidation: CFString
```

## Discussion

When the key is present and the value set to [kCFBooleanTrue](../corefoundation/kcfbooleantrue.md), it indicates the chain is validated for Extended Validation (EV).
