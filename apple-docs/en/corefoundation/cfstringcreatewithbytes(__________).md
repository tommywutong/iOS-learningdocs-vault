---
title: 'CFStringCreateWithBytes(_:_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringcreatewithbytes(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringcreatewithbytes(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringcreatewithbytes%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:5759a1a5e8deca5a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringCreateWithBytes(_:_:_:_:_:)

<sub>Function</sub>

Creates a string from a buffer containing characters in a specified encoding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringCreateWithBytes(_ alloc: CFAllocator!, _ bytes: UnsafePointer<UInt8>!, _ numBytes: CFIndex, _ encoding: CFStringEncoding, _ isExternalRepresentation: Bool) -> CFString!
```

## Parameters

- `alloc` — The allocator to use to allocate memory for the new string. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `bytes` — A buffer containing characters in the encoding specified by `encoding`. The buffer must _not_ contain a length byte (as in Pascal buffers) or any terminating `NULL` character (as in C buffers).

- `numBytes` — The number of bytes in `bytes`.

- `encoding` — The string encoding of the characters in the buffer.

- `isExternalRepresentation` — `true` if the characters in the byte buffer are in an “external representation” format—that is, whether the buffer contains a BOM (byte order marker). This is usually the case for bytes that are read in from a text file or received over the network. Otherwise, pass `false`.

## Return Value

An immutable string, or `NULL` if there was a problem creating the object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

This function handles character data in an “external representation” format by interpreting any BOM (byte order marker) character and performing any necessary byte swapping.

## See Also

### Creating a CFString

- [CFStringCreateArrayBySeparatingStrings](<cfstringcreatearraybyseparatingstrings(______).md>) — Creates an array of CFString objects from a single CFString object.
- [CFStringCreateByCombiningStrings](<cfstringcreatebycombiningstrings(______).md>) — Creates a single string from the individual CFString objects that comprise the elements of an array.
- [CFStringCreateCopy](<cfstringcreatecopy(____).md>) — Creates an immutable copy of a string.
- [CFStringCreateFromExternalRepresentation](<cfstringcreatefromexternalrepresentation(______).md>) — Creates a string from its “external representation.”
- [CFStringCreateWithBytesNoCopy](<cfstringcreatewithbytesnocopy(____________).md>) — Creates a string from a buffer, containing characters in a specified encoding, that might serve as the backing store for the new string.
- [CFStringCreateWithCharacters](<cfstringcreatewithcharacters(______).md>) — Creates a string from a buffer of Unicode characters.
- [CFStringCreateWithCharactersNoCopy](<cfstringcreatewithcharactersnocopy(________).md>) — Creates a string from a buffer of Unicode characters that might serve as the backing store for the object.
- [CFStringCreateWithCString](<cfstringcreatewithcstring(______).md>) — Creates an immutable string from a C string.
- [CFStringCreateWithCStringNoCopy](<cfstringcreatewithcstringnocopy(________).md>) — Creates a CFString object from an external C string buffer that might serve as the backing store for the object.
- [CFStringCreateWithFormatAndArguments](<cfstringcreatewithformatandarguments(________).md>) — Creates an immutable string from a formatted string and a variable number of arguments (specified in a parameter of type `va_list`).
- [CFStringCreateWithPascalString](<cfstringcreatewithpascalstring(______).md>) — Creates an immutable CFString object from a Pascal string.
- [CFStringCreateWithPascalStringNoCopy](<cfstringcreatewithpascalstringnocopy(________).md>) — Creates a CFString object from an external Pascal string buffer that might serve as the backing store for the object.
- [CFStringCreateWithSubstring](<cfstringcreatewithsubstring(______).md>) — Creates an immutable string from a segment (substring) of an existing string.
