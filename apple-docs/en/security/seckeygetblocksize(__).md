---
title: 'SecKeyGetBlockSize(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 4.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/seckeygetblocksize(_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeygetblocksize(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeygetblocksize%28_%3A%29.json'
content_hash: 'sha256:221a166f47239c0e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeyGetBlockSize(_:)

<sub>Function</sub>

Gets the block length associated with a cryptographic key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecKeyGetBlockSize(_ key: SecKey) -> Int
```

## Parameters

- `key` — The key for which you want the block length.

## Return Value

The block length associated with the key in bytes. If the key is an RSA key, for example, this is the size of the modulus.
