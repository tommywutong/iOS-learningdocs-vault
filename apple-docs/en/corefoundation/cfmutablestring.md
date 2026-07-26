---
title: CFMutableString
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfmutablestring
source_url: 'https://developer.apple.com/documentation/corefoundation/cfmutablestring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfmutablestring.json'
content_hash: 'sha256:6cacbb8c61818bcc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFMutableString

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFMutableString
```

## Overview

CFMutableString manages dynamic strings. The basic interface for managing strings is provided by [CFString](cfstring.md). CFMutableString adds functions to modify the contents of a string.

CFMutableString is “toll-free bridged” with its Cocoa Foundation counterpart, [NSMutableString](../foundation/nsmutablestring.md). This means that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. Therefore, in a method where you see an `NSMutableString *` parameter, you can pass in a `CFMutableStringRef`, and in a function where you see a `CFMutableStringRef` parameter, you can pass in an NSMutableString instance. This also applies to concrete subclasses of NSMutableString. See [Toll-Free Bridged Types](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

## Relationships

- **Inherits From**: [CFString](cfstring.md)

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

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
- [CFStringPad](<cfstringpad(________).md>) — Enlarges a string, padding it with specified characters, or truncates the string.
- [CFStringReplace](<cfstringreplace(______).md>) — Replaces part of the character contents of a CFMutableString object with another string.
- [CFStringReplaceAll](<cfstringreplaceall(____).md>) — Replaces all characters of a CFMutableString object with other characters.
- [CFStringSetExternalCharactersNoCopy](<cfstringsetexternalcharactersnocopy(________).md>) — Notifies a CFMutableString object that its external backing store of Unicode characters has changed.
- [CFStringTransform](<cfstringtransform(________).md>) — Perform in-place transliteration on a mutable string.
- [CFStringTrim](<cfstringtrim(____).md>) — Trims a specified substring from the beginning and end of a CFMutableString object.
- [CFStringTrimWhitespace](<cfstringtrimwhitespace(__).md>) — Trims whitespace from the beginning and end of a CFMutableString object.
- [CFStringUppercase](<cfstringuppercase(____).md>) — Changes all lowercase alphabetical characters in a CFMutableString object to uppercase.

### Constants

- [CFStringNormalizationForm](cfstringnormalizationform.md) — Unicode normalization forms as described in Unicode Technical Report #15.
- [Transform Identifiers for CFStringTransform](transform-identifiers-for-cfstringtransform.md) — Constants that identify transforms used with [CFStringTransform](<cfstringtransform(________).md>).

## See Also

### Related Documentation

- [Property List Programming Topics for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPropertyLists/CFPropertyLists.html#//apple_ref/doc/uid/10000130i)
- [String Programming Guide for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/introCFStrings.html#//apple_ref/doc/uid/10000131i)

### Opaque Types

- [CFAllocator](cfallocator.md)
- [CFArray](cfarray.md)
- [CFAttributedString](cfattributedstring.md)
- [CFBag](cfbag.md)
- [CFBinaryHeap](cfbinaryheap.md)
- [CFBitVector](cfbitvector.md)
- [CFBoolean](cfboolean.md)
- [CFBundle](cfbundle.md)
- [CFCalendar](cfcalendar.md)
- [CFCharacterSet](cfcharacterset.md)
- [CFData](cfdata.md)
- [CFDate](cfdate.md)
- [CFDateFormatter](cfdateformatter.md)
- [CFDictionary](cfdictionary.md)
- [CFError](cferror.md)
