---
title: SecCredentialType
framework: Security
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [macOS 10.3+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/seccredentialtype
source_url: 'https://developer.apple.com/documentation/security/seccredentialtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccredentialtype.json'
content_hash: 'sha256:793b14f6fd62e9c8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecCredentialType

<sub>Enumeration</sub>

The credential type to be returned by [SecKeyGetCredentials](seckeygetcredentials.md).

> [!warning] Deprecated
> No longer supported

<sub>macOS</sub>

```swift
enum SecCredentialType
```

## Overview

See the section “Servers and the Keychain” in the [macOS Keychain Services Tasks](https://developer.apple.com/library/archive/documentation/Security/Conceptual/keychainServConcepts/03tasks/tasks.html#//apple_ref/doc/uid/TP30000897-CH205) chapter of [Keychain Services Programming Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/keychainServConcepts/01introduction/introduction.html#//apple_ref/doc/uid/TP30000897) for information on the use of UI with keychain tasks.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kSecCredentialTypeDefault](seccredentialtype/default.md) — The default setting for determining whether to present UI is used. _(deprecated)_
- [kSecCredentialTypeWithUI](seccredentialtype/withui.md) — Keychain operations on keys that have this credential are allowed to present UI if required. _(deprecated)_
- [kSecCredentialTypeNoUI](seccredentialtype/noui.md) — Keychain operations on keys that have this credential are not allowed to present UI, and will fail if UI is required. _(deprecated)_

### Initializers

- [init(rawValue:)](<seccredentialtype/init(rawvalue_).md>) _(deprecated)_
