---
title: scientific
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/numberformatstyleconfiguration/notation/scientific
source_url: 'https://developer.apple.com/documentation/foundation/numberformatstyleconfiguration/notation/scientific'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatstyleconfiguration/notation/scientific.json'
content_hash: 'sha256:f8a6e3e06c00e4d1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NumberFormatStyleConfiguration](../../numberformatstyleconfiguration.md) · [Notation](../notation.md)

# scientific

<sub>Type Property</sub>

A notation constant that formats values with scientific notation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var scientific: NumberFormatStyleConfiguration.Notation { get }
```

## Discussion

The following example shows the effect of using scientific notation with a format style:

```swift
let scientific = 12345.formatted(.number
    .notation(.scientific)) // 1.2345E4"

```

## See Also

### Notations

- [automatic](automatic.md) — A notation that automatically provides locale-appropriate behavior.
- [compactName](compactname.md) — A locale-appropriate compact name notation.
