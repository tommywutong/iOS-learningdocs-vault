---
title: kSecMatchSubjectContains
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecmatchsubjectcontains
source_url: 'https://developer.apple.com/documentation/security/ksecmatchsubjectcontains'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecmatchsubjectcontains.json'
content_hash: 'sha256:fccdfc75db4de19a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecMatchSubjectContains

<sub>Global Variable</sub>

A key whose value is a string to look for in a certificate or identity’s subject.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecMatchSubjectContains: CFString
```

## Discussion

The corresponding value is of type [CFString](../corefoundation/cfstring.md). If provided, returned certificates or identities are limited to those whose subject contains this string.
