---
title: pointerStyleProvider
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/pointerstyleprovider-y4eb
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/pointerstyleprovider-y4eb'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/pointerstyleprovider-y4eb.json'
content_hash: 'sha256:f701727b8af5a17c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# pointerStyleProvider

<sub>Instance Property</sub>

A closure that returns the pointer style to use when the pointer hovers over the button.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency var pointerStyleProvider: UIButton.PointerStyleProvider? { get set }
```

## Discussion

To change the appearance of the pointer when it hovers over the button, create a [PointerStyleProvider](pointerstyleprovider-swift.typealias.md) closure that returns a [UIPointerStyle](../uipointerstyle.md) describing the pointer shape and content effect. Then assign the closure to [pointerStyleProvider](pointerstyleprovider-y4eb.md). For example, the following code listing creates a pointer style that applies a lift effect to the button when the pointer hovers over it.

```swift
threadColorButton.pointerStyleProvider = { button, proposedEffect, proposedShape -> UIPointerStyle? in
    let cornerRadius: CGFloat = 4
    let parameters = UIPreviewParameters()
    let shapePath = UIBezierPath(roundedRect: button.bounds, cornerRadius: cornerRadius)
    parameters.shadowPath = shapePath
    let preview = UITargetedPreview(view: proposedEffect.preview.view, parameters: parameters, target: proposedEffect.preview.target)
    
    let rect = button.convert(button.bounds, to: preview.target.container)
    return UIPointerStyle(effect: .lift(preview), shape: .roundedRect(rect, radius: cornerRadius))
}
```

For more information, see [Enhancing your iPad app with pointer interactions](../enhancing-your-ipad-app-with-pointer-interactions.md).

## See Also

### Supporting pointer interactions

- [pointerInteractionEnabled](ispointerinteractionenabled.md) — A Boolean that enables pointer interaction.
- [hovered](ishovered.md) — A Boolean value that indicates whether a pointer effect is active.
- [PointerStyleProvider](pointerstyleprovider-swift.typealias.md) — A type alias defining a closure that returns a pointer style to apply to a button.
- [UIButtonPointerStyleProvider](../uibuttonpointerstyleprovider.md) — A type alias defining a block that returns a pointer style to apply to a button.
