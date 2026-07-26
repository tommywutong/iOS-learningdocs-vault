---
title: useLockInterval
framework: Security
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seckeychainsettings/uselockinterval
source_url: 'https://developer.apple.com/documentation/security/seckeychainsettings/uselockinterval'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainsettings/uselockinterval.json'
content_hash: 'sha256:bd6652a2ea8b5926'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecKeychainSettings](../seckeychainsettings.md)

# useLockInterval

<sub>Instance Property</sub>

A Boolean value indicating whether the keychain automatically locks after a certain period of time.

<sub>Mac Catalyst, macOS</sub>

```swift
var useLockInterval: DarwinBoolean
```

## Discussion

Use [lockInterval](lockinterval.md) to indicate the time in seconds after which the keychain should automatically be locked.
