---
title: isPointerInteractionEnabled
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/ispointerinteractionenabled
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/ispointerinteractionenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/ispointerinteractionenabled.json'
content_hash: 'sha256:100286c88fc7b9fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# isPointerInteractionEnabled

<sub>Instance Property</sub>

A Boolean that enables pointer interaction.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var isPointerInteractionEnabled: Bool { get set }
```

## Discussion

The default value of this property is [false](../../swift/false.md).

## See Also

### Supporting pointer interactions

- [hovered](ishovered.md) — A Boolean value that indicates whether a pointer effect is active.
- [pointerStyleProvider](pointerstyleprovider-y4eb.md) — A closure that returns the pointer style to use when the pointer hovers over the button.
- [PointerStyleProvider](pointerstyleprovider-swift.typealias.md) — A type alias defining a closure that returns a pointer style to apply to a button.
- [UIButtonPointerStyleProvider](../uibuttonpointerstyleprovider.md) — A type alias defining a block that returns a pointer style to apply to a button.
