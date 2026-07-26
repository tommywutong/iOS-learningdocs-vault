---
title: 'init(repeating:count:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/uniquearray/init(repeating:count:)'
source_url: 'https://developer.apple.com/documentation/swift/uniquearray/init(repeating:count:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uniquearray/init%28repeating%3Acount%3A%29.json'
content_hash: 'sha256:c2ade9f17bc533a6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UniqueArray](../uniquearray.md)

# init(repeating:count:)

<sub>Initializer</sub>

Creates a new array containing the specified number of a single, repeated value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(repeating repeatedValue: Element, count: Int)
```

## Parameters

- `repeatedValue` — The element to repeat.

- `count` — The number of times to repeat the value passed in the `repeating` parameter. `count` must be zero or greater.

## Discussion

> [!abstract] Complexity
> O(`count`)
