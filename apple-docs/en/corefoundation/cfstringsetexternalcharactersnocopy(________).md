---
title: 'CFStringSetExternalCharactersNoCopy(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringsetexternalcharactersnocopy(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringsetexternalcharactersnocopy(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringsetexternalcharactersnocopy%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:26ac919f72953906'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringSetExternalCharactersNoCopy(_:_:_:_:)

<sub>Function</sub>

Notifies a CFMutableString object that its external backing store of Unicode characters has changed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringSetExternalCharactersNoCopy(_ theString: CFMutableString!, _ chars: UnsafeMutablePointer<UniChar>!, _ length: CFIndex, _ capacity: CFIndex)
```

## Parameters

- `theString` — The string to act as a “wrapper” for the external backing store (`chars`). If this value is not a CFMutableString object, an assertion is raised.

- `chars` — The external (client-owned) Unicode buffer acting as the backing store for `theString`.

- `length` — The current length of the contents of `chars` (in Unicode characters).

- `capacity` — The capacity of the Unicode buffer—that is, the total number of Unicode characters that can be stored in it before the buffer has to be grown.

## Discussion

You use this function to reallocate memory for a string, if necessary, and change its references to the data in the buffer. The object must have been created with the [CFStringCreateMutableWithExternalCharactersNoCopy](<cfstringcreatemutablewithexternalcharactersnocopy(__________).md>) function; see the discussion of this function for more information.

## See Also

### CFMutableString Miscellaneous Functions

- [CFStringAppend](<cfstringappend(____).md>) — Appends the characters of a string to those of a CFMutableString object.
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
