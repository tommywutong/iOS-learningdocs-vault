---
title: 'insert(moving:at:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/uniquearray/insert(moving:at:)-4f2qc'
source_url: 'https://developer.apple.com/documentation/swift/uniquearray/insert(moving:at:)-4f2qc'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uniquearray/insert%28moving%3Aat%3A%29-4f2qc.json'
content_hash: 'sha256:2c6753f042cb970b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UniqueArray](../uniquearray.md)

# insert(moving:at:)

<sub>Instance Method</sub>

Moves the elements of a fully initialized buffer into this array, starting at the specified position, and leaving the buffer uninitialized.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func insert(moving items: UnsafeMutableBufferPointer<Element>, at index: Int)
```

## Parameters

- `items` — A fully initialized buffer whose contents to move into the array.

## Discussion

If the array does not have sufficient capacity to hold all elements, then this reallocates storage to extend its capacity, using a geometric growth rate.

> [!abstract] Complexity
> O(`self.count` + `items.count`)
