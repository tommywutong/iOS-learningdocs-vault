---
title: 'CFStringCompareWithOptions(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringcomparewithoptions(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringcomparewithoptions(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringcomparewithoptions%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:31ddc7fb59a589c1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringCompareWithOptions(_:_:_:_:)

<sub>Function</sub>

Compares a range of the characters in one string with that of another string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringCompareWithOptions(_ theString1: CFString!, _ theString2: CFString!, _ rangeToCompare: CFRange, _ compareOptions: CFStringCompareFlags) -> CFComparisonResult
```

## Parameters

- `theString1` — The first string to use in the comparison.

- `theString2` — The second string to use in the comparison.

- `rangeToCompare` — The range of characters in `theString1` to be used in the comparison to `theString2`. To use the whole string, pass the range `CFRangeMake(0, CFStringGetLength(theString1))` or use [CFStringCompare](<cfstringcompare(______).md>). The specified range must not exceed the length of the string.

- `compareOptions` — Flags that select different types of comparisons, such as localized comparison, case-insensitive comparison, and non-literal comparison. If you want the default comparison behavior, pass `0`. See [String Comparison Flags](string-comparison-flags.md) for the available flags.

## Return Value

A [CFComparisonResult](cfcomparisonresult.md) value that indicates whether `theString1` is equal to, less than, or greater than `theString2`.

## Discussion

You can affect how the comparison proceeds by specifying one or more option flags in `compareOptions`.

If you want to compare one entire string with another string, use the [CFStringCompare](<cfstringcompare(______).md>) function.

## See Also

### Comparing Strings

- [CFStringCompare](<cfstringcompare(______).md>) — Compares one string with another string.
- [CFStringCompareWithOptionsAndLocale](<cfstringcomparewithoptionsandlocale(__________).md>) — Compares a range of the characters in one string with another string using a given locale.
- [CFStringHasPrefix](<cfstringhasprefix(____).md>) — Determines if the character data of a string begin with a specified sequence of characters.
- [CFStringHasSuffix](<cfstringhassuffix(____).md>) — Determines if a string ends with a specified sequence of characters.
