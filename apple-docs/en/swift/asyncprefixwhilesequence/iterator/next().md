---
title: next()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncprefixwhilesequence/iterator/next()
source_url: 'https://developer.apple.com/documentation/swift/asyncprefixwhilesequence/iterator/next()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncprefixwhilesequence/iterator/next%28%29.json'
content_hash: 'sha256:48d28b398e5375a7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [AsyncPrefixWhileSequence](../../asyncprefixwhilesequence.md) · [Iterator](../iterator.md)

# next()

<sub>Instance Method</sub>

Produces the next element in the prefix-while sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func next() async rethrows -> Base.Element?
```

## Discussion

If the predicate hasn’t yet failed, this method gets the next element from the base sequence and calls the predicate with it. If this call succeeds, this method passes along the element. Otherwise, it returns `nil`, ending the sequence.
