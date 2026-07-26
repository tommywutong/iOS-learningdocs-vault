---
title: String.StandardComparator
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/string/standardcomparator
source_url: 'https://developer.apple.com/documentation/swift/string/standardcomparator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/standardcomparator.json'
content_hash: 'sha256:a7078c88c098968c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# String.StandardComparator

<sub>Structure</sub>

Compares `String`s using one of a fixed set of standard comparison algorithms.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct StandardComparator
```

## Relationships

- **Conforms To**: [Decodable](../decodable.md), [Encodable](../encodable.md), [Equatable](../equatable.md), [Hashable](../hashable.md), [Sendable](../sendable.md), [SendableMetatype](../sendablemetatype.md), [SortComparator](../../foundation/sortcomparator.md)

## Topics

### Initializers

- [init(_:order:)](<standardcomparator/init(__order_).md>) — Create a `StandardComparator` from the given `StandardComparator` with the given new `order`.

### Type Properties

- [lexical](standardcomparator/lexical.md) — Compares `String`s lexically.
- [localized](standardcomparator/localized.md) — Compares `String`s using a localized comparison in the current locale.
- [localizedStandard](standardcomparator/localizedstandard.md) — Compares `String`s as compared by the Finder.
