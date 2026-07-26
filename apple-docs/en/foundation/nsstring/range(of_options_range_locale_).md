---
title: 'range(of:options:range:locale:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/range(of:options:range:locale:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/range(of:options:range:locale:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/range%28of%3Aoptions%3Arange%3Alocale%3A%29.json'
content_hash: 'sha256:f6d4ceeedb566fa2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# range(of:options:range:locale:)

<sub>Instance Method</sub>

Finds and returns the range of the first occurrence of a given string within a given range of the string, subject to given options, using the specified locale, if any.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func range(of searchString: String, options mask: NSString.CompareOptions = [], range rangeOfReceiverToSearch: NSRange, locale: Locale?) -> NSRange
```

## Parameters

- `searchString` — The string for which to search.

- `mask` — A mask specifying search options. The following options may be specified by combining them with the C bitwise `OR` operator: `NSCaseInsensitiveSearch`, `NSLiteralSearch`, `NSBackwardsSearch`, and `NSAnchoredSearch`. See [String Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/introStrings.html#//apple_ref/doc/uid/10000035i) for details on these options.

- `rangeOfReceiverToSearch` — The range within the receiver for which to search for `aString`. Raises an [NSRangeException](../nsexceptionname/rangeexception.md) if `aRange` is invalid.

- `locale` — The locale to use when comparing the receiver with `aString`. To use the current locale, pass [[NSLocale](../nslocale.md) [currentLocale](../nslocale/current.md)]. To use the system locale, pass `nil`. The locale argument affects the equality checking algorithm. For example, for the Turkish locale, case-insensitive compare matches “I” to “ı” (`U+0131 LATIN SMALL DOTLESS I`), not the normal “i” character.

## Return Value

An [NSRange](../nsrange-c.struct.md) structure giving the location and length in the receiver of `aString` within `aRange` in the receiver, modulo the options in `mask`. The range returned is relative to the start of the string, not to the passed-in range. Returns `{``NSNotFound``, 0}` if `aString` is not found or is empty (`""`).

## Discussion

`NSString` objects are compared by checking the Unicode canonical equivalence of their code point sequences.  The length of the returned range and that of `aString` may differ if equivalent composed character sequences are matched.

> [!important] Important
> When working with text that’s presented to the user, use the [- localizedStandardRangeOfString:](<localizedstandardrange(of_).md>) method instead.

### Special Considerations

This method detects all invalid ranges (including those with negative lengths). For applications linked against macOS 10.6 and later, this error causes an exception; for applications linked against earlier releases, this error causes a warning, which is displayed just once per application execution.

## See Also

### Finding Characters and Substrings

- [- containsString:](<contains(__).md>) — Returns a Boolean value indicating whether the string contains a given string by performing a case-sensitive, locale-unaware search.
- [- localizedCaseInsensitiveContainsString:](<localizedcaseinsensitivecontains(__).md>) — Returns a Boolean value indicating whether the string contains a given string by performing a case-insensitive, locale-aware search.
- [- localizedStandardContainsString:](<localizedstandardcontains(__).md>) — Returns a Boolean value indicating whether the string contains a given string by performing a case and diacritic insensitive, locale-aware search.
- [- rangeOfCharacterFromSet:](<rangeofcharacter(from_).md>) — Finds and returns the range in the string of the first character from a given character set.
- [- rangeOfCharacterFromSet:options:](<rangeofcharacter(from_options_).md>) — Finds and returns the range in the string of the first character, using given options, from a given character set.
- [- rangeOfCharacterFromSet:options:range:](<rangeofcharacter(from_options_range_).md>) — Finds and returns the range in the string of the first character from a given character set found in a given range with given options.
- [- rangeOfString:](<range(of_).md>) — Finds and returns the range of the first occurrence of a given string within the string.
- [- rangeOfString:options:](<range(of_options_).md>) — Finds and returns the range of the first occurrence of a given string within the string, subject to given options.
- [- rangeOfString:options:range:](<range(of_options_range_).md>) — Finds and returns the range of the first occurrence of a given string, within the given range of the string, subject to given options.
- [- localizedStandardRangeOfString:](<localizedstandardrange(of_).md>) — Finds and returns the range of the first occurrence of a given string within the string by performing a case and diacritic insensitive, locale-aware search.
- [- enumerateLinesUsingBlock:](<enumeratelines(__).md>) — Enumerates all the lines in the string.
- [- enumerateSubstringsInRange:options:usingBlock:](<enumeratesubstrings(in_options_using_).md>) — Enumerates the substrings of the specified type in the specified range of the string.
