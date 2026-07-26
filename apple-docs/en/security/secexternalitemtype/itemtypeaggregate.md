---
title: SecExternalItemType.itemTypeAggregate
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secexternalitemtype/itemtypeaggregate
source_url: 'https://developer.apple.com/documentation/security/secexternalitemtype/itemtypeaggregate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secexternalitemtype/itemtypeaggregate.json'
content_hash: 'sha256:3cb52bd1c0fc2fd3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecExternalItemType](../secexternalitemtype.md)

# SecExternalItemType.itemTypeAggregate

<sub>Case</sub>

Indicates a set of certificates or certificates and private keys.

<sub>macOS</sub>

```swift
case itemTypeAggregate
```

## Discussion

Possible values include [kSecFormatPKCS7](../secexternalformat/formatpkcs7.md), [kSecFormatPKCS12](../secexternalformat/formatpkcs12.md), or [kSecFormatPEMSequence](../secexternalformat/formatpemsequence.md) formats (see [SecExternalFormat](../secexternalformat.md)).
