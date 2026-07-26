---
title: kSecUseDataProtectionKeychain
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecusedataprotectionkeychain
source_url: 'https://developer.apple.com/documentation/security/ksecusedataprotectionkeychain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecusedataprotectionkeychain.json'
content_hash: 'sha256:6828c3fb488079f5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecUseDataProtectionKeychain

<sub>Global Variable</sub>

A key whose value indicates whether to treat macOS keychain items like iOS keychain items.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecUseDataProtectionKeychain: CFString
```

## Discussion

Set the value for this key to `true` in the query dictionary when accessing a macOS keychain item that behaves like an iOS keychain item. For example, use the data protection key when adding, searching for, or deleting an item to which the [kSecAttrAccessible](ksecattraccessible.md) or [kSecAttrAccessGroup](ksecattraccessgroup.md) attributes apply.

The data protection key affects operations only in macOS. Other platforms automatically behave as if the key is set to `true`, and ignore the key in the query dictionary. You can safely use the key on all platforms.

> [!tip] Tip
> It’s highly recommended that you set the value of this key to `true` for all keychain operations. This key helps to improve the portability of your code across platforms. Use it unless you specifically need access to items previously stored in a legacy keychain in macOS.

Items that you store or have stored in macOS with the [kSecAttrSynchronizable](ksecattrsynchronizable.md) attribute set to `true` also behave like iOS keychain items. However, a `true` value for that attribute additionally causes iCloud to synchronize the item across all the user’s devices. Use [kSecUseDataProtectionKeychain](ksecusedataprotectionkeychain.md) to get the iOS behavior without synchronization.
