---
title: 'formIndex(after:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/lazyfiltersequence/formindex(after:)-8eya1'
source_url: 'https://developer.apple.com/documentation/swift/lazyfiltersequence/formindex(after:)-8eya1'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazyfiltersequence/formindex%28after%3A%29-8eya1.json'
content_hash: 'sha256:0a168f9cf15fe58a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [LazyFilterSequence](../lazyfiltersequence.md)

# formIndex(after:)

<sub>Instance Method</sub>

Replaces the given index with its successor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func formIndex(after i: inout Self.Index)
```

## Parameters

- `i` — A valid index of the collection. `i` must be less than `endIndex`.
