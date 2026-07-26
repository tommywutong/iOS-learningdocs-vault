---
title: kSecCSCheckAllArchitectures
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kseccscheckallarchitectures
source_url: 'https://developer.apple.com/documentation/security/kseccscheckallarchitectures'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseccscheckallarchitectures.json'
content_hash: 'sha256:a95fdef5094d5175'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecCSCheckAllArchitectures

<sub>Global Variable</sub>

For multi-architecture (universal) Mach-O programs, validate all architectures included.

<sub>Mac Catalyst, macOS</sub>

```swift
var kSecCSCheckAllArchitectures: UInt32 { get }
```

## Discussion

By default, only the native architecture is validated.
