---
title: move()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unsafemutablepointer/move()
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablepointer/move()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablepointer/move%28%29.json'
content_hash: 'sha256:96d801a58bb6399c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutablePointer](../unsafemutablepointer.md)

# move()

<sub>Instance Method</sub>

Retrieves and returns the referenced instance, returning the pointer’s memory to an uninitialized state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func move() -> Pointee
```

## Return Value

The instance referenced by this pointer.

## Discussion

Calling the `move()` method on a pointer `p` that references memory of type `T` is equivalent to the following code, aside from any cost and incidental side effects of copying and destroying the value:

```swift
let value: T = {
    defer { p.deinitialize(count: 1) }
    return p.pointee
}()
```

The memory referenced by this pointer must be initialized. After calling `move()`, the memory is uninitialized.
