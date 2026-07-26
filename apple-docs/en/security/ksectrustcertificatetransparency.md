---
title: kSecTrustCertificateTransparency
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksectrustcertificatetransparency
source_url: 'https://developer.apple.com/documentation/security/ksectrustcertificatetransparency'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksectrustcertificatetransparency.json'
content_hash: 'sha256:58066a51658625b4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecTrustCertificateTransparency

<sub>Global Variable</sub>

A key whose value is a Boolean used to indicate Certificate Transparency.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecTrustCertificateTransparency: CFString
```

## Discussion

When the key is present and the value set to [kCFBooleanTrue](../corefoundation/kcfbooleantrue.md), it indicates the chain is Certificate Transparency (CT) qualified.
