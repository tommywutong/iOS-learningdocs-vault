---
title: 'getVaList(_:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/getvalist(_:)'
source_url: 'https://developer.apple.com/documentation/swift/getvalist(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/getvalist%28_%3A%29.json'
content_hash: 'sha256:e2c76ebe75a72bbe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# getVaList(_:)

<sub>Function</sub>

Returns a `CVaListPointer` that is backed by autoreleased storage, built from the given array of arguments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getVaList(_ args: [any CVarArg]) -> CVaListPointer
```

## Parameters

- `args` — An array of arguments to convert to a C `va_list` pointer.

## Return Value

A pointer that can be used with C functions that take a `va_list` argument.

## Discussion

You should prefer `withVaList(_:_:)` instead of this function. In some uses, such as in a `class` initializer, you may find that the language rules do not allow you to use `withVaList(_:_:)` as intended.

If you need to pass an optional pointer as a `CVarArg` argument, use the `Int(bitPattern:)` initializer to interpret the optional pointer as an `Int` value, which has the same C variadic calling conventions as a pointer on all supported platforms.

## See Also

### C Variadic Functions

- [withVaList(_:_:)](<withvalist(____).md>) — Invokes the given closure with a C `va_list` argument derived from the given array of arguments.
- [CVaListPointer](cvalistpointer.md)
- [CVarArg](cvararg.md) — A type whose instances can be encoded, and appropriately passed, as elements of a C `va_list`.
