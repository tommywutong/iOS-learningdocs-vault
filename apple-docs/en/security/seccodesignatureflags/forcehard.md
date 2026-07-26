---
title: forceHard
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seccodesignatureflags/forcehard
source_url: 'https://developer.apple.com/documentation/security/seccodesignatureflags/forcehard'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccodesignatureflags/forcehard.json'
content_hash: 'sha256:2029cef8750ea382'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecCodeSignatureFlags](../seccodesignatureflags.md)

# forceHard

<sub>Type Property</sub>

Always set the [kSecCodeStatusHard](../seccodestatus/hard.md) status flag on launch.

<sub>Mac Catalyst, macOS</sub>

```swift
static var forceHard: SecCodeSignatureFlags { get }
```

## Discussion

The `kSecCodeStatusHard` flag indicates that the code prefers to be denied access to a resource if gaining such access would cause its invalidation. Once the hard bit is set, it cannot be cleared. Therefore, setting this option flag guarantees that the code will always have the `kSecCodeStatusHard` flag set.
