---
title: defaultChangedEventMask
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seckeychaineventmask/defaultchangedeventmask
source_url: 'https://developer.apple.com/documentation/security/seckeychaineventmask/defaultchangedeventmask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychaineventmask/defaultchangedeventmask.json'
content_hash: 'sha256:138e0059409454f5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecKeychainEventMask](../seckeychaineventmask.md)

# defaultChangedEventMask

<sub>Type Property</sub>

If the bit specified by this mask is set, your callback function is invoked when a different keychain is specified as the default.

<sub>Mac Catalyst, macOS</sub>

```swift
static var defaultChangedEventMask: SecKeychainEventMask { get }
```
