---
title: 'CFStringGetCString(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringgetcstring(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringgetcstring(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringgetcstring%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:d019163beca3a16b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringGetCString(_:_:_:_:)

<sub>Function</sub>

Copies the character contents of a string to a local C string buffer after converting the characters to a given encoding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringGetCString(_ theString: CFString!, _ buffer: UnsafeMutablePointer<CChar>!, _ bufferSize: CFIndex, _ encoding: CFStringEncoding) -> Bool
```

## Parameters

- `theString` — The string whose contents you wish to access.

- `buffer` — The C string buffer into which to copy the string. On return, the buffer contains the converted characters. If there is an error in conversion, the buffer contains only partial results. The buffer must be large enough to contain the converted characters and a `NUL` terminator. For example, if the string is `Toby`, the buffer must be at least 5 bytes long.

- `bufferSize` — The length of `buffer` in bytes.

- `encoding` — The string encoding to which the character contents of `theString` should be converted. The encoding must specify an 8-bit encoding.

## Return Value

`true` upon success or `false` if the conversion fails or the provided buffer is too small.

## Discussion

This function is useful when you need your own copy of a string’s character data as a C string. You also typically call it as a “backup” when a prior call to the [CFStringGetCStringPtr](<cfstringgetcstringptr(____).md>) function fails.

## See Also

### Accessing Characters

- [CFStringCreateExternalRepresentation](<cfstringcreateexternalrepresentation(________).md>) — Creates an “external representation” of a CFString object, that is, a CFData object.
- [CFStringGetBytes](<cfstringgetbytes(________________).md>) — Fetches a range of the characters from a string into a byte buffer after converting the characters to a specified encoding.
- [CFStringGetCharacterAtIndex](<cfstringgetcharacteratindex(____).md>) — Returns the Unicode character at a specified location in a string.
- [CFStringGetCharacters](<cfstringgetcharacters(______).md>) — Copies a range of the Unicode characters from a string to a user-provided buffer.
- [CFStringGetCharactersPtr](<cfstringgetcharactersptr(__).md>) — Quickly obtains a pointer to the contents of a string as a buffer of Unicode characters.
- [CFStringGetCharacterFromInlineBuffer](<cfstringgetcharacterfrominlinebuffer(____).md>) — Returns the Unicode character at a specific location in an in-line buffer.
- [CFStringGetCStringPtr](<cfstringgetcstringptr(____).md>) — Quickly obtains a pointer to a C-string buffer containing the characters of a string in a given encoding.
- [CFStringGetLength](<cfstringgetlength(__).md>) — Returns the number (in terms of UTF-16 code pairs) of Unicode characters in a string.
- [CFStringGetPascalString](<cfstringgetpascalstring(________).md>) — Copies the character contents of a CFString object to a local Pascal string buffer after converting the characters to a requested encoding.
- [CFStringGetPascalStringPtr](<cfstringgetpascalstringptr(____).md>) — Quickly obtains a pointer to a Pascal buffer containing the characters of a string in a given encoding.
- [CFStringGetRangeOfComposedCharactersAtIndex](<cfstringgetrangeofcomposedcharactersatindex(____).md>) — Returns the range of the composed character sequence at a specified index.
- [CFStringInitInlineBuffer](<cfstringinitinlinebuffer(______).md>) — Initializes an in-line buffer to use for efficient access of a CFString object’s characters.
