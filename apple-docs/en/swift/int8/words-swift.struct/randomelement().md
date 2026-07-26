---
title: randomElement()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/int8/words-swift.struct/randomelement()
source_url: 'https://developer.apple.com/documentation/swift/int8/words-swift.struct/randomelement()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int8/words-swift.struct/randomelement%28%29.json'
content_hash: 'sha256:3c3e15ed575531ca'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Int8](../../int8.md) · [Words](../words-swift.struct.md)

# randomElement()

<sub>Instance Method</sub>

Returns a random element of the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func randomElement() -> Self.Element?
```

## Return Value

A random element from the collection. If the collection is empty, the method returns `nil`.

## Discussion

Call `randomElement()` to select a random element from an array or another collection. This example picks a name at random from an array:

```swift
let names = ["Zoey", "Chloe", "Amani", "Amaia"]
let randomName = names.randomElement()!
// randomName == "Amani"
```

This method is equivalent to calling `randomElement(using:)`, passing in the system’s default random generator.

> [!abstract] Complexity
> O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(_n_), where _n_ is the length of the collection.
