---
title: SecItemAttr.pathItemAttr
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secitemattr/pathitemattr
source_url: 'https://developer.apple.com/documentation/security/secitemattr/pathitemattr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secitemattr/pathitemattr.json'
content_hash: 'sha256:f0c63c792d251f3e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecItemAttr](../secitemattr.md)

# SecItemAttr.pathItemAttr

<sub>Case</sub>

Identifies the path attribute.

<sub>Mac Catalyst, macOS</sub>

```swift
case pathItemAttr
```

## Discussion

You use this tag to set or get a string value that represents the path. This is unique to Internet password attributes. Keychain strings should use UTF-8 encoding.
