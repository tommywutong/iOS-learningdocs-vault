---
title: SecAsn1AllocCopy
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（12.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/secasn1alloccopy
source_url: 'https://developer.apple.com/documentation/security/secasn1alloccopy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secasn1alloccopy.json'
content_hash: 'sha256:09d8f6854c755994'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecAsn1AllocCopy

<sub>Function</sub>

Allocates memory for an item’s data field in the coder object’s memory pool and copies in a block of data.

<sub>Mac Catalyst, macOS</sub>

```objc
OSStatus SecAsn1AllocCopy(SecAsn1CoderRef coder, const void *src, size_t len, SecAsn1Item *dest);
```
