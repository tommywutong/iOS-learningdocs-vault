---
title: 'withVaList(_:_:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/withvalist(_:_:)'
source_url: 'https://developer.apple.com/documentation/swift/withvalist(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/withvalist%28_%3A_%3A%29.json'
content_hash: 'sha256:24bec1ae2a1167ba'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# withVaList(_:_:)

<sub>Function</sub>

Invokes the given closure with a C `va_list` argument derived from the given array of arguments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withVaList<R>(_ args: [any CVarArg], _ body: (CVaListPointer) -> R) -> R
```

## Parameters

- `args` — An array of arguments to convert to a C `va_list` pointer.

- `body` — A closure with a `CVaListPointer` parameter that references the arguments passed as `args`. If `body` has a return value, that value is also used as the return value for the `withVaList(_:)` function. The pointer argument is valid only for the duration of the function’s execution.

## Return Value

The return value, if any, of the `body` closure parameter.

## Discussion

The pointer passed as an argument to `body` is valid only during the execution of `withVaList(_:_:)`. Do not store or return the pointer for later use.

If you need to pass an optional pointer as a `CVarArg` argument, use the `Int(bitPattern:)` initializer to interpret the optional pointer as an `Int` value, which has the same C variadic calling conventions as a pointer on all supported platforms.

## See Also

### C Variadic Functions

- [CVaListPointer](cvalistpointer.md)
- [CVarArg](cvararg.md) — A type whose instances can be encoded, and appropriately passed, as elements of a C `va_list`.
- [getVaList(_:)](<getvalist(__).md>) — Returns a `CVaListPointer` that is backed by autoreleased storage, built from the given array of arguments.
