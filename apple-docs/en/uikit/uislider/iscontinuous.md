---
title: isContinuous
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uislider/iscontinuous
source_url: 'https://developer.apple.com/documentation/uikit/uislider/iscontinuous'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uislider/iscontinuous.json'
content_hash: 'sha256:3580c93afdbf9b48'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISlider](../uislider.md)

# isContinuous

<sub>Instance Property</sub>

A Boolean value indicating whether changes in the slider’s value generate continuous update events.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var isContinuous: Bool { get set }
```

## Discussion

If [true](../../swift/true.md), the slider triggers the associated target’s action method repeatedly, as the user moves the thumb. If [false](../../swift/false.md), the slider triggers the associated action method just once, when the user releases the slider’s thumb control to set the final value.

The default value of this property is [true](../../swift/true.md).

## See Also

### Modifying the slider’s behavior

- [behavioralStyle](behavioralstyle.md) — The style that determines how the slider behaves.
- [preferredBehavioralStyle](preferredbehavioralstyle.md) — The preferred behavioral style.
- [UIBehavioralStyle](../uibehavioralstyle.md) — Constants that indicate how a control behaves in apps built with Mac Catalyst.
