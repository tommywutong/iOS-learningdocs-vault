---
title: CTUnderlineStyle
framework: Core Text
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctunderlinestyle
source_url: 'https://developer.apple.com/documentation/coretext/ctunderlinestyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctunderlinestyle.json'
content_hash: 'sha256:fe206a889dbd2078'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTUnderlineStyle

<sub>Structure</sub>

Underline style specifiers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CTUnderlineStyle
```

## Overview

You can apply these underline style specifiers to the value that you set with the [kCTUnderlineStyleAttributeName](kctunderlinestyleattributename.md) attribute. These specifiers control the underline style Core Text uses when rendering the text to which the attribute applies.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Constants

- [kCTUnderlineStyleSingle](ctunderlinestyle/single.md) — A specifier that indicates to draw an underline consisting of a single line.
- [kCTUnderlineStyleThick](ctunderlinestyle/thick.md) — A specifier that indicates to draw an underline consisting of a thick line.
- [kCTUnderlineStyleDouble](ctunderlinestyle/double.md) — A specifier that indicates to draw an underline consisting of a double line.

### Initializers

- [init(rawValue:)](<ctunderlinestyle/init(rawvalue_).md>) — Creates an underline style structure with the specified raw value.

## See Also

### Constants

- [String Attribute Name Constants](string-attribute-name-constants.md) — These constants represent string attribute names.
- [CTUnderlineStyleModifiers](ctunderlinestylemodifiers.md) — Underline style modifiers.
