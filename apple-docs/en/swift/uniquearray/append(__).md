---
title: 'append(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/uniquearray/append(_:)'
source_url: 'https://developer.apple.com/documentation/swift/uniquearray/append(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uniquearray/append%28_%3A%29.json'
content_hash: 'sha256:3178cf216acba8d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UniqueArray](../uniquearray.md)

# append(_:)

<sub>Instance Method</sub>

Adds an element to the end of the array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func append(_ item: consuming Element)
```

## Parameters

- `item` — The element to append to the collection.

## Discussion

If the array does not have sufficient capacity to hold any more elements, then this reallocates the array’s storage to grow its capacity, using a geometric growth rate.

> [!abstract] Complexity
> O(1) as amortized over many invocations on the same array.
