---
title: 'index(before:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/inlinearray/index(before:)'
source_url: 'https://developer.apple.com/documentation/swift/inlinearray/index(before:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/inlinearray/index%28before%3A%29.json'
content_hash: 'sha256:77c5604680147637'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [InlineArray](../inlinearray.md)

# index(before:)

<sub>Instance Method</sub>

Returns the position immediately before the given index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
borrowing func index(before i: InlineArray<count, Element>.Index) -> InlineArray<count, Element>.Index
```

## Parameters

- `i` — A valid index of the array. `i` must be greater than `startIndex`.

## Return Value

The index value immediately before `i`.

## Discussion

> [!abstract] Complexity
> O(1)
