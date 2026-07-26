---
title: 'CFStringCreateWithFormatAndArguments(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringcreatewithformatandarguments(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringcreatewithformatandarguments(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringcreatewithformatandarguments%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:d591324d2a9d53ee'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringCreateWithFormatAndArguments(_:_:_:_:)

<sub>Function</sub>

Creates an immutable string from a formatted string and a variable number of arguments (specified in a parameter of type `va_list`).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringCreateWithFormatAndArguments(_ alloc: CFAllocator!, _ formatOptions: CFDictionary!, _ format: CFString!, _ arguments: CVaListPointer) -> CFString!
```

## Parameters

- `alloc` — The allocator to use to allocate memory for the new string. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `formatOptions` — A CFDictionary object containing formatting options for the string (such as the thousand-separator character, which is dependent on locale). Currently, these options are an unimplemented feature.

- `format` — The formatted string with `printf`-style specifiers. For information on supported specifiers, see [String Format Specifiers](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/formatSpecifiers.html#//apple_ref/doc/uid/TP40004265).

- `arguments` — The variable argument list of values to be inserted into the formatted string contained in `format`.

## Return Value

An immutable string, or `NULL` if there was a problem creating the object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

The programming interface for variable argument lists (`va_list`, `va_start`, `va_end`, and so forth) is declared in the standard C header file `stdarg.h`.

## See Also

### Creating a CFString

- [CFStringCreateArrayBySeparatingStrings](<cfstringcreatearraybyseparatingstrings(______).md>) — Creates an array of CFString objects from a single CFString object.
- [CFStringCreateByCombiningStrings](<cfstringcreatebycombiningstrings(______).md>) — Creates a single string from the individual CFString objects that comprise the elements of an array.
- [CFStringCreateCopy](<cfstringcreatecopy(____).md>) — Creates an immutable copy of a string.
- [CFStringCreateFromExternalRepresentation](<cfstringcreatefromexternalrepresentation(______).md>) — Creates a string from its “external representation.”
- [CFStringCreateWithBytes](<cfstringcreatewithbytes(__________).md>) — Creates a string from a buffer containing characters in a specified encoding.
- [CFStringCreateWithBytesNoCopy](<cfstringcreatewithbytesnocopy(____________).md>) — Creates a string from a buffer, containing characters in a specified encoding, that might serve as the backing store for the new string.
- [CFStringCreateWithCharacters](<cfstringcreatewithcharacters(______).md>) — Creates a string from a buffer of Unicode characters.
- [CFStringCreateWithCharactersNoCopy](<cfstringcreatewithcharactersnocopy(________).md>) — Creates a string from a buffer of Unicode characters that might serve as the backing store for the object.
- [CFStringCreateWithCString](<cfstringcreatewithcstring(______).md>) — Creates an immutable string from a C string.
- [CFStringCreateWithCStringNoCopy](<cfstringcreatewithcstringnocopy(________).md>) — Creates a CFString object from an external C string buffer that might serve as the backing store for the object.
- [CFStringCreateWithPascalString](<cfstringcreatewithpascalstring(______).md>) — Creates an immutable CFString object from a Pascal string.
- [CFStringCreateWithPascalStringNoCopy](<cfstringcreatewithpascalstringnocopy(________).md>) — Creates a CFString object from an external Pascal string buffer that might serve as the backing store for the object.
- [CFStringCreateWithSubstring](<cfstringcreatewithsubstring(______).md>) — Creates an immutable string from a segment (substring) of an existing string.
