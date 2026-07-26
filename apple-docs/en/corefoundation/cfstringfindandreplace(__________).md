---
title: 'CFStringFindAndReplace(_:_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringfindandreplace(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringfindandreplace(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringfindandreplace%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:5200e2395795ab04'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringFindAndReplace(_:_:_:_:_:)

<sub>Function</sub>

Replaces all occurrences of a substring within a given range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringFindAndReplace(_ theString: CFMutableString!, _ stringToFind: CFString!, _ replacementString: CFString!, _ rangeToSearch: CFRange, _ compareOptions: CFStringCompareFlags) -> CFIndex
```

## Parameters

- `theString` — The string to modify.

- `stringToFind` — The substring to search for in `theString`.

- `replacementString` — The replacement string for `stringToFind`.

- `rangeToSearch` — The range within which to search in `theString`.

- `compareOptions` — Flags that select different types of comparisons, such as localized comparison, case-insensitive comparison, and non-literal comparison. If you want the default comparison behavior, pass `0`. See [CFStringCompareFlags](cfstringcompareflags.md) for the available flags.

## Return Value

The number of instances of `stringToFind` that were replaced.

## Discussion

The possible values of `compareOptions` are combinations of the [kCFCompareCaseInsensitive](cfstringcompareflags/comparecaseinsensitive.md), [kCFCompareBackwards](cfstringcompareflags/comparebackwards.md), [kCFCompareNonliteral](cfstringcompareflags/comparenonliteral.md), and [kCFCompareAnchored](cfstringcompareflags/compareanchored.md) constants.

The `kCFCompareBackwards` option can be used to replace a substring starting from the end, which could produce different results. For example, if the parameter `theString` is “AAAAA”, `stringToFind` is “AA”, and `replacementString` is “B”, then the result is normally “BBA”. However, if the `kCFCompareBackwards` constant is used, the result is “ABB.”

The `kCFCompareAnchored` option assures that only anchored but multiple instances are found (the instances must be consecutive at start or end). For example, if the parameter `theString` is “AAXAA”, `stringToFind` is “A”, and `replacementString` is “B”, then the result is normally “BBXBB.” However, if the `kCFCompareAnchored` constant is used, the result is “BBXAA.”

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
- [CFStringFold](<cfstringfold(______).md>) — Folds a given string into the form specified by optional flags.
- [CFStringInsert](<cfstringinsert(______).md>) — Inserts a string at a specified location in the character buffer of a CFMutableString object.
- [CFStringLowercase](<cfstringlowercase(____).md>) — Changes all uppercase alphabetical characters in a CFMutableString to lowercase.
- [CFStringNormalize](<cfstringnormalize(____).md>) — Normalizes the string into the specified form as described in Unicode Technical Report #15.
- [CFStringPad](<cfstringpad(________).md>) — Enlarges a string, padding it with specified characters, or truncates the string.
