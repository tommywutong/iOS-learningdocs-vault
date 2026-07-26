---
title: 'reserveCapacity(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/uniquearray/reservecapacity(_:)'
source_url: 'https://developer.apple.com/documentation/swift/uniquearray/reservecapacity(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uniquearray/reservecapacity%28_%3A%29.json'
content_hash: 'sha256:bf6936a1fe51beed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UniqueArray](../uniquearray.md)

# reserveCapacity(_:)

<sub>Instance Method</sub>

Ensure that the array has capacity to store the specified number of elements, by growing its storage buffer if necessary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func reserveCapacity(_ n: Int)
```

## Discussion

If `capacity < n`, then this operation reallocates the unique array’s storage to grow it; on return, the array’s capacity becomes `n`. Otherwise the array is left as is.

> [!abstract] Complexity
> O(`count`)
