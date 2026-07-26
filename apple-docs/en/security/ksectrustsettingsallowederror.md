---
title: kSecTrustSettingsAllowedError
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksectrustsettingsallowederror
source_url: 'https://developer.apple.com/documentation/security/ksectrustsettingsallowederror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksectrustsettingsallowederror.json'
content_hash: 'sha256:81c6f03ed017358e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecTrustSettingsAllowedError

<sub>Global Variable</sub>

A number which, if encountered during certificate verification, is ignored for that certificate.

<sub>Mac Catalyst, macOS</sub>

```swift
var kSecTrustSettingsAllowedError: String { get }
```

## Discussion

The value is a [CFNumber](../corefoundation/cfnumber.md) object containing an `SInt32` value indicating a `CSSM_RETURN` result code.
