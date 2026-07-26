---
title: SecKeyImportExportFlags
framework: Security
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seckeyimportexportflags
source_url: 'https://developer.apple.com/documentation/security/seckeyimportexportflags'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeyimportexportflags.json'
content_hash: 'sha256:39b22e86e150b162'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeyImportExportFlags

<sub>Structure</sub>

The import/export parameter structure flags.

<sub>macOS</sub>

```swift
struct SecKeyImportExportFlags
```

## Overview

Use an instance of this structure to set the [flags](secitemimportexportkeyparameters/flags.md) property in the [SecItemImportExportKeyParameters](secitemimportexportkeyparameters.md) import/export structure.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<seckeyimportexportflags/init(rawvalue_).md>) — Initialize a key import/export flag structure.

### Constants

- [kSecKeyImportOnlyOne](seckeyimportexportflags/importonlyone.md) — A flag that you set to prevent importing more than one private key.
- [kSecKeySecurePassphrase](seckeyimportexportflags/securepassphrase.md) — A flag that indicates the user should be prompted for a passphrase on import or export.
- [kSecKeyNoAccessControl](seckeyimportexportflags/noaccesscontrol.md) — A flag that indicates imported private keys have no access object attached to them.
