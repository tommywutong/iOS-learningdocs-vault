---
title: currentTitle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/currenttitle
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/currenttitle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/currenttitle.json'
content_hash: 'sha256:915e221321c54bcd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# currentTitle

<sub>Instance Property</sub>

The current title that is displayed on the button.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var currentTitle: String? { get }
```

## Discussion

The value for this property is set automatically whenever the button state changes. For states that do not have a custom title string associated with them, this method returns the title that is currently displayed, which is typically the one associated with the [UIControlStateNormal](../uicontrol/state-swift.struct/normal.md) state. The value may be `nil`.

## See Also

### Related Documentation

- [titleLabel](titlelabel.md) — A view that displays the value of the `currentTitle` property for a button.
- [- setTitle:forState:](<settitle(__for_).md>) — Sets the title to use for the specified state.

### Getting the current state

- [buttonType](buttontype-swift.property.md) — The button type.
- [currentAttributedTitle](currentattributedtitle.md) — The current styled title that is displayed on the button.
- [currentTitleColor](currenttitlecolor.md) — The color used to display the title.
- [currentTitleShadowColor](currenttitleshadowcolor.md) — The color of the title’s shadow.
- [currentImage](currentimage.md) — The current image displayed on the button.
- [currentBackgroundImage](currentbackgroundimage.md) — The current background image displayed on the button.
- [currentPreferredSymbolConfiguration](currentpreferredsymbolconfiguration.md) — The current symbol size, style, and weight.
- [imageView](imageview.md) — The button’s image view.
- [subtitleLabel](subtitlelabel.md) — The label that displays the text of the subtitle.
