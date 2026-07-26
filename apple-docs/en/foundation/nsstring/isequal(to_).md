---
title: 'isEqual(to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/isequal(to:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/isequal(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/isequal%28to%3A%29.json'
content_hash: 'sha256:4ff8c9f6b26be088'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# isEqual(to:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether a given string is equal to the receiver using a literal Unicode-based comparison.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isEqual(to aString: String) -> Bool
```

## Parameters

- `aString` — The string with which to compare the receiver.

## Return Value

[true](../../swift/true.md) if `aString` is equivalent to the receiver (if they have the same id or if they are `NSOrderedSame` in a literal comparison), otherwise [false](../../swift/false.md).

## Discussion

The comparison uses the canonical representation of strings, which for a particular string is the length of the string plus the UTF-16 code units that make up the string. When this method compares two strings, if the individual Unicodes are the same, then the strings are equal, regardless of the backing store. “Literal” when applied to string comparison means that various Unicode decomposition rules are not applied and UTF-16 code units are individually compared. So, for instance, “Ö” represented as the composed character sequence “O” (`U+004F LATIN CAPITAL LETTER O`) and a combining diaeresis “¨” (`U+0308 COMBINING DIAERESIS`) would not compare equal to “Ö” represented as a single Unicode character (`U+00D6 LATIN CAPITAL LETTER O WITH DIAERESIS`).

### Special Considerations

When you know both objects are strings, this method is a faster way to check equality than [isEqual(_:)](<../../objectivec/nsobjectprotocol/isequal(__).md>).

## See Also

### Identifying and Comparing Strings

- [- caseInsensitiveCompare:](<caseinsensitivecompare(__).md>) — Returns the result of invoking [- compare:options:](<compare(__options_).md>) with `NSCaseInsensitiveSearch` as the only option.
- [- localizedCaseInsensitiveCompare:](<localizedcaseinsensitivecompare(__).md>) — Compares the string with a given string using a case-insensitive, localized, comparison.
- [- compare:](<compare(__).md>) — Returns the result of invoking [- compare:options:range:](<compare(__options_range_).md>) with no options and the receiver’s full extent as the range.
- [- localizedCompare:](<localizedcompare(__).md>) — Compares the string and a given string using a localized comparison.
- [- compare:options:](<compare(__options_).md>) — Compares the string with the specified string using the given options.
- [- compare:options:range:](<compare(__options_range_).md>) — Returns the result of invoking [- compare:options:range:locale:](<compare(__options_range_locale_).md>) with a `nil` locale.
- [- compare:options:range:locale:](<compare(__options_range_locale_).md>) — Compares the string using the specified options and returns the lexical ordering for the range.
- [- localizedStandardCompare:](<localizedstandardcompare(__).md>) — Compares strings as sorted by the Finder.
- [- hasPrefix:](<hasprefix(__).md>) — Returns a Boolean value that indicates whether a given string matches the beginning characters of the receiver.
- [- hasSuffix:](<hassuffix(__).md>) — Returns a Boolean value that indicates whether a given string matches the ending characters of the receiver.
- [hash](hash.md) — An unsigned integer that can be used as a hash table address.
- [CompareOptions](compareoptions.md) — These values represent the options available to many of the string classes’ search and comparison methods.
- [EncodingConversionOptions](encodingconversionoptions.md) — Options for converting string encodings.
