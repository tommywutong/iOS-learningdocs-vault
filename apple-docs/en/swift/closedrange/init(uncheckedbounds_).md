---
title: 'init(uncheckedBounds:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/closedrange/init(uncheckedbounds:)'
source_url: 'https://developer.apple.com/documentation/swift/closedrange/init(uncheckedbounds:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/closedrange/init%28uncheckedbounds%3A%29.json'
content_hash: 'sha256:f8ba64fe9a9fc19e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ClosedRange](../closedrange.md)

# init(uncheckedBounds:)

<sub>Initializer</sub>

Creates an instance with the given bounds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(uncheckedBounds bounds: (lower: Bound, upper: Bound))
```

## Parameters

- `bounds` — A tuple of the lower and upper bounds of the range.

## Discussion

Because this initializer does not perform any checks, it should be used as an optimization only when you are absolutely certain that `lower` is less than or equal to `upper`. Using the closed range operator (`...`) to form `ClosedRange` instances is preferred.

## See Also

### Infrequently Used Functionality

- [hashValue](hashvalue.md) — The hash value.
