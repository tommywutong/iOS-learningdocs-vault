---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/array/init(_:)-236cl'
source_url: 'https://developer.apple.com/documentation/swift/array/init(_:)-236cl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/init%28_%3A%29-236cl.json'
content_hash: 'sha256:5a5158697d7e86ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# init(_:)

<sub>Initializer</sub>

Creates an array containing the elements of a sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<S>(_ s: S) where Element == S.Element, S : Sequence
```

## Parameters

- `s` — The sequence of elements to turn into an array.

## Discussion

You can use this initializer to create an array from any other type that conforms to the `Sequence` protocol. For example, you might want to create an array with the integers from 1 through 7. Use this initializer around a range instead of typing all those numbers in an array literal.

```swift
let numbers = Array(1...7)
print(numbers)
// Prints "[1, 2, 3, 4, 5, 6, 7]"
```

You can also use this initializer to convert a complex sequence or collection type back to an array. For example, the `keys` property of a dictionary isn’t an array with its own storage, it’s a collection that maps its elements from the dictionary only when they’re accessed, saving the time and space needed to allocate an array. If you need to pass those keys to a method that takes an array, however, use this initializer to convert that list from its type of `LazyMapCollection<Dictionary<String, Int>, Int>` to a simple `[String]`.

```swift
func cacheImages(withNames names: [String]) {
    // custom image loading and caching
 }

let namedHues: [String: Int] = ["Vermillion": 18, "Magenta": 302,
        "Gold": 50, "Cerise": 320]
let colorNames = Array(namedHues.keys)
cacheImages(withNames: colorNames)

print(colorNames)
// Prints "["Gold", "Cerise", "Magenta", "Vermillion"]"
```

## See Also

### Creating an Array

- [init()](<init().md>) — Creates a new, empty array.
- [init(_:)](<init(__)-1ip9h.md>) — Creates a new instance of a collection containing the elements of a sequence.
- [init(repeating:count:)](<init(repeating_count_).md>) — Creates a new array containing the specified number of a single, repeated value.
- [init(unsafeUninitializedCapacity:initializingWith:)](<init(unsafeuninitializedcapacity_initializingwith_).md>) — Creates an array with the specified capacity, and then calls the given closure with a buffer covering the array’s uninitialized memory.
