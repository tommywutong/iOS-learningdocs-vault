---
title: errAuthorizationDenied
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/errauthorizationdenied
source_url: 'https://developer.apple.com/documentation/security/errauthorizationdenied'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/errauthorizationdenied.json'
content_hash: 'sha256:a53d8fce5c4100e2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# errAuthorizationDenied

<sub>Global Variable</sub>

The Security Server denied authorization for one or more requested rights.

<sub>Mac Catalyst, macOS</sub>

```swift
var errAuthorizationDenied: OSStatus { get }
```

## Discussion

This error is also returned if there was no definition found in the policy database, or a definition could not be created.
