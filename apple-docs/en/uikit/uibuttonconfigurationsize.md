---
title: UIButtonConfigurationSize
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibuttonconfigurationsize
source_url: 'https://developer.apple.com/documentation/uikit/uibuttonconfigurationsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibuttonconfigurationsize.json'
content_hash: 'sha256:5d0987824e50fec7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIButtonConfigurationSize

<sub>Enumeration</sub>

A predefined size for button elements.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
enum UIButtonConfigurationSize : NSInteger;
```

## Overview

You can use this enumeration to choose a predefined size for elements in a button. The value you choose for button size can be effectively overridden by explicitly assigning values for configuration elements like padding, corner style, or title and subtitle font sizes.

## Topics

### Button sizes

- [UIButtonConfigurationSizeLarge](uibuttonconfigurationsize/uibuttonconfigurationsizelarge.md) — Displays button elements at a large size.
- [UIButtonConfigurationSizeMedium](uibuttonconfigurationsize/uibuttonconfigurationsizemedium.md) — Displays button elements at a standard size.
- [UIButtonConfigurationSizeSmall](uibuttonconfigurationsize/uibuttonconfigurationsizesmall.md) — Displays button elements at a small size.
- [UIButtonConfigurationSizeMini](uibuttonconfigurationsize/uibuttonconfigurationsizemini.md) — Displays button elements at the smallest size.

## See Also

### Configuring layout

- [buttonSize](uibuttonconfiguration/buttonsize.md) — A size that requests a preferred size for the button.
- [contentInsets](uibuttonconfiguration/contentinsets.md) — The distance from the button’s content area to its bounds.
- [setDefaultContentInsets](uibuttonconfiguration/setdefaultcontentinsets.md) — Restores the default content insets.
