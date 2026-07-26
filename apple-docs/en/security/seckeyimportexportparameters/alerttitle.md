---
title: alertTitle
framework: Security
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seckeyimportexportparameters/alerttitle
source_url: 'https://developer.apple.com/documentation/security/seckeyimportexportparameters/alerttitle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeyimportexportparameters/alerttitle.json'
content_hash: 'sha256:f5021b8ad6eff08e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecKeyImportExportParameters](../seckeyimportexportparameters.md)

# alertTitle

<sub>Instance Property</sub>

The title to display in the secure passphrase alert panel.

<sub>macOS</sub>

```swift
var alertTitle: Unmanaged<CFString>
```

## Discussion

When importing or exporting a key, if you set the [kSecKeySecurePassphrase](../seckeyimportexportflags/securepassphrase.md) flag bit, you can optionally use this field to specify a string for the password panel’s title bar.
