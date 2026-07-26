---
title: kSecAttrSynchronizable
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattrsynchronizable
source_url: 'https://developer.apple.com/documentation/security/ksecattrsynchronizable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattrsynchronizable.json'
content_hash: 'sha256:02df18559cbc65ee'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrSynchronizable

<sub>Global Variable</sub>

A key with a value that’s a string indicating whether the item synchronizes through iCloud.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecAttrSynchronizable: CFString
```

## Discussion

The corresponding value is of type [CFBoolean](../corefoundation/cfboolean.md) and indicates whether the item in question is synchronized to other devices through iCloud. To add a new synchronizable item, or to obtain synchronizable results from a query, supply this key with a value of [kCFBooleanTrue](../corefoundation/kcfbooleantrue.md). If the key is not supplied, or has a value of [kCFBooleanFalse](../corefoundation/kcfbooleanfalse.md), then no synchronizable items are added or returned. Use [kSecAttrSynchronizableAny](ksecattrsynchronizableany.md) to query for both synchronizable and non-synchronizable results.

A keychain item created in macOS with this attribute behaves like an iOS keychain item. For example, you share the item between apps using Access Groups instead of Access Control Lists. To create a keychain item in macOS that behaves like an iOS keychain item without making it synchronizable, use [kSecUseDataProtectionKeychain](ksecusedataprotectionkeychain.md) instead.

The following caveats apply when you specify the [kSecAttrSynchronizable](ksecattrsynchronizable.md) key:

- You can set the [kSecAttrSynchronizable](ksecattrsynchronizable.md) key on tvOS, but tvOS doesn’t synchronize your app’s keychain items through iCloud. Items that you store on tvOS never leave the device where you create them, and items that you store on other devices don’t synchronize to tvOS devices.
- Updating or deleting items using the [kSecAttrSynchronizable](ksecattrsynchronizable.md) key affects all copies of the item, not just the one on your local device. Be sure that it makes sense to use the same password on all devices before making a password synchronizable.
- Starting in iOS 14, macOS 11, and watchOS 7, the keychain synchronizes passwords, certificates, and cryptographic keys. Earlier OS versions synchronize only passwords.
- Items stored or obtained using the [kSecAttrSynchronizable](ksecattrsynchronizable.md) key cannot specify [SecAccess](secaccess.md)-based access control with [kSecAttrAccess](ksecattraccess.md). If a password is intended to be shared between multiple applications, the [kSecAttrAccessGroup](ksecattraccessgroup.md) key must be specified, and each application using this password must have the [Keychain Access Groups Entitlement](../bundleresources/entitlements/keychain-access-groups.md) enabled, and a common access group specified.
- Items stored or obtained using the [kSecAttrSynchronizable](ksecattrsynchronizable.md) key may not also specify a [kSecAttrAccessible](ksecattraccessible.md) value that is incompatible with syncing (namely, those whose names end with `ThisDeviceOnly`).
- Items stored or obtained using the [kSecAttrSynchronizable](ksecattrsynchronizable.md) key cannot be specified by reference. Use only [kSecReturnAttributes](ksecreturnattributes.md) and/or [kSecReturnData](ksecreturndata.md) to retrieve results.
- Do not use persistent references to synchronizable items. They cannot be moved between devices, and may not resolve if the item is modified on some other device.
- When specifying a query that uses the [kSecAttrSynchronizable](ksecattrsynchronizable.md) key, search keys are limited to the item’s class and attributes. The only search constant that may be used is [kSecMatchLimit](ksecmatchlimit.md); other constants using the `kSecMatch` prefix are not supported.
