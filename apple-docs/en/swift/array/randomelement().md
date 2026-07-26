---
title: randomElement()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/array/randomelement()
source_url: 'https://developer.apple.com/documentation/swift/array/randomelement()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/randomelement%28%29.json'
content_hash: 'sha256:9667d04eb26db22e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

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

## See Also

### Accessing Elements

- [subscript(_:)](<subscript(__)-25iat.md>) — Accesses the element at the specified position.
- [first](first.md) — The first element of the collection.
- [last](last.md) — The last element of the collection.
- [subscript(_:)](<subscript(__)-53fvb.md>) — Accesses a contiguous subrange of the array’s elements.
- [subscript(_:)](<subscript(__)-3kwny.md>)
- [subscript(_:)](<subscript(__)-4h7rl.md>) — Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript(_:)](<subscript(__)-3pmfg.md>)
- [randomElement(using:)](<randomelement(using_).md>) — Returns a random element of the collection, using the given generator as a source for randomness.
