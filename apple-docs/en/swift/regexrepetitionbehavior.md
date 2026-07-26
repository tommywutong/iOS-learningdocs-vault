---
title: RegexRepetitionBehavior
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/regexrepetitionbehavior
source_url: 'https://developer.apple.com/documentation/swift/regexrepetitionbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/regexrepetitionbehavior.json'
content_hash: 'sha256:e9bcbb324c9910d4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# RegexRepetitionBehavior

<sub>Structure</sub>

Specifies how much to attempt to match when using a quantifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct RegexRepetitionBehavior
```

## Overview

See [repetitionBehavior(_:)](<regex/repetitionbehavior(__).md>) for more about specifying the default matching behavior for all or part of a regex.

## Relationships

- **Conforms To**: [Equatable](equatable.md), [Hashable](hashable.md)

## Topics

### Operators

- [==(_:_:)](<regexrepetitionbehavior/==(____).md>) — Returns a Boolean value indicating whether two values are equal.

### Instance Properties

- [hashValue](regexrepetitionbehavior/hashvalue.md) — The hash value.

### Instance Methods

- [hash(into:)](<regexrepetitionbehavior/hash(into_).md>) — Hashes the essential components of this value by feeding them into the given hasher.

### Type Properties

- [eager](regexrepetitionbehavior/eager.md) — Match as much of the input string as possible, backtracking when necessary.
- [possessive](regexrepetitionbehavior/possessive.md) — Match as much of the input string as possible, performing no backtracking.
- [reluctant](regexrepetitionbehavior/reluctant.md) — Match as little of the input string as possible, expanding the matched region as necessary to complete a match.

### Default Implementations

- [Equatable Implementations](regexrepetitionbehavior/equatable-implementations.md)

## See Also

### Regular Expressions

- [Regex](regex.md) — A regular expression.
- [RegexSemanticLevel](regexsemanticlevel.md) — A semantic level to use during regex matching.
- [RegexWordBoundaryKind](regexwordboundarykind.md) — A word boundary algorithm to use during regex matching.
- [AnyRegexOutput](anyregexoutput.md) — The type-erased, dynamic output of a regular expression match.
- [RegexComponent](regexcomponent.md) — A type that represents a regular expression.
- [CustomConsumingRegexComponent](customconsumingregexcomponent.md)
