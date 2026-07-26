---
title: 'joined(separator:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/sequence/joined(separator:)-5zjyj'
source_url: 'https://developer.apple.com/documentation/swift/sequence/joined(separator:)-5zjyj'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/sequence/joined%28separator%3A%29-5zjyj.json'
content_hash: 'sha256:6fce566c696c5a22'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Sequence](../sequence.md)

# joined(separator:)

<sub>Instance Method</sub>

Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func joined(separator: String = "") -> String
```

## Parameters

- `separator` — A string to insert between each of the elements in this sequence. The default separator is an empty string.

## Return Value

A single, concatenated string.

## Discussion

The following example shows how an array of strings can be joined to a single, comma-separated string:

```swift
let cast = ["Vivien", "Marlon", "Kim", "Karl"]
let list = cast.joined(separator: ", ")
print(list)
// Prints "Vivien, Marlon, Kim, Karl"
```

## See Also

### Splitting and Joining Elements

- [split(maxSplits:omittingEmptySubsequences:whereSeparator:)](<split(maxsplits_omittingemptysubsequences_whereseparator_).md>) — Returns the longest possible subsequences of the sequence, in order, that don’t contain elements satisfying the given predicate. Elements that are used to split the sequence are not returned as part of any subsequence.
- [split(separator:maxSplits:omittingEmptySubsequences:)](<split(separator_maxsplits_omittingemptysubsequences_).md>) — Returns the longest possible subsequences of the sequence, in order, around elements equal to the given element.
- [joined()](<joined().md>) — Returns the elements of this sequence of sequences, concatenated.
- [joined(separator:)](<joined(separator_)-7w47r.md>) — Returns the concatenated elements of this sequence of sequences, inserting the given separator between each element.
