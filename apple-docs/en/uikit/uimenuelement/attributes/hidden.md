---
title: hidden
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimenuelement/attributes/hidden
source_url: 'https://developer.apple.com/documentation/uikit/uimenuelement/attributes/hidden'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenuelement/attributes/hidden.json'
content_hash: 'sha256:72a75c2d5732dae3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIMenuElement](../../uimenuelement.md) · [Attributes](../attributes.md)

# hidden

<sub>Type Property</sub>

An attribute indicating the hidden style.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static var hidden: UIMenuElement.Attributes { get }
```

## Discussion

When you use this attribute, the menu system doesn’t display the menu element. However, if the menu element is a [UIKeyCommand](../../uikeycommand.md) object, the user can still select it using the keyboard shortcut specified by the key command object.

## See Also

### Attributes

- [UIMenuElementAttributesDestructive](destructive.md) — An attribute indicating the destructive style.
- [UIMenuElementAttributesDisabled](disabled.md) — An attribute indicating the disabled style.
- [UIMenuElementAttributesKeepsMenuPresented](keepsmenupresented.md) — An attribute indicating that the menu remains presented after firing the element’s action instead of dismissing.
