---
title: lockInterval
framework: Security
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seckeychainsettings/lockinterval
source_url: 'https://developer.apple.com/documentation/security/seckeychainsettings/lockinterval'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainsettings/lockinterval.json'
content_hash: 'sha256:5d1c368562fc46ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecKeychainSettings](../seckeychainsettings.md)

# lockInterval

<sub>Instance Property</sub>

The number of seconds to wait before the keychain locks.

<sub>Mac Catalyst, macOS</sub>

```swift
var lockInterval: UInt32
```

## Discussion

If you set [useLockInterval](uselockinterval.md) to [false](../../swift/false.md), set [lockInterval](lockinterval.md) to `INT_MAX` to indicate that the keychain never locks.
