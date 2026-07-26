---
title: dataAccessEventMask
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.10+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/seckeychaineventmask/dataaccesseventmask
source_url: 'https://developer.apple.com/documentation/security/seckeychaineventmask/dataaccesseventmask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychaineventmask/dataaccesseventmask.json'
content_hash: 'sha256:8a356c84b82ee499'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecKeychainEventMask](../seckeychaineventmask.md)

# dataAccessEventMask

<sub>Type Property</sub>

If the bit specified by this mask is set, your callback function is invoked when a process accesses a keychain item’s data.

> [!warning] Deprecated
> Read events are no longer posted

<sub>Mac Catalyst, macOS</sub>

```swift
static var dataAccessEventMask: SecKeychainEventMask { get }
```
