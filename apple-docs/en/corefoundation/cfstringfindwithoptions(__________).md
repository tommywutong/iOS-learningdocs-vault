---
title: 'CFStringFindWithOptions(_:_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringfindwithoptions(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringfindwithoptions(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringfindwithoptions%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:e35caed116c499c5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringFindWithOptions(_:_:_:_:_:)

<sub>Function</sub>

Searches for a substring within a range of the characters represented by a string and, if the substring is found, returns its range within the object’s characters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringFindWithOptions(_ theString: CFString!, _ stringToFind: CFString!, _ rangeToSearch: CFRange, _ searchOptions: CFStringCompareFlags, _ result: UnsafeMutablePointer<CFRange>!) -> Bool
```

## Parameters

- `theString` — The string in which to to search for `stringToFind`.

- `stringToFind` — The substring to search for in `theString`.

- `rangeToSearch` — A range of the characters to search in `theString`. The specified range must not exceed the length of the string.

- `searchOptions` — The option flags to control the search behavior. See [String Comparison Flags](string-comparison-flags.md) for possible values. The flags [kCFCompareNumerically](cfstringcompareflags/comparenumerically.md) and [kCFCompareForcedOrdering](cfstringcompareflags/compareforcedordering.md) are ignored.

- `result` — On return, if the function result is `true`, contains the starting location and length of the found substring. You may pass `NULL` if you only want to know if the substring exists in the larger string.

## Return Value

`true` if the substring was found, `false` otherwise.

## Discussion

This function allows you to search only part of the characters of a string for a substring. It returns the found range indirectly, in the final `result` parameter. If you want to know if the entire range of characters represented by a string contains a particular substring, you can use the convenience function [CFStringFind](<cfstringfind(______).md>). Both of these functions return upon finding the first occurrence of the substring, so if you want to find out about multiple occurrences, call the [CFStringCreateArrayWithFindResults](<cfstringcreatearraywithfindresults(__________).md>) function.

Depending on the comparison-option flags specified, the length of the resulting range might be different than the length of the search string.

## See Also

### Searching Strings

- [CFStringCreateArrayWithFindResults](<cfstringcreatearraywithfindresults(__________).md>) — Searches a string for multiple occurrences of a substring and creates an array of ranges identifying the locations of these substrings within the target string.
- [CFStringFind](<cfstringfind(______).md>) — Searches for a substring within a string and, if it is found, yields the range of the substring within the object’s characters.
- [CFStringFindCharacterFromSet](<cfstringfindcharacterfromset(__________).md>) — Query the range of the first character contained in the specified character set.
- [CFStringFindWithOptionsAndLocale](<cfstringfindwithoptionsandlocale(____________).md>) — Returns a Boolean value that indicates whether a given string was found in a given source string.
- [CFStringGetLineBounds](<cfstringgetlinebounds(__________).md>) — Given a range of characters in a string, obtains the line bounds—that is, the indexes of the first character and the final characters of the lines containing the range.
