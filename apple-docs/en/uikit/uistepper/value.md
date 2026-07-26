---
title: value
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uistepper/value
source_url: 'https://developer.apple.com/documentation/uikit/uistepper/value'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistepper/value.json'
content_hash: 'sha256:dab1e932c6453393'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIStepper](../uistepper.md)

# value

<sub>Instance Property</sub>

The numeric value of the stepper.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var value: Double { get set }
```

## Discussion

When the value changes, the stepper sends the [UIControlEventValueChanged](../uicontrol/event/valuechanged.md) flag to its target (see [- addTarget:action:forControlEvents:](<../uicontrol/addtarget(__action_for_).md>)). Refer to the description of the [continuous](iscontinuous.md) property for information about whether value change events are sent continuously or when user interaction ends.

The default value for this property is `0`. This property is clamped at its lower extreme to [minimumValue](minimumvalue.md) and is clamped at its upper extreme to [maximumValue](maximumvalue.md).
