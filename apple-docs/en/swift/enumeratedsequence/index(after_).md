---
title: 'index(after:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/enumeratedsequence/index(after:)'
source_url: 'https://developer.apple.com/documentation/swift/enumeratedsequence/index(after:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/enumeratedsequence/index%28after%3A%29.json'
content_hash: 'sha256:94fd0886d666fedd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [EnumeratedSequence](../enumeratedsequence.md)

# index(after:)

<sub>Instance Method</sub>

Returns the position immediately after the given index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func index(after index: EnumeratedSequence<Base>.Index) -> EnumeratedSequence<Base>.Index
```

## Return Value

The index value immediately after `i`.

## Discussion

The successor of an index must be well defined. For an index `i` into a collection `c`, calling `c.index(after: i)` returns the same index every time.
