---
title: SecCodeSignatureFlags
framework: Security
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seccodesignatureflags
source_url: 'https://developer.apple.com/documentation/security/seccodesignatureflags'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccodesignatureflags.json'
content_hash: 'sha256:7a614ec6a207d032'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecCodeSignatureFlags

<sub>Structure</sub>

Specify option flags that can be embedded in a code signature during signing and that govern the use of the signature.

<sub>Mac Catalyst, macOS</sub>

```swift
struct SecCodeSignatureFlags
```

## Overview

Some of these flags can be set through the `codesign(1)` command’s `--options` argument and some are set implicitly based on signing circumstances. The flags here appear as the value associated with the [kSecCodeInfoFlags](kseccodeinfoflags.md) key in the signing information dictionary. See [Signing Information Dictionary Keys](signing-information-dictionary-keys.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<seccodesignatureflags/init(rawvalue_).md>)

### Constants

- [kSecCodeSignatureHost](seccodesignatureflags/host.md) — May host guest code.
- [kSecCodeSignatureAdhoc](seccodesignatureflags/adhoc.md) — Must be used without a signing identity.
- [kSecCodeSignatureForceHard](seccodesignatureflags/forcehard.md) — Always set the [kSecCodeStatusHard](seccodestatus/hard.md) status flag on launch.
- [kSecCodeSignatureForceKill](seccodesignatureflags/forcekill.md) — Always set the termination status flag on launch.
- [kSecCodeSignatureForceExpiration](seccodesignatureflags/forceexpiration.md) — Always set the [kSecCSConsiderExpiration](seccsflags/considerexpiration.md) flag when validating the code.
- [kSecCodeSignatureEnforcement](seccodesignatureflags/enforcement.md) — Enforce code signing.
- [kSecCodeSignatureLibraryValidation](seccodesignatureflags/libraryvalidation.md) — Require library validation.
- [kSecCodeSignatureRestrict](seccodesignatureflags/restrict.md) — Restrict dyld loading.
- [kSecCodeSignatureRuntime](seccodesignatureflags/runtime.md) — Apply runtime hardening policies as required by the hardened runtime version.

### Type Properties

- [kSecCodeSignatureLinkerSigned](seccodesignatureflags/linkersigned.md)
