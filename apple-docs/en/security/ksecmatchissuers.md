---
title: kSecMatchIssuers
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecmatchissuers
source_url: 'https://developer.apple.com/documentation/security/ksecmatchissuers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecmatchissuers.json'
content_hash: 'sha256:119305163b8946b5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecMatchIssuers

<sub>Global Variable</sub>

A key whose value is a string to match against a certificate or identity’s issuers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecMatchIssuers: CFString
```

## Discussion

The corresponding value is of type [CFArray](../corefoundation/cfarray.md), where the array consists of X.500 names of type [CFData](../corefoundation/cfdata.md). If provided, returned certificates or identities are limited to those whose certificate chain contains one of the issuers provided in this list.
