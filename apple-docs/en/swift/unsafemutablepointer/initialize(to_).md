---
title: 'initialize(to:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafemutablepointer/initialize(to:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablepointer/initialize(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablepointer/initialize%28to%3A%29.json'
content_hash: 'sha256:108eb0444222c9a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutablePointer](../unsafemutablepointer.md)

# initialize(to:)

<sub>Instance Method</sub>

Initializes this pointer’s memory with a single instance of the given value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func initialize(to value: consuming Pointee)
```

## Parameters

- `value` — The instance to initialize this pointer’s pointee to.

## Discussion

The destination memory must be uninitialized or the pointer’s `Pointee` must be a trivial type. After a call to `initialize(to:)`, the memory referenced by this pointer is initialized. Calling this method is roughly equivalent to calling `initialize(repeating:count:)` with a `count` of 1.
