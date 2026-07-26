---
title: biometryCurrentSet
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 11.3+, iPadOS 11.3+, Mac Catalyst 13.1+, macOS 10.13.4+, tvOS 11.3+, visionOS 1.0+, watchOS 4.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secaccesscontrolcreateflags/biometrycurrentset
source_url: 'https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/biometrycurrentset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secaccesscontrolcreateflags/biometrycurrentset.json'
content_hash: 'sha256:2f6d5d168028f18c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecAccessControlCreateFlags](../secaccesscontrolcreateflags.md)

# biometryCurrentSet

<sub>Type Property</sub>

Constraint to access an item with Touch ID for currently enrolled fingers, or from Face ID with the currently enrolled user.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var biometryCurrentSet: SecAccessControlCreateFlags { get }
```

## Discussion

Touch ID must be available and enrolled with at least one finger, or Face ID available and enrolled. The item is invalidated if fingers are added or removed for Touch ID, or if the user re-enrolls for Face ID.
