---
title: currentMode
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscreen/currentmode
source_url: 'https://developer.apple.com/documentation/uikit/uiscreen/currentmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreen/currentmode.json'
content_hash: 'sha256:92c9ab1ee42207c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScreen](../uiscreen.md)

# currentMode

<sub>Instance Property</sub>

The current screen mode associated with the screen.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var currentMode: UIScreenMode? { get set }
```

<sub>tvOS</sub>

```swift
var currentMode: UIScreenMode? { get }
```

## Discussion

The default value of this property is the mode containing the highest resolution supported by the screen.

On iOS, you can change the value of this property to support different resolutions as needed. For example, you might want to lower the default resolution to one that your application supports more readily. The value must be one of the values described in the [availableModes](availablemodes.md) property.

On tvOS, the screen mode is read-only.

## See Also

### Managing screen modes

- [preferredMode](preferredmode.md) — The preferred display mode for the screen.
- [availableModes](availablemodes.md) — The display modes that can be associated with the screen.
