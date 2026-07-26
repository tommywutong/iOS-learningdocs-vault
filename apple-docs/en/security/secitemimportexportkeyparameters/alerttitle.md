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
doc_path: /documentation/security/secitemimportexportkeyparameters/alerttitle
source_url: 'https://developer.apple.com/documentation/security/secitemimportexportkeyparameters/alerttitle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secitemimportexportkeyparameters/alerttitle.json'
content_hash: 'sha256:7e62a8506cbaf42c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecItemImportExportKeyParameters](../secitemimportexportkeyparameters.md)

# alertTitle

<sub>Instance Property</sub>

The title to display in the secure passphrase alert panel.

<sub>macOS</sub>

```swift
var alertTitle: Unmanaged<CFString>?
```

## Discussion

When importing or exporting a key, if you set the [kSecKeySecurePassphrase](../seckeyimportexportflags/securepassphrase.md) flag bit, you can optionally use this field to specify a string for the password panel’s title bar.
