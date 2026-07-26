---
title: minimumRelativeValue
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiinterpolatingmotioneffect/minimumrelativevalue
source_url: 'https://developer.apple.com/documentation/uikit/uiinterpolatingmotioneffect/minimumrelativevalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiinterpolatingmotioneffect/minimumrelativevalue.json'
content_hash: 'sha256:62831c002acf2ec1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIInterpolatingMotionEffect](../uiinterpolatingmotioneffect.md)

# minimumRelativeValue

<sub>Instance Property</sub>

The value that maps to the minimum viewer offset.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var minimumRelativeValue: Any? { get set }
```

## Discussion

The value in this property is the value returned when the viewer offset value along the given axis is -1.

## See Also

### Accessing the motion attributes

- [keyPath](keypath.md) — The key path you want to modify on the view.
- [type](type.md) — The tilt direction to monitor.
- [maximumRelativeValue](maximumrelativevalue.md) — The value that maps to the maximum viewer offset.
