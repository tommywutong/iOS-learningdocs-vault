---
title: maximumRelativeValue
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiinterpolatingmotioneffect/maximumrelativevalue
source_url: 'https://developer.apple.com/documentation/uikit/uiinterpolatingmotioneffect/maximumrelativevalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiinterpolatingmotioneffect/maximumrelativevalue.json'
content_hash: 'sha256:76e70c25b6ba63a2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIInterpolatingMotionEffect](../uiinterpolatingmotioneffect.md)

# maximumRelativeValue

<sub>Instance Property</sub>

The value that maps to the maximum viewer offset.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var maximumRelativeValue: Any? { get set }
```

## Discussion

The value in this property is the value returned when the viewer offset value along the given axis is 1.

## See Also

### Accessing the motion attributes

- [keyPath](keypath.md) — The key path you want to modify on the view.
- [type](type.md) — The tilt direction to monitor.
- [minimumRelativeValue](minimumrelativevalue.md) — The value that maps to the minimum viewer offset.
