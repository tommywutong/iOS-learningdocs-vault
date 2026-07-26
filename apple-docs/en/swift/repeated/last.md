---
title: last
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/repeated/last
source_url: 'https://developer.apple.com/documentation/swift/repeated/last'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/repeated/last.json'
content_hash: 'sha256:85f032e99120e8c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Repeated](../repeated.md)

# last

<sub>Instance Property</sub>

The last element of the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var last: Self.Element? { get }
```

## Discussion

If the collection is empty, the value of this property is `nil`.

```swift
let numbers = [10, 20, 30, 40, 50]
if let lastNumber = numbers.last {
    print(lastNumber)
}
// Prints "50"
```

> [!abstract] Complexity
> O(1)
