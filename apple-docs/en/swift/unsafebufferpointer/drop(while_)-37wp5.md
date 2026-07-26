---
title: 'drop(while:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafebufferpointer/drop(while:)-37wp5'
source_url: 'https://developer.apple.com/documentation/swift/unsafebufferpointer/drop(while:)-37wp5'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafebufferpointer/drop%28while%3A%29-37wp5.json'
content_hash: 'sha256:1ac78a6bf5bfa75d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeBufferPointer](../unsafebufferpointer.md)

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
