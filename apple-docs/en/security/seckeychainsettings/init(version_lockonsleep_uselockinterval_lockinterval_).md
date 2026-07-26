---
title: 'init(version:lockOnSleep:useLockInterval:lockInterval:)'
framework: Security
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/security/seckeychainsettings/init(version:lockonsleep:uselockinterval:lockinterval:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychainsettings/init(version:lockonsleep:uselockinterval:lockinterval:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainsettings/init%28version%3Alockonsleep%3Auselockinterval%3Alockinterval%3A%29.json'
content_hash: 'sha256:d7e7b0ab229e92f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecKeychainSettings](../seckeychainsettings.md)

# init(version:lockOnSleep:useLockInterval:lockInterval:)

<sub>Initializer</sub>

Initializes a keychain settings structures with the given values.

<sub>Mac Catalyst, macOS</sub>

```swift
init(version: UInt32, lockOnSleep: DarwinBoolean, useLockInterval: DarwinBoolean, lockInterval: UInt32)
```

## Parameters

- `version` — The keychain version. Use [SEC_KEYCHAIN_SETTINGS_VERS1](../sec_keychain_settings_vers1.md).

- `lockOnSleep` — A Boolean indicating whether the keychain locks when the system enters sleep mode.

- `useLockInterval` — A Boolean indicating whether the keychain locks after an time period elapses, as given by [lockInterval](lockinterval.md).

- `lockInterval` — The number of seconds after which the keychain should lock if [useLockInterval](uselockinterval.md) is [true](../../swift/true.md).
