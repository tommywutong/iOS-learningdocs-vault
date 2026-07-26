---
title: keyPath
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiinterpolatingmotioneffect/keypath
source_url: 'https://developer.apple.com/documentation/uikit/uiinterpolatingmotioneffect/keypath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiinterpolatingmotioneffect/keypath.json'
content_hash: 'sha256:3cce340bfcc58ee2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIInterpolatingMotionEffect](../uiinterpolatingmotioneffect.md)

# keyPath

<sub>Instance Property</sub>

The key path you want to modify on the view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var keyPath: String { get }
```

## Discussion

This property must correspond to an animatable property of the view to which the motion effect is attached.

## See Also

### Accessing the motion attributes

- [type](type.md) — The tilt direction to monitor.
- [minimumRelativeValue](minimumrelativevalue.md) — The value that maps to the minimum viewer offset.
- [maximumRelativeValue](maximumrelativevalue.md) — The value that maps to the maximum viewer offset.
