---
title: userPresence
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secaccesscontrolcreateflags/userpresence
source_url: 'https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/userpresence'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secaccesscontrolcreateflags/userpresence.json'
content_hash: 'sha256:f654a52ccf0a3e64'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecAccessControlCreateFlags](../secaccesscontrolcreateflags.md)

# userPresence

<sub>Type Property</sub>

Constraint to access an item with either biometry or passcode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var userPresence: SecAccessControlCreateFlags { get }
```

## Discussion

Biometry doesn’t have to be available or enrolled. The item is still accessible by Touch ID even if fingers are added or removed, or by Face ID if the user is re-enrolled.

This option is equivalent to specifying [kSecAccessControlBiometryAny](biometryany.md), [kSecAccessControlOr](or.md), and [kSecAccessControlDevicePasscode](devicepasscode.md).
