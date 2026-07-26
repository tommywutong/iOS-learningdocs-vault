---
title: C Interoperability
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/c-interoperability
source_url: 'https://developer.apple.com/documentation/swift/c-interoperability'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/c-interoperability.json'
content_hash: 'sha256:45370d01b902970d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md) · [Swift Standard Library](swift-standard-library.md)

# C Interoperability

<sub>API Collection</sub>

Use imported C types or call C variadic functions.

## Topics

### C and Objective-C Pointers

- [OpaquePointer](opaquepointer.md) — A wrapper around an opaque C pointer.
- [AutoreleasingUnsafeMutablePointer](autoreleasingunsafemutablepointer.md) — A mutable pointer addressing an Objective-C reference that doesn’t own its target.

### C Variadic Functions

- [withVaList(_:_:)](<withvalist(____).md>) — Invokes the given closure with a C `va_list` argument derived from the given array of arguments.
- [CVaListPointer](cvalistpointer.md)
- [CVarArg](cvararg.md) — A type whose instances can be encoded, and appropriately passed, as elements of a C `va_list`.
- [getVaList(_:)](<getvalist(__).md>) — Returns a `CVaListPointer` that is backed by autoreleased storage, built from the given array of arguments.

### Pointers to Values

- [withUnsafePointer(to:_:)](<withunsafepointer(to___)-9fjn6.md>) — Invokes the given closure with a pointer to the given argument.
- [withUnsafePointer(to:_:)](<withunsafepointer(to___)-35wrn.md>) — Invokes the given closure with a pointer to the given argument.
- [withUnsafeMutablePointer(to:_:)](<withunsafemutablepointer(to___).md>) — Calls the given closure with a mutable pointer to the given argument.
- [withUnsafeBytes(of:_:)](<withunsafebytes(of___)-3ywhh.md>) — Invokes the given closure with a buffer pointer covering the raw bytes of the given argument.
- [withUnsafeBytes(of:_:)](<withunsafebytes(of___)-5gesg.md>) — Invokes the given closure with a buffer pointer covering the raw bytes of the given argument.
- [withUnsafeMutableBytes(of:_:)](<withunsafemutablebytes(of___).md>) — Invokes the given closure with a mutable buffer pointer covering the raw bytes of the given argument.

### Aliases for Imported C Types

- [CBool](cbool.md) — The C ‘_Bool’ and C++ ‘bool’ type.
- [CChar](cchar.md) — The C ‘char’ type.
- [CChar8](cchar8.md) — The C++20 ‘char8_t’ type, which has UTF-8 encoding.
- [CChar16](cchar16.md) — The C++11 ‘char16_t’ type, which has UTF-16 encoding.
- [CChar32](cchar32.md) — The C++11 ‘char32_t’ type, which has UTF-32 encoding.
- [CDouble](cdouble.md) — The C ‘double’ type.
- [CLongDouble](clongdouble.md)
- [CFloat](cfloat.md) — The C ‘float’ type.
- [CFloat16](cfloat16.md) — The C ‘_Float16’ type.
- [CInt](cint.md)
- [CLong](clong.md)
- [CLongLong](clonglong.md) — The C ‘long long’ type.
- [CShort](cshort.md) — The C ‘short’ type.
- [CSignedChar](csignedchar.md) — The C ‘signed char’ type.
- [CUnsignedChar](cunsignedchar.md) — The C ‘unsigned char’ type.
- [CUnsignedInt](cunsignedint.md)
- [CUnsignedLong](cunsignedlong.md)
- [CUnsignedLongLong](cunsignedlonglong.md) — The C ‘unsigned long long’ type.
- [CUnsignedShort](cunsignedshort.md) — The C ‘unsigned short’ type.
- [CWideChar](cwidechar.md)

## See Also

### Programming Tasks

- [Input and Output](input-and-output.md) — Print values to the console, read from and write to text streams, and use command line arguments.
- [Debugging and Reflection](debugging-and-reflection.md) — Fortify your code with runtime checks, and examine your values’ runtime representation.
- [Macros](macros.md) — Generate boilerplate code and perform other compile-time operations.
- [Concurrency](concurrency.md) — Perform asynchronous and parallel operations.
- [Key-Path Expressions](key-path-expressions.md) — Use key-path expressions to access properties dynamically.
- [Manual Memory Management](manual-memory-management.md) — Allocate and manage memory manually.
- [Type Casting and Existential Types](type-casting-and-existential-types.md) — Perform casts between types or represent values of any type.
- [Operator Declarations](operator-declarations.md) — Work with prefix, postfix, and infix operators.
