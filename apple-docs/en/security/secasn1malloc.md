---
title: SecAsn1Malloc
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（12.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/secasn1malloc
source_url: 'https://developer.apple.com/documentation/security/secasn1malloc'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secasn1malloc.json'
content_hash: 'sha256:6cf6b172e44822ae'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecAsn1Malloc

<sub>Function</sub>

Allocates memory in the coder object’s memory pool.

<sub>Mac Catalyst, macOS</sub>

```objc
void *SecAsn1Malloc(SecAsn1CoderRef coder, size_t len);
```
