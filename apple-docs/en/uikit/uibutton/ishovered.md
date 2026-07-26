---
title: isHovered
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/ishovered
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/ishovered'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/ishovered.json'
content_hash: 'sha256:94ec5931e38f334c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# isHovered

<sub>Instance Property</sub>

A Boolean value that indicates whether a pointer effect is active.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isHovered: Bool { get }
```

## Discussion

If you enable pointer interaction by setting [pointerInteractionEnabled](ispointerinteractionenabled.md), this property indicates the button has an active pointer effect.

## See Also

### Related Documentation

- [Pointer interactions](../pointer-interactions.md) — Support pointer interactions in your custom controls and views.

### Supporting pointer interactions

- [pointerInteractionEnabled](ispointerinteractionenabled.md) — A Boolean that enables pointer interaction.
- [pointerStyleProvider](pointerstyleprovider-y4eb.md) — A closure that returns the pointer style to use when the pointer hovers over the button.
- [PointerStyleProvider](pointerstyleprovider-swift.typealias.md) — A type alias defining a closure that returns a pointer style to apply to a button.
- [UIButtonPointerStyleProvider](../uibuttonpointerstyleprovider.md) — A type alias defining a block that returns a pointer style to apply to a button.
