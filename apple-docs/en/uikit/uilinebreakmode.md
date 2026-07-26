---
title: UILineBreakMode
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+（6.0 起废弃）, iPadOS 2.0+（6.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uilinebreakmode
source_url: 'https://developer.apple.com/documentation/uikit/uilinebreakmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilinebreakmode.json'
content_hash: 'sha256:be18f8b20cb7bcee'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UILineBreakMode

<sub>Enumeration</sub>

Options for wrapping and truncating text.

> [!warning] Deprecated
> Use [NSLineBreakMode](nslinebreakmode.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
enum UILineBreakMode : NSInteger;
```

## Overview

For methods that draw at a specified point (as opposed to those that draw in a rectangular region), these options specify the clipping behavior that UIKit applies to the string.

## Topics

### Deprecated constants

- [UILineBreakModeWordWrap](uilinebreakmode/uilinebreakmodewordwrap.md) — Wrap or clip the string only at word boundaries. _(deprecated)_
- [UILineBreakModeCharacterWrap](uilinebreakmode/uilinebreakmodecharacterwrap.md) — Wrap or clip the string at the closest character boundary. _(deprecated)_
- [UILineBreakModeClip](uilinebreakmode/uilinebreakmodeclip.md) — Clip the text when reaching the end of the drawing rectangle. _(deprecated)_
- [UILineBreakModeHeadTruncation](uilinebreakmode/uilinebreakmodeheadtruncation.md) — Truncate text (as necessary) from the beginning of the line. _(deprecated)_
- [UILineBreakModeTailTruncation](uilinebreakmode/uilinebreakmodetailtruncation.md) — Truncate text (as necessary) from the end of the line. _(deprecated)_
- [UILineBreakModeMiddleTruncation](uilinebreakmode/uilinebreakmodemiddletruncation.md) — Truncate text (as necessary) from the middle of the line. _(deprecated)_

## See Also

### Strings

- [NSStringDrawingContext](nsstringdrawingcontext.md) — An object that manages metrics for drawing attributed strings.
- [NSStringDrawingOptions](nsstringdrawingoptions.md) — Constants that specify the rendering options for drawing a string.
- [UIBaselineAdjustment](uibaselineadjustment.md) — Vertical adjustment options.
- [UITextAlignment](uitextalignment.md) — Options for aligning text horizontally. _(deprecated)_
- [UITextAttributeFont](uitextattributefont.md) — The key to the font in a text attributes dictionary. _(deprecated)_
- [UITextAttributeTextColor](uitextattributetextcolor.md) — The key to the text color in a text attributes dictionary. _(deprecated)_
- [UITextAttributeTextShadowColor](uitextattributetextshadowcolor.md) — The key to the text shadow color in a text attributes dictionary. _(deprecated)_
- [UITextAttributeTextShadowOffset](uitextattributetextshadowoffset.md) — The key to the offset for the text shadow in a text attributes dictionary. _(deprecated)_
