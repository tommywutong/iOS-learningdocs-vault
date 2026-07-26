---
title: popFirst()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/set/popfirst()
source_url: 'https://developer.apple.com/documentation/swift/set/popfirst()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/set/popfirst%28%29.json'
content_hash: 'sha256:097fd93752ec18b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Set](../set.md)

# popFirst()

<sub>Instance Method</sub>

Removes and returns the first element of the set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func popFirst() -> Element?
```

## Return Value

A member of the set. If the set is empty, returns `nil`.

## Discussion

Because a set is not an ordered collection, the “first” element may not be the first element that was added to the set.

## See Also

### Excluding Elements

- [drop(while:)](<drop(while_).md>) — Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [dropFirst(_:)](<dropfirst(__).md>) — Returns a subsequence containing all but the given number of initial elements.
- [dropLast(_:)](<droplast(__).md>) — Returns a subsequence containing all but the specified number of final elements.
