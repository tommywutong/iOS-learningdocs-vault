---
title: UIButton.Configuration.MacIdiomStyle
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/configuration-swift.struct/macidiomstyle-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/macidiomstyle-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/configuration-swift.struct/macidiomstyle-swift.enum.json'
content_hash: 'sha256:1da68fb3cba39c4f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIButton](../../uibutton.md) · [Configuration](../configuration-swift.struct.md)

# UIButton.Configuration.MacIdiomStyle

<sub>Enumeration</sub>

The button style your app uses when running in macOS.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum MacIdiomStyle
```

## Overview

If you build your app with [Mac Catalyst](../../mac-catalyst.md), you can use these styles to configure how your app displays a button when running on a Mac. To opt in to these styles, choose Optimize Interface for Mac in you project’s general settings.

If you’re configuring your button in Interface Builder, you can choose a style from the Mac Style pop-up menu in the Attributes inspector.

## Relationships

- **Conforms To**: [Equatable](../../../swift/equatable.md), [Hashable](../../../swift/hashable.md)

## Topics

### Button styles

- [UIButton.Configuration.MacIdiomStyle.automatic](macidiomstyle-swift.enum/automatic.md) — The button has a style that matches other content in the button configuration.
- [UIButton.Configuration.MacIdiomStyle.bordered](macidiomstyle-swift.enum/bordered.md) — The button has a bordered style.
- [UIButton.Configuration.MacIdiomStyle.borderless](macidiomstyle-swift.enum/borderless.md) — The button has a borderless style.
- [UIButton.Configuration.MacIdiomStyle.borderlessTinted](macidiomstyle-swift.enum/borderlesstinted.md) — The button has a tinted, borderless style.

## See Also

### Configuring the appearance on macOS

- [macIdiomStyle](macidiomstyle-swift.property.md) — The style to use when this button appears in macOS.
