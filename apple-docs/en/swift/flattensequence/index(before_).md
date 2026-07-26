---
title: 'index(before:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/flattensequence/index(before:)'
source_url: 'https://developer.apple.com/documentation/swift/flattensequence/index(before:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/flattensequence/index%28before%3A%29.json'
content_hash: 'sha256:06ce5cf760303a3d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FlattenSequence](../flattensequence.md)

# index(before:)

<sub>Instance Method</sub>

Returns the position immediately before the given index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func index(before i: FlattenSequence<Base>.Index) -> FlattenSequence<Base>.Index
```

## Parameters

- `i` — A valid index of the collection. `i` must be greater than `startIndex`.

## Return Value

The index value immediately before `i`.
