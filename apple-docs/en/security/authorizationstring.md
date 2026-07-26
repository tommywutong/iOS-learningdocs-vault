---
title: AuthorizationString
framework: Security
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/authorizationstring
source_url: 'https://developer.apple.com/documentation/security/authorizationstring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationstring.json'
content_hash: 'sha256:186729649a528c4d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# AuthorizationString

<sub>Type Alias</sub>

A zero-terminated string in UTF-8 encoding.

<sub>Mac Catalyst, macOS</sub>

```swift
typealias AuthorizationString = UnsafePointer<CChar>
```

## Discussion

Use this in a call to the [AuthorizationCopyInfo](<authorizationcopyinfo(______).md>) function for the `tag` parameter.
