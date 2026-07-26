---
title: preferredBehavioralStyle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationbar/preferredbehavioralstyle
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationbar/preferredbehavioralstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationbar/preferredbehavioralstyle.json'
content_hash: 'sha256:47241f5bb1c62950'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationBar](../uinavigationbar.md)

# preferredBehavioralStyle

<sub>Instance Property</sub>

The preferred behavioral style of the navigation bar.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var preferredBehavioralStyle: UIBehavioralStyle { get set }
```

## Discussion

Use this property to specify the behavioral style for the navigation bar. If the value of the property is [UIBehavioralStyleAutomatic](../uibehavioralstyle/automatic.md), use the [behavioralStyle](behavioralstyle.md) property to determine the actual style.

The default value of this property is [UIBehavioralStyleAutomatic](../uibehavioralstyle/automatic.md). To learn more about behavioral styles, see [UIBehavioralStyle](../uibehavioralstyle.md).

## See Also

### Building with Mac Catalyst

- [behavioralStyle](behavioralstyle.md) — The behavioral style of the navigation bar.
- [currentNSToolbarSection](currentnstoolbarsection.md) — The toolbar section that the navigation bar is currently using.
- [NSToolbarSection](nstoolbarsection.md) — Constants that determine how the system hosts the navigation bar in an AppKit toolbar.
