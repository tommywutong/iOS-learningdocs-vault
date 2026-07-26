---
title: stepValue
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uistepper/stepvalue
source_url: 'https://developer.apple.com/documentation/uikit/uistepper/stepvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistepper/stepvalue.json'
content_hash: 'sha256:d41738f7b4fbd4f6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIStepper](../uistepper.md)

# stepValue

<sub>Instance Property</sub>

The step, or increment, value for the stepper.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var stepValue: Double { get set }
```

## Discussion

Must be numerically greater than `0`. If you attempt to set this property’s value to `0` or to a negative number, the system raises an [invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md) exception.

The default value for this property is `1`.

## See Also

### Configuring the stepper

- [continuous](iscontinuous.md) — A Boolean value that determines whether to send value changes during user interaction or after user interaction ends.
- [autorepeat](autorepeat.md) — A Boolean value that determines whether to repeatedly change the stepper’s value as the user presses and holds a stepper button.
- [wraps](wraps.md) — A Boolean value that determines whether the stepper can wrap its value to the minimum or maximum value when incrementing and decrementing the value.
- [minimumValue](minimumvalue.md) — The lowest possible numeric value for the stepper.
- [maximumValue](maximumvalue.md) — The highest possible numeric value for the stepper.
