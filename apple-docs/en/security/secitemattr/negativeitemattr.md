---
title: SecItemAttr.negativeItemAttr
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secitemattr/negativeitemattr
source_url: 'https://developer.apple.com/documentation/security/secitemattr/negativeitemattr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secitemattr/negativeitemattr.json'
content_hash: 'sha256:7213658fbb6c5627'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecItemAttr](../secitemattr.md)

# SecItemAttr.negativeItemAttr

<sub>Case</sub>

Identifies the negative attribute.

<sub>Mac Catalyst, macOS</sub>

```swift
case negativeItemAttr
```

## Discussion

You use this tag to set or get a value of type `Boolean` that indicates whether there is a valid password associated with this keychain item. This is useful if your application doesn’t want a password for some particular service to be stored in the keychain, but prefers that it always be entered by the user. The item, which is typically invisible and with zero-length data, acts as a placeholder.
