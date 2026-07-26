---
title: SecItemAttr.authenticationTypeItemAttr
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secitemattr/authenticationtypeitemattr
source_url: 'https://developer.apple.com/documentation/security/secitemattr/authenticationtypeitemattr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secitemattr/authenticationtypeitemattr.json'
content_hash: 'sha256:0de39cc5e79c6abe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecItemAttr](../secitemattr.md)

# SecItemAttr.authenticationTypeItemAttr

<sub>Case</sub>

Identifies the authentication type attribute.

<sub>Mac Catalyst, macOS</sub>

```swift
case authenticationTypeItemAttr
```

## Discussion

You use this tag to set or get a value of type `SecAuthenticationType` that represents the Internet authentication scheme. For possible authentication values, see [SecAuthenticationType](../secauthenticationtype.md). This is unique to Internet password attributes.
