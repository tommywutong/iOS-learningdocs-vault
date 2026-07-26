---
title: UIButtonPointerStyleProvider
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibuttonpointerstyleprovider
source_url: 'https://developer.apple.com/documentation/uikit/uibuttonpointerstyleprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibuttonpointerstyleprovider.json'
content_hash: 'sha256:99f8e5217b2bc606'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIButtonPointerStyleProvider

<sub>Type Alias</sub>

A type alias defining a block that returns a pointer style to apply to a button.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
typealias UIButtonPointerStyleProvider = (UIButton, __UIPointerEffect, __UIPointerShape) -> UIPointerStyle?
```

## Parameters

- `button` — The button requesting the pointer style.

- `proposedEffect` — The content effect that the system suggests.

- `proposedShape` — The shape of the pointer that the system suggests.

## Return Value

The pointer style to apply to the button when the pointer hovers over it. Return `nil` when you don’t want to apply a pointer style to the button.

## Discussion

To change the appearance of the pointer when it hovers over the button, create a pointer style provider block and assign it to the button’s [pointerStyleProvider](uibutton/pointerstyleprovider-1d4d2.md) property.

## See Also

### Supporting pointer interactions

- [pointerInteractionEnabled](uibutton/ispointerinteractionenabled.md) — A Boolean that enables pointer interaction.
- [hovered](uibutton/ishovered.md) — A Boolean value that indicates whether a pointer effect is active.
- [pointerStyleProvider](uibutton/pointerstyleprovider-y4eb.md) — A closure that returns the pointer style to use when the pointer hovers over the button.
- [PointerStyleProvider](uibutton/pointerstyleprovider-swift.typealias.md) — A type alias defining a closure that returns a pointer style to apply to a button.
