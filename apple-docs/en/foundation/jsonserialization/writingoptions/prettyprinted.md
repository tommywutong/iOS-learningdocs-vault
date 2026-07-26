---
title: prettyPrinted
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/jsonserialization/writingoptions/prettyprinted
source_url: 'https://developer.apple.com/documentation/foundation/jsonserialization/writingoptions/prettyprinted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/jsonserialization/writingoptions/prettyprinted.json'
content_hash: 'sha256:deb6338d2023295d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [JSONSerialization](../../jsonserialization.md) · [WritingOptions](../writingoptions.md)

# prettyPrinted

<sub>Type Property</sub>

Specifies that the output uses white space and indentation to make the resulting data more readable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var prettyPrinted: JSONSerialization.WritingOptions { get }
```

## Discussion

If this option isn’t set, the serialization generates the most compact possible JSON representation.

## See Also

### Formatting JSON

- [NSJSONWritingFragmentsAllowed](fragmentsallowed.md) — Specifies that the parser should allow top-level objects that aren’t arrays or dictionaries.
- [NSJSONWritingSortedKeys](sortedkeys.md) — Specifies that the output sorts keys in lexicographic order.
- [NSJSONWritingWithoutEscapingSlashes](withoutescapingslashes.md) — Specifies that the output doesn’t prefix slash characters with escape characters.
