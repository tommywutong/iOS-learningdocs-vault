---
title: 'localizedStandardRange(of:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/localizedstandardrange(of:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/localizedstandardrange(of:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/localizedstandardrange%28of%3A%29.json'
content_hash: 'sha256:43edffea35dade20'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# localizedStandardRange(of:)

<sub>Instance Method</sub>

Finds and returns the range of the first occurrence of a given string within the string by performing a case and diacritic insensitive, locale-aware search.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func localizedStandardRange(of str: String) -> NSRange
```

## Parameters

- `str` — The string to search for. This value must not be `nil`.

## Return Value

The range of the first occurrence of `str` in the receiver. Returns `{``NSNotFound``, 0}` if `str` is not found.

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
- [- rangeOfString:options:range:locale:](<range(of_options_range_locale_).md>) — Finds and returns the range of the first occurrence of a given string within a given range of the string, subject to given options, using the specified locale, if any.
- [- enumerateLinesUsingBlock:](<enumeratelines(__).md>) — Enumerates all the lines in the string.
- [- enumerateSubstringsInRange:options:usingBlock:](<enumeratesubstrings(in_options_using_).md>) — Enumerates the substrings of the specified type in the specified range of the string.
