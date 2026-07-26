---
title: CTUnderlineStyleModifiers
framework: Core Text
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctunderlinestylemodifiers
source_url: 'https://developer.apple.com/documentation/coretext/ctunderlinestylemodifiers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctunderlinestylemodifiers.json'
content_hash: 'sha256:3d88106cab849f00'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTUnderlineStyleModifiers

<sub>Structure</sub>

Underline style modifiers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CTUnderlineStyleModifiers
```

## Overview

You can apply these underline style modifiers to the underline style ([CTUnderlineStyle](ctunderlinestyle.md)) that you set with the [kCTUnderlineStyleAttributeName](kctunderlinestyleattributename.md) attribute. These modifiers control the pattern of the underline.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Constants

- [kCTUnderlinePatternSolid](ctunderlinestylemodifiers/patternsolid.md) — A modifier that indicates to draw a solid underline.
- [kCTUnderlinePatternDot](ctunderlinestylemodifiers/patterndot.md) — A modifier that indicates to draw an underline using a pattern of dots.
- [kCTUnderlinePatternDash](ctunderlinestylemodifiers/patterndash.md) — A modifier that indicates to draw an underline using a pattern of dashes.
- [kCTUnderlinePatternDashDot](ctunderlinestylemodifiers/patterndashdot.md) — A modifier that indicates to draw an underline using a pattern of alternating dashes and dots.
- [kCTUnderlinePatternDashDotDot](ctunderlinestylemodifiers/patterndashdotdot.md) — A modifier that indicates to draw an underline using a pattern of a dash followed by two dots.

### Initializers

- [init(rawValue:)](<ctunderlinestylemodifiers/init(rawvalue_).md>) — Creates an underline style modifiers structure with the specified raw value.

## See Also

### Constants

- [String Attribute Name Constants](string-attribute-name-constants.md) — These constants represent string attribute names.
- [CTUnderlineStyle](ctunderlinestyle.md) — Underline style specifiers.
