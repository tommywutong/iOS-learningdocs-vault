---
title: 'CFStringTransform(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringtransform(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringtransform(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringtransform%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:ae9746ea6669e158'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringTransform(_:_:_:_:)

<sub>Function</sub>

Perform in-place transliteration on a mutable string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringTransform(_ string: CFMutableString!, _ range: UnsafeMutablePointer<CFRange>!, _ transform: CFString!, _ reverse: Bool) -> Bool
```

## Parameters

- `string` — The string to transform.

- `range` — A pointer to the range over which the transformation is applied. `NULL` causes the whole string to be transformed. On return, `range` is modified to reflect the new range corresponding to the original range.

- `transform` — A CFString object that identifies the transformation to apply. For a list of valid values, see [Transform Identifiers for CFStringTransform](transform-identifiers-for-cfstringtransform.md). In macOS 10.4 and later, you can also use any valid ICU transform ID defined in the [ICU User Guide for Transforms](https://unicode-org.github.io/icu/userguide/transforms/general/).

- `reverse` — A Boolean that, if `true`, specifies that the inverse transform should be used (if it exists).

## Return Value

`true` if the transform is successful; otherwise `false`.

## Discussion

The transformation represented by `transform` is applied to the given range of `string`, modifying it in place. Only the specified range is modified, but the transform may look at portions of the string outside that range for context. Reasons that the transform may be unsuccessful include an invalid transform identifier, and attempting to reverse an irreversible transform.

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
