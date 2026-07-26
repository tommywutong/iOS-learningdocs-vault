---
title: 'update(repeating:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafemutablebufferpointer/update(repeating:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablebufferpointer/update(repeating:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablebufferpointer/update%28repeating%3A%29.json'
content_hash: 'sha256:c2c0021b62180eca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutableBufferPointer](../unsafemutablebufferpointer.md)

# update(repeating:)

<sub>Instance Method</sub>

Updates every element of this buffer’s initialized memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func update(repeating repeatedValue: Element)
```

## Parameters

- `repeatedValue` — The value used when updating this pointer’s memory.

## Discussion

The buffer’s memory must be initialized or its `Element` type must be a trivial type.

> [!note] Note
> All buffer elements must already be initialized.
