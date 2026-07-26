---
title: kSecAttrAccessible
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattraccessible
source_url: 'https://developer.apple.com/documentation/security/ksecattraccessible'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattraccessible.json'
content_hash: 'sha256:7b512751f532fc8b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrAccessible

<sub>Global Variable</sub>

A key with a value that indicates when the keychain item is accessible.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecAttrAccessible: CFString
```

## Discussion

The corresponding value, one of those found in [Accessibility Values](item-attribute-keys-and-values.md#Accessibility-Values), indicates when your app needs access to the data in a keychain item. Choose the most restrictive option that meets your app’s needs so that the system can protect that item to the greatest extent possible. For more information, see [Restricting keychain item accessibility](restricting-keychain-item-accessibility.md).

> [!important] Important
> You can use this attribute for macOS keychain items only if you also set a value of `true` for the [kSecUseDataProtectionKeychain](ksecusedataprotectionkeychain.md) key, the [kSecAttrSynchronizable](ksecattrsynchronizable.md) key, or both. For any item marked as synchronizable, the value for the [kSecAttrAccessible](ksecattraccessible.md) key may only be one whose name does not end with `ThisDeviceOnly`, as those cannot sync to another device.

> [!note] Note
> The app _must_ provide the contents of the keychain item ([kSecValueData](ksecvaluedata.md)) when changing this attribute in iOS 4 and earlier.
