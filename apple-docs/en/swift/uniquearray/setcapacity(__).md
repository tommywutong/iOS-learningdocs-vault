---
title: 'setCapacity(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/uniquearray/setcapacity(_:)'
source_url: 'https://developer.apple.com/documentation/swift/uniquearray/setcapacity(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uniquearray/setcapacity%28_%3A%29.json'
content_hash: 'sha256:4f6ad2a1a44a60ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UniqueArray](../uniquearray.md)

# setCapacity(_:)

<sub>Instance Method</sub>

Grow or shrink the capacity of a unique array instance without discarding its contents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func setCapacity(_ newCapacity: Int)
```

## Parameters

- `newCapacity` — The desired new capacity. `newCapacity` must be greater than or equal to the current count.

## Discussion

This operation replaces the array’s storage buffer with a newly allocated buffer of the specified capacity, moving all existing elements to its new storage. The old storage is then deallocated.

> [!abstract] Complexity
> O(`count`)
