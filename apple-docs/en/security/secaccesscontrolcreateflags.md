---
title: SecAccessControlCreateFlags
framework: Security
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secaccesscontrolcreateflags
source_url: 'https://developer.apple.com/documentation/security/secaccesscontrolcreateflags'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secaccesscontrolcreateflags.json'
content_hash: 'sha256:be4dffbd3e695f76'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecAccessControlCreateFlags

<sub>Structure</sub>

Access control constants that dictate how a keychain item may be used.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SecAccessControlCreateFlags
```

## Overview

Use these flags with the [SecAccessControlCreateWithFlags](<secaccesscontrolcreatewithflags(________).md>) function, or as the value associated with the [kSecAttrAccessControl](ksecattraccesscontrol.md) key in a keychain item’s attribute dictionary, to control keychain item accessibility.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Constraints

- [kSecAccessControlDevicePasscode](secaccesscontrolcreateflags/devicepasscode.md) — Constraint to access an item with a passcode.
- [kSecAccessControlBiometryAny](secaccesscontrolcreateflags/biometryany.md) — Constraint to access an item with Touch ID for any enrolled fingers, or Face ID.
- [kSecAccessControlBiometryCurrentSet](secaccesscontrolcreateflags/biometrycurrentset.md) — Constraint to access an item with Touch ID for currently enrolled fingers, or from Face ID with the currently enrolled user.
- [kSecAccessControlUserPresence](secaccesscontrolcreateflags/userpresence.md) — Constraint to access an item with either biometry or passcode.
- [kSecAccessControlWatch](secaccesscontrolcreateflags/watch.md) — Constraint to access an item with a watch. _(deprecated)_

### Conjunctions

- [kSecAccessControlAnd](secaccesscontrolcreateflags/and.md) — Indicates that all constraints must be satisfied.
- [kSecAccessControlOr](secaccesscontrolcreateflags/or.md) — Indicates that at least one constraint must be satisfied.

### Additional Options

- [kSecAccessControlApplicationPassword](secaccesscontrolcreateflags/applicationpassword.md) — Option to use an application-provided password for data encryption key generation.
- [kSecAccessControlPrivateKeyUsage](secaccesscontrolcreateflags/privatekeyusage.md) — Enable a private key to be used in signing a block of data or verifying a signed block.

### Initializers

- [init(rawValue:)](<secaccesscontrolcreateflags/init(rawvalue_).md>) — Initialize an access control creation flags object.

### Legacy Constraints

- [kSecAccessControlTouchIDAny](secaccesscontrolcreateflags/touchidany.md) — Constraint to access an item with Touch ID for any enrolled fingers. _(deprecated)_
- [kSecAccessControlTouchIDCurrentSet](secaccesscontrolcreateflags/touchidcurrentset.md) — Constraint to access an item with Touch ID for currently enrolled fingers. _(deprecated)_

### Type Properties

- [kSecAccessControlCompanion](secaccesscontrolcreateflags/companion.md)
