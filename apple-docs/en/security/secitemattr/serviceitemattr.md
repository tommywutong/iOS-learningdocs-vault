---
title: SecItemAttr.serviceItemAttr
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secitemattr/serviceitemattr
source_url: 'https://developer.apple.com/documentation/security/secitemattr/serviceitemattr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secitemattr/serviceitemattr.json'
content_hash: 'sha256:354d1c8c8ff6adbb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecItemAttr](../secitemattr.md)

# SecItemAttr.serviceItemAttr

<sub>Case</sub>

Identifies the service attribute.

<sub>Mac Catalyst, macOS</sub>

```swift
case serviceItemAttr
```

## Discussion

You use this tag to set or get a string that represents the service associated with this item, for example, “iTools”. This is unique to generic password attributes. Keychain strings should use UTF-8 encoding.
