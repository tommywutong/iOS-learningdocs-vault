---
title: 'formIndex(after:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/uniquearray/formindex(after:)'
source_url: 'https://developer.apple.com/documentation/swift/uniquearray/formindex(after:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uniquearray/formindex%28after%3A%29.json'
content_hash: 'sha256:7c750fa27c02f32d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UniqueArray](../uniquearray.md)

# formIndex(after:)

<sub>Instance Method</sub>

Replaces the given index with its successor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func formIndex(after index: inout Int)
```

## Parameters

- `index` — A valid index of the array. `i` must be less than `endIndex`.

## Discussion

> [!note] Note
> To improve performance, this method does not validate that the given index is valid before incrementing it. Index validation is deferred until the resulting index is used to access an element. This optimization may be removed in future versions; do not rely on it.

> [!abstract] Complexity
> O(1)
