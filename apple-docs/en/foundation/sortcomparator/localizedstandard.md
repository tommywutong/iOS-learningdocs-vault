---
title: localizedStandard
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/sortcomparator/localizedstandard
source_url: 'https://developer.apple.com/documentation/foundation/sortcomparator/localizedstandard'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/sortcomparator/localizedstandard.json'
content_hash: 'sha256:da4e1e3b3ec10125'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [SortComparator](../sortcomparator.md)

# localizedStandard

<sub>Type Property</sub>

A comparator that compares a string using a localized, numeric comparison in the current locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var localizedStandard: String.Comparator { get }
```

## Discussion

Compares [String](../../swift/string.md) in a manner similar to the Finder.

## See Also

### Inspecting a Comparator

- [order](order.md) — The sort order that the comparator uses to compare.
- [localized](localized.md) — A comparator that compares a string using a localized comparison in the current locale.
