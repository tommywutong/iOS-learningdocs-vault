---
title: kSecTrustCertificateTransparencyWhiteList
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 10.0+（11.0 起废弃）, iPadOS 10.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.12+（10.13 起废弃）, tvOS 10.0+（11.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 3.0+（4.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/ksectrustcertificatetransparencywhitelist
source_url: 'https://developer.apple.com/documentation/security/ksectrustcertificatetransparencywhitelist'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksectrustcertificatetransparencywhitelist.json'
content_hash: 'sha256:14a1bca0be9b9e85'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecTrustCertificateTransparencyWhiteList

<sub>Global Variable</sub>

A key whose value is a Boolean used to indicate the chain satisfies Certificate Transparency by being on the allow list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecTrustCertificateTransparencyWhiteList: CFString
```

## Discussion

When the key is present and the value set to [kCFBooleanTrue](../corefoundation/kcfbooleantrue.md), it indicates the chain is Extended Validation (EV) and not Certificate Transparency (CT) qualified, but is nonetheless included on the allow list.
