---
title: 'enumerateLines(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/enumeratelines(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/enumeratelines(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/enumeratelines%28_%3A%29.json'
content_hash: 'sha256:0ade3928a00416b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# enumerateLines(_:)

<sub>Instance Method</sub>

Enumerates all the lines in the string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func enumerateLines(_ block: @escaping (String, UnsafeMutablePointer<ObjCBool>) -> Void)
```

## Parameters

- `block` — The block executed for the enumeration. The block takes two arguments: - **line** — The current line of the string being enumerated. The line contains just the contents of the line, without the line terminators. See [- getLineStart:end:contentsEnd:forRange:](<getlinestart(__end_contentsend_for_).md>) for a discussion of line terminators. - **stop** — A reference to a Boolean value that the block can use to stop the enumeration by setting `*stop = YES`; it should not touch `*stop` otherwise.

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
- [- localizedStandardRangeOfString:](<localizedstandardrange(of_).md>) — Finds and returns the range of the first occurrence of a given string within the string by performing a case and diacritic insensitive, locale-aware search.
- [- enumerateSubstringsInRange:options:usingBlock:](<enumeratesubstrings(in_options_using_).md>) — Enumerates the substrings of the specified type in the specified range of the string.
