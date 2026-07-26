---
title: 'layoutManager(_:shouldUse:forControlCharacterAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanagerdelegate/layoutmanager(_:shoulduse:forcontrolcharacterat:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanagerdelegate/layoutmanager(_:shoulduse:forcontrolcharacterat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanagerdelegate/layoutmanager%28_%3Ashoulduse%3Aforcontrolcharacterat%3A%29.json'
content_hash: 'sha256:5b87401442891407'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManagerDelegate](../nslayoutmanagerdelegate.md)

# layoutManager(_:shouldUse:forControlCharacterAt:)

<sub>Instance Method</sub>

Returns the control character action for the control character at the specified character index.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func layoutManager(_ layoutManager: NSLayoutManager, shouldUse action: NSLayoutManager.ControlCharacterAction, forControlCharacterAt charIndex: Int) -> NSLayoutManager.ControlCharacterAction
```

## Parameters

- `layoutManager` — The layout manager doing the layout.

- `action` — The proposed control character action for the character at the given index. Possible values are enumerated by  [ControlCharacterAction](../nslayoutmanager/controlcharacteraction.md).

- `charIndex` — The index of the control character for which the action is proposed.

## Return Value

The control character action for the control character at the given index.

## See Also

### Invalidating glyphs and layout

- [- layoutManagerDidInvalidateLayout:](<layoutmanagerdidinvalidatelayout(__).md>) — Informs the delegate when the specified layout manager invalidates layout information (not glyph information).
- [- layoutManager:shouldGenerateGlyphs:properties:characterIndexes:font:forGlyphRange:](<layoutmanager(__shouldgenerateglyphs_properties_characterindexes_font_forglyphrange_).md>) — Enables customization of the initial glyph generation process.
- [ControlCharacterAction](../nslayoutmanager/controlcharacteraction.md) — Constants that describe actions for control characters.
