---
title: applicationPassword
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.12.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secaccesscontrolcreateflags/applicationpassword
source_url: 'https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/applicationpassword'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secaccesscontrolcreateflags/applicationpassword.json'
content_hash: 'sha256:b5dd46c6520708d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecAccessControlCreateFlags](../secaccesscontrolcreateflags.md)

# applicationPassword

<sub>Type Property</sub>

Option to use an application-provided password for data encryption key generation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var applicationPassword: SecAccessControlCreateFlags { get }
```

## Discussion

This may be specified in addition to any constraints.
