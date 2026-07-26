---
title: SecItemAttr.accountItemAttr
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secitemattr/accountitemattr
source_url: 'https://developer.apple.com/documentation/security/secitemattr/accountitemattr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secitemattr/accountitemattr.json'
content_hash: 'sha256:b08d1e9063c2c526'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecItemAttr](../secitemattr.md)

# SecItemAttr.accountItemAttr

<sub>Case</sub>

Identifies the account attribute.

<sub>Mac Catalyst, macOS</sub>

```swift
case accountItemAttr
```

## Discussion

You use this tag to set or get a string that represents the user account. It also applies to generic, Internet, and AppleShare password items. Keychain strings should use UTF-8 encoding.
