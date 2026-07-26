---
title: updateEventMask
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seckeychaineventmask/updateeventmask
source_url: 'https://developer.apple.com/documentation/security/seckeychaineventmask/updateeventmask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychaineventmask/updateeventmask.json'
content_hash: 'sha256:6f00774586803de5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecKeychainEventMask](../seckeychaineventmask.md)

# updateEventMask

<sub>Type Property</sub>

If the bit specified by this mask is set, your callback function is invoked when a keychain item is updated.

<sub>Mac Catalyst, macOS</sub>

```swift
static var updateEventMask: SecKeychainEventMask { get }
```
