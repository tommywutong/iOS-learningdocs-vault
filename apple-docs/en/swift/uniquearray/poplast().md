---
title: popLast()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swift/uniquearray/poplast()
source_url: 'https://developer.apple.com/documentation/swift/uniquearray/poplast()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uniquearray/poplast%28%29.json'
content_hash: 'sha256:a7929ac6474d337b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UniqueArray](../uniquearray.md)

# popLast()

<sub>Instance Method</sub>

Removes and returns the last element of the array, if there is one.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func popLast() -> Element?
```

## Return Value

The last element of the array if the array is not empty; otherwise, `nil`.

## Discussion

> [!abstract] Complexity
> O(1)
