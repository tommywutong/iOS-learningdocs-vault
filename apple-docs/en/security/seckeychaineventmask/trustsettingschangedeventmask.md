---
title: trustSettingsChangedEventMask
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seckeychaineventmask/trustsettingschangedeventmask
source_url: 'https://developer.apple.com/documentation/security/seckeychaineventmask/trustsettingschangedeventmask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychaineventmask/trustsettingschangedeventmask.json'
content_hash: 'sha256:c5ab4c743015277e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecKeychainEventMask](../seckeychaineventmask.md)

# trustSettingsChangedEventMask

<sub>Type Property</sub>

If the bit specified by this mask is set, your callback function is invoked when there is a change in certificate trust settings.

<sub>Mac Catalyst, macOS</sub>

```swift
static var trustSettingsChangedEventMask: SecKeychainEventMask { get }
```
