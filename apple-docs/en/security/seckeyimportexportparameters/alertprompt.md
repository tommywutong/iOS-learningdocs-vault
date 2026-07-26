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
doc_path: /documentation/security/seckeyimportexportparameters/alertprompt
source_url: 'https://developer.apple.com/documentation/security/seckeyimportexportparameters/alertprompt'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeyimportexportparameters/alertprompt.json'
content_hash: 'sha256:b2a8e2821f292f8d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecKeyImportExportParameters](../seckeyimportexportparameters.md)

# alertPrompt

<sub>Instance Property</sub>

The prompt to display in the secure passphrase alert panel.

<sub>macOS</sub>

```swift
var alertPrompt: Unmanaged<CFString>
```

## Discussion

When importing or exporting a key, if you set the [kSecKeySecurePassphrase](../seckeyimportexportflags/securepassphrase.md) flag bit, you can optionally use this field to specify a string for the prompt that appears in the password panel.
