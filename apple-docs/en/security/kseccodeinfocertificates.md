---
title: kSecCodeInfoCertificates
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kseccodeinfocertificates
source_url: 'https://developer.apple.com/documentation/security/kseccodeinfocertificates'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseccodeinfocertificates.json'
content_hash: 'sha256:3c1cd61889e520ad'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecCodeInfoCertificates

<sub>Global Variable</sub>

A key whose value is an array of certificates representing the certificate chain of the signing certificate as seen by the system.

<sub>Mac Catalyst, macOS</sub>

```swift
let kSecCodeInfoCertificates: CFString
```

## Discussion

The value is a [CFArray](../corefoundation/cfarray.md) array of [SecCertificate](seccertificate.md) objects that the system uses to process the signature. Absent for ad-hoc signed code. May be partial or absent in the case of error.

Specify the [kSecCSSigningInformation](kseccssigninginformation.md) flag when calling the [SecCodeCopySigningInformation](<seccodecopysigninginformation(______).md>) function to get this information.
