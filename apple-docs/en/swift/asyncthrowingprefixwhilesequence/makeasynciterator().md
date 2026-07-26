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
doc_path: /documentation/swift/asyncthrowingprefixwhilesequence/makeasynciterator()
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingprefixwhilesequence/makeasynciterator()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingprefixwhilesequence/makeasynciterator%28%29.json'
content_hash: 'sha256:38b688e6667381ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncThrowingPrefixWhileSequence](../asyncthrowingprefixwhilesequence.md)

# makeAsyncIterator()

<sub>Instance Method</sub>

Creates the asynchronous iterator that produces elements of this asynchronous sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func makeAsyncIterator() -> AsyncThrowingPrefixWhileSequence<Base>.Iterator
```

## Return Value

An instance of the `AsyncIterator` type used to produce elements of the asynchronous sequence.
