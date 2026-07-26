---
title: buttonSize
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibuttonconfiguration/buttonsize
source_url: 'https://developer.apple.com/documentation/uikit/uibuttonconfiguration/buttonsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibuttonconfiguration/buttonsize.json'
content_hash: 'sha256:7184cf92360f9970'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButtonConfiguration](../uibuttonconfiguration.md)

# buttonSize

<sub>Instance Property</sub>

A size that requests a preferred size for the button.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, assign, readwrite) UIButtonConfigurationSize buttonSize;
```

## Discussion

The size indicates a system-defined size you prefer for this button. The exact size of the button may change regardless of this value.

## See Also

### Configuring layout

- [UIButtonConfigurationSize](../uibuttonconfigurationsize.md) — A predefined size for button elements.
- [contentInsets](contentinsets.md) — The distance from the button’s content area to its bounds.
- [setDefaultContentInsets](setdefaultcontentinsets.md) — Restores the default content insets.
