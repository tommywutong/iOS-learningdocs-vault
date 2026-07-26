---
title: value
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uislider/value
source_url: 'https://developer.apple.com/documentation/uikit/uislider/value'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uislider/value.json'
content_hash: 'sha256:2997a72ac14bc1e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISlider](../uislider.md)

# value

<sub>Instance Property</sub>

The slider’s current value.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var value: Float { get set }
```

## Discussion

Use this property to get and set the slider’s current value. To render an animated transition from the current value to the new value, use the [- setValue:animated:](<setvalue(__animated_).md>) method instead.

If you try to set a value that’s below the minimum or above the maximum, the minimum or maximum value is set instead. The default value of this property is `0.0`.

## See Also

### Accessing the slider’s value

- [- setValue:animated:](<setvalue(__animated_).md>) — Sets the slider’s current value, allowing you to animate the change visually.
