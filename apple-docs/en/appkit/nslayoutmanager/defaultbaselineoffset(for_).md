---
title: 'defaultBaselineOffset(for:)'
framework: AppKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/appkit/nslayoutmanager/defaultbaselineoffset(for:)'
source_url: 'https://developer.apple.com/documentation/appkit/nslayoutmanager/defaultbaselineoffset(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nslayoutmanager/defaultbaselineoffset%28for%3A%29.json'
content_hash: 'sha256:eea86cd8fe00b3ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSLayoutManager](../nslayoutmanager.md)

# defaultBaselineOffset(for:)

<sub>Instance Method</sub>

Returns the default baseline offset that the layout manager’s typesetter uses for the specified font.

<sub>macOS</sub>

```swift
func defaultBaselineOffset(for theFont: NSFont) -> CGFloat
```

## Parameters

- `theFont` — The font for which to return the default baseline offset.

## Return Value

The default baseline offset for a line of text drawn using `theFont`.

## Discussion

The value returned may vary according to the layout manager’s typesetter behavior.

## See Also

### Managing the typesetter

- [typesetter](typesetter.md) — The current typesetter.
- [typesetterBehavior](typesetterbehavior-swift.property.md) — The default typesetter behavior.
- [TypesetterBehavior](typesetterbehavior-swift.enum.md) — Constants that determine the layout manager’s behavior during layout.
- [- defaultLineHeightForFont:](<defaultlineheight(for_).md>) — Returns the default line height for a line of text that uses a specified font.
