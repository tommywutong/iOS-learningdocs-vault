---
title: 'localizedCompare(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/localizedcompare(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/localizedcompare(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/localizedcompare%28_%3A%29.json'
content_hash: 'sha256:c690dda2d0b207bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# localizedCompare(_:)

<sub>Instance Method</sub>

Compares the string and a given string using a localized comparison.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func localizedCompare(_ string: String) -> ComparisonResult
```

## Parameters

- `string` — The string with which to compare the receiver. This value must not be `nil`. If this value is `nil`, the behavior is undefined and may change in future versions of macOS.

## Return Value

Returns an [ComparisonResult](../comparisonresult.md) value that indicates the lexical ordering. [NSOrderedAscending](../comparisonresult/orderedascending.md) the receiver precedes `aString` in lexical ordering, [NSOrderedSame](../comparisonresult/orderedsame.md) the receiver and `aString` are equivalent in lexical value, and [NSOrderedDescending](../comparisonresult/ordereddescending.md) if the receiver follows `aString`.

## Discussion

This method uses the current locale.

> [!important] Important
> When working with text that’s presented to the user, use the [- localizedStandardCompare:](<localizedstandardcompare(__).md>) method instead.

## See Also

### Identifying and Comparing Strings

- [- caseInsensitiveCompare:](<caseinsensitivecompare(__).md>) — Returns the result of invoking [- compare:options:](<compare(__options_).md>) with `NSCaseInsensitiveSearch` as the only option.
- [- localizedCaseInsensitiveCompare:](<localizedcaseinsensitivecompare(__).md>) — Compares the string with a given string using a case-insensitive, localized, comparison.
- [- compare:](<compare(__).md>) — Returns the result of invoking [- compare:options:range:](<compare(__options_range_).md>) with no options and the receiver’s full extent as the range.
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
