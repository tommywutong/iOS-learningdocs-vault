---
title: preferredBehavioralStyle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/preferredbehavioralstyle
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/preferredbehavioralstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/preferredbehavioralstyle.json'
content_hash: 'sha256:d74925262c717f2c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# preferredBehavioralStyle

<sub>Instance Property</sub>

The preferred behavioral style.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var preferredBehavioralStyle: UIBehavioralStyle { get set }
```

## Discussion

Use this property to specify the behavioral style for the button. If the value of the property is [UIBehavioralStyleAutomatic](../uibehavioralstyle/automatic.md), use the [behavioralStyle](behavioralstyle.md) property to determine the actual style.

The default value for [preferredBehavioralStyle](preferredbehavioralstyle.md) is [UIBehavioralStyleAutomatic](../uibehavioralstyle/automatic.md). To learn more about behavioral styles, see [UIBehavioralStyle](../uibehavioralstyle.md).

## See Also

### Specifying the behavioral style

- [behavioralStyle](behavioralstyle.md) — The style that determines how the button behaves.
- [UIBehavioralStyle](../uibehavioralstyle.md) — Constants that indicate how a control behaves in apps built with Mac Catalyst.
