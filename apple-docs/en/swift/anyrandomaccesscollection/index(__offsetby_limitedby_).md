---
title: 'index(_:offsetBy:limitedBy:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/anyrandomaccesscollection/index(_:offsetby:limitedby:)'
source_url: 'https://developer.apple.com/documentation/swift/anyrandomaccesscollection/index(_:offsetby:limitedby:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anyrandomaccesscollection/index%28_%3Aoffsetby%3Alimitedby%3A%29.json'
content_hash: 'sha256:a67c4907b6712b47'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AnyRandomAccessCollection](../anyrandomaccesscollection.md)

# index(_:offsetBy:limitedBy:)

<sub>Instance Method</sub>

Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func index(_ i: AnyRandomAccessCollection<Element>.Index, offsetBy n: Int, limitedBy limit: AnyRandomAccessCollection<Element>.Index) -> AnyRandomAccessCollection<Element>.Index?
```

## Parameters

- `i` — A valid index of the collection.

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
> O(1)
