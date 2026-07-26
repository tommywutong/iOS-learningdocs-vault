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
doc_path: '/documentation/swift/string/index(_:offsetby:limitedby:)'
source_url: 'https://developer.apple.com/documentation/swift/string/index(_:offsetby:limitedby:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/index%28_%3Aoffsetby%3Alimitedby%3A%29.json'
content_hash: 'sha256:b50b2b5b4306adfb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# index(_:offsetBy:limitedBy:)

<sub>Instance Method</sub>

Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func index(_ i: String.Index, offsetBy distance: Int, limitedBy limit: String.Index) -> String.Index?
```

## Parameters

- `i` — A valid index of the collection.

- `distance` — The distance to offset `i`.

- `limit` — A valid index of the collection to use as a limit. If `distance > 0`, a limit that is less than `i` has no effect. Likewise, if `distance < 0`, a limit that is greater than `i` has no effect.

## Return Value

An index offset by `distance` from the index `i`, unless that index would be beyond `limit` in the direction of movement. In that case, the method returns `nil`.

## Discussion

The following example obtains an index advanced four positions from a string’s starting index and then prints the character at that position. The operation doesn’t require going beyond the limiting `s.endIndex` value, so it succeeds.

```swift
let s = "Swift"
if let i = s.index(s.startIndex, offsetBy: 4, limitedBy: s.endIndex) {
    print(s[i])
}
// Prints "t"
```

The next example attempts to retrieve an index six positions from `s.startIndex` but fails, because that distance is beyond the index passed as `limit`.

```swift
let j = s.index(s.startIndex, offsetBy: 6, limitedBy: s.endIndex)
print(j)
// Prints "nil"
```

The value passed as `distance` must not offset `i` beyond the bounds of the collection, unless the index passed as `limit` prevents offsetting beyond those bounds.

> [!abstract] Complexity
> O(_n_), where _n_ is the absolute value of `distance`.

## See Also

### Manipulating Indices

- [startIndex](startindex.md) — The position of the first character in a nonempty string.
- [endIndex](endindex.md) — A string’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [index(after:)](<index(after_).md>) — Returns the position immediately after the given index.
- [formIndex(after:)](<formindex(after_).md>) — Replaces the given index with its successor.
- [index(before:)](<index(before_).md>) — Returns the position immediately before the given index.
- [formIndex(before:)](<formindex(before_).md>) — Replaces the given index with its predecessor.
- [index(_:offsetBy:)](<index(__offsetby_).md>) — Returns an index that is the specified distance from the given index.
- [formIndex(_:offsetBy:)](<formindex(__offsetby_).md>) — Offsets the given index by the specified distance.
- [formIndex(_:offsetBy:limitedBy:)](<formindex(__offsetby_limitedby_).md>) — Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [distance(from:to:)](<distance(from_to_).md>) — Returns the distance between two indices.
- [indices](indices-swift.property.md) — The indices that are valid for subscripting the collection, in ascending order.
