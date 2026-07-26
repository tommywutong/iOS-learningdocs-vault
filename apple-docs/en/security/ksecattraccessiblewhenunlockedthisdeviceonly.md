---
title: kSecAttrAccessibleWhenUnlockedThisDeviceOnly
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattraccessiblewhenunlockedthisdeviceonly
source_url: 'https://developer.apple.com/documentation/security/ksecattraccessiblewhenunlockedthisdeviceonly'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattraccessiblewhenunlockedthisdeviceonly.json'
content_hash: 'sha256:030afa6f8f5a3278'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrAccessibleWhenUnlockedThisDeviceOnly

<sub>Global Variable</sub>

The data in the keychain item can be accessed only while the device is unlocked by the user.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecAttrAccessibleWhenUnlockedThisDeviceOnly: CFString
```

## Discussion

This is recommended for items that need to be accessible only while the application is in the foreground. Items with this attribute _do not_ migrate to a new device. Thus, after restoring from a backup of a different device, these items will not be present.
