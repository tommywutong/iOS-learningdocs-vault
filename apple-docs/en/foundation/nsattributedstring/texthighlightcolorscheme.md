---
title: NSAttributedString.TextHighlightColorScheme
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/texthighlightcolorscheme
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/texthighlightcolorscheme'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/texthighlightcolorscheme.json'
content_hash: 'sha256:184e5c4b6c5ad683'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# NSAttributedString.TextHighlightColorScheme

<sub>Structure</sub>

Constants that specify the highlight color to use with the text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct TextHighlightColorScheme
```

## Overview

Use an [TextHighlightColorScheme](texthighlightcolorscheme.md) structure as the value of the [textHighlightColorScheme](key/texthighlightcolorscheme.md) attribute. That attribute specifies which color to use when drawing the highlight on the text. This attribute specifies only the color option. To display the highlight itself, add the [textHighlightStyle](key/texthighlightstyle.md) attribute to the text.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting the color schemes

- [default](texthighlightcolorscheme/default.md) — The default system highlight color.
- [blue](texthighlightcolorscheme/blue.md) — A blue highlight color.
- [mint](texthighlightcolorscheme/mint.md) — A mint green highlight color.
- [orange](texthighlightcolorscheme/orange.md) — An orange highlight color.
- [pink](texthighlightcolorscheme/pink.md) — A pink highlight color.
- [purple](texthighlightcolorscheme/purple.md) — A purple highlight color.

### Creating a color scheme

- [init(_:)](<texthighlightcolorscheme/init(__).md>)
- [init(rawValue:)](<texthighlightcolorscheme/init(rawvalue_).md>)

## See Also

### Getting text content attributes

- [Key](key.md) — The attributes you apply to ranges of characters in an attributed string.
- [TextHighlightStyle](texthighlightstyle.md) — Constants that specify the type of highlight to apply to text.
- [TextEffectStyle](texteffectstyle.md) — Constants for the type of effect to apply to the text.
- [SpellingState](spellingstate.md) — Constants for the spelling state attribute key.
- [NSUnderlineStyle](../../uikit/nsunderlinestyle.md) — Constants for the underline style and strikethrough style attribute keys.
- [NSWritingDirectionFormatType](../../uikit/nswritingdirectionformattype.md) — Constants for the writing direction attribute key.
