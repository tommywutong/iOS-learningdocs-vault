---
title: lockEventMask
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seckeychaineventmask/lockeventmask
source_url: 'https://developer.apple.com/documentation/security/seckeychaineventmask/lockeventmask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychaineventmask/lockeventmask.json'
content_hash: 'sha256:d794fc28ac4b9b84'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecKeychainEventMask](../seckeychaineventmask.md)

# lockEventMask

<sub>Type Property</sub>

If the bit specified by this mask is set, your callback function is invoked when a keychain is locked.

<sub>Mac Catalyst, macOS</sub>

```swift
static var lockEventMask: SecKeychainEventMask { get }
```
