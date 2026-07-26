---
title: 'playerViewController:didSelectExternalSubtitleOptionLanguage:'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [tvOS 9.0+]
languages: [occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller:didselectexternalsubtitleoptionlanguage:'
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller:didselectexternalsubtitleoptionlanguage:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller%3Adidselectexternalsubtitleoptionlanguage%3A.json'
content_hash: 'sha256:6781a5ae00fde137'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewControllerDelegate](../avplayerviewcontrollerdelegate.md)

# playerViewController:didSelectExternalSubtitleOptionLanguage:

<sub>Instance Method</sub>

Tells the delegate when the user selects a specific subtitle option.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```objc
- (void) playerViewController:(AVPlayerViewController *) playerViewController didSelectExternalSubtitleOptionLanguage:(NSString *) language;
```

## Parameters

- `playerViewController` — The player view controller.

- `language` — The IETF BCP 47 language code.

## Discussion

The framework calls this method only for external subtitle languages specified by the player item’s [externalSubtitleOptionLanguages](../../avfoundation/avplayeritem/externalsubtitleoptionlanguages.md) property. For all other options, the framework calls [- playerViewController:didSelectMediaSelectionOption:inMediaSelectionGroup:](<playerviewcontroller(__didselect_in_).md>) instead. The delegate is responsible for displaying the corresponding subtitles.

## See Also

### Responding to Media Selection

- [- playerViewController:didSelectMediaSelectionOption:inMediaSelectionGroup:](<playerviewcontroller(__didselect_in_).md>) — Tells the delegate when the user selects a media option from a media selection group.
