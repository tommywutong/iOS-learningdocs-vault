---
title: removeLast()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swift/uniquearray/removelast()
source_url: 'https://developer.apple.com/documentation/swift/uniquearray/removelast()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uniquearray/removelast%28%29.json'
content_hash: 'sha256:11a138b567b0bf6f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UniqueArray](../uniquearray.md)

# removeLast()

<sub>Instance Method</sub>

Removes and returns the last element of the array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult mutating func removeLast() -> Element
```

## Return Value

The last element of the original array.

## Discussion

The array must not be empty.

> [!abstract] Complexity
> O(1)
