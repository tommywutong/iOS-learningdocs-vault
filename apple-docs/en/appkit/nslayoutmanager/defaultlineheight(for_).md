---
title: 'defaultLineHeight(for:)'
framework: AppKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/appkit/nslayoutmanager/defaultlineheight(for:)'
source_url: 'https://developer.apple.com/documentation/appkit/nslayoutmanager/defaultlineheight(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nslayoutmanager/defaultlineheight%28for%3A%29.json'
content_hash: 'sha256:531cf6d1ffac2d7c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSLayoutManager](../nslayoutmanager.md)

# defaultLineHeight(for:)

<sub>Instance Method</sub>

Returns the default line height for a line of text that uses a specified font.

<sub>macOS</sub>

```swift
func defaultLineHeight(for theFont: NSFont) -> CGFloat
```

## Parameters

- `theFont` — The font for which to determine the default line height.

## Return Value

The default line height for a line of text drawn using `theFont`.

## Discussion

The value returned may vary according to the layout manager’s typesetter behavior.

## See Also

### Managing the typesetter

- [typesetter](typesetter.md) — The current typesetter.
- [typesetterBehavior](typesetterbehavior-swift.property.md) — The default typesetter behavior.
- [TypesetterBehavior](typesetterbehavior-swift.enum.md) — Constants that determine the layout manager’s behavior during layout.
- [- defaultBaselineOffsetForFont:](<defaultbaselineoffset(for_).md>) — Returns the default baseline offset that the layout manager’s typesetter uses for the specified font.
