---
title: noAccessControl
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seckeyimportexportflags/noaccesscontrol
source_url: 'https://developer.apple.com/documentation/security/seckeyimportexportflags/noaccesscontrol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeyimportexportflags/noaccesscontrol.json'
content_hash: 'sha256:6f54398e9e709fe9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecKeyImportExportFlags](../seckeyimportexportflags.md)

# noAccessControl

<sub>Type Property</sub>

A flag that indicates imported private keys have no access object attached to them.

<sub>macOS</sub>

```swift
static var noAccessControl: SecKeyImportExportFlags { get }
```

## Discussion

In the absence of both this bit and the [accessRef](../secitemimportexportkeyparameters/accessref.md) field in the [SecItemImportExportKeyParameters](../secitemimportexportkeyparameters.md) structure, imported private keys receive default access controls.
