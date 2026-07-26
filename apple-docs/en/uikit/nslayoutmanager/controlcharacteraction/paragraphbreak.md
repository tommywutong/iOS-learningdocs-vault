---
title: paragraphBreak
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nslayoutmanager/controlcharacteraction/paragraphbreak
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/controlcharacteraction/paragraphbreak'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/controlcharacteraction/paragraphbreak.json'
content_hash: 'sha256:fca8bad20d63f9de'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [NSLayoutManager](../../nslayoutmanager.md) · [ControlCharacterAction](../controlcharacteraction.md)

# paragraphBreak

<sub>Type Property</sub>

An action that causes a paragraph break.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static var paragraphBreak: NSLayoutManager.ControlCharacterAction { get }
```

## Discussion

The value in [firstLineHeadIndent](../../nsparagraphstyle/firstlineheadindent.md) is used for the following glyph.

## See Also

### Actions

- [NSControlCharacterActionContainerBreak](containerbreak.md) — An action that triggers a break in layout for the current container.
- [NSControlCharacterActionHorizontalTab](horizontaltab.md) — An action that inserts a horizontal tab.
- [NSControlCharacterActionLineBreak](linebreak.md) — An action that causes a line break.
- [NSControlCharacterActionWhitespace](whitespace.md) — An action that adds whitespace.
- [NSControlCharacterActionZeroAdvancement](zeroadvancement.md) — An action that removes the glyph from layout.
