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
doc_path: '/documentation/swift/uniquearray/append(moving:)-71oaj'
source_url: 'https://developer.apple.com/documentation/swift/uniquearray/append(moving:)-71oaj'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uniquearray/append%28moving%3A%29-71oaj.json'
content_hash: 'sha256:5a175b9ed0cf989d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UniqueArray](../uniquearray.md)

# append(moving:)

<sub>Instance Method</sub>

Moves the elements of a buffer to the end of this array, leaving the buffer uninitialized.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func append(moving items: UnsafeMutableBufferPointer<Element>)
```

## Parameters

- `items` — A fully initialized buffer whose contents to move into the array.

## Discussion

If the array does not have sufficient capacity to hold all items in the buffer, then this reallocates the array’s storage to grow its capacity, using a geometric growth rate.

> [!abstract] Complexity
> O(`count` + `items.count`)
