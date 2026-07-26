---
title: SecItemAttr.descriptionItemAttr
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secitemattr/descriptionitemattr
source_url: 'https://developer.apple.com/documentation/security/secitemattr/descriptionitemattr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secitemattr/descriptionitemattr.json'
content_hash: 'sha256:32acc8e79a1f4ada'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecItemAttr](../secitemattr.md)

# SecItemAttr.descriptionItemAttr

<sub>Case</sub>

Identifies the description attribute.

<sub>Mac Catalyst, macOS</sub>

```swift
case descriptionItemAttr
```

## Discussion

You use this tag to set or get a string value that represents a user-visible string describing this particular kind of item, for example “disk image password”. Keychain strings should use UTF-8 encoding.
