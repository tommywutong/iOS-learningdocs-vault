---
title: kSecPolicyName
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecpolicyname
source_url: 'https://developer.apple.com/documentation/security/ksecpolicyname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecpolicyname.json'
content_hash: 'sha256:ed0ebce95ff37e55'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecPolicyName

<sub>Global Variable</sub>

A name (`CFStringRef`) that the certificate must match to satisfy this policy. For SSL/TLS, this specifies the server name which must match the common name of the certificate. For S/MIME, this specifies the RFC 822 email address.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecPolicyName: CFString
```
