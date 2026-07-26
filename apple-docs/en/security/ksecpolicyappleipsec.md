---
title: kSecPolicyAppleIPsec
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecpolicyappleipsec
source_url: 'https://developer.apple.com/documentation/security/ksecpolicyappleipsec'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecpolicyappleipsec.json'
content_hash: 'sha256:32fa34ac934cf318'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecPolicyAppleIPsec

<sub>Global Variable</sub>

Policy for use in IPsec communication. Functionally identical to SSL policy. A separate OID is provided to facilitate per-policy, per-certificate trust settings using the `SecTrust` mechanism.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecPolicyAppleIPsec: CFString
```
