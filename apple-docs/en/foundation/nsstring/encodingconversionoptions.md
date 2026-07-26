---
title: NSString.EncodingConversionOptions
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsstring/encodingconversionoptions
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/encodingconversionoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/encodingconversionoptions.json'
content_hash: 'sha256:c1a0b0ef727d4669'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# NSString.EncodingConversionOptions

<sub>Structure</sub>

Options for converting string encodings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct EncodingConversionOptions
```

## Overview

These constants are available in OS X v10.4; they are, however, differently named:

```objc
typedef enum {
    NSAllowLossyEncodingConversion = 1,
    NSExternalRepresentationEncodingConversion = 2
} NSStringEncodingConversionOptions;
```

You can use them in OS X v10.4 if you define the symbols as `extern` constants.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Constants

- [NSStringEncodingConversionAllowLossy](encodingconversionoptions/allowlossy.md) — Allows lossy conversion.
- [NSStringEncodingConversionExternalRepresentation](encodingconversionoptions/externalrepresentation.md) — Specifies an external representation (with a byte-order mark, if necessary, to indicate endianness).

### Initializers

- [init(rawValue:)](<encodingconversionoptions/init(rawvalue_).md>)

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
- [- isEqualToString:](<isequal(to_).md>) — Returns a Boolean value that indicates whether a given string is equal to the receiver using a literal Unicode-based comparison.
- [hash](hash.md) — An unsigned integer that can be used as a hash table address.
- [CompareOptions](compareoptions.md) — These values represent the options available to many of the string classes’ search and comparison methods.
