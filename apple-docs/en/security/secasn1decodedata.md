---
title: SecAsn1DecodeData
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（12.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/secasn1decodedata
source_url: 'https://developer.apple.com/documentation/security/secasn1decodedata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secasn1decodedata.json'
content_hash: 'sha256:82d54b6142346b3e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecAsn1DecodeData

<sub>Function</sub>

Decodes an ASN.1 item in DER format.

<sub>Mac Catalyst, macOS</sub>

```objc
OSStatus SecAsn1DecodeData(SecAsn1CoderRef coder, const SecAsn1Item *src, const SecAsn1Template *templ, void *dest);
```
