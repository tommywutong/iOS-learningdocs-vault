---
title: SecItemAttr.labelItemAttr
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secitemattr/labelitemattr
source_url: 'https://developer.apple.com/documentation/security/secitemattr/labelitemattr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secitemattr/labelitemattr.json'
content_hash: 'sha256:6081aba123fc05b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecItemAttr](../secitemattr.md)

# SecItemAttr.labelItemAttr

<sub>Case</sub>

Identifies the label attribute.

<sub>Mac Catalyst, macOS</sub>

```swift
case labelItemAttr
```

## Discussion

You use this tag to set or get a string value that represents a user-editable string containing the label for this item. Keychain strings should use UTF-8 encoding.
