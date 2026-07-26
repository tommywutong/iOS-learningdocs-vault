---
title: kSecRevocationUseAnyAvailableMethod
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecrevocationuseanyavailablemethod
source_url: 'https://developer.apple.com/documentation/security/ksecrevocationuseanyavailablemethod'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecrevocationuseanyavailablemethod.json'
content_hash: 'sha256:59625674d75a95af'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecRevocationUseAnyAvailableMethod

<sub>Global Variable</sub>

Perform either OCSP or CRL checking.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var kSecRevocationUseAnyAvailableMethod: CFOptionFlags { get }
```

## Discussion

The checking is performed according to the method(s) specified in the certificate and the value of [kSecRevocationPreferCRL](ksecrevocationprefercrl.md).
