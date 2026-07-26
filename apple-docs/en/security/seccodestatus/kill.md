---
title: kill
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seccodestatus/kill
source_url: 'https://developer.apple.com/documentation/security/seccodestatus/kill'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccodestatus/kill.json'
content_hash: 'sha256:d20daf16749dc31f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecCodeStatus](../seccodestatus.md)

# kill

<sub>Type Property</sub>

The code wants to be terminated if it ever loses its validity.

<sub>Mac Catalyst, macOS</sub>

```swift
static var kill: SecCodeStatus { get }
```

## Discussion

This bit can not be cleared on running code; it can only be set. Running code that has this flag set is guaranteed to be valid, because if it were invalid it would have been terminated.
