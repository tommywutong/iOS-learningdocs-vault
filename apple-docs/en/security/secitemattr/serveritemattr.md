---
title: SecItemAttr.serverItemAttr
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secitemattr/serveritemattr
source_url: 'https://developer.apple.com/documentation/security/secitemattr/serveritemattr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secitemattr/serveritemattr.json'
content_hash: 'sha256:acc56ba85cc873c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecItemAttr](../secitemattr.md)

# SecItemAttr.serverItemAttr

<sub>Case</sub>

Identifies the server attribute.

<sub>Mac Catalyst, macOS</sub>

```swift
case serverItemAttr
```

## Discussion

You use this tag to set or get a string that represents the Internet server’s domain name or IP address. This is unique to Internet password attributes. Keychain strings should use UTF-8 encoding.
