---
title: currentPreferredSymbolConfiguration
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/currentpreferredsymbolconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/currentpreferredsymbolconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/currentpreferredsymbolconfiguration.json'
content_hash: 'sha256:7a5decd6eaa50963'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# currentPreferredSymbolConfiguration

<sub>Instance Property</sub>

The current symbol size, style, and weight.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var currentPreferredSymbolConfiguration: UIImage.SymbolConfiguration? { get }
```

## Discussion

This can be `nil` or `unspecifiedConfiguration`, which is essentially the same as `nil` but more explicit.

## See Also

### Getting the current state

- [buttonType](buttontype-swift.property.md) — The button type.
- [currentTitle](currenttitle.md) — The current title that is displayed on the button.
- [currentAttributedTitle](currentattributedtitle.md) — The current styled title that is displayed on the button.
- [currentTitleColor](currenttitlecolor.md) — The color used to display the title.
- [currentTitleShadowColor](currenttitleshadowcolor.md) — The color of the title’s shadow.
- [currentImage](currentimage.md) — The current image displayed on the button.
- [currentBackgroundImage](currentbackgroundimage.md) — The current background image displayed on the button.
- [imageView](imageview.md) — The button’s image view.
- [subtitleLabel](subtitlelabel.md) — The label that displays the text of the subtitle.
