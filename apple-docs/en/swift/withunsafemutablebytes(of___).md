---
title: 'withUnsafeMutableBytes(of:_:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/withunsafemutablebytes(of:_:)'
source_url: 'https://developer.apple.com/documentation/swift/withunsafemutablebytes(of:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/withunsafemutablebytes%28of%3A_%3A%29.json'
content_hash: 'sha256:db26731091f53c9a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# withUnsafeMutableBytes(of:_:)

<sub>Function</sub>

Invokes the given closure with a mutable buffer pointer covering the raw bytes of the given argument.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withUnsafeMutableBytes<T, E, Result>(of value: inout T, _ body: (UnsafeMutableRawBufferPointer) throws(E) -> Result) throws(E) -> Result where E : Error, T : ~Copyable, T : ~Escapable, Result : ~Copyable
```

## Parameters

- `value` — An instance to temporarily access through a mutable raw buffer pointer. Note that the `inout` exclusivity rules mean that, like any other `inout` argument, `value` cannot be directly accessed by other code for the duration of `body`. Access must only occur through the pointer argument to `body` until `body` returns.

- `body` — A closure that takes a raw buffer pointer to the bytes of `value` as its sole argument. If the closure has a return value, that value is also used as the return value of the `withUnsafeMutableBytes(of:_:)` function. The buffer pointer argument is valid only for the duration of the closure’s execution.

## Return Value

The return value, if any, of the `body` closure.

## Discussion

The buffer pointer argument to the `body` closure provides a collection interface to the raw bytes of `value`. The buffer is the size of the instance passed as `value` and does not include any remote storage.

## See Also

### Pointers to Values

- [withUnsafePointer(to:_:)](<withunsafepointer(to___)-9fjn6.md>) — Invokes the given closure with a pointer to the given argument.
- [withUnsafePointer(to:_:)](<withunsafepointer(to___)-35wrn.md>) — Invokes the given closure with a pointer to the given argument.
- [withUnsafeMutablePointer(to:_:)](<withunsafemutablepointer(to___).md>) — Calls the given closure with a mutable pointer to the given argument.
- [withUnsafeBytes(of:_:)](<withunsafebytes(of___)-3ywhh.md>) — Invokes the given closure with a buffer pointer covering the raw bytes of the given argument.
- [withUnsafeBytes(of:_:)](<withunsafebytes(of___)-5gesg.md>) — Invokes the given closure with a buffer pointer covering the raw bytes of the given argument.
