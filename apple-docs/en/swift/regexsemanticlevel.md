---
title: RegexSemanticLevel
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/regexsemanticlevel
source_url: 'https://developer.apple.com/documentation/swift/regexsemanticlevel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/regexsemanticlevel.json'
content_hash: 'sha256:e23cde5316707ff9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# RegexSemanticLevel

<sub>Structure</sub>

A semantic level to use during regex matching.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct RegexSemanticLevel
```

## Overview

The semantic level determines whether a regex matches with the same character-based semantics as string comparisons or by matching individual Unicode scalar values. See [matchingSemantics(_:)](<regex/matchingsemantics(__).md>) for more about changing the semantic level for all or part of a regex.

## Relationships

- **Conforms To**: [Equatable](equatable.md), [Hashable](hashable.md)

## Topics

### Operators

- [==(_:_:)](<regexsemanticlevel/==(____).md>) — Returns a Boolean value indicating whether two values are equal.

### Instance Properties

- [hashValue](regexsemanticlevel/hashvalue.md) — The hash value.

### Instance Methods

- [hash(into:)](<regexsemanticlevel/hash(into_).md>) — Hashes the essential components of this value by feeding them into the given hasher.

### Type Properties

- [graphemeCluster](regexsemanticlevel/graphemecluster.md) — Match at the character level.
- [unicodeScalar](regexsemanticlevel/unicodescalar.md) — Match at the Unicode scalar level.

### Default Implementations

- [Equatable Implementations](regexsemanticlevel/equatable-implementations.md)

## See Also

### Regular Expressions

- [Regex](regex.md) — A regular expression.
- [RegexRepetitionBehavior](regexrepetitionbehavior.md) — Specifies how much to attempt to match when using a quantifier.
- [RegexWordBoundaryKind](regexwordboundarykind.md) — A word boundary algorithm to use during regex matching.
- [AnyRegexOutput](anyregexoutput.md) — The type-erased, dynamic output of a regular expression match.
- [RegexComponent](regexcomponent.md) — A type that represents a regular expression.
- [CustomConsumingRegexComponent](customconsumingregexcomponent.md)
