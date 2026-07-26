---
title: 'CFStringCompareWithOptionsAndLocale(_:_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringcomparewithoptionsandlocale(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringcomparewithoptionsandlocale(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringcomparewithoptionsandlocale%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:9641cbbdff31eef3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringCompareWithOptionsAndLocale(_:_:_:_:_:)

<sub>Function</sub>

Compares a range of the characters in one string with another string using a given locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringCompareWithOptionsAndLocale(_ theString1: CFString!, _ theString2: CFString!, _ rangeToCompare: CFRange, _ compareOptions: CFStringCompareFlags, _ locale: CFLocale!) -> CFComparisonResult
```

## Parameters

- `theString1` — The first string to use in the comparison.

- `theString2` — The second string to use in the comparison. The full range of this string is used.

- `rangeToCompare` — The range of characters in `theString1` to be used in the comparison to `theString2`. To use the whole string, pass the range `CFRangeMake(0, CFStringGetLength(theString1))`. The specified range must not exceed the bounds of the string.

- `compareOptions` — Flags that select different types of comparisons, such as case-insensitive comparison and non-literal comparison. See [String Comparison Flags](string-comparison-flags.md) for the available flags. Specifying the `kCFCompareBackwards` or `kCFCompareAnchored` option has no effect. Specifying the `kCFCompareLocalized` option and passing `NULL` for `locale` causes the current locale (the return value of [CFLocaleCopyCurrent](<cflocalecopycurrent().md>)) to be used.

- `locale` — The locale to use for the comparison, which affects both equality and ordering algorithms. For example, in some locales, accented characters are ordered immediately after the base; other locales order them after “z”. If `NULL` and the `kCFCompareLocalized` option is not specified for `compareOptions`, the comparison is nonlocalized.

## Return Value

A [CFComparisonResult](cfcomparisonresult.md) value that indicates whether `theString1` is equal to, less than, or greater than `theString2`.

## See Also

### Comparing Strings

- [CFStringCompare](<cfstringcompare(______).md>) — Compares one string with another string.
- [CFStringCompareWithOptions](<cfstringcomparewithoptions(________).md>) — Compares a range of the characters in one string with that of another string.
- [CFStringHasPrefix](<cfstringhasprefix(____).md>) — Determines if the character data of a string begin with a specified sequence of characters.
- [CFStringHasSuffix](<cfstringhassuffix(____).md>) — Determines if a string ends with a specified sequence of characters.
