---
title: pointerStyleProvider
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/pointerstyleprovider-1d4d2
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/pointerstyleprovider-1d4d2'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/pointerstyleprovider-1d4d2.json'
content_hash: 'sha256:772cded56b37d5fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# pointerStyleProvider

<sub>Instance Property</sub>

A block that returns the pointer style to use when the pointer hovers over the button.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, copy, readwrite, nullable) UIButtonPointerStyleProvider pointerStyleProvider;
```

## Discussion

To change the appearance of the pointer when it hovers over the button, create a [UIButtonPointerStyleProvider](../uibuttonpointerstyleprovider.md) block that returns a [UIPointerStyle](../uipointerstyle.md) describing the pointer shape and content effect. Then assign the closure to [pointerStyleProvider](pointerstyleprovider-1d4d2.md). For more information, see [Enhancing your iPad app with pointer interactions](../enhancing-your-ipad-app-with-pointer-interactions.md).

## See Also

### Supporting pointer interactions

- [pointerInteractionEnabled](ispointerinteractionenabled.md) — A Boolean that enables pointer interaction.
- [hovered](ishovered.md) — A Boolean value that indicates whether a pointer effect is active.
- [UIButtonPointerStyleProvider](../uibuttonpointerstyleprovider.md) — A type alias defining a block that returns a pointer style to apply to a button.
