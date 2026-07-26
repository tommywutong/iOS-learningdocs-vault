---
title: 'moveElement(from:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/slice/moveelement(from:)'
source_url: 'https://developer.apple.com/documentation/swift/slice/moveelement(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/slice/moveelement%28from%3A%29.json'
content_hash: 'sha256:d9953054cd6c9315'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Slice](../slice.md)

# moveElement(from:)

<sub>Instance Method</sub>

Retrieves and returns the element at `index`, leaving that element’s underlying memory uninitialized.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func moveElement<Element>(from index: Slice<Base>.Index) -> Element where Base == UnsafeMutableBufferPointer<Element>
```

## Parameters

- `index` — The index of the buffer element to retrieve and deinitialize.

## Return Value

The instance referenced by this index in this buffer.

## Discussion

The memory underlying the element at `index` must be initialized. After calling `moveElement(from:)`, the memory underlying this element of the buffer slice is uninitialized, and still bound to type `Element`.
