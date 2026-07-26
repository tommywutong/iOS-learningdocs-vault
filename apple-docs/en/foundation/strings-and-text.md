---
title: Strings and Text
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/strings-and-text
source_url: 'https://developer.apple.com/documentation/foundation/strings-and-text'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/strings-and-text.json'
content_hash: 'sha256:29ba24613ebaf4a6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# Strings and Text

<sub>API Collection</sub>

Create and process strings of Unicode characters, use regular expressions to find patterns, and perform natural language analysis of text.

## Topics

### Strings

- [String](../swift/string.md) — A Unicode string value that is a collection of characters.
- [String Encodings](1497293-string-encodings.md) — Constants for encoding standards used when converting raw data to and from string representations.

### Strings with Metadata

- [AttributedString](attributedstring.md) — A value type for a string with associated attributes for portions of its text.
- [AttributedSubstring](attributedsubstring.md) — A portion of an attributed string.
- [Attributed String Supporting Types](attributed-string-supporting-types.md) — Types that the attributed string, attributed substring, and helper types extend or conform to, for sharing common functionality.
- [NSAttributedString](nsattributedstring.md) — A string of text that manages data, layout, and stylistic information for ranges of characters to support rendering.
- [NSMutableAttributedString](nsmutableattributedstring.md) — A mutable string with associated attributes (such as visual style, hyperlinks, or accessibility data) for portions of its text.

### Characters

- [CharacterSet](characterset.md) — A set of Unicode character values for use in search operations.
- [UnicodeScalar](../swift/unicodescalar.md)

### Pattern Matching

- [Scanner](scanner.md) — A string parser that scans for substrings or characters in a character set, and for numeric values from decimal, hexadecimal, and floating-point representations.
- [NSRegularExpression](nsregularexpression.md) — An immutable representation of a compiled regular expression that you apply to Unicode strings.
- [NSDataDetector](nsdatadetector.md) — A specialized regular expression object that matches natural language text for predefined data patterns.
- [NSTextCheckingResult](nstextcheckingresult.md) — An occurrence of textual content found during the analysis of a block of text, such as when matching a regular expression.
- [NSNotFound](nsnotfound-4qp9h.md) — A value indicating that a requested item couldn’t be found or doesn’t exist.

### Spelling and Grammar

- [NSSpellServer](nsspellserver.md) — A server that your app uses to provide a spell checker service to other apps running in the system.
- [NSSpellServerDelegate](nsspellserverdelegate.md) — The optional methods implemented by the delegate of a spell server.

### Localization

- [Locale](locale.md) — Information about linguistic, cultural, and technological conventions for use in formatting data for presentation.
- [NSOrthography](nsorthography.md) — A description of the linguistic content of natural language text, typically used for spelling and grammar checking.
- [NSLocalizedString(_:tableName:bundle:value:comment:)](<nslocalizedstring(__tablename_bundle_value_comment_).md>) — Returns a localized string from a table that Xcode generates for you when exporting localizations.
- [LocalizedStringResource](localizedstringresource.md) — A reference to a localizable string, accessible from another process.
- [CustomLocalizedStringResourceConvertible](customlocalizedstringresourceconvertible.md) — A type that provides an out-of-process localizable description.
- [URLResource](urlresource.md) — A resource located at a particular file URL within a bundle.

### Deprecated

- [NSLinguisticTagger](nslinguistictagger.md) — Analyze natural language text to tag part of speech and lexical class, identify names, perform lemmatization, and determine the language and script. _(deprecated)_
- [Deprecated String Encodings](1497268-deprecated-string-encodings.md)

## See Also

### Fundamentals

- [Numbers, Data, and Basic Values](numbers-data-and-basic-values.md) — Work with primitive values and other fundamental types used throughout Cocoa.
- [Collections](collections.md) — Use arrays, dictionaries, sets, and specialized collections to store and iterate groups of objects or values.
- [Dates and Times](dates-and-times.md) — Compare dates and times, and perform calendar and time zone calculations.
- [Units and Measurement](units-and-measurement.md) — Label numeric quantities with physical dimensions to allow locale-aware formatting and conversion between related units.
- [Data Formatting](data-formatting.md) — Convert numbers, dates, measurements, and other values to and from locale-aware string representations.
- [Filters and Sorting](filters-and-sorting.md) — Use predicates, expressions, and sort descriptors to examine elements in collections and other services.
