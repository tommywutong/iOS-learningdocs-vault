---
title: subtitle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibuttonconfiguration/subtitle
source_url: 'https://developer.apple.com/documentation/uikit/uibuttonconfiguration/subtitle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibuttonconfiguration/subtitle.json'
content_hash: 'sha256:a2119747db52b1ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButtonConfiguration](../uibuttonconfiguration.md)

# subtitle

<sub>Instance Property</sub>

The text the subtitle label of the button displays.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, copy, readwrite, nullable) NSString * subtitle;
```

## Discussion

This property matches the string value of the [attributedSubtitle](attributedsubtitle.md) property. To change the button subtitle when the button state changes, use [configurationUpdateHandler](../uibutton/configurationupdatehandler-swift.property.md) or [- updateConfiguration](<../uibutton/updateconfiguration().md>).

## See Also

### Configuring titles

- [title](title.md) — The text of the title label the button displays.
- [attributedTitle](attributedtitle.md) — The text and style attributes for the button’s title label.
- [attributedSubtitle](attributedsubtitle.md) — The text and style attributes for the button’s subtitle label.
- [titleTextAttributesTransformer](titletextattributestransformer.md) — A transformer to update the attributed title when the button state changes.
- [subtitleTextAttributesTransformer](subtitletextattributestransformer.md) — A transformer to update the attributed subtitle when the button state changes.
- [UIConfigurationTextAttributesTransformer](../uiconfigurationtextattributestransformer-c.typealias.md) — Defines a text transformation that can affect the visual appearance of a string.
- [titlePadding](titlepadding.md) — The distance between the title and subtitle labels.
- [titleAlignment](titlealignment.md) — The text alignment the button uses to lay out the title and subtitle.
- [UIButtonConfigurationTitleAlignment](../uibuttonconfigurationtitlealignment.md) — Specifies how to align a button’s title and subtitle.
- [titleLineBreakMode](titlelinebreakmode.md) — The line break mode the button uses to lay out the button’s title.
- [subtitleLineBreakMode](subtitlelinebreakmode.md) — The line break mode the button uses to lay out the button’s subtitle.
