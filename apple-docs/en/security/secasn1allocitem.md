---
title: SecAsn1AllocItem
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（12.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/secasn1allocitem
source_url: 'https://developer.apple.com/documentation/security/secasn1allocitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secasn1allocitem.json'
content_hash: 'sha256:627f0e53736dd654'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecAsn1AllocItem

<sub>Function</sub>

Allocates memory for an item’s data field in the coder object’s memory pool.

<sub>Mac Catalyst, macOS</sub>

```objc
OSStatus SecAsn1AllocItem(SecAsn1CoderRef coder, SecAsn1Item *item, size_t len);
```
