---
title: CVarArg
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/cvararg
source_url: 'https://developer.apple.com/documentation/swift/cvararg'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/cvararg.json'
content_hash: 'sha256:6569edd3f13c313b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# CVarArg

<sub>Protocol</sub>

A type whose instances can be encoded, and appropriately passed, as elements of a C `va_list`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol CVarArg
```

## Overview

You use this protocol to present a native Swift interface to a C “varargs” API. For example, a program can import a C API like the one defined here:

```c
int c_api(int, va_list arguments)
```

To create a wrapper for the `c_api` function, write a function that takes `CVarArg` arguments, and then call the imported C function using the `withVaList(_:_:)` function:

```swift
func swiftAPI(_ x: Int, arguments: CVarArg...) -> Int {
    return withVaList(arguments) { c_api(x, $0) }
}
```

Swift only imports C variadic functions that use a `va_list` for their arguments. C functions that use the `...` syntax for variadic arguments are not imported, and therefore can’t be called using `CVarArg` arguments.

If you need to pass an optional pointer as a `CVarArg` argument, use the `Int(bitPattern:)` initializer to interpret the optional pointer as an `Int` value, which has the same C variadic calling conventions as a pointer on all supported platforms.

> [!note] Note
> Declaring conformance to the `CVarArg` protocol for types defined outside the standard library is not supported.

## Relationships

- **Conforming Types**: [Array](array.md), [AutoreleasingUnsafeMutablePointer](autoreleasingunsafemutablepointer.md), [Bool](bool.md), [Dictionary](dictionary.md), [Double](double.md), [Float](float.md), [Float80](float80.md), [Int](int.md), [Int16](int16.md), [Int32](int32.md), [Int64](int64.md), [Int8](int8.md), [OpaquePointer](opaquepointer.md), [Set](set.md), [String](string.md), [UInt](uint.md), [UInt16](uint16.md), [UInt32](uint32.md), [UInt64](uint64.md), [UInt8](uint8.md), [UnsafeMutablePointer](unsafemutablepointer.md), [UnsafePointer](unsafepointer.md)

## See Also

### C Variadic Functions

- [withVaList(_:_:)](<withvalist(____).md>) — Invokes the given closure with a C `va_list` argument derived from the given array of arguments.
- [CVaListPointer](cvalistpointer.md)
- [getVaList(_:)](<getvalist(__).md>) — Returns a `CVaListPointer` that is backed by autoreleased storage, built from the given array of arguments.
