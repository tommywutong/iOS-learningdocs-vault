---
title: 'randomElement(using:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/array/randomelement(using:)'
source_url: 'https://developer.apple.com/documentation/swift/array/randomelement(using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/randomelement%28using%3A%29.json'
content_hash: 'sha256:6694b392c2a40c0c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

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

## See Also

### Accessing Elements

- [subscript(_:)](<subscript(__)-25iat.md>) — Accesses the element at the specified position.
- [first](first.md) — The first element of the collection.
- [last](last.md) — The last element of the collection.
- [subscript(_:)](<subscript(__)-53fvb.md>) — Accesses a contiguous subrange of the array’s elements.
- [subscript(_:)](<subscript(__)-3kwny.md>)
- [subscript(_:)](<subscript(__)-4h7rl.md>) — Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript(_:)](<subscript(__)-3pmfg.md>)
- [randomElement()](<randomelement().md>) — Returns a random element of the collection.
