---
title: NSLayoutManager.ControlCharacterAction
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nslayoutmanager/controlcharacteraction
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/controlcharacteraction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/controlcharacteraction.json'
content_hash: 'sha256:2c7e39e10147776c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# NSLayoutManager.ControlCharacterAction

<sub>Structure</sub>

Constants that describe actions for control characters.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct ControlCharacterAction
```

## Overview

These constants [- layoutManager:shouldUseAction:forControlCharacterAtIndex:](<../nslayoutmanagerdelegate/layoutmanager(__shoulduse_forcontrolcharacterat_).md>) delegate method uses.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Actions

- [NSControlCharacterActionContainerBreak](controlcharacteraction/containerbreak.md) — An action that triggers a break in layout for the current container.
- [NSControlCharacterActionHorizontalTab](controlcharacteraction/horizontaltab.md) — An action that inserts a horizontal tab.
- [NSControlCharacterActionLineBreak](controlcharacteraction/linebreak.md) — An action that causes a line break.
- [NSControlCharacterActionParagraphBreak](controlcharacteraction/paragraphbreak.md) — An action that causes a paragraph break.
- [NSControlCharacterActionWhitespace](controlcharacteraction/whitespace.md) — An action that adds whitespace.
- [NSControlCharacterActionZeroAdvancement](controlcharacteraction/zeroadvancement.md) — An action that removes the glyph from layout.

### Initializers

- [init(rawValue:)](<controlcharacteraction/init(rawvalue_).md>) — Creates a new control character action with the specified raw value.

## See Also

### Invalidating glyphs and layout

- [- layoutManagerDidInvalidateLayout:](<../nslayoutmanagerdelegate/layoutmanagerdidinvalidatelayout(__).md>) — Informs the delegate when the specified layout manager invalidates layout information (not glyph information).
- [- layoutManager:shouldGenerateGlyphs:properties:characterIndexes:font:forGlyphRange:](<../nslayoutmanagerdelegate/layoutmanager(__shouldgenerateglyphs_properties_characterindexes_font_forglyphrange_).md>) — Enables customization of the initial glyph generation process.
- [- layoutManager:shouldUseAction:forControlCharacterAtIndex:](<../nslayoutmanagerdelegate/layoutmanager(__shoulduse_forcontrolcharacterat_).md>) — Returns the control character action for the control character at the specified character index.
