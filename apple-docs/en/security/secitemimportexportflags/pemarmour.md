---
title: pemArmour
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secitemimportexportflags/pemarmour
source_url: 'https://developer.apple.com/documentation/security/secitemimportexportflags/pemarmour'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secitemimportexportflags/pemarmour.json'
content_hash: 'sha256:cad8e720339fa761'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecItemImportExportFlags](../secitemimportexportflags.md)

# pemArmour

<sub>Type Property</sub>

A flag that indicates the exported data should have PEM armor.

<sub>macOS</sub>

```swift
static var pemArmour: SecItemImportExportFlags { get }
```

## Discussion

PEM armor refers to a way of expressing binary data as an ASCII string so that it can be transferred over text-only channels such as email. (PEM stands for an Internet standard, Privacy Enhanced Mail.)
