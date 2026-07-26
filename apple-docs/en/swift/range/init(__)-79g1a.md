---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/range/init(_:)-79g1a'
source_url: 'https://developer.apple.com/documentation/swift/range/init(_:)-79g1a'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/range/init%28_%3A%29-79g1a.json'
content_hash: 'sha256:1f5f4133e7c13a17'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Range](../range.md)

# init(_:)

<sub>Initializer</sub>

Creates an instance equivalent to the given `ClosedRange`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ other: ClosedRange<Bound>)
```

## Parameters

- `other` — A closed range to convert to a `Range` instance.

## Discussion

An equivalent range must be representable as an instance of Range. For example, passing a closed range with an upper bound of `Int.max` triggers a runtime error, because the resulting half-open range would require an upper bound of `Int.max + 1`, which is not representable as an `Int`.
