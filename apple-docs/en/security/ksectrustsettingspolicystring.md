---
title: kSecTrustSettingsPolicyString
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksectrustsettingspolicystring
source_url: 'https://developer.apple.com/documentation/security/ksectrustsettingspolicystring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksectrustsettingspolicystring.json'
content_hash: 'sha256:1e01c8476cdcafc6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecTrustSettingsPolicyString

<sub>Global Variable</sub>

A string containing policy-specific data.

<sub>Mac Catalyst, macOS</sub>

```swift
var kSecTrustSettingsPolicyString: String { get }
```

## Discussion

The value is a [CFString](../corefoundation/cfstring.md) object. For the SMIME policy, this string contains an email address. For the SSL policy, it contains a host name.
