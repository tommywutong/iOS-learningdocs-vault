---
title: 'CFStringLowercase(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringlowercase(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringlowercase(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringlowercase%28_%3A_%3A%29.json'
content_hash: 'sha256:fb550316807be40e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringLowercase(_:_:)

<sub>Function</sub>

Changes all uppercase alphabetical characters in a CFMutableString to lowercase.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringLowercase(_ theString: CFMutableString!, _ locale: CFLocale!)
```

## Parameters

- `theString` — The string to be lowercased. If this value is not a CFMutableString object, an assertion is raised.

- `locale` — The locale to use when the lowercasing operation is performed. Prior to OS X v10.3 this parameter was an untyped pointer and not used. The locale argument affects the case mapping algorithm. For example, for the Turkish locale, case-insensitive compare matches “I” to “ı” (Unicode code point U+0131, Latin Small Dotless I), not the normal “i” character.

## Discussion

The `locale` parameter type changed from void * to CFLocaleRef in OS X v10.3.

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
- [CFStringNormalize](<cfstringnormalize(____).md>) — Normalizes the string into the specified form as described in Unicode Technical Report #15.
- [CFStringPad](<cfstringpad(________).md>) — Enlarges a string, padding it with specified characters, or truncates the string.
