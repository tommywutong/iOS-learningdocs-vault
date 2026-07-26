---
title: makeAsyncIterator()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncprefixsequence/makeasynciterator()
source_url: 'https://developer.apple.com/documentation/swift/asyncprefixsequence/makeasynciterator()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncprefixsequence/makeasynciterator%28%29.json'
content_hash: 'sha256:7c27cd2f942b88a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncPrefixSequence](../asyncprefixsequence.md)

# makeAsyncIterator()

<sub>Instance Method</sub>

Creates the asynchronous iterator that produces elements of this asynchronous sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func makeAsyncIterator() -> AsyncPrefixSequence<Base>.Iterator
```

## Return Value

An instance of the `AsyncIterator` type used to produce elements of the asynchronous sequence.
