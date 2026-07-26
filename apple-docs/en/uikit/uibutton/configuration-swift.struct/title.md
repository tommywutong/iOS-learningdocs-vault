---
title: title
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/configuration-swift.struct/title
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/title'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/configuration-swift.struct/title.json'
content_hash: 'sha256:d540866f0e22f2de'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIButton](../../uibutton.md) · [Configuration](../configuration-swift.struct.md)

# title

<sub>Instance Property</sub>

The text of the title label the button displays.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var title: String? { get set }
```

## Discussion

This property matches the string value of the [attributedTitle](attributedtitle.md) property. To change the button title when the button state changes, use [configurationUpdateHandler](../configurationupdatehandler-swift.property.md) or [- updateConfiguration](<../updateconfiguration().md>).

## See Also

### Configuring titles

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
- [subtitleLineBreakMode](subtitlelinebreakmode.md) — The line break mode the button uses to lay out the button’s subtitle.
