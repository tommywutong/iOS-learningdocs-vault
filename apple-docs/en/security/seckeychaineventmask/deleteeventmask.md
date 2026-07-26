---
title: deleteEventMask
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seckeychaineventmask/deleteeventmask
source_url: 'https://developer.apple.com/documentation/security/seckeychaineventmask/deleteeventmask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychaineventmask/deleteeventmask.json'
content_hash: 'sha256:c7c1deb6dfc4039d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecKeychainEventMask](../seckeychaineventmask.md)

# deleteEventMask

<sub>Type Property</sub>

If the bit specified by this mask is set, your callback function is invoked when an item is deleted from a keychain.

<sub>Mac Catalyst, macOS</sub>

```swift
static var deleteEventMask: SecKeychainEventMask { get }
```
