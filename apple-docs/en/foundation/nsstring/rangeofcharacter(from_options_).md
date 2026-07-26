---
title: 'rangeOfCharacter(from:options:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/rangeofcharacter(from:options:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/rangeofcharacter(from:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/rangeofcharacter%28from%3Aoptions%3A%29.json'
content_hash: 'sha256:195695d72a16163d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# rangeOfCharacter(from:options:)

<sub>Instance Method</sub>

Finds and returns the range in the string of the first character, using given options, from a given character set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func rangeOfCharacter(from searchSet: CharacterSet, options mask: NSString.CompareOptions = []) -> NSRange
```

## Parameters

- `searchSet` — A character set. This value must not be `nil`. Raises an `NSInvalidArgumentException` if `aSet` is `nil`.

- `mask` — A mask specifying search options. The following options may be specified by combining them with the C bitwise `OR` operator: [NSAnchoredSearch](compareoptions/anchored.md), [NSBackwardsSearch](compareoptions/backwards.md).

## Return Value

The range in the receiver of the first character found from `aSet`. Returns a range of `{``NSNotFound``, 0}` if none of the characters in `aSet` are found.

## Discussion

Invokes [- rangeOfCharacterFromSet:options:range:](<rangeofcharacter(from_options_range_).md>) with `mask` for the options and the entire extent of the receiver for the range.

## See Also

### Finding Characters and Substrings

- [- containsString:](<contains(__).md>) — Returns a Boolean value indicating whether the string contains a given string by performing a case-sensitive, locale-unaware search.
- [- localizedCaseInsensitiveContainsString:](<localizedcaseinsensitivecontains(__).md>) — Returns a Boolean value indicating whether the string contains a given string by performing a case-insensitive, locale-aware search.
- [- localizedStandardContainsString:](<localizedstandardcontains(__).md>) — Returns a Boolean value indicating whether the string contains a given string by performing a case and diacritic insensitive, locale-aware search.
- [- rangeOfCharacterFromSet:](<rangeofcharacter(from_).md>) — Finds and returns the range in the string of the first character from a given character set.
- [- rangeOfCharacterFromSet:options:range:](<rangeofcharacter(from_options_range_).md>) — Finds and returns the range in the string of the first character from a given character set found in a given range with given options.
- [- rangeOfString:](<range(of_).md>) — Finds and returns the range of the first occurrence of a given string within the string.
- [- rangeOfString:options:](<range(of_options_).md>) — Finds and returns the range of the first occurrence of a given string within the string, subject to given options.
- [- rangeOfString:options:range:](<range(of_options_range_).md>) — Finds and returns the range of the first occurrence of a given string, within the given range of the string, subject to given options.
- [- rangeOfString:options:range:locale:](<range(of_options_range_locale_).md>) — Finds and returns the range of the first occurrence of a given string within a given range of the string, subject to given options, using the specified locale, if any.
- [- localizedStandardRangeOfString:](<localizedstandardrange(of_).md>) — Finds and returns the range of the first occurrence of a given string within the string by performing a case and diacritic insensitive, locale-aware search.
- [- enumerateLinesUsingBlock:](<enumeratelines(__).md>) — Enumerates all the lines in the string.
- [- enumerateSubstringsInRange:options:usingBlock:](<enumeratesubstrings(in_options_using_).md>) — Enumerates the substrings of the specified type in the specified range of the string.
