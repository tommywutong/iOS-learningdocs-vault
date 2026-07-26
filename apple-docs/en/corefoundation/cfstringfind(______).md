---
title: 'CFStringFind(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringfind(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringfind(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringfind%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:a9201a888753d05d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringFind(_:_:_:)

<sub>Function</sub>

Searches for a substring within a string and, if it is found, yields the range of the substring within the object’s characters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringFind(_ theString: CFString!, _ stringToFind: CFString!, _ compareOptions: CFStringCompareFlags) -> CFRange
```

## Parameters

- `theString` — The string in which to search for `stringToFind`.

- `stringToFind` — The string to search for in `theString`.

- `compareOptions` — Flags that select different types of comparisons, such as localized comparison, case-insensitive comparison, and non-literal comparison. If you want the default comparison behavior, pass `0`. See [String Comparison Flags](string-comparison-flags.md) for the available flags.

## Return Value

The range of the located substring within `theString`. If a match is not located, the returned [CFRange](cfrange.md) structure will have a location of [kCFNotFound](kcfnotfound.md) and a length of `0` (either of which is enough to indicate failure).

## Discussion

This function is a convenience when you want to know if the entire range of characters represented by a string contains a particular substring. If you want to search only part of the characters of a string, use the [CFStringFindWithOptions](<cfstringfindwithoptions(__________).md>) function. Both of these functions return upon finding the first occurrence of the substring, so if you want to find out about multiple occurrences, call the [CFStringCreateArrayWithFindResults](<cfstringcreatearraywithfindresults(__________).md>) function.

Depending on the comparison-option flags specified, the length of the resulting range might be different than the length of the search string.

## See Also

### Searching Strings

- [CFStringCreateArrayWithFindResults](<cfstringcreatearraywithfindresults(__________).md>) — Searches a string for multiple occurrences of a substring and creates an array of ranges identifying the locations of these substrings within the target string.
- [CFStringFindCharacterFromSet](<cfstringfindcharacterfromset(__________).md>) — Query the range of the first character contained in the specified character set.
- [CFStringFindWithOptions](<cfstringfindwithoptions(__________).md>) — Searches for a substring within a range of the characters represented by a string and, if the substring is found, returns its range within the object’s characters.
- [CFStringFindWithOptionsAndLocale](<cfstringfindwithoptionsandlocale(____________).md>) — Returns a Boolean value that indicates whether a given string was found in a given source string.
- [CFStringGetLineBounds](<cfstringgetlinebounds(__________).md>) — Given a range of characters in a string, obtains the line bounds—that is, the indexes of the first character and the final characters of the lines containing the range.
