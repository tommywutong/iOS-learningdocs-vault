---
title: 'init(rawValue:)'
framework: Security
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/security/secitemimportexportflags/init(rawvalue:)'
source_url: 'https://developer.apple.com/documentation/security/secitemimportexportflags/init(rawvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secitemimportexportflags/init%28rawvalue%3A%29.json'
content_hash: 'sha256:7c59dd24e838079c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecItemImportExportFlags](../secitemimportexportflags.md)

# init(rawValue:)

<sub>Initializer</sub>

Initialize an item import/export flag structure.

<sub>macOS</sub>

```swift
init(rawValue: UInt32)
```

## Parameters

- `rawValue` — An initial value for the structure composed as the bitwise `OR` of zero or more of the valid values.
