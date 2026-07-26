---
title: maximumValue
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uistepper/maximumvalue
source_url: 'https://developer.apple.com/documentation/uikit/uistepper/maximumvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistepper/maximumvalue.json'
content_hash: 'sha256:8c4a0ac300f10d94'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIStepper](../uistepper.md)

# maximumValue

<sub>Instance Property</sub>

The highest possible numeric value for the stepper.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var maximumValue: Double { get set }
```

## Discussion

Must be numerically greater than [minimumValue](minimumvalue.md). If you attempt to set a value equal to or lower than [minimumValue](minimumvalue.md), the system raises an [invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md) exception.

The default value of this property is `100`.

## See Also

### Configuring the stepper

- [continuous](iscontinuous.md) — A Boolean value that determines whether to send value changes during user interaction or after user interaction ends.
- [autorepeat](autorepeat.md) — A Boolean value that determines whether to repeatedly change the stepper’s value as the user presses and holds a stepper button.
- [wraps](wraps.md) — A Boolean value that determines whether the stepper can wrap its value to the minimum or maximum value when incrementing and decrementing the value.
- [minimumValue](minimumvalue.md) — The lowest possible numeric value for the stepper.
- [stepValue](stepvalue.md) — The step, or increment, value for the stepper.
