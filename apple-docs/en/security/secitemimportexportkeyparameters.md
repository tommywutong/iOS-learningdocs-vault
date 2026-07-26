---
title: SecItemImportExportKeyParameters
framework: Security
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secitemimportexportkeyparameters
source_url: 'https://developer.apple.com/documentation/security/secitemimportexportkeyparameters'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secitemimportexportkeyparameters.json'
content_hash: 'sha256:4fe83a96c578aba7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecItemImportExportKeyParameters

<sub>Structure</sub>

The import/export parameter structure.

<sub>macOS</sub>

```swift
struct SecItemImportExportKeyParameters
```

## Overview

Use this structure as the `keyParams` input parameter to the [SecItemExport](<secitemexport(__________).md>) and the [SecItemImport](<secitemimport(________________).md>) functions.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## Topics

### Instance Properties

- [accessRef](secitemimportexportkeyparameters/accessref.md) — Specifies the initial access controls of imported private keys.
- [alertPrompt](secitemimportexportkeyparameters/alertprompt.md) — The prompt to display in the secure passphrase alert panel.
- [alertTitle](secitemimportexportkeyparameters/alerttitle.md) — The title to display in the secure passphrase alert panel.
- [flags](secitemimportexportkeyparameters/flags.md) — The bitwise `OR` of zero or more key import/export flags.
- [keyAttributes](secitemimportexportkeyparameters/keyattributes.md) — An array containing zero or more key attributes for an imported key.
- [keyUsage](secitemimportexportkeyparameters/keyusage.md) — An array containing usage attributes applied to a key on import.
- [passphrase](secitemimportexportkeyparameters/passphrase.md) — The password to use during key import or export.
- [version](secitemimportexportkeyparameters/version.md) — The version of this structure.

### Initializers

- [init()](<secitemimportexportkeyparameters/init().md>)
- [init(version:flags:passphrase:alertTitle:alertPrompt:accessRef:keyUsage:keyAttributes:)](<secitemimportexportkeyparameters/init(version_flags_passphrase_alerttitle_alertprompt_accessref_keyusage_keyattributes_).md>)
