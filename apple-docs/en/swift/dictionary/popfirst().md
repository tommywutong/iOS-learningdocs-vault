---
title: popFirst()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/dictionary/popfirst()
source_url: 'https://developer.apple.com/documentation/swift/dictionary/popfirst()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dictionary/popfirst%28%29.json'
content_hash: 'sha256:58f1017083fa2fd5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Dictionary](../dictionary.md)

# popFirst()

<sub>Instance Method</sub>

Removes and returns the first key-value pair of the dictionary if the dictionary isn’t empty.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func popFirst() -> Dictionary<Key, Value>.Element?
```

## Return Value

The first key-value pair of the dictionary if the dictionary is not empty; otherwise, `nil`.

## Discussion

The first element of the dictionary is not necessarily the first element added. Don’t expect any particular ordering of key-value pairs.

> [!abstract] Complexity
> Averages to O(1) over many calls to `popFirst()`.

## See Also

### Excluding Elements

- [dropFirst(_:)](<dropfirst(__).md>) — Returns a subsequence containing all but the given number of initial elements.
- [drop(while:)](<drop(while_).md>) — Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [dropLast(_:)](<droplast(__).md>) — Returns a subsequence containing all but the specified number of final elements.
