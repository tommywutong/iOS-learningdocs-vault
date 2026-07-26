---
title: kSecUseUserIndependentKeychain
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [tvOS 16.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecuseuserindependentkeychain
source_url: 'https://developer.apple.com/documentation/security/ksecuseuserindependentkeychain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecuseuserindependentkeychain.json'
content_hash: 'sha256:51110e41f2d8c02b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecUseUserIndependentKeychain

<sub>Global Variable</sub>

A key with a value that indicates whether to store the data in a keychain available to anyone who uses the device.

<sub>tvOS</sub>

```swift
let kSecUseUserIndependentKeychain: CFString
```

## Discussion

The corresponding value is of type [CFBoolean](../corefoundation/cfboolean.md). A value of [kCFBooleanTrue](../corefoundation/kcfbooleantrue.md) stores the item in a shared keychain that your app can access even when a different user is active. A value of [kCFBooleanFalse](../corefoundation/kcfbooleanfalse.md) or omitting this key-value pair stores the item in the current user’s keychain.

To view a sample code project that uses this key to streamline experiences like family media accounts, see [Mapping Apple TV users to app profiles](../tvservices/mapping-apple-tv-users-to-app-profiles.md).
