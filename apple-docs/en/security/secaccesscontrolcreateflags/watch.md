---
title: watch
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.15+（15.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/secaccesscontrolcreateflags/watch
source_url: 'https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/watch'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secaccesscontrolcreateflags/watch.json'
content_hash: 'sha256:cf1cf46220f67297'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecAccessControlCreateFlags](../secaccesscontrolcreateflags.md)

# watch

<sub>Type Property</sub>

Constraint to access an item with a watch.

<sub>Mac Catalyst, macOS</sub>

```swift
static var watch: SecAccessControlCreateFlags { get }
```

## Discussion

The system attempts to locate a nearby, paired Apple Watch running watchOS 6 or later.
