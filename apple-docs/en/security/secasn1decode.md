---
title: SecAsn1Decode
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（12.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/secasn1decode
source_url: 'https://developer.apple.com/documentation/security/secasn1decode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secasn1decode.json'
content_hash: 'sha256:68d16058d9a73e9c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecAsn1Decode

<sub>Function</sub>

Decodes untyped DER data.

<sub>Mac Catalyst, macOS</sub>

```objc
OSStatus SecAsn1Decode(SecAsn1CoderRef coder, const void *src, size_t len, const SecAsn1Template *templates, void *dest);
```
