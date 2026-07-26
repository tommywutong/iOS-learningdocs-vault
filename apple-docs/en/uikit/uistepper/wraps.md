---
title: wraps
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uistepper/wraps
source_url: 'https://developer.apple.com/documentation/uikit/uistepper/wraps'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistepper/wraps.json'
content_hash: 'sha256:4a56576a4e36de52'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIStepper](../uistepper.md)

# wraps

<sub>Instance Property</sub>

A Boolean value that determines whether the stepper can wrap its value to the minimum or maximum value when incrementing and decrementing the value.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var wraps: Bool { get set }
```

## Discussion

If [true](../../swift/true.md), incrementing beyond [maximumValue](maximumvalue.md) sets [value](value.md) to [minimumValue](minimumvalue.md); likewise, decrementing below [minimumValue](minimumvalue.md) sets [value](value.md) to [maximumValue](maximumvalue.md). If [false](../../swift/false.md), the stepper doesn’t increment beyond [maximumValue](maximumvalue.md) nor does it decrement below [minimumValue](minimumvalue.md) but rather holds at those values.

The default value for this property is [false](../../swift/false.md).

## See Also

### Configuring the stepper

- [continuous](iscontinuous.md) — A Boolean value that determines whether to send value changes during user interaction or after user interaction ends.
- [autorepeat](autorepeat.md) — A Boolean value that determines whether to repeatedly change the stepper’s value as the user presses and holds a stepper button.
- [minimumValue](minimumvalue.md) — The lowest possible numeric value for the stepper.
- [maximumValue](maximumvalue.md) — The highest possible numeric value for the stepper.
- [stepValue](stepvalue.md) — The step, or increment, value for the stepper.
