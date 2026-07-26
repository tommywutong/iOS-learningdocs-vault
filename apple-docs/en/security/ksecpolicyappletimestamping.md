---
title: kSecPolicyAppleTimeStamping
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecpolicyappletimestamping
source_url: 'https://developer.apple.com/documentation/security/ksecpolicyappletimestamping'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecpolicyappletimestamping.json'
content_hash: 'sha256:726db426c429425b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecPolicyAppleTimeStamping

<sub>Global Variable</sub>

Policy that causes evaluation of the validity of the time stamp on a signature. This can be used to allow verification that a certificate was valid at the time that something was signed with that certificate even if the certificate is no longer valid.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecPolicyAppleTimeStamping: CFString
```
