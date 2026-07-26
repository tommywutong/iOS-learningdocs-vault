---
title: next()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unsaferawbufferpointer/iterator/next()
source_url: 'https://developer.apple.com/documentation/swift/unsaferawbufferpointer/iterator/next()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsaferawbufferpointer/iterator/next%28%29.json'
content_hash: 'sha256:ef6841a49908f8de'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [UnsafeRawBufferPointer](../../unsaferawbufferpointer.md) · [Iterator](../iterator.md)

# next()

<sub>Instance Method</sub>

Advances to the next byte and returns it, or `nil` if no next byte exists.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func next() -> UInt8?
```

## Return Value

The next sequential byte in the raw buffer if another byte exists; otherwise, `nil`.

## Discussion

Once `nil` has been returned, all subsequent calls return `nil`.
