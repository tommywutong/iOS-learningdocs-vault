---
title: 'extracting(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafebufferpointer/extracting(_:)-4bn8q'
source_url: 'https://developer.apple.com/documentation/swift/unsafebufferpointer/extracting(_:)-4bn8q'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafebufferpointer/extracting%28_%3A%29-4bn8q.json'
content_hash: 'sha256:dedc028980f14fb9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeBufferPointer](../unsafebufferpointer.md)

# extracting(_:)

<sub>Instance Method</sub>

Extracts and returns a copy of the entire buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func extracting(_ bounds: UnboundedRange) -> UnsafeBufferPointer<Element>
```

## Return Value

The same buffer as `self`.

## Discussion

When `Element` is copyable, the `extracting` operation is equivalent to slicing the buffer then rebasing the resulting buffer slice:

```swift
let a = buffer
let b = buffer.extracting(...)
let c = UnsafeBufferPointer(rebasing: buffer[...])
// `a`, `b` and `c` are now all referring to the same buffer
```

Note that unlike slicing, the `extracting` operation remains available even if `Element` happens to be noncopyable.
