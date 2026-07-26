---
title: 'CFStringGetCharacterAtIndex(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringgetcharacteratindex(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringgetcharacteratindex(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringgetcharacteratindex%28_%3A_%3A%29.json'
content_hash: 'sha256:8156519877588a46'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringGetCharacterAtIndex(_:_:)

<sub>Function</sub>

Returns the Unicode character at a specified location in a string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringGetCharacterAtIndex(_ theString: CFString!, _ idx: CFIndex) -> UniChar
```

## Parameters

- `theString` — The string from which the Unicode character is obtained.

- `idx` — The position of the Unicode character in the CFString.

## Return Value

A Unicode character.

## Discussion

This function is typically called in a loop to fetch the Unicode characters of a string in sequence or to fetch a character at a known position (first or last, for example). Using it in a loop can be inefficient, especially with longer strings, so consider the [CFStringGetCharacters](<cfstringgetcharacters(______).md>) function or the in-line buffer functions ([CFStringInitInlineBuffer](<cfstringinitinlinebuffer(______).md>) and [CFStringGetCharacterFromInlineBuffer](<cfstringgetcharacterfrominlinebuffer(____).md>)) as alternatives.

## See Also

### Accessing Characters

- [CFStringCreateExternalRepresentation](<cfstringcreateexternalrepresentation(________).md>) — Creates an “external representation” of a CFString object, that is, a CFData object.
- [CFStringGetBytes](<cfstringgetbytes(________________).md>) — Fetches a range of the characters from a string into a byte buffer after converting the characters to a specified encoding.
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
