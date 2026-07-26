---
title: SecItemAttr.addressItemAttr
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secitemattr/addressitemattr
source_url: 'https://developer.apple.com/documentation/security/secitemattr/addressitemattr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secitemattr/addressitemattr.json'
content_hash: 'sha256:a3f02ce29904e35a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecItemAttr](../secitemattr.md)

# SecItemAttr.addressItemAttr

<sub>Case</sub>

Identifies the address attribute.

<sub>Mac Catalyst, macOS</sub>

```swift
case addressItemAttr
```

## Discussion

You use this tag to set or get a value of type `string` that represents the AppleTalk zone name, or the IP or domain name that represents the server address. This is unique to AppleShare password attributes. Keychain strings should use UTF-8 encoding.
