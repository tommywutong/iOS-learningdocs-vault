---
title: 'init(rawValue:)'
framework: Security
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/security/secaccesscontrolcreateflags/init(rawvalue:)'
source_url: 'https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/init(rawvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secaccesscontrolcreateflags/init%28rawvalue%3A%29.json'
content_hash: 'sha256:97d8a32872d10741'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecAccessControlCreateFlags](../secaccesscontrolcreateflags.md)

# init(rawValue:)

<sub>Initializer</sub>

Initialize an access control creation flags object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(rawValue: CFOptionFlags)
```

## Parameters

- `rawValue` — The logical `OR` of one or more of the defined access flags values.
