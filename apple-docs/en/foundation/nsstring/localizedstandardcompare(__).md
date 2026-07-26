---
title: 'localizedStandardCompare(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/localizedstandardcompare(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/localizedstandardcompare(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/localizedstandardcompare%28_%3A%29.json'
content_hash: 'sha256:6f51481ebfd3a916'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# localizedStandardCompare(_:)

<sub>Instance Method</sub>

Compares strings as sorted by the Finder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func localizedStandardCompare(_ string: String) -> ComparisonResult
```

## Parameters

- `string` — The string to compare with the receiver.

## Return Value

The result of the comparison.

## Discussion

This method should be used whenever file names or other strings are presented in lists and tables where Finder-like sorting is appropriate. The exact sorting behavior of this method is different under different locales and may be changed in future releases. This method uses the current locale.

## See Also

### Identifying and Comparing Strings

- [- caseInsensitiveCompare:](<caseinsensitivecompare(__).md>) — Returns the result of invoking [- compare:options:](<compare(__options_).md>) with `NSCaseInsensitiveSearch` as the only option.
- [- localizedCaseInsensitiveCompare:](<localizedcaseinsensitivecompare(__).md>) — Compares the string with a given string using a case-insensitive, localized, comparison.
- [- compare:](<compare(__).md>) — Returns the result of invoking [- compare:options:range:](<compare(__options_range_).md>) with no options and the receiver’s full extent as the range.
- [- localizedCompare:](<localizedcompare(__).md>) — Compares the string and a given string using a localized comparison.
- [- compare:options:](<compare(__options_).md>) — Compares the string with the specified string using the given options.
- [- compare:options:range:](<compare(__options_range_).md>) — Returns the result of invoking [- compare:options:range:locale:](<compare(__options_range_locale_).md>) with a `nil` locale.
- [- compare:options:range:locale:](<compare(__options_range_locale_).md>) — Compares the string using the specified options and returns the lexical ordering for the range.
- [- hasPrefix:](<hasprefix(__).md>) — Returns a Boolean value that indicates whether a given string matches the beginning characters of the receiver.
- [- hasSuffix:](<hassuffix(__).md>) — Returns a Boolean value that indicates whether a given string matches the ending characters of the receiver.
- [- isEqualToString:](<isequal(to_).md>) — Returns a Boolean value that indicates whether a given string is equal to the receiver using a literal Unicode-based comparison.
- [hash](hash.md) — An unsigned integer that can be used as a hash table address.
- [CompareOptions](compareoptions.md) — These values represent the options available to many of the string classes’ search and comparison methods.
- [EncodingConversionOptions](encodingconversionoptions.md) — Options for converting string encodings.
