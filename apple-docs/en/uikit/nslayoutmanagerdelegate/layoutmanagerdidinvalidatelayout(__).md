---
title: 'layoutManagerDidInvalidateLayout(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanagerdelegate/layoutmanagerdidinvalidatelayout(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanagerdelegate/layoutmanagerdidinvalidatelayout(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanagerdelegate/layoutmanagerdidinvalidatelayout%28_%3A%29.json'
content_hash: 'sha256:2aeaa869866df237'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManagerDelegate](../nslayoutmanagerdelegate.md)

# layoutManagerDidInvalidateLayout(_:)

<sub>Instance Method</sub>

Informs the delegate when the specified layout manager invalidates layout information (not glyph information).

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func layoutManagerDidInvalidateLayout(_ sender: NSLayoutManager)
```

## Parameters

- `sender` — The layout manager that invalidated layout.

## Discussion

This method is invoked only when layout was complete and then became invalidated for some reason. Delegates can use this information to show an indicator of background layout or to enable a button that forces immediate layout of text.

## See Also

### Invalidating glyphs and layout

- [- layoutManager:shouldGenerateGlyphs:properties:characterIndexes:font:forGlyphRange:](<layoutmanager(__shouldgenerateglyphs_properties_characterindexes_font_forglyphrange_).md>) — Enables customization of the initial glyph generation process.
- [- layoutManager:shouldUseAction:forControlCharacterAtIndex:](<layoutmanager(__shoulduse_forcontrolcharacterat_).md>) — Returns the control character action for the control character at the specified character index.
- [ControlCharacterAction](../nslayoutmanager/controlcharacteraction.md) — Constants that describe actions for control characters.
