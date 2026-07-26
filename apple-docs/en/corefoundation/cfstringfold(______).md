---
title: 'CFStringFold(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringfold(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringfold(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringfold%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:21c2b2d344e9a002'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringFold(_:_:_:)

<sub>Function</sub>

Folds a given string into the form specified by optional flags.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringFold(_ theString: CFMutableString!, _ theFlags: CFStringCompareFlags, _ theLocale: CFLocale!)
```

## Parameters

- `theString` — The string which is to be folded.  If this parameter is not a valid mutable CFString, the behavior is undefined.

- `theFlags` — The equivalency flags which describes the character folding form. See “String Comparison Flags” in [CFString](cfstring.md) for possible values. Only those flags containing the word “insensitive” are recognized; other flags are ignored. Folding with `kCFCompareCaseInsensitive` removes case distinctions in accordance with the mapping specified by [ftp://ftp.unicode.org/Public/UNIDATA/CaseFolding.txt](ftp://ftp.unicode.org/Public/UNIDATA/CaseFolding.txt).  Folding with `kCFCompareDiacriticInsensitive` removes distinctions of accents and other diacritics.  Folding with `kCFCompareWidthInsensitive` removes character width distinctions by mapping characters in the range `U+FF00-U+FFEF` to their ordinary equivalents.

- `theLocale` — The locale to use for the operation. `NULL` specifies the canonical locale (the return value from [CFLocaleGetSystem](<cflocalegetsystem().md>)). The locale argument affects the case mapping algorithm. For example, for the Turkish locale, case-insensitive compare matches “I” to “ı” (Unicode code point U+0131, Latin Small Dotless I), not the normal “i” character.

## Discussion

Character foldings are operations that convert any of a set of characters sharing similar semantics into a single representative from that set.

You can use this function to preprocess strings that are to be compared, searched, or indexed. Note that folding does not include normalization, so you must use [CFStringNormalize](<cfstringnormalize(____).md>) in addition to CFStringFold in order to obtain the effect of `kCFCompareNonliteral`.

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
- [CFStringInsert](<cfstringinsert(______).md>) — Inserts a string at a specified location in the character buffer of a CFMutableString object.
- [CFStringLowercase](<cfstringlowercase(____).md>) — Changes all uppercase alphabetical characters in a CFMutableString to lowercase.
- [CFStringNormalize](<cfstringnormalize(____).md>) — Normalizes the string into the specified form as described in Unicode Technical Report #15.
- [CFStringPad](<cfstringpad(________).md>) — Enlarges a string, padding it with specified characters, or truncates the string.
