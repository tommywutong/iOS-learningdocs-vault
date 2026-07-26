---
title: Regex
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/regex
source_url: 'https://developer.apple.com/documentation/swift/regex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/regex.json'
content_hash: 'sha256:e6704821ec65873b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# Regex

<sub>Structure</sub>

A regular expression.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Regex<Output>
```

## Overview

Regular expressions are a concise way of describing a pattern, which can help you match or extract portions of a string. You can create a `Regex` instance using regular expression syntax, either in a regex literal or a string.

```swift
// 'keyAndValue' is created using a regex literal
let keyAndValue = /(.+?): (.+)/
// 'simpleDigits' is created from a pattern in a string
let simpleDigits = try Regex("[0-9]+")
```

You can use a `Regex` to search for a pattern in a string or substring. Call `contains(_:)` to check for the presence of a pattern, or `firstMatch(of:)` or `matches(of:)` to find matches.

```swift
let setting = "color: 161 103 230"
if setting.contains(simpleDigits) {
    print("'\(setting)' contains some digits.")
}
// Prints "'color: 161 103 230' contains some digits."
```

When you find a match, the resulting [Match](regex/match.md) type includes an [output](regex/match/output.md) property that contains the matched substring along with any captures:

```swift
if let match = setting.firstMatch(of: keyAndValue) {
    print("Key: \(match.1)")
    print("Value: \(match.2)")
}
// Key: color
// Value: 161 103 230
```

When you import the `RegexBuilder` module, you can also create `Regex` instances using a clear and flexible declarative syntax. Using this style, you can combine, capture, and transform regexes, `RegexBuilder` types, and custom parsers.

> [!note] Note
> Prior to Swift 6, you might need to write `#/myregex/#` instead of `/myregex/` when you make a regular expression using a literal. For more information, see [Regular Expression Literals](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/lexicalstructure/#Regular-Expression-Literals) in  _[The Swift Programming Language](https://docs.swift.org/swift-book/)_.

## Relationships

- **Conforms To**: [RegexComponent](regexcomponent.md)

## Topics

### Structures

- [Match](regex/match.md) — The result of matching a regular expression against a string.

### Initializers

- [init(_:)](<regex/init(__)-4ef55.md>) — Creates a regular expression using a RegexBuilder closure.
- [init(_:)](<regex/init(__)-52kg.md>) — Creates a regular expression from the given string, using a dynamic capture list.
- [init(_:)](<regex/init(__)-92siq.md>) — Creates a regular expression with a dynamic capture list from the given regular expression.
- [init(_:as:)](<regex/init(__as_)-2ucu7.md>) — Creates a regular expression with a strongly-typed capture list from the given regular expression.
- [init(_:as:)](<regex/init(__as_)-5z5nu.md>) — Creates a regular expression from the given string, using the specified capture type.
- [init(verbatim:)](<regex/init(verbatim_).md>) — Creates a regular expression that matches the given string exactly, as though every metacharacter in it was escaped.

### Instance Properties

- [regex](regex/regex.md) — The regular expression represented by this component.

### Instance Methods

- [anchorsMatchLineEndings(_:)](<regex/anchorsmatchlineendings(__).md>) — Returns a regular expression where the start and end of input anchors (`^` and `$`) also match against the start and end of a line.
- [asciiOnlyCharacterClasses(_:)](<regex/asciionlycharacterclasses(__).md>) — Returns a regular expression that matches only ASCII characters when matching character classes.
- [asciiOnlyDigits(_:)](<regex/asciionlydigits(__).md>) — Returns a regular expression that matches only ASCII characters as digits.
- [asciiOnlyWhitespace(_:)](<regex/asciionlywhitespace(__).md>) — Returns a regular expression that matches only ASCII characters as space characters.
- [asciiOnlyWordCharacters(_:)](<regex/asciionlywordcharacters(__).md>) — Returns a regular expression that matches only ASCII characters as word characters.
- [contains(captureNamed:)](<regex/contains(capturenamed_).md>) — Returns a Boolean value indicating whether a named capture with the given name exists.
- [dotMatchesNewlines(_:)](<regex/dotmatchesnewlines(__).md>) — Returns a regular expression where the “any” metacharacter (`.`) also matches against the start and end of a line.
- [firstMatch(in:)](<regex/firstmatch(in_)-45hz7.md>) — Returns the first match for this regex found in the given substring.
- [firstMatch(in:)](<regex/firstmatch(in_)-6s8x0.md>) — Returns the first match for this regex found in the given string.
- [ignoresCase(_:)](<regex/ignorescase(__).md>) — Returns a regular expression that ignores case when matching.
- [matchingSemantics(_:)](<regex/matchingsemantics(__).md>) — Returns a regular expression that matches with the specified semantic level.
- [prefixMatch(in:)](<regex/prefixmatch(in_)-1an24.md>) — Returns a match if this regex matches the given substring at its start.
- [prefixMatch(in:)](<regex/prefixmatch(in_)-5oh8i.md>) — Returns a match if this regex matches the given string at its start.
- [repetitionBehavior(_:)](<regex/repetitionbehavior(__).md>) — Returns a regular expression where quantifiers use the specified behavior by default.
- [wholeMatch(in:)](<regex/wholematch(in_)-8hr88.md>) — Returns a match if this regex matches the given substring in its entirety.
- [wholeMatch(in:)](<regex/wholematch(in_)-9do8t.md>) — Returns a match if this regex matches the given string in its entirety.
- [wordBoundaryKind(_:)](<regex/wordboundarykind(__).md>) — Returns a regular expression that uses the specified word boundary algorithm.

### Type Aliases

- [RegexOutput](regex/regexoutput.md) — The output type for this regular expression.

## See Also

### Regular Expressions

- [RegexRepetitionBehavior](regexrepetitionbehavior.md) — Specifies how much to attempt to match when using a quantifier.
- [RegexSemanticLevel](regexsemanticlevel.md) — A semantic level to use during regex matching.
- [RegexWordBoundaryKind](regexwordboundarykind.md) — A word boundary algorithm to use during regex matching.
- [AnyRegexOutput](anyregexoutput.md) — The type-erased, dynamic output of a regular expression match.
- [RegexComponent](regexcomponent.md) — A type that represents a regular expression.
- [CustomConsumingRegexComponent](customconsumingregexcomponent.md)
