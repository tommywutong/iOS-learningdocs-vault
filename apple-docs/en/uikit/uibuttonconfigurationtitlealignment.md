---
title: UIButtonConfigurationTitleAlignment
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibuttonconfigurationtitlealignment
source_url: 'https://developer.apple.com/documentation/uikit/uibuttonconfigurationtitlealignment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibuttonconfigurationtitlealignment.json'
content_hash: 'sha256:f1c8b547a139bcbe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIButtonConfigurationTitleAlignment

<sub>Enumeration</sub>

Specifies how to align a button’s title and subtitle.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
enum UIButtonConfigurationTitleAlignment : NSInteger;
```

## Overview

If your button displays both [title](uibuttonconfiguration/title.md) and [subtitle](uibuttonconfiguration/subtitle.md), use this enumeration to configure how the text aligns.

## Topics

### Title alignments

- [UIButtonConfigurationTitleAlignmentAutomatic](uibuttonconfigurationtitlealignment/uibuttonconfigurationtitlealignmentautomatic.md) — Aligns the title and subtitle based on other elements in the button configuration, like an image or activity indicator.
- [UIButtonConfigurationTitleAlignmentCenter](uibuttonconfigurationtitlealignment/uibuttonconfigurationtitlealignmentcenter.md) — Aligns the title and subtitle on their horizontal centers.
- [UIButtonConfigurationTitleAlignmentLeading](uibuttonconfigurationtitlealignment/uibuttonconfigurationtitlealignmentleading.md) — Aligns the title and subtitle on their leading edges.
- [UIButtonConfigurationTitleAlignmentTrailing](uibuttonconfigurationtitlealignment/uibuttonconfigurationtitlealignmenttrailing.md) — Aligns the title and subtitle on their trailing edges.

## See Also

### Configuring titles

- [title](uibuttonconfiguration/title.md) — The text of the title label the button displays.
- [subtitle](uibuttonconfiguration/subtitle.md) — The text the subtitle label of the button displays.
- [attributedTitle](uibuttonconfiguration/attributedtitle.md) — The text and style attributes for the button’s title label.
- [attributedSubtitle](uibuttonconfiguration/attributedsubtitle.md) — The text and style attributes for the button’s subtitle label.
- [titleTextAttributesTransformer](uibuttonconfiguration/titletextattributestransformer.md) — A transformer to update the attributed title when the button state changes.
- [subtitleTextAttributesTransformer](uibuttonconfiguration/subtitletextattributestransformer.md) — A transformer to update the attributed subtitle when the button state changes.
- [UIConfigurationTextAttributesTransformer](uiconfigurationtextattributestransformer-c.typealias.md) — Defines a text transformation that can affect the visual appearance of a string.
- [titlePadding](uibuttonconfiguration/titlepadding.md) — The distance between the title and subtitle labels.
- [titleAlignment](uibuttonconfiguration/titlealignment.md) — The text alignment the button uses to lay out the title and subtitle.
- [titleLineBreakMode](uibuttonconfiguration/titlelinebreakmode.md) — The line break mode the button uses to lay out the button’s title.
- [subtitleLineBreakMode](uibuttonconfiguration/subtitlelinebreakmode.md) — The line break mode the button uses to lay out the button’s subtitle.
