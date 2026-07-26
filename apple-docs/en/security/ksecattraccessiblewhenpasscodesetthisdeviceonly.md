---
title: kSecAttrAccessibleWhenPasscodeSetThisDeviceOnly
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattraccessiblewhenpasscodesetthisdeviceonly
source_url: 'https://developer.apple.com/documentation/security/ksecattraccessiblewhenpasscodesetthisdeviceonly'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattraccessiblewhenpasscodesetthisdeviceonly.json'
content_hash: 'sha256:a9ec569288877c48'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrAccessibleWhenPasscodeSetThisDeviceOnly

<sub>Global Variable</sub>

The data in the keychain can only be accessed when the device is unlocked. Only available if a passcode is set on the device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecAttrAccessibleWhenPasscodeSetThisDeviceOnly: CFString
```

## Discussion

This is recommended for items that only need to be accessible while the application is in the foreground. Items with this attribute never migrate to a new device. After a backup is restored to a new device, these items are missing. No items can be stored in this class on devices without a passcode. Disabling the device passcode causes all items in this class to be deleted.
