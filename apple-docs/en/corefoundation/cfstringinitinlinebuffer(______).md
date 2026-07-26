---
title: 'CFStringInitInlineBuffer(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringinitinlinebuffer(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringinitinlinebuffer(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringinitinlinebuffer%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:564a22c3dc69dcc8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringInitInlineBuffer(_:_:_:)

<sub>Function</sub>

Initializes an in-line buffer to use for efficient access of a CFString object’s characters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringInitInlineBuffer(_ str: CFString!, _ buf: UnsafeMutablePointer<CFStringInlineBuffer>!, _ range: CFRange)
```

## Parameters

- `str` — The string to copy to the in-line buffer.

- `buf` — The (uninitialized) [CFStringInlineBuffer](cfstringinlinebuffer.md) structure to initialize. On return, an initialized structure that can be used in a [CFStringGetCharacterFromInlineBuffer](<cfstringgetcharacterfrominlinebuffer(____).md>) function call. Typically this buffer is allocated on the stack.

- `range` — The range of characters in `str` to copy to `buf`. The specified range must not exceed the length of the string.

## Discussion

This function initializes an [CFStringInlineBuffer](cfstringinlinebuffer.md) structure that can be used for accessing the characters of a string. Once the buffer is initialized you can call the [CFStringGetCharacterFromInlineBuffer](<cfstringgetcharacterfrominlinebuffer(____).md>) function to access the characters in the buffer one at a time. The in-line buffer functions, along with the [CFStringInlineBuffer](cfstringinlinebuffer.md) structure, give you fast access to the characters of a string. The technique for in-line buffer access combines the convenience of one-at-a-time character access with the efficiency of bulk access.

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
- [CFStringGetPascalString](<cfstringgetpascalstring(________).md>) — Copies the character contents of a CFString object to a local Pascal string buffer after converting the characters to a requested encoding.
- [CFStringGetPascalStringPtr](<cfstringgetpascalstringptr(____).md>) — Quickly obtains a pointer to a Pascal buffer containing the characters of a string in a given encoding.
- [CFStringGetRangeOfComposedCharactersAtIndex](<cfstringgetrangeofcomposedcharactersatindex(____).md>) — Returns the range of the composed character sequence at a specified index.
