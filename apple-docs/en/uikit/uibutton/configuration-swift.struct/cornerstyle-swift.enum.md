---
title: UIButton.Configuration.CornerStyle
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/configuration-swift.struct/cornerstyle-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/cornerstyle-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/configuration-swift.struct/cornerstyle-swift.enum.json'
content_hash: 'sha256:afb91e921c8d2518'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIButton](../../uibutton.md) · [Configuration](../configuration-swift.struct.md)

# UIButton.Configuration.CornerStyle

<sub>Enumeration</sub>

Settings that determine the appearance of the background corner radius.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum CornerStyle
```

## Overview

Use this property to control how the button uses the [cornerRadius](../../uibackgroundconfiguration-swift.struct/cornerradius.md) property of the button’s [background](background.md).

## Relationships

- **Conforms To**: [Equatable](../../../swift/equatable.md), [Hashable](../../../swift/hashable.md)

## Topics

### Corner styles

- [UIButton.Configuration.CornerStyle.dynamic](cornerstyle-swift.enum/dynamic.md) — A style that adjusts the background corner radius for dynamic type.
- [UIButton.Configuration.CornerStyle.fixed](cornerstyle-swift.enum/fixed.md) — A style that uses the background corner radius without modification.
- [UIButton.Configuration.CornerStyle.capsule](cornerstyle-swift.enum/capsule.md) — A style that ignores the background corner radius and uses a corner radius that generates a capsule.
- [UIButton.Configuration.CornerStyle.large](cornerstyle-swift.enum/large.md) — A style that ignores the background corner radius and uses a large system-defined corner radius.
- [UIButton.Configuration.CornerStyle.medium](cornerstyle-swift.enum/medium.md) — A style that ignores the background corner radius and uses a medium system-defined corner radius.
- [UIButton.Configuration.CornerStyle.small](cornerstyle-swift.enum/small.md) — A style that ignores the background corner radius and uses a small system-defined corner radius.

## See Also

### Configuring the button background

- [background](background.md) — The configuration to customize the button background.
- [cornerStyle](cornerstyle-swift.property.md) — The button style that controls the display behavior of the background corner radius.
