---
title: item
framework: Security
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seckeychaincallbackinfo/item
source_url: 'https://developer.apple.com/documentation/security/seckeychaincallbackinfo/item'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychaincallbackinfo/item.json'
content_hash: 'sha256:303c566722f0cdb5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecKeychainCallbackInfo](../seckeychaincallbackinfo.md)

# item

<sub>Instance Property</sub>

A reference to the keychain item in which the event occurred. If the event did not involve an item, this field is not valid.

<sub>macOS</sub>

```swift
var item: Unmanaged<SecKeychainItem>
```
