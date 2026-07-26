---
title: CustomConsumingRegexComponent
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/customconsumingregexcomponent
source_url: 'https://developer.apple.com/documentation/swift/customconsumingregexcomponent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/customconsumingregexcomponent.json'
content_hash: 'sha256:1028fb97ad3ef636'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# CustomConsumingRegexComponent

<sub>Protocol</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol CustomConsumingRegexComponent : RegexComponent
```

## Relationships

- **Inherits From**: [RegexComponent](regexcomponent.md)

## Topics

### Instance Methods

- [consuming(_:startingAt:in:)](<customconsumingregexcomponent/consuming(__startingat_in_).md>) — Process the input string within the specified bounds, beginning at the given index, and return the end position (upper bound) of the match and the produced output.

## See Also

### Regular Expressions

- [Regex](regex.md) — A regular expression.
- [RegexRepetitionBehavior](regexrepetitionbehavior.md) — Specifies how much to attempt to match when using a quantifier.
- [RegexSemanticLevel](regexsemanticlevel.md) — A semantic level to use during regex matching.
- [RegexWordBoundaryKind](regexwordboundarykind.md) — A word boundary algorithm to use during regex matching.
- [AnyRegexOutput](anyregexoutput.md) — The type-erased, dynamic output of a regular expression match.
- [RegexComponent](regexcomponent.md) — A type that represents a regular expression.
