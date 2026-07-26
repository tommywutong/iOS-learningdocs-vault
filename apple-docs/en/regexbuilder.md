---
title: RegexBuilder
framework: RegexBuilder
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/regexbuilder
source_url: 'https://developer.apple.com/documentation/regexbuilder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/regexbuilder.json'
content_hash: 'sha256:fa20ae80e04c9f12'
translated: false
---

> Navigation: [Technologies](technologies.md)

# RegexBuilder

<sub>Framework</sub>

Use an expressive domain-specific language to build regular expressions, for operations like searching and replacing in text.

## Overview

Regular expressions, also known as regexes, are a powerful tool for matching patterns in text. Swift supports several ways to create a regular expression, including from a string, as a literal, and using this DSL. For example:

```swift
let word = OneOrMore(.word)
let emailPattern = Regex {
    Capture {
        ZeroOrMore {
            word
            "."
        }
        word
    }
    "@"
    Capture {
        word
        OneOrMore {
            "."
            word
        }
    }
}

let text = "My email is my.name@example.com."
if let match = text.firstMatch(of: emailPattern) {
    let (wholeMatch, name, domain) = match.output
    // wholeMatch is "my.name@example.com"
    // name is "my.name"
    // domain is "example.com"
}
```

## Topics

### Components

- [CharacterClass](regexbuilder/characterclass.md) — A class of characters that match in a regex.
- [Anchor](regexbuilder/anchor.md) — A regex component that matches a specific condition at a particular position in an input string.
- [Lookahead](regexbuilder/lookahead.md) — A regex component that allows a match to continue only if its contents match at the given location.
- [NegativeLookahead](regexbuilder/negativelookahead.md) — A regex component that allows a match to continue only if its contents do not match at the given location.
- [ChoiceOf](regexbuilder/choiceof.md) — A regex component that chooses exactly one of its constituent regex components when matching.

### Quantifiers

- [One](regexbuilder/one.md) — A regex component that matches exactly one occurrence of its underlying component.
- [Optionally](regexbuilder/optionally.md) — A regex component that matches zero or one occurrences of its underlying component.
- [ZeroOrMore](regexbuilder/zeroormore.md) — A regex component that matches zero or more occurrences of its underlying component.
- [OneOrMore](regexbuilder/oneormore.md) — A regex component that matches one or more occurrences of its underlying component.
- [Repeat](regexbuilder/repeat.md) — A regex component that matches a selectable number of occurrences of its underlying component.
- [Local](regexbuilder/local.md) — A regex component that represents an atomic group.

### Captures

- [Capture](regexbuilder/capture.md) — A regex component that saves the matched substring, or a transformed result, for access in a regex match.
- [TryCapture](regexbuilder/trycapture.md) — A regex component that attempts to transform a matched substring, saving the result if successful and backtracking if the transformation fails.
- [Reference](regexbuilder/reference.md) — A reference to a captured portion of a regular expression.

### Builders

- [RegexComponentBuilder](regexbuilder/regexcomponentbuilder.md) — A custom parameter attribute that constructs regular expressions from closures.
- [AlternationBuilder](regexbuilder/alternationbuilder.md) — A custom parameter attribute that constructs regular expression alternations from closures.

### Operators

- [...(_:_:)](<regexbuilder/'...(____)-16g2a.md>) — Returns a character class that includes the characters in the given range.
- [...(_:_:)](<regexbuilder/'...(____)-629xh.md>) — Returns a character class that includes the Unicode scalars in the given range.
