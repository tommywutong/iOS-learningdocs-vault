---
title: withoutEscapingSlashes
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/jsonserialization/writingoptions/withoutescapingslashes
source_url: 'https://developer.apple.com/documentation/foundation/jsonserialization/writingoptions/withoutescapingslashes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/jsonserialization/writingoptions/withoutescapingslashes.json'
content_hash: 'sha256:2eef984bbf403fb4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [JSONSerialization](../../jsonserialization.md) · [WritingOptions](../writingoptions.md)

# withoutEscapingSlashes

<sub>Type Property</sub>

Specifies that the output doesn’t prefix slash characters with escape characters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var withoutEscapingSlashes: JSONSerialization.WritingOptions { get }
```

## See Also

### Formatting JSON

- [NSJSONWritingFragmentsAllowed](fragmentsallowed.md) — Specifies that the parser should allow top-level objects that aren’t arrays or dictionaries.
- [NSJSONWritingPrettyPrinted](prettyprinted.md) — Specifies that the output uses white space and indentation to make the resulting data more readable.
- [NSJSONWritingSortedKeys](sortedkeys.md) — Specifies that the output sorts keys in lexicographic order.
