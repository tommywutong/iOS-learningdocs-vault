---
title: kSecAttrComment
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattrcomment
source_url: 'https://developer.apple.com/documentation/security/ksecattrcomment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattrcomment.json'
content_hash: 'sha256:b3211ab2a2e156a6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrComment

<sub>Global Variable</sub>

A key with a value that’s a string indicating a comment associated with the item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecAttrComment: CFString
```

## Discussion

The corresponding value is of type [CFString](../corefoundation/cfstring.md) and contains the user-editable comment for this item.
