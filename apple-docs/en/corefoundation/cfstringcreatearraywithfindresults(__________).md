---
title: 'CFStringCreateArrayWithFindResults(_:_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringcreatearraywithfindresults(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringcreatearraywithfindresults(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringcreatearraywithfindresults%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:33feac8a52a95436'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringCreateArrayWithFindResults(_:_:_:_:_:)

<sub>Function</sub>

Searches a string for multiple occurrences of a substring and creates an array of ranges identifying the locations of these substrings within the target string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringCreateArrayWithFindResults(_ alloc: CFAllocator!, _ theString: CFString!, _ stringToFind: CFString!, _ rangeToSearch: CFRange, _ compareOptions: CFStringCompareFlags) -> CFArray!
```

## Parameters

- `alloc` — The allocator to use to allocate memory for the new CFArray object. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `theString` — The string in which to search for `stringToFind`.

- `stringToFind` — The string to search for in `theString`.

- `rangeToSearch` — The range of characters within `theString` to be searched. The specified range must not exceed the length of the string.

- `compareOptions` — Flags that select different types of comparisons, such as localized comparison, case-insensitive comparison, and non-literal comparison. If you want the default comparison behavior, pass `0`. See [String Comparison Flags](string-comparison-flags.md) for the available flags.

## Return Value

An array that contains pointers to [CFRange](cfrange.md) structures identifying the character locations of `stringToFind` in `theString`. Returns `NULL`, if no matching substring is found in the source object, or if there was a problem creating the array. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Searching Strings

- [CFStringFind](<cfstringfind(______).md>) — Searches for a substring within a string and, if it is found, yields the range of the substring within the object’s characters.
- [CFStringFindCharacterFromSet](<cfstringfindcharacterfromset(__________).md>) — Query the range of the first character contained in the specified character set.
- [CFStringFindWithOptions](<cfstringfindwithoptions(__________).md>) — Searches for a substring within a range of the characters represented by a string and, if the substring is found, returns its range within the object’s characters.
- [CFStringFindWithOptionsAndLocale](<cfstringfindwithoptionsandlocale(____________).md>) — Returns a Boolean value that indicates whether a given string was found in a given source string.
- [CFStringGetLineBounds](<cfstringgetlinebounds(__________).md>) — Given a range of characters in a string, obtains the line bounds—that is, the indexes of the first character and the final characters of the lines containing the range.
