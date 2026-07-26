---
title: kSecImportItemTrust
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecimportitemtrust
source_url: 'https://developer.apple.com/documentation/security/ksecimportitemtrust'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecimportitemtrust.json'
content_hash: 'sha256:bf302d0f548af3a0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecImportItemTrust

<sub>Global Variable</sub>

Trust management object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecImportItemTrust: CFString
```

## Discussion

The corresponding value is of type `SecTrustRef`. The trust reference returned by the [SecPKCS12Import](<secpkcs12import(______).md>) function has been evaluated against the basic X.509 policy and includes as complete a certificate chain as could be constructed from the certificates in the PKCS #12 blob, certificates on the keychain, and any other certificates available to the system. You can use the [SecTrustEvaluate](<sectrustevaluate(____).md>) function if you want to know whether the certificate chain is complete and valid (according to the basic X.509 policy). There is no guarantee that the evaluation will succeed.
