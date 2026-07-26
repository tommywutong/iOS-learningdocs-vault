---
title: SecKeyImportExportParameters
framework: Security
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/seckeyimportexportparameters
source_url: 'https://developer.apple.com/documentation/security/seckeyimportexportparameters'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeyimportexportparameters.json'
content_hash: 'sha256:88c050cf87e2b5e6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeyImportExportParameters

<sub>Structure</sub>

The legacy import/export parameter structure.

> [!warning] Deprecated
> This structure is passed in the `keyParams` parameter as input to the deprecated [SecKeychainItemExport](seckeychainitemexport.md) and [SecKeychainItemImport](seckeychainitemimport.md) functions. Use [SecItemExport](<secitemexport(__________).md>) and [SecItemImport](<secitemimport(________________).md>) instead. The newer functions rely on the similar but distinct [SecItemImportExportKeyParameters](secitemimportexportkeyparameters.md) structure as input rather than the structure defined here.

<sub>macOS</sub>

```swift
struct SecKeyImportExportParameters
```

## Overview

PKCS12 is an abbreviation for Public-Key Cryptography Standard # 12. This standard, by RSA Security, provides a format for external representation of keys and certificates and is described in _PKCS 12 v1.0: Personal Information Exchange Syntax_.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## Topics

### Instance Properties

- [accessRef](seckeyimportexportparameters/accessref.md) — Specifies the initial access controls of imported private keys.
- [alertPrompt](seckeyimportexportparameters/alertprompt.md) — The prompt to display in the secure passphrase alert panel.
- [alertTitle](seckeyimportexportparameters/alerttitle.md) — The title to display in the secure passphrase alert panel.
- [flags](seckeyimportexportparameters/flags.md) — The bitwise `OR` of zero or more key import/export flags.
- [keyAttributes](seckeyimportexportparameters/keyattributes.md) — A word of bits constituting the low-level attribute flags for imported keys.
- [keyUsage](seckeyimportexportparameters/keyusage.md) — A word of bits constituting the low-level use flags for imported keys.
- [passphrase](seckeyimportexportparameters/passphrase.md) — The password to use during key import or export.
- [version](seckeyimportexportparameters/version.md) — The version of this structure.

### Initializers

- [init(version:flags:passphrase:alertTitle:alertPrompt:accessRef:keyUsage:keyAttributes:)](<seckeyimportexportparameters/init(version_flags_passphrase_alerttitle_alertprompt_accessref_keyusage_keyattributes_).md>) — Creates a new import/export parameter structure.
