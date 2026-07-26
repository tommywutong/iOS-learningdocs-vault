---
title: SecItemAttr.volumeItemAttr
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secitemattr/volumeitemattr
source_url: 'https://developer.apple.com/documentation/security/secitemattr/volumeitemattr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secitemattr/volumeitemattr.json'
content_hash: 'sha256:b6de1e9073e00447'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecItemAttr](../secitemattr.md)

# SecItemAttr.volumeItemAttr

<sub>Case</sub>

Identifies the volume attribute.

<sub>Mac Catalyst, macOS</sub>

```swift
case volumeItemAttr
```

## Discussion

You use this tag to set or get a string value that represents the AppleShare volume. This is unique to AppleShare password attributes. Keychain strings should use UTF-8 encoding.
