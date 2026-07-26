---
title: isContinuous
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uistepper/iscontinuous
source_url: 'https://developer.apple.com/documentation/uikit/uistepper/iscontinuous'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistepper/iscontinuous.json'
content_hash: 'sha256:89b121ba3ccb5866'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIStepper](../uistepper.md)

# isContinuous

<sub>Instance Property</sub>

A Boolean value that determines whether to send value changes during user interaction or after user interaction ends.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var isContinuous: Bool { get set }
```

## Discussion

If [true](../../swift/true.md), the stepper sends value change events immediately as the value changes during user interaction. If [false](../../swift/false.md), the stepper sends a value change event after user interaction ends.

The default value for this property is [true](../../swift/true.md).

## See Also

### Configuring the stepper

- [autorepeat](autorepeat.md) — A Boolean value that determines whether to repeatedly change the stepper’s value as the user presses and holds a stepper button.
- [wraps](wraps.md) — A Boolean value that determines whether the stepper can wrap its value to the minimum or maximum value when incrementing and decrementing the value.
- [minimumValue](minimumvalue.md) — The lowest possible numeric value for the stepper.
- [maximumValue](maximumvalue.md) — The highest possible numeric value for the stepper.
- [stepValue](stepvalue.md) — The step, or increment, value for the stepper.
