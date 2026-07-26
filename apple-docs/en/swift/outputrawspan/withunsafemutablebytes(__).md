---
title: 'withUnsafeMutableBytes(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/outputrawspan/withunsafemutablebytes(_:)'
source_url: 'https://developer.apple.com/documentation/swift/outputrawspan/withunsafemutablebytes(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/outputrawspan/withunsafemutablebytes%28_%3A%29.json'
content_hash: 'sha256:072ebde81458f33c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [OutputRawSpan](../outputrawspan.md)

# withUnsafeMutableBytes(_:)

<sub>Instance Method</sub>

Call the given closure with the unsafe buffer pointer addressed by this OutputRawSpan and a mutable reference to its count of initialized bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func withUnsafeMutableBytes<E, R>(_ body: (UnsafeMutableRawBufferPointer, inout Int) throws(E) -> R) throws(E) -> R where E : Error, R : ~Copyable
```

## Parameters

- `body` — A closure that can read from and write to the buffer and update the initialized count.

## Return Value

The return value of the `body` closure.

## Discussion

This method provides a way to process or populate an `OutputRawSpan` using unsafe operations, such as dispatching to code written in legacy (memory-unsafe) languages.

The supplied closure may process the buffer in any way it wants; however, when it finishes (whether by returning or throwing), it must leave the buffer in a state that satisfies the invariants of the output span:

1. The inout integer passed in as the second argument must be the exact number of initialized bytes in the buffer passed in as the first argument.
2. These initialized bytes must be located in a single contiguous region starting at the beginning of the buffer. The rest of the buffer must hold uninitialized memory.

This function cannot verify these two invariants, and therefore this is an unsafe operation. Violating the invariants of `OutputRawSpan` may result in undefined behavior.
