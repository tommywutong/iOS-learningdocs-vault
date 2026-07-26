---
title: SecKeyGeneratePairBlock
framework: Security
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seckeygeneratepairblock
source_url: 'https://developer.apple.com/documentation/security/seckeygeneratepairblock'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeygeneratepairblock.json'
content_hash: 'sha256:01c28b6ac98b9fba'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeyGeneratePairBlock

<sub>Type Alias</sub>

A block called with the results of a call to [SecKeyGeneratePairAsync](<seckeygeneratepairasync(______).md>).

<sub>macOS</sub>

```swift
typealias SecKeyGeneratePairBlock = (SecKey, SecKey, CFError) -> Void
```
