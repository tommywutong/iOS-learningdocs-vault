---
title: contentInsets
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibuttonconfiguration/contentinsets
source_url: 'https://developer.apple.com/documentation/uikit/uibuttonconfiguration/contentinsets'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibuttonconfiguration/contentinsets.json'
content_hash: 'sha256:1cadcd3ae7b05a28'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButtonConfiguration](../uibuttonconfiguration.md)

# contentInsets

<sub>Instance Property</sub>

The distance from the button’s content area to its bounds.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, assign, readwrite) NSDirectionalEdgeInsets contentInsets;
```

## Discussion

A button has a default inset based on its styling. This property is an additional inset applied after that default inset.

## See Also

### Configuring layout

- [buttonSize](buttonsize.md) — A size that requests a preferred size for the button.
- [UIButtonConfigurationSize](../uibuttonconfigurationsize.md) — A predefined size for button elements.
- [setDefaultContentInsets](setdefaultcontentinsets.md) — Restores the default content insets.
