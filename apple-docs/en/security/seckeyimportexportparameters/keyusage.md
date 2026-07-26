---
title: keyUsage
framework: Security
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seckeyimportexportparameters/keyusage
source_url: 'https://developer.apple.com/documentation/security/seckeyimportexportparameters/keyusage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeyimportexportparameters/keyusage.json'
content_hash: 'sha256:b545714cadc133cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecKeyImportExportParameters](../seckeyimportexportparameters.md)

# keyUsage

<sub>Instance Property</sub>

A word of bits constituting the low-level use flags for imported keys.

<sub>macOS</sub>

```swift
var keyUsage: CSSM_KEYUSE
```

## Discussion

Use flags defined in `cssmtype.h`. If this field is `0` or `keyParams` is `NULL`, the default value is `CSSM_KEYUSE_ANY`.
