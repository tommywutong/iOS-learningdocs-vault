---
title: kSecTransformErrorDomain
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksectransformerrordomain
source_url: 'https://developer.apple.com/documentation/security/ksectransformerrordomain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksectransformerrordomain.json'
content_hash: 'sha256:0c8903501bf12626'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecTransformErrorDomain

<sub>Global Variable</sub>

The domain of any error object created by a transform on failure.

<sub>Mac Catalyst, macOS</sub>

```swift
let kSecTransformErrorDomain: CFString
```

## Discussion

Use this [CFError](../corefoundation/cferror.md) object to determine what went wrong.
