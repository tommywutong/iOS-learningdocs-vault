---
title: String.Comparator
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/string/comparator
source_url: 'https://developer.apple.com/documentation/swift/string/comparator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/comparator.json'
content_hash: 'sha256:d53aaaaa503d6b56'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# String.Comparator

<sub>Structure</sub>

A `String` comparison performed using the given comparison options and locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Comparator
```

## Relationships

- **Conforms To**: [Decodable](../decodable.md), [Encodable](../encodable.md), [Equatable](../equatable.md), [Hashable](../hashable.md), [Sendable](../sendable.md), [SendableMetatype](../sendablemetatype.md), [SortComparator](../../foundation/sortcomparator.md)

## Topics

### Initializers

- [init(_:)](<comparator/init(__).md>) — Creates a `String.Comparator` that represents the same comparison as the given `String.StandardComparator`.
- [init(options:locale:order:)](<comparator/init(options_locale_order_).md>) — Creates a `String.Comparator` with the given `CompareOptions` and `Locale`.

### Instance Properties

- [locale](comparator/locale.md) — The locale to use for comparison if the comparator is localized, otherwise nil.
- [options](comparator/options.md) — The options to use for comparison.
