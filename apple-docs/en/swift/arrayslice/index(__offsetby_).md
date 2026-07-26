---
title: 'index(_:offsetBy:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/arrayslice/index(_:offsetby:)'
source_url: 'https://developer.apple.com/documentation/swift/arrayslice/index(_:offsetby:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/arrayslice/index%28_%3Aoffsetby%3A%29.json'
content_hash: 'sha256:0cb0fe7f5daf45e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ArraySlice](../arrayslice.md)

# index(_:offsetBy:)

<sub>Instance Method</sub>

Returns an index that is the specified distance from the given index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func index(_ i: Int, offsetBy distance: Int) -> Int
```

## Parameters

- `i` — A valid index of the array.

- `distance` — The distance to offset `i`.

## Return Value

An index offset by `distance` from the index `i`. If `distance` is positive, this is the same value as the result of `distance` calls to `index(after:)`. If `distance` is negative, this is the same value as the result of `abs(distance)` calls to `index(before:)`.

## Discussion

The following example obtains an index advanced four positions from an array’s starting index and then prints the element at that position.

```swift
let numbers = [10, 20, 30, 40, 50]
let i = numbers.index(numbers.startIndex, offsetBy: 4)
print(numbers[i])
// Prints "50"
```

The value passed as `distance` must not offset `i` beyond the bounds of the collection.
