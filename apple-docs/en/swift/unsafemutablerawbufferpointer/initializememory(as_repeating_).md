---
title: 'initializeMemory(as:repeating:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafemutablerawbufferpointer/initializememory(as:repeating:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablerawbufferpointer/initializememory(as:repeating:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablerawbufferpointer/initializememory%28as%3Arepeating%3A%29.json'
content_hash: 'sha256:59bd6d2bf6637858'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutableRawBufferPointer](../unsafemutablerawbufferpointer.md)

# initializeMemory(as:repeating:)

<sub>Instance Method</sub>

Initializes the memory referenced by this buffer with the given value, binds the memory to the value’s type, and returns a typed buffer of the initialized memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult func initializeMemory<T>(as type: T.Type, repeating repeatedValue: T) -> UnsafeMutableBufferPointer<T>
```

## Parameters

- `type` — The type to bind this buffer’s memory to.

- `repeatedValue` — The instance to copy into memory.

## Return Value

A typed buffer of the memory referenced by this raw buffer. The typed buffer contains `self.count / MemoryLayout<T>.stride` instances of `T`.

## Discussion

The memory referenced by this buffer must be uninitialized or initialized to a trivial type, and must be properly aligned for accessing `T`.

After calling this method on a raw buffer with non-nil `baseAddress` `b`, the region starting at `b` and continuing up to `b + self.count - self.count % MemoryLayout<T>.stride` is bound to type `T` and is initialized. If `T` is a nontrivial type, you must eventually deinitialize or move the values in this region to avoid leaks. If `baseAddress` is `nil`, this function does nothing and returns an empty buffer pointer.
