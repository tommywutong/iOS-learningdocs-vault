---
title: behavioralStyle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uislider/behavioralstyle
source_url: 'https://developer.apple.com/documentation/uikit/uislider/behavioralstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uislider/behavioralstyle.json'
content_hash: 'sha256:5de12116347699d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISlider](../uislider.md)

# behavioralStyle

<sub>Instance Property</sub>

The style that determines how the slider behaves.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var behavioralStyle: UIBehavioralStyle { get }
```

## Discussion

Use this property to determine the actual behavior style when the [preferredBehavioralStyle](../uibutton/preferredbehavioralstyle.md) is [UIBehavioralStyleAutomatic](../uibehavioralstyle/automatic.md).

## See Also

### Modifying the slider’s behavior

- [continuous](iscontinuous.md) — A Boolean value indicating whether changes in the slider’s value generate continuous update events.
- [preferredBehavioralStyle](preferredbehavioralstyle.md) — The preferred behavioral style.
- [UIBehavioralStyle](../uibehavioralstyle.md) — Constants that indicate how a control behaves in apps built with Mac Catalyst.
