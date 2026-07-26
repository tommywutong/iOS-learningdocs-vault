---
title: titleAlignment
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibuttonconfiguration/titlealignment
source_url: 'https://developer.apple.com/documentation/uikit/uibuttonconfiguration/titlealignment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibuttonconfiguration/titlealignment.json'
content_hash: 'sha256:c3a473a9330de4bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButtonConfiguration](../uibuttonconfiguration.md)

# titleAlignment

<sub>Instance Property</sub>

The text alignment the button uses to lay out the title and subtitle.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, assign, readwrite) UIButtonConfigurationTitleAlignment titleAlignment;
```

## Discussion

The title aligment can align the title and subtitle labels along the leading or trailing edges, or center them relative to each other.

## See Also

### Configuring titles

- [title](title.md) — The text of the title label the button displays.
- [subtitle](subtitle.md) — The text the subtitle label of the button displays.
- [attributedTitle](attributedtitle.md) — The text and style attributes for the button’s title label.
- [attributedSubtitle](attributedsubtitle.md) — The text and style attributes for the button’s subtitle label.
- [titleTextAttributesTransformer](titletextattributestransformer.md) — A transformer to update the attributed title when the button state changes.
- [subtitleTextAttributesTransformer](subtitletextattributestransformer.md) — A transformer to update the attributed subtitle when the button state changes.
- [UIConfigurationTextAttributesTransformer](../uiconfigurationtextattributestransformer-c.typealias.md) — Defines a text transformation that can affect the visual appearance of a string.
- [titlePadding](titlepadding.md) — The distance between the title and subtitle labels.
- [UIButtonConfigurationTitleAlignment](../uibuttonconfigurationtitlealignment.md) — Specifies how to align a button’s title and subtitle.
- [titleLineBreakMode](titlelinebreakmode.md) — The line break mode the button uses to lay out the button’s title.
- [subtitleLineBreakMode](subtitlelinebreakmode.md) — The line break mode the button uses to lay out the button’s subtitle.
