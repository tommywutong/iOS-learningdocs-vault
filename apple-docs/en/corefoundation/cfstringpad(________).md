---
title: 'CFStringPad(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringpad(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringpad(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringpad%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:de7c3688e4969a08'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringPad(_:_:_:_:)

<sub>Function</sub>

Enlarges a string, padding it with specified characters, or truncates the string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringPad(_ theString: CFMutableString!, _ padString: CFString!, _ length: CFIndex, _ indexIntoPad: CFIndex)
```

## Parameters

- `theString` — The string to modify.

- `padString` — A string containing the characters with which to fill the extended character buffer. Pass `NULL` to truncate the string.

- `length` — The new length of `theString`. If this length is greater than the current length, padding takes place; if it is less, truncation takes place.

- `indexIntoPad` — The index of the character in `padString` with which to begin padding. If you are truncating the string represented by the object, this parameter is ignored.

## Discussion

This function has two purposes. It either enlarges the character buffer of a CFMutableString object to a given length, padding the added length with a given character or characters, or it truncates the character buffer to a smaller size. The key parameter for this behavior is `length`; if it is greater than the current length of the represented string, padding takes place, and if it less than the current length, truncation occurs.

For example, say you have a string, `aMutStr`, containing the characters “abcdef”. The call

```objc
CFStringPad(aMutStr, CFSTR("123"), 9, 1);
```

results in `aMutStr` containing “abcdef231”. However, the following call

```objc
CFStringPad(aMutStr, NULL, 3, 0);
```

results in `aMutStr` containing “abc”.

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
