---
title: CVaListPointer
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/cvalistpointer
source_url: 'https://developer.apple.com/documentation/swift/cvalistpointer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/cvalistpointer.json'
content_hash: 'sha256:836e6785b3e764c9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# CVaListPointer

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct CVaListPointer
```

## Relationships

- **Conforms To**: [BitwiseCopyable](bitwisecopyable.md), [Copyable](copyable.md), [CustomDebugStringConvertible](customdebugstringconvertible.md), [Escapable](escapable.md)

## Topics

### Default Implementations

- [CustomDebugStringConvertible Implementations](cvalistpointer/customdebugstringconvertible-implementations.md)

## See Also

### C Variadic Functions

- [withVaList(_:_:)](<withvalist(____).md>) — Invokes the given closure with a C `va_list` argument derived from the given array of arguments.
- [CVarArg](cvararg.md) — A type whose instances can be encoded, and appropriately passed, as elements of a C `va_list`.
- [getVaList(_:)](<getvalist(__).md>) — Returns a `CVaListPointer` that is backed by autoreleased storage, built from the given array of arguments.
