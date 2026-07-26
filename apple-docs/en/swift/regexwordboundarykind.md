---
title: RegexWordBoundaryKind
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/regexwordboundarykind
source_url: 'https://developer.apple.com/documentation/swift/regexwordboundarykind'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/regexwordboundarykind.json'
content_hash: 'sha256:58b40ac9a4fbe6e2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# RegexWordBoundaryKind

<sub>Structure</sub>

A word boundary algorithm to use during regex matching.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct RegexWordBoundaryKind
```

## Overview

See [wordBoundaryKind(_:)](<regex/wordboundarykind(__).md>) for information about specifying the word boundary kind for all or part of a regex.

## Relationships

- **Conforms To**: [Equatable](equatable.md), [Hashable](hashable.md)

## Topics

### Operators

- [==(_:_:)](<regexwordboundarykind/==(____).md>) — Returns a Boolean value indicating whether two values are equal.

### Instance Properties

- [hashValue](regexwordboundarykind/hashvalue.md) — The hash value.

### Instance Methods

- [hash(into:)](<regexwordboundarykind/hash(into_).md>) — Hashes the essential components of this value by feeding them into the given hasher.

### Type Properties

- [default](regexwordboundarykind/default.md) — A word boundary algorithm that implements the “default word boundary” Unicode recommendation.
- [simple](regexwordboundarykind/simple.md) — A word boundary algorithm that implements the “simple word boundary” Unicode recommendation.

### Default Implementations

- [Equatable Implementations](regexwordboundarykind/equatable-implementations.md)

## See Also

### Regular Expressions

- [Regex](regex.md) — A regular expression.
- [RegexRepetitionBehavior](regexrepetitionbehavior.md) — Specifies how much to attempt to match when using a quantifier.
- [RegexSemanticLevel](regexsemanticlevel.md) — A semantic level to use during regex matching.
- [AnyRegexOutput](anyregexoutput.md) — The type-erased, dynamic output of a regular expression match.
- [RegexComponent](regexcomponent.md) — A type that represents a regular expression.
- [CustomConsumingRegexComponent](customconsumingregexcomponent.md)
