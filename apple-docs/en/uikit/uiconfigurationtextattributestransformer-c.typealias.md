---
title: UIConfigurationTextAttributesTransformer
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiconfigurationtextattributestransformer-c.typealias
source_url: 'https://developer.apple.com/documentation/uikit/uiconfigurationtextattributestransformer-c.typealias'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiconfigurationtextattributestransformer-c.typealias.json'
content_hash: 'sha256:ebcbd1ba475cca0a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIConfigurationTextAttributesTransformer

<sub>Type Alias</sub>

Defines a text transformation that can affect the visual appearance of a string.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
typedef NSDictionary<NSString *,id> *(^)(NSDictionary<NSString *,id> *) UIConfigurationTextAttributesTransformer;
```

## Discussion

Use a transformer to affect how your attributed text appears on the UI. You provide a closure when initializing the transformer. Your closure accepts a container with the current text attributes and returns a container with the new text attributes.

```objc
UIConfigurationTextAttributesTransformer transformer;
transformer = ^(NSDictionary<NSAttributedStringKey, id> *incoming) {
    NSMutableDictionary<NSAttributedStringKey, id> *outgoing = [incoming mutableCopy];
    outgoing[NSForegroundColorAttributeName] = [UIColor blackColor];
    outgoing[NSFontAttributeName] = [UIFont boldSystemFontOfSize:20];
    return outgoing;
};
```

## See Also

### Configuring titles

- [title](uibuttonconfiguration/title.md) — The text of the title label the button displays.
- [subtitle](uibuttonconfiguration/subtitle.md) — The text the subtitle label of the button displays.
- [attributedTitle](uibuttonconfiguration/attributedtitle.md) — The text and style attributes for the button’s title label.
- [attributedSubtitle](uibuttonconfiguration/attributedsubtitle.md) — The text and style attributes for the button’s subtitle label.
- [titleTextAttributesTransformer](uibuttonconfiguration/titletextattributestransformer.md) — A transformer to update the attributed title when the button state changes.
- [subtitleTextAttributesTransformer](uibuttonconfiguration/subtitletextattributestransformer.md) — A transformer to update the attributed subtitle when the button state changes.
- [titlePadding](uibuttonconfiguration/titlepadding.md) — The distance between the title and subtitle labels.
- [titleAlignment](uibuttonconfiguration/titlealignment.md) — The text alignment the button uses to lay out the title and subtitle.
- [UIButtonConfigurationTitleAlignment](uibuttonconfigurationtitlealignment.md) — Specifies how to align a button’s title and subtitle.
- [titleLineBreakMode](uibuttonconfiguration/titlelinebreakmode.md) — The line break mode the button uses to lay out the button’s title.
- [subtitleLineBreakMode](uibuttonconfiguration/subtitlelinebreakmode.md) — The line break mode the button uses to lay out the button’s subtitle.
