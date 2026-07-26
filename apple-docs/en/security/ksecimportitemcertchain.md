---
title: kSecImportItemCertChain
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecimportitemcertchain
source_url: 'https://developer.apple.com/documentation/security/ksecimportitemcertchain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecimportitemcertchain.json'
content_hash: 'sha256:e60b9963ebe02446'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecImportItemCertChain

<sub>Global Variable</sub>

Certificate list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecImportItemCertChain: CFString
```

## Discussion

The corresponding value is of type `CFArrayRef`. The array consists of `SecCertificateRef` objects for all the certificates in the PKCS #12 blob. This list might differ from that in the trust management object if there is more than one identity in the blob or if the blob contains extra certificates (for example, an intermediate certificate that is not yet valid but might be needed to establish validity in the near future).
