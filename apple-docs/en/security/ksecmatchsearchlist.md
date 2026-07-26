---
title: kSecMatchSearchList
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecmatchsearchlist
source_url: 'https://developer.apple.com/documentation/security/ksecmatchsearchlist'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecmatchsearchlist.json'
content_hash: 'sha256:57df41a30d5aa2a5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecMatchSearchList

<sub>Global Variable</sub>

A key whose value indicates a list of items to search.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecMatchSearchList: CFString
```

## Discussion

The value is a [CFArray](../corefoundation/cfarray.md) of [SecKeychain](seckeychain.md) items. If provided, the search will be limited to the keychain items contained in this list.
