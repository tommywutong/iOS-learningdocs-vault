---
title: buttonSize
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/configuration-swift.struct/buttonsize
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/buttonsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/configuration-swift.struct/buttonsize.json'
content_hash: 'sha256:fee831eaee45909f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIButton](../../uibutton.md) · [Configuration](../configuration-swift.struct.md)

# buttonSize

<sub>Instance Property</sub>

A size that requests a preferred size for the button.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var buttonSize: UIButton.Configuration.Size { get set }
```

## Discussion

The size indicates a system-defined size you prefer for this button. The exact size of the button may change regardless of this value.

## See Also

### Configuring layout

- [Size](size.md) — A predefined size for button elements.
- [contentInsets](contentinsets.md) — The distance from the button’s content area to its bounds.
- [setDefaultContentInsets()](<setdefaultcontentinsets().md>) — Restores the default content insets.
