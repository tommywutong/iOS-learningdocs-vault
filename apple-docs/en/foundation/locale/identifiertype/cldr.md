---
title: Locale.IdentifierType.cldr
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/identifiertype/cldr
source_url: 'https://developer.apple.com/documentation/foundation/locale/identifiertype/cldr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/identifiertype/cldr.json'
content_hash: 'sha256:39f18f80dd07cb9a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Locale](../../locale.md) · [IdentifierType](../identifiertype.md)

# Locale.IdentifierType.cldr

<sub>Case</sub>

The type of identifiers that follow CLDR (Common Locale Data Repository) conventions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case cldr
```

## Discussion

The components in this type of identifier use the same components as in [Locale.IdentifierType.icu](icu.md), but don’t use the key-value type keyword list. An example of this type is `th_TH_u_ca_gregory_nu_thai`.

## See Also

### Standard Identifier Types

- [Locale.IdentifierType.icu](icu.md) — The type of identifiers that follow ICU (International Components for Unicode) conventions.
- [Locale.IdentifierType.bcp47](bcp47.md) — The type of BCP 47 language identifiers.
