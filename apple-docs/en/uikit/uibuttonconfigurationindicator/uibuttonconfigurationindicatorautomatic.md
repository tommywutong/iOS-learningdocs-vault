---
title: UIButtonConfigurationIndicatorAutomatic
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibuttonconfigurationindicator/uibuttonconfigurationindicatorautomatic
source_url: 'https://developer.apple.com/documentation/uikit/uibuttonconfigurationindicator/uibuttonconfigurationindicatorautomatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibuttonconfigurationindicator/uibuttonconfigurationindicatorautomatic.json'
content_hash: 'sha256:7b28f6d12f5309a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButtonConfigurationIndicator](../uibuttonconfigurationindicator.md)

# UIButtonConfigurationIndicatorAutomatic

<sub>Enumeration Case</sub>

A constant that automatically determines an indicator style according to the button’s properties.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
UIButtonConfigurationIndicatorAutomatic
```

## Discussion

With this behavior, the system automatically shows an indicator if the button shows a menu and has single-selection behavior (when its [contextMenuInteractionEnabled](../uicontrol/iscontextmenuinteractionenabled.md), [showsMenuAsPrimaryAction](../uicontrol/showsmenuasprimaryaction.md), and [changesSelectionAsPrimaryAction](../uibutton/changesselectionasprimaryaction.md) properties are [true](../../swift/true.md)).

## See Also

### Indicator styles

- [UIButtonConfigurationIndicatorNone](uibuttonconfigurationindicatornone.md) — A constant that doesn’t show an indicator.
- [UIButtonConfigurationIndicatorPopup](uibuttonconfigurationindicatorpopup.md) — A constant that shows a popup-style indicator.
