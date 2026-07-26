---
title: kSecMatchValidOnDate
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecmatchvalidondate
source_url: 'https://developer.apple.com/documentation/security/ksecmatchvalidondate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecmatchvalidondate.json'
content_hash: 'sha256:e010c9b405413c8f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecMatchValidOnDate

<sub>Global Variable</sub>

A key whose value indicates the validity date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecMatchValidOnDate: CFString
```

## Discussion

The corresponding value is of type [CFDate](../corefoundation/cfdate.md). If provided, returned keys, certificates or identities are limited to those that are valid for the given date. Pass a value of [kCFNull](../corefoundation/kcfnull.md) to indicate the current date.
