---
title: kSecCFErrorResourceAdded
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kseccferrorresourceadded
source_url: 'https://developer.apple.com/documentation/security/kseccferrorresourceadded'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseccferrorresourceadded.json'
content_hash: 'sha256:adaf62c0c866445d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecCFErrorResourceAdded

<sub>Global Variable</sub>

A key whose value is a URL pointing to the resource on disk that is not included in the signed resources for the code.

<sub>Mac Catalyst, macOS</sub>

```swift
let kSecCFErrorResourceAdded: CFString
```

## Discussion

This key is present when an unsealed resource is found.
