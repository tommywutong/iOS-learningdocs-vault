---
title: 'CFStringCreateExternalRepresentation(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringcreateexternalrepresentation(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringcreateexternalrepresentation(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringcreateexternalrepresentation%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:ade4baaf125a3f46'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringCreateExternalRepresentation(_:_:_:_:)

<sub>Function</sub>

Creates an “external representation” of a CFString object, that is, a CFData object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringCreateExternalRepresentation(_ alloc: CFAllocator!, _ theString: CFString!, _ encoding: CFStringEncoding, _ lossByte: UInt8) -> CFData!
```

## Parameters

- `alloc` — The allocator to use to allocate memory for the new CFData object. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `theString` — The string to convert to an external representation.

- `encoding` — The string encoding to use for the external representation.

- `lossByte` — The character value to assign to characters that cannot be converted to the requested encoding. Pass `0` if you want conversion to stop at the first such error; if this happens, the function returns `NULL`.

## Return Value

A CFData object that stores the characters of the CFString object as an “external representation.” Returns `NULL` if no loss byte was specified and the function could not convert the characters to the specified encoding. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

In the CFData object form, the string can be written to disk as a file or be sent out over a network. If the encoding of the characters in the data object is Unicode, the function may insert a BOM (byte-order marker) to indicate endianness. However, representations created with encoding constants `kCFStringEncodingUTF16BE`, `kCFStringEncodingUTF16LE`, `kCFStringEncodingUTF32BE`, and `kCFStringEncodingUTF32LE` do not include a BOM because the byte order is explicitly indicated by the letters “BE” (big-endian) and “LE” (little-endian).

This function allows the specification of a “loss byte” to represent characters that cannot be converted to the requested encoding.

When you create an external representation from a CFMutableString object, it loses this mutability characteristic when it is converted back to a CFString object.

The [CFStringCreateFromExternalRepresentation](<cfstringcreatefromexternalrepresentation(______).md>) function complements this function by creating a CFString object from an “external representation” CFData object.

## See Also

### Accessing Characters

- [CFStringGetBytes](<cfstringgetbytes(________________).md>) — Fetches a range of the characters from a string into a byte buffer after converting the characters to a specified encoding.
- [CFStringGetCharacterAtIndex](<cfstringgetcharacteratindex(____).md>) — Returns the Unicode character at a specified location in a string.
- [CFStringGetCharacters](<cfstringgetcharacters(______).md>) — Copies a range of the Unicode characters from a string to a user-provided buffer.
- [CFStringGetCharactersPtr](<cfstringgetcharactersptr(__).md>) — Quickly obtains a pointer to the contents of a string as a buffer of Unicode characters.
- [CFStringGetCharacterFromInlineBuffer](<cfstringgetcharacterfrominlinebuffer(____).md>) — Returns the Unicode character at a specific location in an in-line buffer.
- [CFStringGetCString](<cfstringgetcstring(________).md>) — Copies the character contents of a string to a local C string buffer after converting the characters to a given encoding.
- [CFStringGetCStringPtr](<cfstringgetcstringptr(____).md>) — Quickly obtains a pointer to a C-string buffer containing the characters of a string in a given encoding.
- [CFStringGetLength](<cfstringgetlength(__).md>) — Returns the number (in terms of UTF-16 code pairs) of Unicode characters in a string.
- [CFStringGetPascalString](<cfstringgetpascalstring(________).md>) — Copies the character contents of a CFString object to a local Pascal string buffer after converting the characters to a requested encoding.
- [CFStringGetPascalStringPtr](<cfstringgetpascalstringptr(____).md>) — Quickly obtains a pointer to a Pascal buffer containing the characters of a string in a given encoding.
- [CFStringGetRangeOfComposedCharactersAtIndex](<cfstringgetrangeofcomposedcharactersatindex(____).md>) — Returns the range of the composed character sequence at a specified index.
- [CFStringInitInlineBuffer](<cfstringinitinlinebuffer(______).md>) — Initializes an in-line buffer to use for efficient access of a CFString object’s characters.
