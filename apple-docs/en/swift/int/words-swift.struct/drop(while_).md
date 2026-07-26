---
title: 'drop(while:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/int/words-swift.struct/drop(while:)'
source_url: 'https://developer.apple.com/documentation/swift/int/words-swift.struct/drop(while:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int/words-swift.struct/drop%28while%3A%29.json'
content_hash: 'sha256:b4aa959c94652cbd'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Int](../../int.md) · [Words](../words-swift.struct.md)

# drop(while:)

<sub>Instance Method</sub>

Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func drop(while predicate: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence
```

## Parameters

- `predicate` — A closure that takes an element of the sequence as its argument and returns `true` if the element should be skipped or `false` if it should be included. Once the predicate returns `false` it will not be called again.

## Discussion

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the collection.
