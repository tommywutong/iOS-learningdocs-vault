---
title: kSecAttrSubject
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattrsubject
source_url: 'https://developer.apple.com/documentation/security/ksecattrsubject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattrsubject.json'
content_hash: 'sha256:a617f8e50b8e81bc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrSubject

<sub>Global Variable</sub>

A key whose value indicates the item’s subject name.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecAttrSubject: CFString
```

## Discussion

The corresponding value is of type [CFData](../corefoundation/cfdata.md) and contains the X.500 subject name of a certificate. Items of class [kSecClassCertificate](ksecclasscertificate.md) have this attribute. Read only.
