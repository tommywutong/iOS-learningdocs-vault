---
title: debugged
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seccodestatus/debugged
source_url: 'https://developer.apple.com/documentation/security/seccodestatus/debugged'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccodestatus/debugged.json'
content_hash: 'sha256:a243715d4a40268a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecCodeStatus](../seccodestatus.md)

# debugged

<sub>Type Property</sub>

The code has been debugged by another process that was allowed to do so.

<sub>Mac Catalyst, macOS</sub>

```swift
static var debugged: SecCodeStatus { get }
```

## Discussion

The debugger sets this flag when it attaches.
