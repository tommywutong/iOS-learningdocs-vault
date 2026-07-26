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
doc_path: /documentation/uikit/uislider/preferredbehavioralstyle
source_url: 'https://developer.apple.com/documentation/uikit/uislider/preferredbehavioralstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uislider/preferredbehavioralstyle.json'
content_hash: 'sha256:5d27e2f70a9cd401'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISlider](../uislider.md)

# preferredBehavioralStyle

<sub>Instance Property</sub>

The preferred behavioral style.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var preferredBehavioralStyle: UIBehavioralStyle { get set }
```

## Discussion

Use this property to specify the behavioral style for the slider. If the value of the property is [UIBehavioralStyleAutomatic](../uibehavioralstyle/automatic.md), use the [behavioralStyle](behavioralstyle.md) property to determine the actual style.

The default value for [preferredBehavioralStyle](preferredbehavioralstyle.md) is [UIBehavioralStyleAutomatic](../uibehavioralstyle/automatic.md). To learn more about behavior styles, see [UIBehavioralStyle](../uibehavioralstyle.md).

## See Also

### Modifying the slider’s behavior

- [continuous](iscontinuous.md) — A Boolean value indicating whether changes in the slider’s value generate continuous update events.
- [behavioralStyle](behavioralstyle.md) — The style that determines how the slider behaves.
- [UIBehavioralStyle](../uibehavioralstyle.md) — Constants that indicate how a control behaves in apps built with Mac Catalyst.
