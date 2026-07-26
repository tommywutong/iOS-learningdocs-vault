---
title: biometryAny
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 11.3+, iPadOS 11.3+, Mac Catalyst 13.1+, macOS 10.13.4+, tvOS 11.3+, visionOS 1.0+, watchOS 4.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secaccesscontrolcreateflags/biometryany
source_url: 'https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/biometryany'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secaccesscontrolcreateflags/biometryany.json'
content_hash: 'sha256:5e20878b4e51be30'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecAccessControlCreateFlags](../secaccesscontrolcreateflags.md)

# biometryAny

<sub>Type Property</sub>

Constraint to access an item with Touch ID for any enrolled fingers, or Face ID.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var biometryAny: SecAccessControlCreateFlags { get }
```

## Discussion

Touch ID must be available and enrolled with at least one finger, or Face ID must be available and enrolled. The item is still accessible by Touch ID if fingers are added or removed, or by Face ID if the user is re-enrolled.
