---
title: 'withUnsafePointer(to:_:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/withunsafepointer(to:_:)-35wrn'
source_url: 'https://developer.apple.com/documentation/swift/withunsafepointer(to:_:)-35wrn'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/withunsafepointer%28to%3A_%3A%29-35wrn.json'
content_hash: 'sha256:cf426c158316165e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# withUnsafePointer(to:_:)

<sub>Function</sub>

Invokes the given closure with a pointer to the given argument.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withUnsafePointer<T, E, Result>(to value: borrowing T, _ body: (UnsafePointer<T>) throws(E) -> Result) throws(E) -> Result where E : Error, T : ~Copyable, Result : ~Copyable
```

## Parameters

- `value` — An instance to temporarily use via pointer.

- `body` — A closure that takes a pointer to `value` as its sole argument. If the closure has a return value, that value is also used as the return value of the `withUnsafePointer(to:_:)` function. The pointer argument is valid only for the duration of the function’s execution. It is undefined behavior to try to mutate through the pointer argument by converting it to `UnsafeMutablePointer` or any other mutable pointer type. If you need to mutate the argument through the pointer, use `withUnsafeMutablePointer(to:_:)` instead.

## Return Value

The return value, if any, of the `body` closure.

## Discussion

The `withUnsafePointer(to:_:)` function is useful for calling Objective-C APIs that take in parameters by const pointer.

The pointer argument to `body` is valid only during the execution of `withUnsafePointer(to:_:)`. Do not store or return the pointer for later use.

## See Also

### Pointers to Values

- [withUnsafePointer(to:_:)](<withunsafepointer(to___)-9fjn6.md>) — Invokes the given closure with a pointer to the given argument.
- [withUnsafeMutablePointer(to:_:)](<withunsafemutablepointer(to___).md>) — Calls the given closure with a mutable pointer to the given argument.
- [withUnsafeBytes(of:_:)](<withunsafebytes(of___)-3ywhh.md>) — Invokes the given closure with a buffer pointer covering the raw bytes of the given argument.
- [withUnsafeBytes(of:_:)](<withunsafebytes(of___)-5gesg.md>) — Invokes the given closure with a buffer pointer covering the raw bytes of the given argument.
- [withUnsafeMutableBytes(of:_:)](<withunsafemutablebytes(of___).md>) — Invokes the given closure with a mutable buffer pointer covering the raw bytes of the given argument.
