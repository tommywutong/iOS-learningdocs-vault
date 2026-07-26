---
title: unlockEventMask
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seckeychaineventmask/unlockeventmask
source_url: 'https://developer.apple.com/documentation/security/seckeychaineventmask/unlockeventmask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychaineventmask/unlockeventmask.json'
content_hash: 'sha256:5900aba94358b2e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecKeychainEventMask](../seckeychaineventmask.md)

# unlockEventMask

<sub>Type Property</sub>

If the bit specified by this mask is set, your callback function is invoked when a keychain is unlocked.

<sub>Mac Catalyst, macOS</sub>

```swift
static var unlockEventMask: SecKeychainEventMask { get }
```
