---
title: SecItemImportExportFlags
framework: Security
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secitemimportexportflags
source_url: 'https://developer.apple.com/documentation/security/secitemimportexportflags'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secitemimportexportflags.json'
content_hash: 'sha256:b4f1edf50b82bac2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecItemImportExportFlags

<sub>Structure</sub>

The import and export function flags.

<sub>macOS</sub>

```swift
struct SecItemImportExportFlags
```

## Overview

Use an instance of this structure a the flags input to the [SecItemImport](<secitemimport(________________).md>) and [SecItemExport](<secitemexport(__________).md>) functions.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<secitemimportexportflags/init(rawvalue_).md>) — Initialize an item import/export flag structure.

### Constants

- [kSecItemPemArmour](secitemimportexportflags/pemarmour.md) — A flag that indicates the exported data should have PEM armor.
