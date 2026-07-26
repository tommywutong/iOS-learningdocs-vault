---
title: keychainListChangedMask
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seckeychaineventmask/keychainlistchangedmask
source_url: 'https://developer.apple.com/documentation/security/seckeychaineventmask/keychainlistchangedmask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychaineventmask/keychainlistchangedmask.json'
content_hash: 'sha256:5404db6f5d84bd74'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecKeychainEventMask](../seckeychaineventmask.md)

# keychainListChangedMask

<sub>Type Property</sub>

If the bit specified by this mask is set, your callback function is invoked when a keychain list is changed.

<sub>Mac Catalyst, macOS</sub>

```swift
static var keychainListChangedMask: SecKeychainEventMask { get }
```
