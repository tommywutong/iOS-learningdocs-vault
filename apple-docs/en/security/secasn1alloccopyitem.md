---
title: SecAsn1AllocCopyItem
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（12.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/secasn1alloccopyitem
source_url: 'https://developer.apple.com/documentation/security/secasn1alloccopyitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secasn1alloccopyitem.json'
content_hash: 'sha256:755fd98386b563a1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecAsn1AllocCopyItem

<sub>Function</sub>

Allocates memory for an item’s data field in the coder object’s memory pool and copies in a block of data from another item.

<sub>Mac Catalyst, macOS</sub>

```objc
OSStatus SecAsn1AllocCopyItem(SecAsn1CoderRef coder, const SecAsn1Item *src, SecAsn1Item *dest);
```
