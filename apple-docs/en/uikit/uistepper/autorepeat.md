---
title: autorepeat
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uistepper/autorepeat
source_url: 'https://developer.apple.com/documentation/uikit/uistepper/autorepeat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistepper/autorepeat.json'
content_hash: 'sha256:52aef265b34dae24'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIStepper](../uistepper.md)

# autorepeat

<sub>Instance Property</sub>

A Boolean value that determines whether to repeatedly change the stepper’s value as the user presses and holds a stepper button.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var autorepeat: Bool { get set }
```

## Discussion

If [true](../../swift/true.md), the user pressing and holding on the stepper repeatedly alters [value](value.md).

The default value for this property is [true](../../swift/true.md).

## See Also

### Configuring the stepper

- [continuous](iscontinuous.md) — A Boolean value that determines whether to send value changes during user interaction or after user interaction ends.
- [wraps](wraps.md) — A Boolean value that determines whether the stepper can wrap its value to the minimum or maximum value when incrementing and decrementing the value.
- [minimumValue](minimumvalue.md) — The lowest possible numeric value for the stepper.
- [maximumValue](maximumvalue.md) — The highest possible numeric value for the stepper.
- [stepValue](stepvalue.md) — The step, or increment, value for the stepper.
