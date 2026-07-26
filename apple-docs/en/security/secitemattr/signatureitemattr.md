---
title: SecItemAttr.signatureItemAttr
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secitemattr/signatureitemattr
source_url: 'https://developer.apple.com/documentation/security/secitemattr/signatureitemattr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secitemattr/signatureitemattr.json'
content_hash: 'sha256:b7ad8d588317d4e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecItemAttr](../secitemattr.md)

# SecItemAttr.signatureItemAttr

<sub>Case</sub>

Identifies the server signature attribute.

<sub>Mac Catalyst, macOS</sub>

```swift
case signatureItemAttr
```

## Discussion

You use this tag to set or get a value of type [SecAFPServerSignature](../secafpserversignature.md) that represents the server signature block. This is unique to AppleShare password attributes.
