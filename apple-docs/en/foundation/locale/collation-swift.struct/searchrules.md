---
title: searchRules
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/collation-swift.struct/searchrules
source_url: 'https://developer.apple.com/documentation/foundation/locale/collation-swift.struct/searchrules'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/collation-swift.struct/searchrules.json'
content_hash: 'sha256:cee808de32ede1ae'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Locale](../../locale.md) · [Collation](../collation-swift.struct.md)

# searchRules

<sub>Type Property</sub>

A collation used for string search.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let searchRules: Locale.Collation
```

## Discussion

Use this collation only for determining whether to consider two strings as equivalent. Using this collation may modify the string for search purposes. For example, this colloation supresses the contractions in Thai and Lao.

Don’t use this collation to determine the relative order of two strings.

## See Also

### Using special-purpose collations

- [standard](standard.md) — A collation that provides the default ordering for each language.
