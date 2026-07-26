---
title: base
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/reversedcollection/index/base
source_url: 'https://developer.apple.com/documentation/swift/reversedcollection/index/base'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/reversedcollection/index/base.json'
content_hash: 'sha256:dea453bcd683f54b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [ReversedCollection](../../reversedcollection.md) · [Index](../index.md)

# base

<sub>Instance Property</sub>

The position after this position in the underlying collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let base: Base.Index
```

## Discussion

To find the position that corresponds with this index in the original, underlying collection, use that collection’s `index(before:)` method with the `base` property.

The following example declares a function that returns the index of the last even number in the passed array, if one is found. First, the function finds the position of the last even number as a `ReversedIndex` in a reversed view of the array of numbers. Next, the function calls the array’s `index(before:)` method to return the correct position in the passed array.

```swift
func indexOfLastEven(_ numbers: [Int]) -> Int? {
    let reversedNumbers = numbers.reversed()
    guard let i = reversedNumbers.firstIndex(where: { $0 % 2 == 0 })
        else { return nil }

    return numbers.index(before: i.base)
}

let numbers = [10, 20, 13, 19, 30, 52, 17, 40, 51]
if let lastEven = indexOfLastEven(numbers) {
    print("Last even number: \(numbers[lastEven])")
}
// Prints "Last even number: 40"
```
