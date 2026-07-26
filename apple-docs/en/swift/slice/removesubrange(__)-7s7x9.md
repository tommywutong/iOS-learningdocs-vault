---
title: 'removeSubrange(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/slice/removesubrange(_:)-7s7x9'
source_url: 'https://developer.apple.com/documentation/swift/slice/removesubrange(_:)-7s7x9'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/slice/removesubrange%28_%3A%29-7s7x9.json'
content_hash: 'sha256:4d5f0b53194b27ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Slice](../slice.md)

# removeSubrange(_:)

<sub>Instance Method</sub>

Removes the specified subrange of elements from the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func removeSubrange(_ bounds: Range<Slice<Base>.Index>)
```

## Parameters

- `bounds` — The subrange of the collection to remove. The bounds of the range must be valid indices of the collection.

## Discussion

```swift
var bugs = ["Aphid", "Bumblebee", "Cicada", "Damselfly", "Earwig"]
bugs.removeSubrange(1...3)
print(bugs)
// Prints "["Aphid", "Earwig"]"
```

Calling this method may invalidate any existing indices for use with this collection.

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the collection.
