---
title: 'init(coder:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicubictimingparameters/init(coder:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicubictimingparameters/init(coder:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicubictimingparameters/init%28coder%3A%29.json'
content_hash: 'sha256:5f06b67fc708f3e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICubicTimingParameters](../uicubictimingparameters.md)

# init(coder:)

<sub>Initializer</sub>

Creates a timing parameters object from data in an unarchiver.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init?(coder: NSCoder)
```

## See Also

### Initializing a cubic timing parameters object

- [- init](<init().md>) — Initializes the object with the system’s default timing curve.
- [- initWithAnimationCurve:](<init(animationcurve_).md>) — Initializes the object with the specified UIKit timing curve.
- [- initWithControlPoint1:controlPoint2:](<init(controlpoint1_controlpoint2_).md>) — Initializes the object with the specified control points for a cubic Bézier curve.
