---
title: 'withUTF8Buffer(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/staticstring/withutf8buffer(_:)'
source_url: 'https://developer.apple.com/documentation/swift/staticstring/withutf8buffer(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/staticstring/withutf8buffer%28_%3A%29.json'
content_hash: 'sha256:ecc0ff1b255f3bfb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [StaticString](../staticstring.md)

# withUTF8Buffer(_:)

<sub>Instance Method</sub>

Invokes the given closure with a buffer containing the static string’s UTF-8 code unit sequence (excluding the null terminator).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withUTF8Buffer<R>(_ body: (UnsafeBufferPointer<UInt8>) -> R) -> R
```

## Parameters

- `body` — A closure that takes a buffer pointer to the static string’s UTF-8 code unit sequence as its sole argument. If the closure has a return value, that value is also used as the return value of the `withUTF8Buffer(_:)` method. The pointer argument is valid only for the duration of the method’s execution.

## Return Value

The return value, if any, of the `body` closure.

## Discussion

This method works regardless of whether the static string stores a pointer or a single Unicode scalar value.

The pointer argument to `body` is valid only during the execution of `withUTF8Buffer(_:)`. Do not store or return the pointer for later use.
