---
title: 'initializeMemory(as:to:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafemutablerawpointer/initializememory(as:to:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablerawpointer/initializememory(as:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablerawpointer/initializememory%28as%3Ato%3A%29.json'
content_hash: 'sha256:7a5991913716c781'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutableRawPointer](../unsafemutablerawpointer.md)

# initializeMemory(as:to:)

<sub>Instance Method</sub>

Initializes the memory referenced by this pointer with the given value, binds the memory to the value’s type, and returns a typed pointer to the initialized memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult func initializeMemory<T>(as type: T.Type, to value: consuming T) -> UnsafeMutablePointer<T> where T : ~Copyable
```

## Parameters

- `type` — The type to which this memory will be bound.

- `value` — The value used to initialize this memory.

## Return Value

A typed pointer to the memory referenced by this raw pointer.

## Discussion

The memory referenced by this pointer must be uninitialized or initialized to a trivial type, and must be properly aligned for accessing `T`.

The following example allocates raw memory for one instance of `UInt`, and then uses the `initializeMemory(as:to:)` method to initialize the allocated memory.

```swift
let bytePointer = UnsafeMutableRawPointer.allocate(
        byteCount: MemoryLayout<UInt>.stride,
        alignment: MemoryLayout<UInt>.alignment)
let int8Pointer = bytePointer.initializeMemory(as: UInt.self, to: 0)

// After using 'int8Pointer':
int8Pointer.deallocate()
```

After calling this method on a raw pointer `p`, the region starting at `self` and continuing up to `p + MemoryLayout<T>.stride` is bound to type `T` and initialized. If `T` is a nontrivial type, you must eventually deinitialize the memory in this region to avoid memory leaks.
