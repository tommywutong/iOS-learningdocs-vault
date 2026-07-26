---
title: lineBreakMode
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（3.0 起废弃）, iPadOS 2.0+（3.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uibutton/linebreakmode
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/linebreakmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/linebreakmode.json'
content_hash: 'sha256:22d7bb46fa574911'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# lineBreakMode

<sub>Instance Property</sub>

The line break mode to use when drawing text.

> [!warning] Deprecated
> Use the `lineBreakMode` property of the [titleLabel](titlelabel.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic) NSLineBreakMode lineBreakMode;
```

## Discussion

This property is one of the constants described in the [UILineBreakMode](../uilinebreakmode.md) enumeration in NSString UIKit Additions Reference. The default value is [UILineBreakModeMiddleTruncation](../uilinebreakmode/uilinebreakmodemiddletruncation.md).

## See Also

### Title effects

- [font](font.md) — The font used to display text on the button. _(deprecated)_
- [titleShadowOffset](titleshadowoffset.md) — The offset of the shadow used to display the receiver’s title. _(deprecated)_
- [reversesTitleShadowWhenHighlighted](reversestitleshadowwhenhighlighted.md) — A Boolean value that determines whether the title shadow changes when the button is highlighted. _(deprecated)_
