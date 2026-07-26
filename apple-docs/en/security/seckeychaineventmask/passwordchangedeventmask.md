---
title: passwordChangedEventMask
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seckeychaineventmask/passwordchangedeventmask
source_url: 'https://developer.apple.com/documentation/security/seckeychaineventmask/passwordchangedeventmask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychaineventmask/passwordchangedeventmask.json'
content_hash: 'sha256:9ac94ccd76ff7187'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecKeychainEventMask](../seckeychaineventmask.md)

# passwordChangedEventMask

<sub>Type Property</sub>

If the bit specified by this mask is set, your callback function is invoked when the keychain password is changed.

<sub>Mac Catalyst, macOS</sub>

```swift
static var passwordChangedEventMask: SecKeychainEventMask { get }
```
