---
title: 'CFStringGetPascalString(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringgetpascalstring(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringgetpascalstring(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringgetpascalstring%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:8e7b329e72efcea8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringGetPascalString(_:_:_:_:)

<sub>Function</sub>

Copies the character contents of a CFString object to a local Pascal string buffer after converting the characters to a requested encoding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringGetPascalString(_ theString: CFString!, _ buffer: StringPtr!, _ bufferSize: CFIndex, _ encoding: CFStringEncoding) -> Bool
```

## Parameters

- `theString` — The string to examine.

- `buffer` — The Pascal string buffer into which to copy the `theString`. The buffer must be at least `bufferSize` bytes in length. On return, contains the converted characters. If there is an error in conversion, the buffer contains only partial results.

- `bufferSize` — The length of the local `buffer` in bytes (accounting for the length byte).

- `encoding` — The string encoding to which the character contents of `theString` should be converted.

## Return Value

`true` if the operation succeeds or `false` if the conversion fails or the provided buffer is too small.

## Discussion

This function is useful when you need your own copy of a CFString object’s character data as a Pascal string. You can also call it as a “backup” operation when a prior call to the [CFStringGetPascalStringPtr](<cfstringgetpascalstringptr(____).md>) function fails.

## See Also

### Accessing Characters

- [CFStringCreateExternalRepresentation](<cfstringcreateexternalrepresentation(________).md>) — Creates an “external representation” of a CFString object, that is, a CFData object.
- [CFStringGetBytes](<cfstringgetbytes(________________).md>) — Fetches a range of the characters from a string into a byte buffer after converting the characters to a specified encoding.
- [CFStringGetCharacterAtIndex](<cfstringgetcharacteratindex(____).md>) — Returns the Unicode character at a specified location in a string.
- [CFStringGetCharacters](<cfstringgetcharacters(______).md>) — Copies a range of the Unicode characters from a string to a user-provided buffer.
- [CFStringGetCharactersPtr](<cfstringgetcharactersptr(__).md>) — Quickly obtains a pointer to the contents of a string as a buffer of Unicode characters.
- [CFStringGetCharacterFromInlineBuffer](<cfstringgetcharacterfrominlinebuffer(____).md>) — Returns the Unicode character at a specific location in an in-line buffer.
- [CFStringGetCString](<cfstringgetcstring(________).md>) — Copies the character contents of a string to a local C string buffer after converting the characters to a given encoding.
- [CFStringGetCStringPtr](<cfstringgetcstringptr(____).md>) — Quickly obtains a pointer to a C-string buffer containing the characters of a string in a given encoding.
- [CFStringGetLength](<cfstringgetlength(__).md>) — Returns the number (in terms of UTF-16 code pairs) of Unicode characters in a string.
- [CFStringGetPascalStringPtr](<cfstringgetpascalstringptr(____).md>) — Quickly obtains a pointer to a Pascal buffer containing the characters of a string in a given encoding.
- [CFStringGetRangeOfComposedCharactersAtIndex](<cfstringgetrangeofcomposedcharactersatindex(____).md>) — Returns the range of the composed character sequence at a specified index.
- [CFStringInitInlineBuffer](<cfstringinitinlinebuffer(______).md>) — Initializes an in-line buffer to use for efficient access of a CFString object’s characters.
