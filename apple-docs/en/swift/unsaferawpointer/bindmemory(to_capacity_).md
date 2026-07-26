---
title: 'bindMemory(to:capacity:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsaferawpointer/bindmemory(to:capacity:)'
source_url: 'https://developer.apple.com/documentation/swift/unsaferawpointer/bindmemory(to:capacity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsaferawpointer/bindmemory%28to%3Acapacity%3A%29.json'
content_hash: 'sha256:62f8eb489cb9df2e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeRawPointer](../unsaferawpointer.md)

# bindMemory(to:capacity:)

<sub>Instance Method</sub>

Binds the memory to the specified type and returns a typed pointer to the bound memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult func bindMemory<T>(to type: T.Type, capacity count: Int) -> UnsafePointer<T> where T : ~Copyable
```

## Parameters

- `type` — The type `T` to bind the memory to.

- `count` — The amount of memory to bind to type `T`, counted as instances of `T`.

## Return Value

A typed pointer to the newly bound memory. The memory in this region is bound to `T`, but has not been modified in any other way. The number of bytes in this region is `count * MemoryLayout<T>.stride`.

## Discussion

Use the `bindMemory(to:capacity:)` method to bind the memory referenced by this pointer to the type `T`. The memory must be uninitialized or initialized to a type that is layout compatible with `T`. If the memory is uninitialized, it is still uninitialized after being bound to `T`.

In this example, 100 bytes of raw memory are allocated for the pointer `bytesPointer`, and then the first four bytes are bound to the `Int8` type.

```swift
let count = 4
let bytesPointer = UnsafeMutableRawPointer.allocate(
        byteCount: 100,
        alignment: MemoryLayout<Int8>.alignment)
let int8Pointer = bytesPointer.bindMemory(to: Int8.self, capacity: count)
```

After calling `bindMemory(to:capacity:)`, the first four bytes of the memory referenced by `bytesPointer` are bound to the `Int8` type, though they remain uninitialized. The remainder of the allocated region is unbound raw memory. All 100 bytes of memory must eventually be deallocated.

> [!warning] Warning
> A memory location may only be bound to one type at a time. The behavior of accessing memory as a type unrelated to its bound type is undefined.
