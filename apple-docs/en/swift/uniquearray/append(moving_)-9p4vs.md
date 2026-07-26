---
title: 'append(moving:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/uniquearray/append(moving:)-9p4vs'
source_url: 'https://developer.apple.com/documentation/swift/uniquearray/append(moving:)-9p4vs'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uniquearray/append%28moving%3A%29-9p4vs.json'
content_hash: 'sha256:0c94abf7b7ffae39'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UniqueArray](../uniquearray.md)

# append(moving:)

<sub>Instance Method</sub>

Moves the elements of a output span to the end of this array, leaving the span empty.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func append(moving items: inout OutputSpan<Element>)
```

## Parameters

- `items` — An output span whose contents need to be appended to this array.

## Discussion

If the array does not have sufficient capacity to hold all new items, then this reallocates the array’s storage to grow its capacity, using a geometric growth rate.

> [!abstract] Complexity
> O(`items.count`)
