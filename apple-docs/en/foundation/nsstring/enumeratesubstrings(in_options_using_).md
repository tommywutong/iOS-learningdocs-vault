---
title: 'enumerateSubstrings(in:options:using:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/enumeratesubstrings(in:options:using:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/enumeratesubstrings(in:options:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/enumeratesubstrings%28in%3Aoptions%3Ausing%3A%29.json'
content_hash: 'sha256:39f4f65347ff5729'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# enumerateSubstrings(in:options:using:)

<sub>Instance Method</sub>

Enumerates the substrings of the specified type in the specified range of the string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func enumerateSubstrings(in range: NSRange, options opts: NSString.EnumerationOptions = [], using block: @escaping (String?, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)
```

## Parameters

- `range` — The range within the string to enumerate substrings.

- `opts` — Options specifying types of substrings and enumeration styles.

- `block` — The block executed for the enumeration. The block takes four arguments: - **substring** — The enumerated string. - **substringRange** — The range of the enumerated string in the receiver. - **enclosingRange** — The range that includes the substring as well as any separator or filler characters that follow. For instance, for lines, `enclosingRange` contains the line terminators. The `enclosingRange` for the first string enumerated also contains any characters that occur before the string. Consecutive enclosing ranges are guaranteed not to overlap, and every single character in the enumerated range is included in one and only one enclosing range. - **stop** — A reference to a Boolean value that the block can use to stop the enumeration by setting `*stop = YES`; it should not touch `*stop` otherwise.

## Discussion

If this method is sent to an instance of `NSMutableString`, mutation (deletion, addition, or change) is allowed, as long as it is within `enclosingRange`. After a mutation, the enumeration continues with the range immediately following the processed range, after the length of the processed range is adjusted for the mutation. (The enumerator assumes any change in length occurs in the specified range.)

For example, if the block is called with a range starting at location N, and the block deletes all the characters in the supplied range, the next call will also pass N as the index of the range. This is the case even if mutation of the previous range changes the string in such a way that the following substring would have extended to include the already enumerated range. For example, if the string “Hello World” is enumerated via words, and the block changes “Hello “ to “Hello”, thus forming “HelloWorld”, the next enumeration will return “World” rather than “HelloWorld”.

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
- [- enumerateLinesUsingBlock:](<enumeratelines(__).md>) — Enumerates all the lines in the string.
