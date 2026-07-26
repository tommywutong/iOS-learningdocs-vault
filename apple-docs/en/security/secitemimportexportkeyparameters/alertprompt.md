---
title: alertPrompt
framework: Security
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secitemimportexportkeyparameters/alertprompt
source_url: 'https://developer.apple.com/documentation/security/secitemimportexportkeyparameters/alertprompt'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secitemimportexportkeyparameters/alertprompt.json'
content_hash: 'sha256:1e5382fe09441a8e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecItemImportExportKeyParameters](../secitemimportexportkeyparameters.md)

# alertPrompt

<sub>Instance Property</sub>

The prompt to display in the secure passphrase alert panel.

<sub>macOS</sub>

```swift
var alertPrompt: Unmanaged<CFString>?
```

## Discussion

When importing or exporting a key, if you set the [kSecKeySecurePassphrase](../seckeyimportexportflags/securepassphrase.md) flag bit, you can optionally use this field to specify a string for the prompt that appears in the password panel.
