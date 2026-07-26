---
title: font
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（3.0 起废弃）, iPadOS 2.0+（3.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uibutton/font
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/font'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/font.json'
content_hash: 'sha256:988aec9d6b98f518'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# font

<sub>Instance Property</sub>

The font used to display text on the button.

> [!warning] Deprecated
> Use the `font` property of the [titleLabel](titlelabel.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, strong) UIFont * font;
```

## Discussion

If `nil`, a system font is used. The default value is `nil`.

## See Also

### Related Documentation

- [titleLabel](titlelabel.md) — A view that displays the value of the `currentTitle` property for a button.

### Title effects

- [lineBreakMode](linebreakmode.md) — The line break mode to use when drawing text. _(deprecated)_
- [titleShadowOffset](titleshadowoffset.md) — The offset of the shadow used to display the receiver’s title. _(deprecated)_
- [reversesTitleShadowWhenHighlighted](reversestitleshadowwhenhighlighted.md) — A Boolean value that determines whether the title shadow changes when the button is highlighted. _(deprecated)_
