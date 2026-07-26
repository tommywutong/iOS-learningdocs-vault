---
title: kSecMatchLimit
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecmatchlimit
source_url: 'https://developer.apple.com/documentation/security/ksecmatchlimit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecmatchlimit.json'
content_hash: 'sha256:d12d5071c34b1ca4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecMatchLimit

<sub>Global Variable</sub>

A key whose value indicates the match limit.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecMatchLimit: CFString
```

## Discussion

The corresponding value is of type [CFNumber](../corefoundation/cfnumber.md). If provided, this value specifies the maximum number of results to return or otherwise act upon. For a single item, specify [kSecMatchLimitOne](ksecmatchlimitone.md). To specify all matching items, specify [kSecMatchLimitAll](ksecmatchlimitall.md). The default behavior is function-dependent.
