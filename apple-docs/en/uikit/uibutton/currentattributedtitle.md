---
title: currentAttributedTitle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/currentattributedtitle
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/currentattributedtitle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/currentattributedtitle.json'
content_hash: 'sha256:70ad8ae5bc2ffdbf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# currentAttributedTitle

<sub>Instance Property</sub>

The current styled title that is displayed on the button.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var currentAttributedTitle: NSAttributedString? { get }
```

## Discussion

The value for this property reflects the title associated with the control’s current state. For states that do not have a custom title string associated with them, this method returns the attributed title that is currently displayed, which is typically the one associated with the [UIControlStateNormal](../uicontrol/state-swift.struct/normal.md) state.

## See Also

### Getting the current state

- [buttonType](buttontype-swift.property.md) — The button type.
- [currentTitle](currenttitle.md) — The current title that is displayed on the button.
- [currentTitleColor](currenttitlecolor.md) — The color used to display the title.
- [currentTitleShadowColor](currenttitleshadowcolor.md) — The color of the title’s shadow.
- [currentImage](currentimage.md) — The current image displayed on the button.
- [currentBackgroundImage](currentbackgroundimage.md) — The current background image displayed on the button.
- [currentPreferredSymbolConfiguration](currentpreferredsymbolconfiguration.md) — The current symbol size, style, and weight.
- [imageView](imageview.md) — The button’s image view.
- [subtitleLabel](subtitlelabel.md) — The label that displays the text of the subtitle.
