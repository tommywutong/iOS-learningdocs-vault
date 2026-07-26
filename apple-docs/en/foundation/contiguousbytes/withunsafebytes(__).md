---
title: 'withUnsafeBytes(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/contiguousbytes/withunsafebytes(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/contiguousbytes/withunsafebytes(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/contiguousbytes/withunsafebytes%28_%3A%29.json'
content_hash: 'sha256:3f944490527305a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ContiguousBytes](../contiguousbytes.md)

# withUnsafeBytes(_:)

<sub>Instance Method</sub>

Calls the given closure with a pointer to the underlying bytes of the type’s contiguous storage.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withUnsafeBytes<R>(_ body: (UnsafeRawBufferPointer) throws -> R) rethrows -> R
```

## Parameters

- `body` — A closure with an [UnsafeRawBufferPointer](../../swift/unsaferawbufferpointer.md) parameter that points to the contiguous storage for the type. If no such storage exists, the method creates it. If `body` has a return value, this method also returns that value. The argument is valid only for the duration of the closure’s execution.

## Return Value

The return value, if any, of the body closure parameter.

## Discussion

The following example copies the bytes from a string encoded using `utf8` into a buffer of `UInt8`:

```swift
let data = "Hello".data(using: .utf8)
var byteBuffer: [UInt8] = []
_ = data?.withUnsafeBytes { buffer in
    byteBuffer.append(contentsOf: buffer)
}

// byteBuffer = [72, 101, 108, 108, 111]
```
