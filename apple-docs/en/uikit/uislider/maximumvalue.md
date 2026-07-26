---
title: maximumValue
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uislider/maximumvalue
source_url: 'https://developer.apple.com/documentation/uikit/uislider/maximumvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uislider/maximumvalue.json'
content_hash: 'sha256:67d650b207ff62f8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISlider](../uislider.md)

# maximumValue

<sub>Instance Property</sub>

The maximum value of the slider.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var maximumValue: Float { get set }
```

## Discussion

Use this property to set the value that the trailing end of the slider represents. If you change the value of this property, and the current value of the slider is above the new maximum, the slider adjusts the [value](value.md) property to match the new maximum. If you set the maximum value to a value smaller than the minimum, the slider updates the minimum value to equal the maximum.

The default value of this property is 1.0.

## See Also

### Accessing the slider’s value limits

- [minimumValue](minimumvalue.md) — The minimum value of the slider.
