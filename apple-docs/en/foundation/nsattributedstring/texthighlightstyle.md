---
title: NSAttributedString.TextHighlightStyle
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/texthighlightstyle
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/texthighlightstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/texthighlightstyle.json'
content_hash: 'sha256:d6142af5ce9b1120'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# NSAttributedString.TextHighlightStyle

<sub>Structure</sub>

Constants that specify the type of highlight to apply to text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct TextHighlightStyle
```

## Overview

Use an [TextHighlightStyle](texthighlightstyle.md) structure as the value of the [textHighlightStyle](key/texthighlightstyle.md) attribute. That attribute applies a highlight to the text to emphasize it. The highlight contributes a background color and a contrasting foreground color to the text.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting the highlight styles

- [default](texthighlightstyle/default.md) — The default highlight style to apply to text.

### Creating a highlight style

- [init(_:)](<texthighlightstyle/init(__).md>)
- [init(rawValue:)](<texthighlightstyle/init(rawvalue_).md>)

## See Also

### Getting text content attributes

- [Key](key.md) — The attributes you apply to ranges of characters in an attributed string.
- [TextHighlightColorScheme](texthighlightcolorscheme.md) — Constants that specify the highlight color to use with the text.
- [TextEffectStyle](texteffectstyle.md) — Constants for the type of effect to apply to the text.
- [SpellingState](spellingstate.md) — Constants for the spelling state attribute key.
- [NSUnderlineStyle](../../uikit/nsunderlinestyle.md) — Constants for the underline style and strikethrough style attribute keys.
- [NSWritingDirectionFormatType](../../uikit/nswritingdirectionformattype.md) — Constants for the writing direction attribute key.
