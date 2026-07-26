---
title: first
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/string/utf8view/first
source_url: 'https://developer.apple.com/documentation/swift/string/utf8view/first'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/utf8view/first.json'
content_hash: 'sha256:c88ce792c8ea9537'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [String](../../string.md) · [UTF8View](../utf8view.md)

# first

<sub>Instance Property</sub>

The first element of the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var first: Self.Element? { get }
```

## Discussion

If the collection is empty, the value of this property is `nil`.

```swift
let numbers = [10, 20, 30, 40, 50]
if let firstNumber = numbers.first {
    print(firstNumber)
}
// Prints "10"
```
