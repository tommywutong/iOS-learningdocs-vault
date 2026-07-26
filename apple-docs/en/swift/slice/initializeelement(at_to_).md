---
title: 'initializeElement(at:to:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/slice/initializeelement(at:to:)'
source_url: 'https://developer.apple.com/documentation/swift/slice/initializeelement(at:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/slice/initializeelement%28at%3Ato%3A%29.json'
content_hash: 'sha256:60fa6d3784c82e1c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Slice](../slice.md)

# initializeElement(at:to:)

<sub>Instance Method</sub>

Initializes the element at `index` to the given value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func initializeElement<Element>(at index: Int, to value: Element) where Base == UnsafeMutableBufferPointer<Element>
```

## Parameters

- `index` — The index of the element to initialize

- `value` — The value used to initialize the buffer element’s memory.

## Discussion

The memory underlying the destination element must be uninitialized, or `Element` must be a trivial type. After a call to `initialize(to:)`, the memory underlying this element of the buffer slice is initialized.
