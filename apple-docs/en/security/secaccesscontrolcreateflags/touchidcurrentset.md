---
title: touchIDCurrentSet
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 9.0+（11.3 起废弃）, iPadOS 9.0+（11.3 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.12.1+（10.13.4 起废弃）, tvOS 9.0+（11.3 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（4.3 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/secaccesscontrolcreateflags/touchidcurrentset
source_url: 'https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/touchidcurrentset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secaccesscontrolcreateflags/touchidcurrentset.json'
content_hash: 'sha256:bcf8b621993b09c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecAccessControlCreateFlags](../secaccesscontrolcreateflags.md)

# touchIDCurrentSet

<sub>Type Property</sub>

Constraint to access an item with Touch ID for currently enrolled fingers.

> [!warning] Deprecated
> Use [kSecAccessControlBiometryCurrentSet](biometrycurrentset.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var touchIDCurrentSet: SecAccessControlCreateFlags { get }
```

## Discussion

Touch ID must be available and enrolled with at least one finger. The item is invalidated if fingers are added or removed.
