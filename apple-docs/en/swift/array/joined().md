---
title: joined()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/array/joined()
source_url: 'https://developer.apple.com/documentation/swift/array/joined()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/joined%28%29.json'
content_hash: 'sha256:20978f3d24ba384c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# joined()

<sub>Instance Method</sub>

Returns the elements of this sequence of sequences, concatenated.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func joined() -> FlattenSequence<Self>
```

## Return Value

A flattened view of the elements of this sequence of sequences.

## Discussion

In this example, an array of three ranges is flattened so that the elements of each range can be iterated in turn.

```swift
let ranges = [0..<3, 8..<10, 15..<17]

// A for-in loop over 'ranges' accesses each range:
for range in ranges {
  print(range)
}
// Prints "0..<3"
// Prints "8..<10"
// Prints "15..<17"

// Use 'joined()' to access each element of each range:
for index in ranges.joined() {
    print(index, terminator: " ")
}
// Prints: "0 1 2 8 9 15 16"
```

## See Also

### Splitting and Joining Elements

- [split(separator:maxSplits:omittingEmptySubsequences:)](<split(separator_maxsplits_omittingemptysubsequences_)-3dgmv.md>) — Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [split(maxSplits:omittingEmptySubsequences:whereSeparator:)](<split(maxsplits_omittingemptysubsequences_whereseparator_).md>) — Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [joined(separator:)](<joined(separator_)-7uber.md>) — Returns the concatenated elements of this sequence of sequences, inserting the given separator between each element.
- [joined(separator:)](<joined(separator_)-5do1g.md>) — Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.
- [joined(separator:)](<joined(separator_)-1ckod.md>) — Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.
