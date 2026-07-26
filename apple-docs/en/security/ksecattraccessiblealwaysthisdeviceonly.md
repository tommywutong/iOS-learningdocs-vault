---
title: kSecAttrAccessibleAlwaysThisDeviceOnly
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 4.0+（12.0 起废弃）, iPadOS 4.0+（12.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.9+（10.14 起废弃）, tvOS 9.0+（12.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（5.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/ksecattraccessiblealwaysthisdeviceonly
source_url: 'https://developer.apple.com/documentation/security/ksecattraccessiblealwaysthisdeviceonly'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattraccessiblealwaysthisdeviceonly.json'
content_hash: 'sha256:0212764e73a3df5b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrAccessibleAlwaysThisDeviceOnly

<sub>Global Variable</sub>

The data in the keychain item can always be accessed regardless of whether the device is locked.

> [!warning] Deprecated
> Use an accessibility level that provides some user protection, such as kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecAttrAccessibleAlwaysThisDeviceOnly: CFString
```

## Discussion

This is not recommended for application use. Items with this attribute _do not_ migrate to a new device. Thus, after restoring from a backup of a different device, these items will not be present.
