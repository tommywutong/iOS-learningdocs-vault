---
title: SecItemAttr.protocolItemAttr
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secitemattr/protocolitemattr
source_url: 'https://developer.apple.com/documentation/security/secitemattr/protocolitemattr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secitemattr/protocolitemattr.json'
content_hash: 'sha256:a6d2ca6d52aed820'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecItemAttr](../secitemattr.md)

# SecItemAttr.protocolItemAttr

<sub>Case</sub>

Identifies the protocol attribute.

<sub>Mac Catalyst, macOS</sub>

```swift
case protocolItemAttr
```

## Discussion

You use this tag to set or get a value of type `SecProtocolType` that represents the Internet protocol. For possible protocol type values, see [SecProtocolType](../secprotocoltype.md). This is unique to AppleShare and Internet password attributes.
