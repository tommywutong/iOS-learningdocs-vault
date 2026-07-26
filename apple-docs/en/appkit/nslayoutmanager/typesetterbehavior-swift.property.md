---
title: typesetterBehavior
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nslayoutmanager/typesetterbehavior-swift.property
source_url: 'https://developer.apple.com/documentation/appkit/nslayoutmanager/typesetterbehavior-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nslayoutmanager/typesetterbehavior-swift.property.json'
content_hash: 'sha256:791a1789f693d6fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSLayoutManager](../nslayoutmanager.md)

# typesetterBehavior

<sub>Instance Property</sub>

The default typesetter behavior.

<sub>macOS</sub>

```swift
var typesetterBehavior: NSLayoutManager.TypesetterBehavior { get set }
```

## Discussion

The typesetter behavior affects glyph spacing and line height.

## See Also

### Managing the typesetter

- [typesetter](typesetter.md) — The current typesetter.
- [TypesetterBehavior](typesetterbehavior-swift.enum.md) — Constants that determine the layout manager’s behavior during layout.
- [- defaultLineHeightForFont:](<defaultlineheight(for_).md>) — Returns the default line height for a line of text that uses a specified font.
- [- defaultBaselineOffsetForFont:](<defaultbaselineoffset(for_).md>) — Returns the default baseline offset that the layout manager’s typesetter uses for the specified font.
