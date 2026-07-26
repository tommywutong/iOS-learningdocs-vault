---
title: minimumValue
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uislider/minimumvalue
source_url: 'https://developer.apple.com/documentation/uikit/uislider/minimumvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uislider/minimumvalue.json'
content_hash: 'sha256:ccbd925c39367bc8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISlider](../uislider.md)

# minimumValue

<sub>Instance Property</sub>

The minimum value of the slider.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var minimumValue: Float { get set }
```

## Discussion

Use this property to set the value that the leading end of the slider represents. If you change the value of this property, and the current value of the slider is below the new minimum, the slider adjusts the [value](value.md) property to match the new minimum. If you set the minimum value to a value larger than the maximum, the slider updates the maximum value to equal the minimum.

The default value of this property is 0.0.

## See Also

### Accessing the slider’s value limits

- [maximumValue](maximumvalue.md) — The maximum value of the slider.
