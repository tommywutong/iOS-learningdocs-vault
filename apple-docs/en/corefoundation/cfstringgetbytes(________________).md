---
title: 'CFStringGetBytes(_:_:_:_:_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringgetbytes(_:_:_:_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringgetbytes(_:_:_:_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringgetbytes%28_%3A_%3A_%3A_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:bfe44ede8c745c73'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringGetBytes(_:_:_:_:_:_:_:_:)

<sub>Function</sub>

Fetches a range of the characters from a string into a byte buffer after converting the characters to a specified encoding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringGetBytes(_ theString: CFString!, _ range: CFRange, _ encoding: CFStringEncoding, _ lossByte: UInt8, _ isExternalRepresentation: Bool, _ buffer: UnsafeMutablePointer<UInt8>!, _ maxBufLen: CFIndex, _ usedBufLen: UnsafeMutablePointer<CFIndex>!) -> CFIndex
```

## Parameters

- `theString` — The string upon which to operate.

- `range` — The range of characters in `theString` to process. The specified range must not exceed the length of the string.

- `encoding` — The string encoding of the characters to copy to the byte buffer. 8, 16, and 32-bit encodings are supported.

- `lossByte` — A character (for example, ‘?’) that should be substituted for characters that cannot be converted to the specified encoding. Pass `0` if you do not want lossy conversion to occur.

- `isExternalRepresentation` — `true` if you want the result to be in an “external representation” format, otherwise `false`. In an “external representation” format, the result may contain a byte order marker (BOM) specifying endianness and this function might have to perform byte swapping.

- `buffer` — The byte buffer into which the converted characters are written. The buffer can be allocated on the heap or stack. Pass `NULL` if you do not want conversion to take place but instead want to know if conversion will succeed (the function result is greater than `0`) and, if so, how many bytes are required (`usedBufLen`).

- `maxBufLen` — The size of `buffer` and the maximum number of bytes that can be written to it.

- `usedBufLen` — On return, the number of converted bytes actually in `buffer`. You may pass `NULL` if you are not interested in this information.

## Return Value

The number of characters converted.

## Discussion

This function is the basic encoding-conversion function for CFString objects. As with the other functions that get the character contents of CFString objects, it allows conversion to a supported 8-bit encoding. Unlike most of those other functions, it also allows “lossy conversion.” The function permits the specification of a “loss byte” in a parameter; if a character cannot be converted this character is substituted and conversion proceeds. (With the other functions, conversion stops at the first error and the operation fails.)

Because this function takes a range and returns the number of characters converted, it can be called repeatedly with a small fixed size buffer and different ranges of the string to do the conversion incrementally.

This function also handles any necessary manipulation of character data in an “external representation” format. This format makes the data portable and persistent (disk-writable); in Unicode it often includes a BOM (byte order marker) that specifies the endianness of the data.

The [CFStringCreateExternalRepresentation](<cfstringcreateexternalrepresentation(________).md>) function also handles external representations and performs lossy conversions. The complementary function [CFStringCreateWithBytes](<cfstringcreatewithbytes(__________).md>) creates a string from the characters in a byte buffer.

## See Also

### Accessing Characters

- [CFStringCreateExternalRepresentation](<cfstringcreateexternalrepresentation(________).md>) — Creates an “external representation” of a CFString object, that is, a CFData object.
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
