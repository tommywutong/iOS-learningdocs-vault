---
title: allowFragments
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+（27.0 起废弃）, iPadOS 5.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.7+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/jsonserialization/readingoptions/allowfragments
source_url: 'https://developer.apple.com/documentation/foundation/jsonserialization/readingoptions/allowfragments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/jsonserialization/readingoptions/allowfragments.json'
content_hash: 'sha256:256b7db83845f7f2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [JSONSerialization](../../jsonserialization.md) · [ReadingOptions](../readingoptions.md)

# allowFragments

<sub>Type Property</sub>

A deprecated option that specifies that the parser should allow top-level objects that aren’t arrays or dictionaries.

> [!warning] Deprecated
> Use [NSJSONReadingFragmentsAllowed](fragmentsallowed.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var allowFragments: JSONSerialization.ReadingOptions { get }
```

## See Also

### Reading Options

- [NSJSONReadingMutableContainers](mutablecontainers.md) — Specifies that arrays and dictionaries in the returned object are mutable.
- [NSJSONReadingMutableLeaves](mutableleaves.md) — Specifies that leaf strings in the JSON object graph are mutable.
- [NSJSONReadingFragmentsAllowed](fragmentsallowed.md) — Specifies that the parser allows top-level objects that aren’t arrays or dictionaries.
- [NSJSONReadingJSON5Allowed](json5allowed.md) — Specifies that reading serialized JSON data supports the JSON5 syntax.
- [NSJSONReadingTopLevelDictionaryAssumed](topleveldictionaryassumed.md) — Specifies that the parser assumes the top level of the JSON data is a dictionary, even if it doesn’t begin and end with curly braces.
