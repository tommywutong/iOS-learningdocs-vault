---
title: 'withUnsafeBufferPointer(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/array/withunsafebufferpointer(_:)'
source_url: 'https://developer.apple.com/documentation/swift/array/withunsafebufferpointer(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/withunsafebufferpointer%28_%3A%29.json'
content_hash: 'sha256:7dbe09198137b91f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# withUnsafeBufferPointer(_:)

<sub>Instance Method</sub>

Calls a closure with a pointer to the array’s contiguous storage.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withUnsafeBufferPointer<R, E>(_ body: (UnsafeBufferPointer<Element>) throws(E) -> R) throws(E) -> R where E : Error
```

## Parameters

- `body` — A closure with an `UnsafeBufferPointer` parameter that points to the contiguous storage for the array.  If no such storage exists, it is created. If `body` has a return value, that value is also used as the return value for the `withUnsafeBufferPointer(_:)` method. The pointer argument is valid only for the duration of the method’s execution.

## Return Value

The return value, if any, of the `body` closure parameter.

## Discussion

Often, the optimizer can eliminate bounds checks within an array algorithm, but when that fails, invoking the same algorithm on the buffer pointer passed into your closure lets you trade safety for speed.

The following example shows how you can iterate over the contents of the buffer pointer:

```swift
let numbers = [1, 2, 3, 4, 5]
let sum = numbers.withUnsafeBufferPointer { buffer -> Int in
    var result = 0
    for i in stride(from: buffer.startIndex, to: buffer.endIndex, by: 2) {
        result += buffer[i]
    }
    return result
}
// 'sum' == 9
```

The pointer passed as an argument to `body` is valid only during the execution of `withUnsafeBufferPointer(_:)`. Do not store or return the pointer for later use.

## See Also

### Accessing Underlying Storage

- [withUnsafeMutableBufferPointer(_:)](<withunsafemutablebufferpointer(__).md>) — Calls the given closure with a pointer to the array’s mutable contiguous storage.
- [withUnsafeBytes(_:)](<withunsafebytes(__).md>) — Calls the given closure with a pointer to the underlying bytes of the array’s contiguous storage.
- [withUnsafeMutableBytes(_:)](<withunsafemutablebytes(__).md>) — Calls the given closure with a pointer to the underlying bytes of the array’s mutable contiguous storage.
- [withContiguousStorageIfAvailable(_:)](<withcontiguousstorageifavailable(__).md>) — Executes a closure on the sequence’s contiguous storage.
- [withContiguousMutableStorageIfAvailable(_:)](<withcontiguousmutablestorageifavailable(__).md>) — Executes a closure on the collection’s contiguous storage.
