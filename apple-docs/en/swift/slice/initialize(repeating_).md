---
title: 'initialize(repeating:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/slice/initialize(repeating:)'
source_url: 'https://developer.apple.com/documentation/swift/slice/initialize(repeating:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/slice/initialize%28repeating%3A%29.json'
content_hash: 'sha256:2aad88e642215cde'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Slice](../slice.md)

# initialize(repeating:)

<sub>Instance Method</sub>

Initializes every element in this buffer slice’s memory to a copy of the given value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func initialize<Element>(repeating repeatedValue: Element) where Base == UnsafeMutableBufferPointer<Element>
```

## Parameters

- `repeatedValue` — The value with which to initialize this buffer slice’s memory.

## Discussion

The destination memory must be uninitialized or the buffer’s `Element` must be a trivial type. After a call to `initialize(repeating:)`, the entire region of memory referenced by this buffer slice is initialized.
