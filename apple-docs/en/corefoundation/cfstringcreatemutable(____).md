---
title: 'CFStringCreateMutable(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringcreatemutable(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringcreatemutable(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringcreatemutable%28_%3A_%3A%29.json'
content_hash: 'sha256:61523717bb5af411'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringCreateMutable(_:_:)

<sub>Function</sub>

Creates an empty CFMutableString object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringCreateMutable(_ alloc: CFAllocator!, _ maxLength: CFIndex) -> CFMutableString!
```

## Parameters

- `alloc` — The allocator to use to allocate memory for the new string. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `maxLength` — The maximum number of Unicode characters that can be stored by the returned string. Pass `0` if there should be no character limit. Note that initially the string still has a length of `0`; this parameter simply specifies what the maximum size is. CFMutableString might try to optimize its internal storage by paying attention to this value.

## Return Value

A new empty CFMutableString object or `NULL` if there was a problem creating the object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

This function creates an empty (that is, content-less) CFMutableString object. You can add character data to this object with any of the `CFStringAppend...` functions, and thereafter you can insert, delete, replace, pad, and trim characters with the appropriate CFString functions. If the `maxLength` parameter is greater than `0`, any attempt to add characters beyond this limit results in a run-time error.

## See Also

### CFMutableString Miscellaneous Functions

- [CFStringAppend](<cfstringappend(____).md>) — Appends the characters of a string to those of a CFMutableString object.
- [CFStringAppendCharacters](<cfstringappendcharacters(______).md>) — Appends a buffer of Unicode characters to the character contents of a CFMutableString object.
- [CFStringAppendCString](<cfstringappendcstring(______).md>) — Appends a C string to the character contents of a CFMutableString object.
- [CFStringAppendFormatAndArguments](<cfstringappendformatandarguments(________).md>) — Appends a formatted string to the character contents of a CFMutableString object.
- [CFStringAppendPascalString](<cfstringappendpascalstring(______).md>) — Appends a Pascal string to the character contents of a CFMutableString object.
- [CFStringCapitalize](<cfstringcapitalize(____).md>) — Changes the first character in each word of a string to uppercase (if it is a lowercase alphabetical character).
- [CFStringCreateMutableCopy](<cfstringcreatemutablecopy(______).md>) — Creates a mutable copy of a string.
- [CFStringCreateMutableWithExternalCharactersNoCopy](<cfstringcreatemutablewithexternalcharactersnocopy(__________).md>) — Creates a CFMutableString object whose Unicode character buffer is controlled externally.
- [CFStringDelete](<cfstringdelete(____).md>) — Deletes a range of characters in a string.
- [CFStringFindAndReplace](<cfstringfindandreplace(__________).md>) — Replaces all occurrences of a substring within a given range.
- [CFStringFold](<cfstringfold(______).md>) — Folds a given string into the form specified by optional flags.
- [CFStringInsert](<cfstringinsert(______).md>) — Inserts a string at a specified location in the character buffer of a CFMutableString object.
- [CFStringLowercase](<cfstringlowercase(____).md>) — Changes all uppercase alphabetical characters in a CFMutableString to lowercase.
- [CFStringNormalize](<cfstringnormalize(____).md>) — Normalizes the string into the specified form as described in Unicode Technical Report #15.
- [CFStringPad](<cfstringpad(________).md>) — Enlarges a string, padding it with specified characters, or truncates the string.
