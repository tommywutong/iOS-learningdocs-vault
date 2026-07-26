---
title: errSecCSSignatureNotVerifiable
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/errseccssignaturenotverifiable
source_url: 'https://developer.apple.com/documentation/security/errseccssignaturenotverifiable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/errseccssignaturenotverifiable.json'
content_hash: 'sha256:198aa530fa9901a0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# errSecCSSignatureNotVerifiable

<sub>Global Variable</sub>

Signature cannot be read.

<sub>Mac Catalyst, macOS</sub>

```swift
var errSecCSSignatureNotVerifiable: OSStatus { get }
```

## Discussion

This error might be due to a filesystem that maps root to an unprivileged user, for example.
