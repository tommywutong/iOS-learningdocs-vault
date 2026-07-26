---
title: 'caseInsensitiveCompare(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/caseinsensitivecompare(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/caseinsensitivecompare(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/caseinsensitivecompare%28_%3A%29.json'
content_hash: 'sha256:45662ec8e84d7bc0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# caseInsensitiveCompare(_:)

<sub>Instance Method</sub>

Returns the result of invoking [- compare:options:](<compare(__options_).md>) with `NSCaseInsensitiveSearch` as the only option.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func caseInsensitiveCompare(_ string: String) -> ComparisonResult
```

## Parameters

- `string` — The string with which to compare the receiver.

## Return Value

Returns an [ComparisonResult](../comparisonresult.md) value that indicates the lexical ordering. [NSOrderedAscending](../comparisonresult/orderedascending.md) the receiver precedes `aString` in lexical ordering, [NSOrderedSame](../comparisonresult/orderedsame.md) the receiver and `aString` are equivalent in lexical value, and [NSOrderedDescending](../comparisonresult/ordereddescending.md) if the receiver follows `aString`.

## Discussion

This method is the equivalent of invoking [- compare:options:](<compare(__options_).md>) with [NSCaseInsensitiveSearch](compareoptions/caseinsensitive.md) as the only option.

> [!important] Important
> When working with text that’s presented to the user, use the [- localizedCaseInsensitiveCompare:](<localizedcaseinsensitivecompare(__).md>) method instead.

## See Also

### Identifying and Comparing Strings

- [- localizedCaseInsensitiveCompare:](<localizedcaseinsensitivecompare(__).md>) — Compares the string with a given string using a case-insensitive, localized, comparison.
- [- compare:](<compare(__).md>) — Returns the result of invoking [- compare:options:range:](<compare(__options_range_).md>) with no options and the receiver’s full extent as the range.
- [- localizedCompare:](<localizedcompare(__).md>) — Compares the string and a given string using a localized comparison.
- [- compare:options:](<compare(__options_).md>) — Compares the string with the specified string using the given options.
- [- compare:options:range:](<compare(__options_range_).md>) — Returns the result of invoking [- compare:options:range:locale:](<compare(__options_range_locale_).md>) with a `nil` locale.
- [- compare:options:range:locale:](<compare(__options_range_locale_).md>) — Compares the string using the specified options and returns the lexical ordering for the range.
- [- localizedStandardCompare:](<localizedstandardcompare(__).md>) — Compares strings as sorted by the Finder.
- [- hasPrefix:](<hasprefix(__).md>) — Returns a Boolean value that indicates whether a given string matches the beginning characters of the receiver.
- [- hasSuffix:](<hassuffix(__).md>) — Returns a Boolean value that indicates whether a given string matches the ending characters of the receiver.
- [- isEqualToString:](<isequal(to_).md>) — Returns a Boolean value that indicates whether a given string is equal to the receiver using a literal Unicode-based comparison.
- [hash](hash.md) — An unsigned integer that can be used as a hash table address.
- [CompareOptions](compareoptions.md) — These values represent the options available to many of the string classes’ search and comparison methods.
- [EncodingConversionOptions](encodingconversionoptions.md) — Options for converting string encodings.
