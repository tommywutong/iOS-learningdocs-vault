---
title: kSecTrustSettingsResult
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksectrustsettingsresult
source_url: 'https://developer.apple.com/documentation/security/ksectrustsettingsresult'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksectrustsettingsresult.json'
content_hash: 'sha256:01406e0c47e44a7c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecTrustSettingsResult

<sub>Global Variable</sub>

A number indicating the effective trust setting for this usage constraints dictionary.

<sub>Mac Catalyst, macOS</sub>

```swift
var kSecTrustSettingsResult: String { get }
```

## Discussion

The value is a [CFNumber](../corefoundation/cfnumber.md) object containing an `SInt32` value.
