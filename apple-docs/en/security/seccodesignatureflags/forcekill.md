---
title: forceKill
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seccodesignatureflags/forcekill
source_url: 'https://developer.apple.com/documentation/security/seccodesignatureflags/forcekill'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccodesignatureflags/forcekill.json'
content_hash: 'sha256:74719c95f64e496e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecCodeSignatureFlags](../seccodesignatureflags.md)

# forceKill

<sub>Type Property</sub>

Always set the termination status flag on launch.

<sub>Mac Catalyst, macOS</sub>

```swift
static var forceKill: SecCodeSignatureFlags { get }
```

## Discussion

The `kSecCodeStatusKill` flag indicates that the code wishes to be terminated if it is ever invalidated. Once this is set, it cannot be cleared. Therefore, setting this option flag guarantees that the running code will always be valid, since it will die immediately if it becomes invalid.
