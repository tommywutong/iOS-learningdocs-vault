---
title: AnyRegexOutput.Iterator
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/anyregexoutput/iterator
source_url: 'https://developer.apple.com/documentation/swift/anyregexoutput/iterator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anyregexoutput/iterator.json'
content_hash: 'sha256:1487caaf57c5fe94'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AnyRegexOutput](../anyregexoutput.md)

# AnyRegexOutput.Iterator

<sub>Type Alias</sub>

A type that provides the collection’s iteration interface and encapsulates its iteration state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Iterator = IndexingIterator<AnyRegexOutput>
```

## Discussion

By default, a collection conforms to the `Sequence` protocol by supplying `IndexingIterator` as its associated `Iterator` type.
