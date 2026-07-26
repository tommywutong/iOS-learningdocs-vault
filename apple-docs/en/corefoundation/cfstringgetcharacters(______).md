---
title: 'CFStringGetCharacters(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringgetcharacters(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringgetcharacters(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringgetcharacters%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:1d9bad35137f93d3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringGetCharacters(_:_:_:)

<sub>Function</sub>

Copies a range of the Unicode characters from a string to a user-provided buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringGetCharacters(_ theString: CFString!, _ range: CFRange, _ buffer: UnsafeMutablePointer<UniChar>!)
```

## Parameters

- `theString` — The string from which the characters are to be obtained.

- `range` — The range of characters to copy. The specified range must not exceed the length of the string.

- `buffer` — The `UniChar` buffer of length `range.length` that you have allocated on the stack or heap. On return, the buffer contains the requested Unicode characters.

## Discussion

Use this function to obtain some or all of the Unicode characters represented by a CFString object. If this operation involves a large number of characters, the function call can be expensive in terms of memory. Instead you might want to consider using the in-line buffer functions [CFStringInitInlineBuffer](<cfstringinitinlinebuffer(______).md>) and [CFStringGetCharacterFromInlineBuffer](<cfstringgetcharacterfrominlinebuffer(____).md>) to extract the characters incrementally.

## See Also

### Accessing Characters

- [CFStringCreateExternalRepresentation](<cfstringcreateexternalrepresentation(________).md>) — Creates an “external representation” of a CFString object, that is, a CFData object.
- [CFStringGetBytes](<cfstringgetbytes(________________).md>) — Fetches a range of the characters from a string into a byte buffer after converting the characters to a specified encoding.
- [CFStringGetCharacterAtIndex](<cfstringgetcharacteratindex(____).md>) — Returns the Unicode character at a specified location in a string.
- [CFStringGetCharactersPtr](<cfstringgetcharactersptr(__).md>) — Quickly obtains a pointer to the contents of a string as a buffer of Unicode characters.
- [CFStringGetCharacterFromInlineBuffer](<cfstringgetcharacterfrominlinebuffer(____).md>) — Returns the Unicode character at a specific location in an in-line buffer.
- [CFStringGetCString](<cfstringgetcstring(________).md>) — Copies the character contents of a string to a local C string buffer after converting the characters to a given encoding.
- [CFStringGetCStringPtr](<cfstringgetcstringptr(____).md>) — Quickly obtains a pointer to a C-string buffer containing the characters of a string in a given encoding.
- [CFStringGetLength](<cfstringgetlength(__).md>) — Returns the number (in terms of UTF-16 code pairs) of Unicode characters in a string.
- [CFStringGetPascalString](<cfstringgetpascalstring(________).md>) — Copies the character contents of a CFString object to a local Pascal string buffer after converting the characters to a requested encoding.
- [CFStringGetPascalStringPtr](<cfstringgetpascalstringptr(____).md>) — Quickly obtains a pointer to a Pascal buffer containing the characters of a string in a given encoding.
- [CFStringGetRangeOfComposedCharactersAtIndex](<cfstringgetrangeofcomposedcharactersatindex(____).md>) — Returns the range of the composed character sequence at a specified index.
- [CFStringInitInlineBuffer](<cfstringinitinlinebuffer(______).md>) — Initializes an in-line buffer to use for efficient access of a CFString object’s characters.
