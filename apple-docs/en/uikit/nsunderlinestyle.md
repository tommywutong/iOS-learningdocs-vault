---
title: NSUnderlineStyle
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsunderlinestyle
source_url: 'https://developer.apple.com/documentation/uikit/nsunderlinestyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsunderlinestyle.json'
content_hash: 'sha256:72cbaefda5bd0da3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSUnderlineStyle

<sub>Structure</sub>

Constants for the underline style and strikethrough style attribute keys.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
struct NSUnderlineStyle
```

## Overview

Use these constants to specify the [NSUnderlineStyleAttributeName](nsunderlinestyleattributename.md) and [NSStrikethroughStyleAttributeName](nsstrikethroughstyleattributename.md) attributes of an attributed string.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [Hashable](../swift/hashable.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Getting the line style

- [NSUnderlineStyleSingle](nsunderlinestyle/single.md) — Draw a single line.
- [NSUnderlineStyleThick](nsunderlinestyle/thick.md) — Draw a thick line.
- [NSUnderlineStyleDouble](nsunderlinestyle/double.md) — Draw a double line.
- [NSUnderlineStylePatternDot](nsunderlinestyle/patterndot.md) — Draw a line of dots.
- [NSUnderlineStylePatternDash](nsunderlinestyle/patterndash.md) — Draw a line of dashes.
- [NSUnderlineStylePatternDashDot](nsunderlinestyle/patterndashdot.md) — Draw a line of alternating dashes and dots.
- [NSUnderlineStylePatternDashDotDot](nsunderlinestyle/patterndashdotdot.md) — Draw a line of alternating dashes and two dots.
- [NSUnderlineStyleByWord](nsunderlinestyle/byword.md) — Draw the line only beneath or through words, not whitespace.

### Initializers

- [init(_:)](<nsunderlinestyle/init(__).md>) — Creates a [NSUnderlineStyle](nsunderlinestyle.md) from `Text.LineStyle`.
- [init(rawValue:)](<nsunderlinestyle/init(rawvalue_).md>) — Creates an underline style with the specified raw value.

## See Also

### Getting text content attributes

- [NSWritingDirectionFormatType](nswritingdirectionformattype.md) — Constants for the writing direction attribute key.
