---
title: 'init(_:order:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/standardcomparator/init(_:order:)'
source_url: 'https://developer.apple.com/documentation/swift/string/standardcomparator/init(_:order:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/standardcomparator/init%28_%3Aorder%3A%29.json'
content_hash: 'sha256:574feffb4f31208b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [String](../../string.md) · [StandardComparator](../standardcomparator.md)

# init(_:order:)

<sub>Initializer</sub>

Create a `StandardComparator` from the given `StandardComparator` with the given new `order`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ base: String.StandardComparator, order: SortOrder = .forward)
```

## Parameters

- `base` — The standard comparator to modify the order of.

- `order` — The initial order of the new `StandardComparator`.
