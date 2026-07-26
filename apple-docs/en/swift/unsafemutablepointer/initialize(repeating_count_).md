---
title: 'initialize(repeating:count:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafemutablepointer/initialize(repeating:count:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablepointer/initialize(repeating:count:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablepointer/initialize%28repeating%3Acount%3A%29.json'
content_hash: 'sha256:fd1e0dcd188862b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutablePointer](../unsafemutablepointer.md)

# initialize(repeating:count:)

<sub>Instance Method</sub>

Initializes this pointer’s memory with the specified number of consecutive copies of the given value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func initialize(repeating repeatedValue: Pointee, count: Int)
```

## Parameters

- `repeatedValue` — The instance to initialize this pointer’s memory with.

- `count` — The number of consecutive copies of `newValue` to initialize. `count` must not be negative.

## Discussion

The destination memory must be uninitialized or the pointer’s `Pointee` must be a trivial type. After a call to `initialize(repeating:count:)`, the memory referenced by this pointer is initialized.
