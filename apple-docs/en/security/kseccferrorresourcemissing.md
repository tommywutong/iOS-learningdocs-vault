---
title: kSecCFErrorResourceMissing
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kseccferrorresourcemissing
source_url: 'https://developer.apple.com/documentation/security/kseccferrorresourcemissing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseccferrorresourcemissing.json'
content_hash: 'sha256:ee4961c44a1b00c6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecCFErrorResourceMissing

<sub>Global Variable</sub>

A key whose value is a URL indicating the location of the missing resource as it is specified in the `CodeResources` file.

<sub>Mac Catalyst, macOS</sub>

```swift
let kSecCFErrorResourceMissing: CFString
```

## Discussion

This key is present when a non-optional sealed resource is missing.
