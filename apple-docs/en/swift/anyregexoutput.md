---
title: AnyRegexOutput
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/anyregexoutput
source_url: 'https://developer.apple.com/documentation/swift/anyregexoutput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anyregexoutput.json'
content_hash: 'sha256:bee58fe7f3f2fb41'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# AnyRegexOutput

<sub>Structure</sub>

The type-erased, dynamic output of a regular expression match.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AnyRegexOutput
```

## Overview

When you find a match using regular expression that has `AnyRegexOutput` as its output type, you can find information about matches by iterating

## Relationships

- **Conforms To**: [BidirectionalCollection](bidirectionalcollection.md), [Collection](collection.md), [Copyable](copyable.md), [Escapable](escapable.md), [RandomAccessCollection](randomaccesscollection.md), [Sequence](sequence.md)

## Topics

### Initializers

- [init(_:)](<anyregexoutput/init(__).md>) — Creates a dynamic regular expression match output from an existing match.

### Instance Methods

- [extractValues(as:)](<anyregexoutput/extractvalues(as_).md>) — Returns strongly-typed match output by converting this type-erased output to the specified type, if possible.

### Subscripts

- [subscript(_:)](<anyregexoutput/subscript(__)-6qdcr.md>) — Accesses the capture with the specified name, if a capture with that name exists.

### Default Implementations

- [BidirectionalCollection Implementations](anyregexoutput/bidirectionalcollection-implementations.md)
- [Collection Implementations](anyregexoutput/collection-implementations.md)
- [RandomAccessCollection Implementations](anyregexoutput/randomaccesscollection-implementations.md)
- [Sequence Implementations](anyregexoutput/sequence-implementations.md)

## See Also

### Regular Expressions

- [Regex](regex.md) — A regular expression.
- [RegexRepetitionBehavior](regexrepetitionbehavior.md) — Specifies how much to attempt to match when using a quantifier.
- [RegexSemanticLevel](regexsemanticlevel.md) — A semantic level to use during regex matching.
- [RegexWordBoundaryKind](regexwordboundarykind.md) — A word boundary algorithm to use during regex matching.
- [RegexComponent](regexcomponent.md) — A type that represents a regular expression.
- [CustomConsumingRegexComponent](customconsumingregexcomponent.md)
