---
title: 'bindMemory(to:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/slice/bindmemory(to:)-4ombl'
source_url: 'https://developer.apple.com/documentation/swift/slice/bindmemory(to:)-4ombl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/slice/bindmemory%28to%3A%29-4ombl.json'
content_hash: 'sha256:f651327f5a24a484'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Slice](../slice.md)

# bindMemory(to:)

<sub>Instance Method</sub>

Binds this buffer slice’s memory to the specified type and returns a typed buffer of the bound memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult func bindMemory<T>(to type: T.Type) -> UnsafeBufferPointer<T> where T : ~Copyable
```

## Parameters

- `type` — The type `T` to bind the memory to.

## Return Value

A typed buffer of the newly bound memory. The memory in this region is bound to `T`, but has not been modified in any other way. The typed buffer references `self.count / MemoryLayout<T>.stride` instances of `T`.

## Discussion

Use the `bindMemory(to:)` method to bind the memory referenced by this buffer slice to the type `T`. The memory must be uninitialized or initialized to a type that is layout compatible with `T`. If the memory is uninitialized, it is still uninitialized after being bound to `T`.

> [!warning] Warning
> A memory location may only be bound to one type at a time. The behavior of accessing memory as a type unrelated to its bound type is undefined.
