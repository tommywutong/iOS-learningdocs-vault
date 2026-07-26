---
title: keepsMenuPresented
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimenuelement/attributes/keepsmenupresented
source_url: 'https://developer.apple.com/documentation/uikit/uimenuelement/attributes/keepsmenupresented'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenuelement/attributes/keepsmenupresented.json'
content_hash: 'sha256:c51b7e5cadedf29a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIMenuElement](../../uimenuelement.md) · [Attributes](../attributes.md)

# keepsMenuPresented

<sub>Type Property</sub>

An attribute indicating that the menu remains presented after firing the element’s action instead of dismissing.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static var keepsMenuPresented: UIMenuElement.Attributes { get }
```

## Discussion

Use this attribute to allow a person to perform a menu action multiple times without dismissing the menu in between.

This attribute doesn’t have an effect if you build your app with Mac Catalyst.

## See Also

### Attributes

- [UIMenuElementAttributesDestructive](destructive.md) — An attribute indicating the destructive style.
- [UIMenuElementAttributesDisabled](disabled.md) — An attribute indicating the disabled style.
- [UIMenuElementAttributesHidden](hidden.md) — An attribute indicating the hidden style.
