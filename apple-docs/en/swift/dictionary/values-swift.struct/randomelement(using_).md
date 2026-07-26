---
title: 'randomElement(using:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/dictionary/values-swift.struct/randomelement(using:)'
source_url: 'https://developer.apple.com/documentation/swift/dictionary/values-swift.struct/randomelement(using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dictionary/values-swift.struct/randomelement%28using%3A%29.json'
content_hash: 'sha256:ed3f21116aa62ef1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Dictionary](../../dictionary.md) · [Values](../values-swift.struct.md)

# randomElement(using:)

<sub>Instance Method</sub>

Returns a random element of the collection, using the given generator as a source for randomness.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func randomElement<T>(using generator: inout T) -> Self.Element? where T : RandomNumberGenerator
```

## Parameters

- `generator` — The random number generator to use when choosing a random element.

## Return Value

A random element from the collection. If the collection is empty, the method returns `nil`.

## Discussion

Call `randomElement(using:)` to select a random element from an array or another collection when you are using a custom random number generator. This example picks a name at random from an array:

```swift
let names = ["Zoey", "Chloe", "Amani", "Amaia"]
let randomName = names.randomElement(using: &myGenerator)!
// randomName == "Amani"
```

> [!abstract] Complexity
> O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(_n_), where _n_ is the length of the collection.

> [!note] Note
> The algorithm used to select a random element may change in a future version of Swift. If you’re passing a generator that results in the same sequence of elements each time you run your program, that sequence may change when your program is compiled using a different version of Swift.
