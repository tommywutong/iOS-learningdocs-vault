---
title: localizedStandard
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/string/standardcomparator/localizedstandard
source_url: 'https://developer.apple.com/documentation/swift/string/standardcomparator/localizedstandard'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/standardcomparator/localizedstandard.json'
content_hash: 'sha256:9863838fec00cb82'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [String](../../string.md) · [StandardComparator](../standardcomparator.md)

# localizedStandard

<sub>Type Property</sub>

Compares `String`s as compared by the Finder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let localizedStandard: String.StandardComparator
```

## Discussion

Uses a localized, numeric comparison in the current locale.

The default `SortComparator` used in `String` comparisons.
