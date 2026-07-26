---
title: subtitleLineBreakMode
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/configuration-swift.struct/subtitlelinebreakmode
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/subtitlelinebreakmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/configuration-swift.struct/subtitlelinebreakmode.json'
content_hash: 'sha256:370be98315973d07'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIButton](../../uibutton.md) · [Configuration](../configuration-swift.struct.md)

# subtitleLineBreakMode

<sub>Instance Property</sub>

The line break mode the button uses to lay out the button’s subtitle.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var subtitleLineBreakMode: NSLineBreakMode { get set }
```

## Discussion

Word and character wrapping modes enable multiline text, while other modes restrict the text to a single line.

The default value is [NSLineBreakByWordWrapping](../../nslinebreakmode/bywordwrapping.md).

## See Also

### Configuring titles

- [title](title.md) — The text of the title label the button displays.
- [subtitle](subtitle.md) — The text the subtitle label of the button displays.
- [attributedTitle](attributedtitle.md) — The text and style attributes for the button’s title label.
- [attributedSubtitle](attributedsubtitle.md) — The text and style attributes for the button’s subtitle label.
- [titleTextAttributesTransformer](titletextattributestransformer.md) — A structure to update the attributed title when the button state changes.
- [subtitleTextAttributesTransformer](subtitletextattributestransformer.md) — A structure to update the attributed subtitle when the button state changes.
- [UIConfigurationTextAttributesTransformer](../../uiconfigurationtextattributestransformer-swift.struct.md) — Defines a text transformation that can affect the visual appearance of a string.
- [titlePadding](titlepadding.md) — The distance between the title and subtitle labels.
- [titleAlignment](titlealignment-swift.property.md) — The text alignment the button uses to lay out the title and subtitle.
- [TitleAlignment](titlealignment-swift.enum.md) — Specifies how to align a button’s title and subtitle.
- [titleLineBreakMode](titlelinebreakmode.md) — The line break mode the button uses to lay out the button’s title.
