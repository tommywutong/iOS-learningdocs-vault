---
title: 'CFStringAppend(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringappend(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringappend(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringappend%28_%3A_%3A%29.json'
content_hash: 'sha256:7256661b46635276'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringAppend(_:_:)

<sub>Function</sub>

Appends the characters of a string to those of a CFMutableString object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringAppend(_ theString: CFMutableString!, _ appendedString: CFString!)
```

## Parameters

- `theString` — The string to which `appendedString` is appended. If `theString` is not a CFMutableString object, an assertion is raised.

- `appendedString` — The string to append.

## Discussion

This function reallocates the backing store of `theString` to accommodate the new length.

## See Also

### CFMutableString Miscellaneous Functions

- [CFStringAppendCharacters](<cfstringappendcharacters(______).md>) — Appends a buffer of Unicode characters to the character contents of a CFMutableString object.
- [CFStringAppendCString](<cfstringappendcstring(______).md>) — Appends a C string to the character contents of a CFMutableString object.
- [CFStringAppendFormatAndArguments](<cfstringappendformatandarguments(________).md>) — Appends a formatted string to the character contents of a CFMutableString object.
- [CFStringAppendPascalString](<cfstringappendpascalstring(______).md>) — Appends a Pascal string to the character contents of a CFMutableString object.
- [CFStringCapitalize](<cfstringcapitalize(____).md>) — Changes the first character in each word of a string to uppercase (if it is a lowercase alphabetical character).
- [CFStringCreateMutable](<cfstringcreatemutable(____).md>) — Creates an empty CFMutableString object.
- [CFStringCreateMutableCopy](<cfstringcreatemutablecopy(______).md>) — Creates a mutable copy of a string.
- [CFStringCreateMutableWithExternalCharactersNoCopy](<cfstringcreatemutablewithexternalcharactersnocopy(__________).md>) — Creates a CFMutableString object whose Unicode character buffer is controlled externally.
- [CFStringDelete](<cfstringdelete(____).md>) — Deletes a range of characters in a string.
- [CFStringFindAndReplace](<cfstringfindandreplace(__________).md>) — Replaces all occurrences of a substring within a given range.
- [CFStringFold](<cfstringfold(______).md>) — Folds a given string into the form specified by optional flags.
- [CFStringInsert](<cfstringinsert(______).md>) — Inserts a string at a specified location in the character buffer of a CFMutableString object.
- [CFStringLowercase](<cfstringlowercase(____).md>) — Changes all uppercase alphabetical characters in a CFMutableString to lowercase.
- [CFStringNormalize](<cfstringnormalize(____).md>) — Normalizes the string into the specified form as described in Unicode Technical Report #15.
- [CFStringPad](<cfstringpad(________).md>) — Enlarges a string, padding it with specified characters, or truncates the string.
