---
title: StringProtocol
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/stringprotocol
source_url: 'https://developer.apple.com/documentation/swift/stringprotocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/stringprotocol.json'
content_hash: 'sha256:80b26b40448545c5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# StringProtocol

<sub>Protocol</sub>

A type that can represent a string as a collection of characters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol StringProtocol : BidirectionalCollection, Comparable, ExpressibleByStringInterpolation, Hashable, LosslessStringConvertible, TextOutputStream, TextOutputStreamable where Self.Element == Character, Self.Index == String.Index, Self.StringInterpolation == DefaultStringInterpolation, Self.SubSequence : StringProtocol
```

## Overview

Do not declare new conformances to `StringProtocol`. Only the `String` and `Substring` types in the standard library are valid conforming types.

## Relationships

- **Inherits From**: [BidirectionalCollection](bidirectionalcollection.md), [Collection](collection.md), [Comparable](comparable.md), [CustomStringConvertible](customstringconvertible.md), [Equatable](equatable.md), [ExpressibleByExtendedGraphemeClusterLiteral](expressiblebyextendedgraphemeclusterliteral.md), [ExpressibleByStringInterpolation](expressiblebystringinterpolation.md), [ExpressibleByStringLiteral](expressiblebystringliteral.md), [ExpressibleByUnicodeScalarLiteral](expressiblebyunicodescalarliteral.md), [Hashable](hashable.md), [LosslessStringConvertible](losslessstringconvertible.md), [Sequence](sequence.md), [TextOutputStream](textoutputstream.md), [TextOutputStreamable](textoutputstreamable.md)

- **Conforming Types**: [String](string.md), [Substring](substring.md)

## Topics

### Operators

- [!=(_:_:)](<stringprotocol/!=(____).md>)

### Associated Types

- [SubSequence](stringprotocol/subsequence.md) — A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
- [UTF16View](stringprotocol/utf16view.md)
- [UTF8View](stringprotocol/utf8view.md)
- [UnicodeScalarView](stringprotocol/unicodescalarview.md)

### Initializers

- [init(cString:)](<stringprotocol/init(cstring_).md>) — Creates a string from the null-terminated, UTF-8 encoded sequence of bytes at the given pointer.
- [init(decoding:as:)](<stringprotocol/init(decoding_as_).md>) — Creates a string from the given Unicode code units in the specified encoding.
- [init(decodingCString:as:)](<stringprotocol/init(decodingcstring_as_).md>) — Creates a string from the null-terminated sequence of bytes at the given pointer.

### Instance Properties

- [capitalized](stringprotocol/capitalized.md) — A copy of the string with each word changed to its corresponding capitalized spelling.
- [decomposedStringWithCanonicalMapping](stringprotocol/decomposedstringwithcanonicalmapping.md) — A string created by normalizing the string’s contents using Form D.
- [decomposedStringWithCompatibilityMapping](stringprotocol/decomposedstringwithcompatibilitymapping.md) — A string created by normalizing the string’s contents using Form KD.
- [fastestEncoding](stringprotocol/fastestencoding.md) — The fastest encoding to which the string can be converted without loss of information.
- [hash](stringprotocol/hash.md) — An unsigned integer that can be used as a hash table address.
- [localizedCapitalized](stringprotocol/localizedcapitalized.md) — A capitalized representation of the string that is produced using the current locale.
- [localizedLowercase](stringprotocol/localizedlowercase.md) — A lowercase version of the string that is produced using the current locale.
- [localizedUppercase](stringprotocol/localizeduppercase.md) — An uppercase version of the string that is produced using the current locale.
- [precomposedStringWithCanonicalMapping](stringprotocol/precomposedstringwithcanonicalmapping.md) — A string created by normalizing the string’s contents using Form C.
- [precomposedStringWithCompatibilityMapping](stringprotocol/precomposedstringwithcompatibilitymapping.md) — A string created by normalizing the string’s contents using Form KC.
- [removingPercentEncoding](stringprotocol/removingpercentencoding.md) — Returns a new string created by replacing all percent-encoded sequences with the matching UTF-8 characters.
- [smallestEncoding](stringprotocol/smallestencoding.md) — The smallest encoding to which the string can be converted without loss of information.
- [unicodeScalars](stringprotocol/unicodescalars.md)
- [utf16](stringprotocol/utf16.md)
- [utf8](stringprotocol/utf8.md)

### Instance Methods

- [addingPercentEncoding(withAllowedCharacters:)](<stringprotocol/addingpercentencoding(withallowedcharacters_).md>) — Returns a new string created by replacing all characters not in the specified set with percent-encoded characters.
- [appending(_:)](<stringprotocol/appending(__).md>) — Returns a new string created by appending the given string.
- [appendingFormat(_:_:)](<stringprotocol/appendingformat(____).md>) — Returns a string created by appending a string constructed from a given format string and the following arguments.
- [applyingTransform(_:reverse:)](<stringprotocol/applyingtransform(__reverse_).md>) — Perform string transliteration.
- [cString(using:)](<stringprotocol/cstring(using_).md>) — Returns a representation of the string as a C string using a given encoding.
- [canBeConverted(to:)](<stringprotocol/canbeconverted(to_).md>) — Returns a Boolean value that indicates whether the string can be converted to the specified encoding without loss of information.
- [capitalized(with:)](<stringprotocol/capitalized(with_).md>) — Returns a capitalized representation of the string using the specified locale.
- [caseInsensitiveCompare(_:)](<stringprotocol/caseinsensitivecompare(__).md>) — Returns the result of invoking `compare:options:` with `NSCaseInsensitiveSearch` as the only option.
- [commonPrefix(with:options:)](<stringprotocol/commonprefix(with_options_).md>) — Returns a string containing characters this string and the given string have in common, starting from the beginning of each up to the first characters that aren’t equivalent.
- [compare(_:options:range:locale:)](<stringprotocol/compare(__options_range_locale_).md>) — Compares the string using the specified options and returns the lexical ordering for the range.
- [completePath(into:caseSensitive:matchesInto:filterTypes:)](<stringprotocol/completepath(into_casesensitive_matchesinto_filtertypes_).md>) — Interprets the string as a path in the file system and attempts to perform filename completion, returning a numeric value that indicates whether a match was possible, and by reference the longest path that matches the string.
- [components(separatedBy:)](<stringprotocol/components(separatedby_)-4j26n.md>) — Returns an array containing substrings from the string that have been divided by characters in the given set.
- [components(separatedBy:)](<stringprotocol/components(separatedby_)-8gl9t.md>) — Returns an array containing substrings from the string that have been divided by the given separator.
- [contains(_:)](<stringprotocol/contains(__)-40kbf.md>) — Returns `true` if `other` is non-empty and contained within `self` by case-sensitive, non-literal search. Otherwise, returns `false`.
- [contains(_:)](<stringprotocol/contains(__)-78f5t.md>)
- [contains(_:)](<stringprotocol/contains(__)-78p35.md>)
- [data(using:allowLossyConversion:)](<stringprotocol/data(using_allowlossyconversion_).md>) — Returns a `Data` containing a representation of the `String` encoded using a given encoding.
- [dataDetectorMatches(_:options:)](<stringprotocol/datadetectormatches(__options_).md>) — Searches for known data types in a string or a substring.
- [enumerateLines(invoking:)](<stringprotocol/enumeratelines(invoking_).md>) — Enumerates all the lines in a string.
- [enumerateLinguisticTags(in:scheme:options:orthography:invoking:)](<stringprotocol/enumeratelinguistictags(in_scheme_options_orthography_invoking_).md>) — Performs linguistic analysis on the specified string by enumerating the specific range of the string, providing the Block with the located tags.
- [enumerateSubstrings(in:options:_:)](<stringprotocol/enumeratesubstrings(in_options___).md>) — Enumerates the substrings of the specified type in the specified range of the string.
- [folding(options:locale:)](<stringprotocol/folding(options_locale_).md>) — Returns a string with the given character folding options applied.
- [getBytes(_:maxLength:usedLength:encoding:options:range:remaining:)](<stringprotocol/getbytes(__maxlength_usedlength_encoding_options_range_remaining_).md>) — Writes the given `range` of characters into `buffer` in a given `encoding`, without any allocations.  Does not NULL-terminate.
- [getCString(_:maxLength:encoding:)](<stringprotocol/getcstring(__maxlength_encoding_).md>) — Converts the `String`’s content to a given encoding and stores them in a buffer.
- [getLineStart(_:end:contentsEnd:for:)](<stringprotocol/getlinestart(__end_contentsend_for_).md>) — Returns by reference the beginning of the first line and the end of the last line touched by the given range.
- [getParagraphStart(_:end:contentsEnd:for:)](<stringprotocol/getparagraphstart(__end_contentsend_for_).md>) — Returns by reference the beginning of the first paragraph and the end of the last paragraph touched by the given range.
- [hasPrefix(_:)](<stringprotocol/hasprefix(__).md>)
- [hasSuffix(_:)](<stringprotocol/hassuffix(__).md>)
- [lengthOfBytes(using:)](<stringprotocol/lengthofbytes(using_).md>) — Returns the number of bytes required to store the `String` in a given encoding.
- [lineRange(for:)](<stringprotocol/linerange(for_).md>) — Returns the range of characters representing the line or lines containing a given range.
- [linguisticTags(in:scheme:options:orthography:tokenRanges:)](<stringprotocol/linguistictags(in_scheme_options_orthography_tokenranges_).md>) — Returns an array of linguistic tags for the specified range and requested tags within the receiving string.
- [localizedCaseInsensitiveCompare(_:)](<stringprotocol/localizedcaseinsensitivecompare(__).md>) — Compares the string and the given string using a case-insensitive, localized, comparison.
- [localizedCaseInsensitiveContains(_:)](<stringprotocol/localizedcaseinsensitivecontains(__).md>) — Returns a Boolean value indicating whether the given string is non-empty and contained within this string by case-insensitive, non-literal search, taking into account the current locale.
- [localizedCompare(_:)](<stringprotocol/localizedcompare(__).md>) — Compares the string and the given string using a localized comparison.
- [localizedStandardCompare(_:)](<stringprotocol/localizedstandardcompare(__).md>) — Compares the string and the given string as sorted by the Finder.
- [localizedStandardContains(_:)](<stringprotocol/localizedstandardcontains(__).md>) — Returns a Boolean value indicating whether the string contains the given string, taking the current locale into account.
- [localizedStandardRange(of:)](<stringprotocol/localizedstandardrange(of_).md>) — Finds and returns the range of the first occurrence of a given string, taking the current locale into account.  Returns `nil` if the string was not found.
- [lowercased()](<stringprotocol/lowercased().md>)
- [lowercased(with:)](<stringprotocol/lowercased(with_).md>) — Returns a version of the string with all letters converted to lowercase, taking into account the specified locale.
- [maximumLengthOfBytes(using:)](<stringprotocol/maximumlengthofbytes(using_).md>) — Returns the maximum number of bytes needed to store the `String` in a given encoding.
- [padding(toLength:withPad:startingAt:)](<stringprotocol/padding(tolength_withpad_startingat_).md>) — Returns a new string formed from the `String` by either removing characters from the end, or by appending as many occurrences as necessary of a given pad string.
- [paragraphRange(for:)](<stringprotocol/paragraphrange(for_).md>) — Returns the range of characters representing the paragraph or paragraphs containing a given range.
- [propertyList()](<stringprotocol/propertylist().md>) — Parses the `String` as a text representation of a property list, returning an NSString, NSData, NSArray, or NSDictionary object, according to the topmost element.
- [propertyListFromStringsFileFormat()](<stringprotocol/propertylistfromstringsfileformat().md>) — Returns a dictionary object initialized with the keys and values found in the `String`.
- [range(of:options:range:locale:)](<stringprotocol/range(of_options_range_locale_).md>) — Finds and returns the range of the first occurrence of a given string within a given range of the `String`, subject to given options, using the specified locale, if any.
- [rangeOfCharacter(from:options:range:)](<stringprotocol/rangeofcharacter(from_options_range_).md>) — Finds and returns the range in the `String` of the first character from a given character set found in a given range with given options.
- [rangeOfComposedCharacterSequence(at:)](<stringprotocol/rangeofcomposedcharactersequence(at_).md>) — Returns the range in the `String` of the composed character sequence located at a given index.
- [rangeOfComposedCharacterSequences(for:)](<stringprotocol/rangeofcomposedcharactersequences(for_).md>) — Returns the range in the string of the composed character sequences for a given range.
- [replacingCharacters(in:with:)](<stringprotocol/replacingcharacters(in_with_).md>) — Returns a new string in which the characters in a specified range of the `String` are replaced by a given string.
- [replacingOccurrences(of:with:options:range:)](<stringprotocol/replacingoccurrences(of_with_options_range_).md>) — Returns a new string in which all occurrences of a target string in a specified range of the string are replaced by another given string.
- [split(separator:maxSplits:omittingEmptySubsequences:)](<stringprotocol/split(separator_maxsplits_omittingemptysubsequences_)-7mfus.md>)
- [split(separator:maxSplits:omittingEmptySubsequences:)](<stringprotocol/split(separator_maxsplits_omittingemptysubsequences_)-8wzc1.md>)
- [substring(from:)](<stringprotocol/substring(from_).md>) — Returns a new string containing the characters of the `String` from the one at a given index to the end.
- [substring(to:)](<stringprotocol/substring(to_).md>) — Returns a new string containing the characters of the `String` up to, but not including, the one at a given index.
- [substring(with:)](<stringprotocol/substring(with_).md>) — Returns a string object containing the characters of the `String` that lie within a given range.
- [trimmingCharacters(in:)](<stringprotocol/trimmingcharacters(in_).md>) — Returns a new string made by removing from both ends of the `String` characters contained in a given character set.
- [uppercased()](<stringprotocol/uppercased().md>)
- [uppercased(with:)](<stringprotocol/uppercased(with_).md>) — Returns a version of the string with all letters converted to uppercase, taking into account the specified locale.
- [withCString(_:)](<stringprotocol/withcstring(__).md>) — Calls the given closure with a pointer to the contents of the string, represented as a null-terminated sequence of UTF-8 code units.
- [withCString(encodedAs:_:)](<stringprotocol/withcstring(encodedas___).md>) — Calls the given closure with a pointer to the contents of the string, represented as a null-terminated sequence of code units.
- [write(to:atomically:encoding:)](<stringprotocol/write(to_atomically_encoding_).md>) — Writes the contents of the `String` to the URL specified by url using the specified encoding.
- [write(toFile:atomically:encoding:)](<stringprotocol/write(tofile_atomically_encoding_).md>) — Writes the contents of the `String` to a file at a given path using a given encoding.

## See Also

### Related String Types

- [Substring](substring.md) — A slice of a string.
- [Index](string/index.md) — A position of a character or code unit in a string.
- [UnicodeScalarView](string/unicodescalarview.md) — A view of a string’s contents as a collection of Unicode scalar values.
- [UTF16View](string/utf16view.md) — A view of a string’s contents as a collection of UTF-16 code units.
- [UTF8View](string/utf8view.md) — A view of a string’s contents as a collection of UTF-8 code units.
- [Iterator](string/iterator.md) — A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [Encoding](string/encoding.md)
