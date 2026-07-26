---
title: contentInsets
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/configuration-swift.struct/contentinsets
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/contentinsets'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/configuration-swift.struct/contentinsets.json'
content_hash: 'sha256:ce69c1d3dbd044a2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIButton](../../uibutton.md) · [Configuration](../configuration-swift.struct.md)

# contentInsets

<sub>Instance Property</sub>

The distance from the button’s content area to its bounds.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var contentInsets: NSDirectionalEdgeInsets { get set }
```

## Discussion

A button has a default inset based on its styling. This property is an additional inset applied after that default inset.

## See Also

### Configuring layout

- [buttonSize](buttonsize.md) — A size that requests a preferred size for the button.
- [Size](size.md) — A predefined size for button elements.
- [setDefaultContentInsets()](<setdefaultcontentinsets().md>) — Restores the default content insets.
