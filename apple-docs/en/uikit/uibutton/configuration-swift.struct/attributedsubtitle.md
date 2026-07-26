---
title: attributedSubtitle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/configuration-swift.struct/attributedsubtitle
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/attributedsubtitle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/configuration-swift.struct/attributedsubtitle.json'
content_hash: 'sha256:b0bb3143427c99f6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIButton](../../uibutton.md) · [Configuration](../configuration-swift.struct.md)

# attributedSubtitle

<sub>Instance Property</sub>

The text and style attributes for the button’s subtitle label.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var attributedSubtitle: AttributedString? { get set }
```

## Discussion

The configuration sets the [subtitle](subtitle.md) property to match the string value of this attributed string. To change the button subtitle when the button state changes, use [configurationUpdateHandler](../configurationupdatehandler-swift.property.md) or [- updateConfiguration](<../updateconfiguration().md>).

## See Also

### Configuring titles

- [title](title.md) — The text of the title label the button displays.
- [subtitle](subtitle.md) — The text the subtitle label of the button displays.
- [attributedTitle](attributedtitle.md) — The text and style attributes for the button’s title label.
- [titleTextAttributesTransformer](titletextattributestransformer.md) — A structure to update the attributed title when the button state changes.
- [subtitleTextAttributesTransformer](subtitletextattributestransformer.md) — A structure to update the attributed subtitle when the button state changes.
- [UIConfigurationTextAttributesTransformer](../../uiconfigurationtextattributestransformer-swift.struct.md) — Defines a text transformation that can affect the visual appearance of a string.
- [titlePadding](titlepadding.md) — The distance between the title and subtitle labels.
- [titleAlignment](titlealignment-swift.property.md) — The text alignment the button uses to lay out the title and subtitle.
- [TitleAlignment](titlealignment-swift.enum.md) — Specifies how to align a button’s title and subtitle.
- [titleLineBreakMode](titlelinebreakmode.md) — The line break mode the button uses to lay out the button’s title.
- [subtitleLineBreakMode](subtitlelinebreakmode.md) — The line break mode the button uses to lay out the button’s subtitle.
