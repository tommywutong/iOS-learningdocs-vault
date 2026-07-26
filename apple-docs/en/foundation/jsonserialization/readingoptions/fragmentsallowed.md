---
title: fragmentsAllowed
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/jsonserialization/readingoptions/fragmentsallowed
source_url: 'https://developer.apple.com/documentation/foundation/jsonserialization/readingoptions/fragmentsallowed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/jsonserialization/readingoptions/fragmentsallowed.json'
content_hash: 'sha256:7bc778cae53ca99d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [JSONSerialization](../../jsonserialization.md) · [ReadingOptions](../readingoptions.md)

# fragmentsAllowed

<sub>Type Property</sub>

Specifies that the parser allows top-level objects that aren’t arrays or dictionaries.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var fragmentsAllowed: JSONSerialization.ReadingOptions { get }
```

## See Also

### Reading Options

- [NSJSONReadingMutableContainers](mutablecontainers.md) — Specifies that arrays and dictionaries in the returned object are mutable.
- [NSJSONReadingMutableLeaves](mutableleaves.md) — Specifies that leaf strings in the JSON object graph are mutable.
- [NSJSONReadingJSON5Allowed](json5allowed.md) — Specifies that reading serialized JSON data supports the JSON5 syntax.
- [NSJSONReadingTopLevelDictionaryAssumed](topleveldictionaryassumed.md) — Specifies that the parser assumes the top level of the JSON data is a dictionary, even if it doesn’t begin and end with curly braces.
- [NSJSONReadingAllowFragments](allowfragments.md) — A deprecated option that specifies that the parser should allow top-level objects that aren’t arrays or dictionaries. _(deprecated)_
