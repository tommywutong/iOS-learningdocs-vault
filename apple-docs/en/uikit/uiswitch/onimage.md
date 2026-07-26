---
title: onImage
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiswitch/onimage
source_url: 'https://developer.apple.com/documentation/uikit/uiswitch/onimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiswitch/onimage.json'
content_hash: 'sha256:fe6720e297c37637'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISwitch](../uiswitch.md)

# onImage

<sub>Instance Property</sub>

The image displayed when the switch is in the on position.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var onImage: UIImage? { get set }
```

## Discussion

In iOS 7 and later, this property has no effect.

In iOS 6, this image represents the interior contents of the switch. The image you specify is composited with the switch’s rounded bezel and thumb to create the final appearance.

## See Also

### Deprecated

- [offImage](offimage.md) — The image displayed when the switch is in the off position.
