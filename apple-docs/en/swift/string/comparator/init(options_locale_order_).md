---
title: 'init(options:locale:order:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/comparator/init(options:locale:order:)'
source_url: 'https://developer.apple.com/documentation/swift/string/comparator/init(options:locale:order:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/comparator/init%28options%3Alocale%3Aorder%3A%29.json'
content_hash: 'sha256:05cab17048173008'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [String](../../string.md) · [Comparator](../comparator.md)

# init(options:locale:order:)

<sub>Initializer</sub>

Creates a `String.Comparator` with the given `CompareOptions` and `Locale`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(options: String.CompareOptions, locale: Locale? = Locale.current, order: SortOrder = .forward)
```

## Parameters

- `options` — The options to use for comparison.

- `locale` — The locale to use for comparison. If `nil`, the comparison is unlocalized.

- `order` — The initial order to use for ordered comparison.
