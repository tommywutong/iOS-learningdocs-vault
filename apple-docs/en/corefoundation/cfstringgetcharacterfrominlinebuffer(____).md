---
title: 'CFStringGetCharacterFromInlineBuffer(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringgetcharacterfrominlinebuffer(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringgetcharacterfrominlinebuffer(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringgetcharacterfrominlinebuffer%28_%3A_%3A%29.json'
content_hash: 'sha256:b99e0a87f6c77e9a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringGetCharacterFromInlineBuffer(_:_:)

<sub>Function</sub>

Returns the Unicode character at a specific location in an in-line buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringGetCharacterFromInlineBuffer(_ buf: UnsafeMutablePointer<CFStringInlineBuffer>!, _ idx: CFIndex) -> UniChar
```

## Parameters

- `buf` — The initialized CFStringInlineBuffer structure in which the characters are stored. You should initialize the structure with the [CFStringInitInlineBuffer](<cfstringinitinlinebuffer(______).md>) function.

- `idx` — The location of a character in the in-line buffer `buf`. This index is relative to the range specified when `buf` was created.

## Return Value

A Unicode character, or `0` if a location outside the original range is specified.

## Discussion

This function accesses one of the characters of a string written to an in-line buffer. It is typically called from within a loop to access each character in the buffer in sequence. You should initialize the buffer with the [CFStringInitInlineBuffer](<cfstringinitinlinebuffer(______).md>) function. The in-line buffer functions, along with the [CFStringInlineBuffer](cfstringinlinebuffer.md) structure, give you fast access to the characters of a CFString object. The technique for in-line buffer access combines the convenience of one-at-a-time character access with the efficiency of bulk access.

## See Also

### Accessing Characters

- [CFStringCreateExternalRepresentation](<cfstringcreateexternalrepresentation(________).md>) — Creates an “external representation” of a CFString object, that is, a CFData object.
- [CFStringGetBytes](<cfstringgetbytes(________________).md>) — Fetches a range of the characters from a string into a byte buffer after converting the characters to a specified encoding.
- [CFStringGetCharacterAtIndex](<cfstringgetcharacteratindex(____).md>) — Returns the Unicode character at a specified location in a string.
- [CFStringGetCharacters](<cfstringgetcharacters(______).md>) — Copies a range of the Unicode characters from a string to a user-provided buffer.
- [CFStringGetCharactersPtr](<cfstringgetcharactersptr(__).md>) — Quickly obtains a pointer to the contents of a string as a buffer of Unicode characters.
- [CFStringGetCString](<cfstringgetcstring(________).md>) — Copies the character contents of a string to a local C string buffer after converting the characters to a given encoding.
- [CFStringGetCStringPtr](<cfstringgetcstringptr(____).md>) — Quickly obtains a pointer to a C-string buffer containing the characters of a string in a given encoding.
- [CFStringGetLength](<cfstringgetlength(__).md>) — Returns the number (in terms of UTF-16 code pairs) of Unicode characters in a string.
- [CFStringGetPascalString](<cfstringgetpascalstring(________).md>) — Copies the character contents of a CFString object to a local Pascal string buffer after converting the characters to a requested encoding.
- [CFStringGetPascalStringPtr](<cfstringgetpascalstringptr(____).md>) — Quickly obtains a pointer to a Pascal buffer containing the characters of a string in a given encoding.
- [CFStringGetRangeOfComposedCharactersAtIndex](<cfstringgetrangeofcomposedcharactersatindex(____).md>) — Returns the range of the composed character sequence at a specified index.
- [CFStringInitInlineBuffer](<cfstringinitinlinebuffer(______).md>) — Initializes an in-line buffer to use for efficient access of a CFString object’s characters.
