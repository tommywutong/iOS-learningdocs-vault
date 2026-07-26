---
title: SecAsn1EncodeItem
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（12.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/secasn1encodeitem
source_url: 'https://developer.apple.com/documentation/security/secasn1encodeitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secasn1encodeitem.json'
content_hash: 'sha256:852ac50221cb4c9b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecAsn1EncodeItem

<sub>Function</sub>

Encodes data in DER format.

<sub>Mac Catalyst, macOS</sub>

```objc
OSStatus SecAsn1EncodeItem(SecAsn1CoderRef coder, const void *src, const SecAsn1Template *templates, SecAsn1Item *dest);
```
