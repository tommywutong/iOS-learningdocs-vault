---
title: 'CFStringFindCharacterFromSet(_:_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringfindcharacterfromset(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringfindcharacterfromset(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringfindcharacterfromset%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:38840b2109448f01'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringFindCharacterFromSet(_:_:_:_:_:)

<sub>Function</sub>

Query the range of the first character contained in the specified character set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringFindCharacterFromSet(_ theString: CFString!, _ theSet: CFCharacterSet!, _ rangeToSearch: CFRange, _ searchOptions: CFStringCompareFlags, _ result: UnsafeMutablePointer<CFRange>!) -> Bool
```

## Parameters

- `theString` — The string to search.

- `theSet` — The character set against which the membership of characters is checked.

- `rangeToSearch` — The range of characters within `theString` to search. If the range location or end point (defined by the location plus length minus `1`) are outside the index space of the string (`0` to `N-1` inclusive, where `N` is the length of the string), the behavior is undefined. The specified range must not exceed the length of the string. If the range length is negative, the behavior is undefined. The range may be empty (length `0`), in which case no search is performed.

- `searchOptions` — The option flags to control the search behavior. The supported options are [kCFCompareBackwards](cfstringcompareflags/comparebackwards.md) and [kCFCompareAnchored](cfstringcompareflags/compareanchored.md). If other option flags are specified, the behavior is undefined.

- `result` — On return, a pointer to a CFRange structure (supplied by the caller) in which the search result is stored. Note that the length of this range could be more than `1` (if the character in question is a multi-byte character). You may pass `NULL` if you don’t need this result.

## Return Value

`true` if a character in the character set is found and `result` is filled, `false` otherwise.

## See Also

### Searching Strings

- [CFStringCreateArrayWithFindResults](<cfstringcreatearraywithfindresults(__________).md>) — Searches a string for multiple occurrences of a substring and creates an array of ranges identifying the locations of these substrings within the target string.
- [CFStringFind](<cfstringfind(______).md>) — Searches for a substring within a string and, if it is found, yields the range of the substring within the object’s characters.
- [CFStringFindWithOptions](<cfstringfindwithoptions(__________).md>) — Searches for a substring within a range of the characters represented by a string and, if the substring is found, returns its range within the object’s characters.
- [CFStringFindWithOptionsAndLocale](<cfstringfindwithoptionsandlocale(____________).md>) — Returns a Boolean value that indicates whether a given string was found in a given source string.
- [CFStringGetLineBounds](<cfstringgetlinebounds(__________).md>) — Given a range of characters in a string, obtains the line bounds—that is, the indexes of the first character and the final characters of the lines containing the range.
