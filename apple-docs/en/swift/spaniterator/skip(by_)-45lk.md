---
title: 'skip(by:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/spaniterator/skip(by:)-45lk'
source_url: 'https://developer.apple.com/documentation/swift/spaniterator/skip(by:)-45lk'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/spaniterator/skip%28by%3A%29-45lk.json'
content_hash: 'sha256:adfe6ef921b58bf4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SpanIterator](../spaniterator.md)

# skip(by:)

<sub>Instance Method</sub>

Advances the position of this iterator by the specified offset, or until the end of the underlying type’s elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func skip(by offset: Int) -> Int
```

## Return Value

The number of items that were skipped. If the returned count is less than `maximumOffset`, then the underlying type did not have enough elements left to skip the requested number of items. In that case, the iterator’s position is set to the end of the underlying type.
