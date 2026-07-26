---
title: 'index(_:offsetBy:limitedBy:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/array/index(_:offsetby:limitedby:)'
source_url: 'https://developer.apple.com/documentation/swift/array/index(_:offsetby:limitedby:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/index%28_%3Aoffsetby%3Alimitedby%3A%29.json'
content_hash: 'sha256:dd914ee3d89f21e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# index(_:offsetBy:limitedBy:)

<sub>Instance Method</sub>

Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func index(_ i: Int, offsetBy distance: Int, limitedBy limit: Int) -> Int?
```

## Parameters

- `i` — A valid index of the array.

- `distance` — The distance to offset `i`.

- `limit` — A valid index of the collection to use as a limit. If `distance > 0`, `limit` has no effect if it is less than `i`. Likewise, if `distance < 0`, `limit` has no effect if it is greater than `i`.

## Return Value

An index offset by `distance` from the index `i`, unless that index would be beyond `limit` in the direction of movement. In that case, the method returns `nil`.

## Discussion

The following example obtains an index advanced four positions from an array’s starting index and then prints the element at that position. The operation doesn’t require going beyond the limiting `numbers.endIndex` value, so it succeeds.

```swift
let numbers = [10, 20, 30, 40, 50]
if let i = numbers.index(numbers.startIndex,
                         offsetBy: 4,
                         limitedBy: numbers.endIndex) {
    print(numbers[i])
}
// Prints "50"
```

The next example attempts to retrieve an index ten positions from `numbers.startIndex`, but fails, because that distance is beyond the index passed as `limit`.

```swift
let j = numbers.index(numbers.startIndex,
                      offsetBy: 10,
                      limitedBy: numbers.endIndex)
print(j)
// Prints "nil"
```

The value passed as `distance` must not offset `i` beyond the bounds of the collection, unless the index passed as `limit` prevents offsetting beyond those bounds.

> [!abstract] Complexity
> O(1)

## See Also

### Manipulating Indices

- [startIndex](startindex.md) — The position of the first element in a nonempty array.
- [endIndex](endindex.md) — The array’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [index(after:)](<index(after_).md>) — Returns the position immediately after the given index.
- [formIndex(after:)](<formindex(after_).md>) — Replaces the given index with its successor.
- [index(before:)](<index(before_).md>) — Returns the position immediately before the given index.
- [formIndex(before:)](<formindex(before_).md>) — Replaces the given index with its predecessor.
- [index(_:offsetBy:)](<index(__offsetby_).md>) — Returns an index that is the specified distance from the given index.
- [formIndex(_:offsetBy:)](<formindex(__offsetby_).md>) — Offsets the given index by the specified distance.
- [formIndex(_:offsetBy:limitedBy:)](<formindex(__offsetby_limitedby_).md>) — Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [distance(from:to:)](<distance(from_to_).md>) — Returns the distance between two indices.
