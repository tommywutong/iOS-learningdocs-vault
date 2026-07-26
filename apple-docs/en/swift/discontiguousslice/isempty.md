---
title: isEmpty
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/discontiguousslice/isempty
source_url: 'https://developer.apple.com/documentation/swift/discontiguousslice/isempty'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/discontiguousslice/isempty.json'
content_hash: 'sha256:39d3376f84fca7e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [DiscontiguousSlice](../discontiguousslice.md)

# isEmpty

<sub>Instance Property</sub>

A Boolean value indicating whether the collection is empty.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isEmpty: Bool { get }
```

## Discussion

When you need to check whether your collection is empty, use the `isEmpty` property instead of checking that the `count` property is equal to zero. For collections that don’t conform to `RandomAccessCollection`, accessing the `count` property iterates through the elements of the collection.

```swift
let horseName = "Silver"
if horseName.isEmpty {
    print("My horse has no name.")
} else {
    print("Hi ho, \(horseName)!")
}
// Prints "Hi ho, Silver!"
```

> [!abstract] Complexity
> O(1)
