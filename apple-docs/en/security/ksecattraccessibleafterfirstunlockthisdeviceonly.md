---
title: kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattraccessibleafterfirstunlockthisdeviceonly
source_url: 'https://developer.apple.com/documentation/security/ksecattraccessibleafterfirstunlockthisdeviceonly'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattraccessibleafterfirstunlockthisdeviceonly.json'
content_hash: 'sha256:8a1739aba4b4ec73'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly

<sub>Global Variable</sub>

The data in the keychain item cannot be accessed after a restart until the device has been unlocked once by the user.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly: CFString
```

## Discussion

After the first unlock, the data remains accessible until the next restart. This is recommended for items that need to be accessed by background applications. Items with this attribute _do not_ migrate to a new device. Thus, after restoring from a backup of a different device, these items will not be present.
