---
title: 'withUnsafeMutablePointer(to:_:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/withunsafemutablepointer(to:_:)'
source_url: 'https://developer.apple.com/documentation/swift/withunsafemutablepointer(to:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/withunsafemutablepointer%28to%3A_%3A%29.json'
content_hash: 'sha256:f3a520f0631eb38b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# withUnsafeMutablePointer(to:_:)

<sub>Function</sub>

Calls the given closure with a mutable pointer to the given argument.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withUnsafeMutablePointer<T, E, Result>(to value: inout T, _ body: (UnsafeMutablePointer<T>) throws(E) -> Result) throws(E) -> Result where E : Error, T : ~Copyable, Result : ~Copyable
```

## Parameters

- `value` — An instance to temporarily use via pointer. Note that the `inout` exclusivity rules mean that, like any other `inout` argument, `value` cannot be directly accessed by other code for the duration of `body`. Access must only occur through the pointer argument to `body` until `body` returns.

- `body` — A closure that takes a mutable pointer to `value` as its sole argument. If the closure has a return value, that value is also used as the return value of the `withUnsafeMutablePointer(to:_:)` function. The pointer argument is valid only for the duration of the function’s execution.

## Return Value

The return value, if any, of the `body` closure.

## Discussion

The `withUnsafeMutablePointer(to:_:)` function is useful for calling Objective-C APIs that take in/out parameters (and default-constructible out parameters) by pointer.

The pointer argument to `body` is valid only during the execution of `withUnsafeMutablePointer(to:_:)`. Do not store or return the pointer for later use.

## See Also

### Pointers to Values

- [withUnsafePointer(to:_:)](<withunsafepointer(to___)-9fjn6.md>) — Invokes the given closure with a pointer to the given argument.
- [withUnsafePointer(to:_:)](<withunsafepointer(to___)-35wrn.md>) — Invokes the given closure with a pointer to the given argument.
- [withUnsafeBytes(of:_:)](<withunsafebytes(of___)-3ywhh.md>) — Invokes the given closure with a buffer pointer covering the raw bytes of the given argument.
- [withUnsafeBytes(of:_:)](<withunsafebytes(of___)-5gesg.md>) — Invokes the given closure with a buffer pointer covering the raw bytes of the given argument.
- [withUnsafeMutableBytes(of:_:)](<withunsafemutablebytes(of___).md>) — Invokes the given closure with a mutable buffer pointer covering the raw bytes of the given argument.
