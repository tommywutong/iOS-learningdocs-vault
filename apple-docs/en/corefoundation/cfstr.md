---
title: CFSTR
framework: Core Foundation
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfstr
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstr.json'
content_hash: 'sha256:d1fa5d4c5af04415'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSTR

<sub>Macro</sub>

Creates an immutable string from a constant compile-time string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define CFSTR(cStr)
```

## Parameters

- `cStr` — A constant C string (that is, text enclosed in double-quotation marks) from which the string is to be created.

## Return Value

An immutable string, or `NULL` if there was a problem creating the object. The returned object is a constant. You may retain and release it, similar to other immutable CFString objects, but are not required to do so—it will remain valid until the program terminates.

## Discussion

The `CFSTR` macro is a convenient way to create CFString representations of constant compile-time strings.

A value returned by `CFSTR` has the following semantics:

- Values returned from `CFSTR` are not released by CFString—they are guaranteed to be valid until the program terminates.
- You can retain and release values returned from `CFSTR` in a balanced fashion, like any other CFString, but you are not required to do so.

> [!note] Note
> When using this macro as an initializer, you must build using the `-fconstant-cfstrings` compiler flag.

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
- [CFStringCreateWithFormat](cfstringcreatewithformat.md) — Creates an immutable string from a formatted string and a variable number of arguments.
- [CFStringCreateWithFormatAndArguments](<cfstringcreatewithformatandarguments(________).md>) — Creates an immutable string from a formatted string and a variable number of arguments (specified in a parameter of type `va_list`).
- [CFStringCreateWithPascalString](<cfstringcreatewithpascalstring(______).md>) — Creates an immutable CFString object from a Pascal string.
- [CFStringCreateWithPascalStringNoCopy](<cfstringcreatewithpascalstringnocopy(________).md>) — Creates a CFString object from an external Pascal string buffer that might serve as the backing store for the object.
- [CFStringCreateWithSubstring](<cfstringcreatewithsubstring(______).md>) — Creates an immutable string from a segment (substring) of an existing string.
