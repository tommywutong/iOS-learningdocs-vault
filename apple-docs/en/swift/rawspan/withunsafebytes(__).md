---
title: 'withUnsafeBytes(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/rawspan/withunsafebytes(_:)'
source_url: 'https://developer.apple.com/documentation/swift/rawspan/withunsafebytes(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rawspan/withunsafebytes%28_%3A%29.json'
content_hash: 'sha256:ecd4ae486f56a73d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RawSpan](../rawspan.md)

# withUnsafeBytes(_:)

<sub>Instance Method</sub>

Calls the given closure with a pointer to the underlying bytes of the viewed contiguous storage.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withUnsafeBytes<E, Result>(_ body: (UnsafeRawBufferPointer) throws(E) -> Result) throws(E) -> Result where E : Error, Result : ~Copyable
```

## Parameters

- `body` — A closure with an `UnsafeRawBufferPointer` parameter that points to the viewed contiguous storage. If `body` has a return value, that value is also used as the return value for the `withUnsafeBytes(_:)` method. The closure’s parameter is valid only for the duration of its execution.

## Return Value

The return value of the `body` closure parameter.

## Discussion

The buffer pointer passed as an argument to `body` is valid only during the execution of `withUnsafeBytes(_:)`. Do not store or return the pointer for later use.
