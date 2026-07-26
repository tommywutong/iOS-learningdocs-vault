---
title: availableModes
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscreen/availablemodes
source_url: 'https://developer.apple.com/documentation/uikit/uiscreen/availablemodes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreen/availablemodes.json'
content_hash: 'sha256:863204487f48efe4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScreen](../uiscreen.md)

# availableModes

<sub>Instance Property</sub>

The display modes that can be associated with the screen.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var availableModes: [UIScreenMode] { get }
```

## Discussion

The array contains one or more [UIScreenMode](../uiscreenmode.md) objects, each of which represents a display mode supported by the screen.

## See Also

### Managing screen modes

- [currentMode](currentmode.md) — The current screen mode associated with the screen.
- [preferredMode](preferredmode.md) — The preferred display mode for the screen.
