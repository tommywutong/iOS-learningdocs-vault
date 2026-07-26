---
title: compactName
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/numberformatstyleconfiguration/notation/compactname
source_url: 'https://developer.apple.com/documentation/foundation/numberformatstyleconfiguration/notation/compactname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatstyleconfiguration/notation/compactname.json'
content_hash: 'sha256:2d632c6833f8fd1b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NumberFormatStyleConfiguration](../../numberformatstyleconfiguration.md) · [Notation](../notation.md)

# compactName

<sub>Type Property</sub>

A locale-appropriate compact name notation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var compactName: NumberFormatStyleConfiguration.Notation { get }
```

## Discussion

A compact name notation, when available in the format style’s locale, that uses prefixes or suffixes corresponding to powers of ten. The following example shows a compact name notation in the `fr_FR` locale:

```swift
let compactNameFormatted = 1234.formatted(.number
    .locale(Locale(identifier: "fr_FR"))
    .notation(.compactName)) // "1,2 k"
```

## See Also

### Notations

- [automatic](automatic.md) — A notation that automatically provides locale-appropriate behavior.
- [scientific](scientific.md) — A notation constant that formats values with scientific notation.
