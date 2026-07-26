---
title: SecItemAttr.scriptCodeItemAttr
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secitemattr/scriptcodeitemattr
source_url: 'https://developer.apple.com/documentation/security/secitemattr/scriptcodeitemattr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secitemattr/scriptcodeitemattr.json'
content_hash: 'sha256:b0024f9ae16bdcff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecItemAttr](../secitemattr.md)

# SecItemAttr.scriptCodeItemAttr

<sub>Case</sub>

Identifies the script code attribute.

<sub>Mac Catalyst, macOS</sub>

```swift
case scriptCodeItemAttr
```

## Discussion

You use this tag to set or get a value of type `ScriptCode` that represents the script code for all strings. Use of this attribute is deprecated; string attributes should always be stored in UTF-8 encoding.
