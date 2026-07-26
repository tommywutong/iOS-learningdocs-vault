---
title: inputAccessoryView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiresponder/inputaccessoryview
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder/inputaccessoryview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder/inputaccessoryview.json'
content_hash: 'sha256:e9527cbb1eb156e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponder](../uiresponder.md)

# inputAccessoryView

<sub>Instance Property</sub>

The custom input accessory view to display when the responder becomes the first responder.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var inputAccessoryView: UIView? { get }
```

## Discussion

This property is typically used to attach an accessory view to the system-supplied keyboard that’s presented for [UITextField](../uitextfield.md) and [UITextView](../uitextview.md) objects.

The value of this read-only property is `nil`. If you want to attach custom controls to a system-supplied input view (such as the system keyboard) or to a custom input view (one you provide in the [inputView](inputview.md) property), redeclare this property as read-write in a [UIResponder](../uiresponder.md) subclass. You can then use this property to manage a custom accessory view. When the responder becomes the first responder, the responder infrastructure attaches the accessory view to the appropriate input view before displaying it.

This property has special considerations in visionOS:

- In apps built for visionOS, this property isn’t available. Use [bottomOrnament](../../swiftui/toolbaritemplacement/bottomornament.md) instead.
- In compatible iPad and iPhone apps running in visionOS, the app’s idiom determines this property’s behavior. For apps running in the [UIUserInterfaceIdiomPad](../uiuserinterfaceidiom/pad.md) idiom, the accessory view renders at the bottom of the app window. For apps running in the [UIUserInterfaceIdiomPhone](../uiuserinterfaceidiom/phone.md) idiom, this property doesn’t have any effect.

## See Also

### Managing input views

- [inputView](inputview.md) — The custom input view to display when the responder becomes the first responder.
- [inputViewController](inputviewcontroller.md) — The custom input view controller to use when the responder becomes the first responder.
- [inputAccessoryViewController](inputaccessoryviewcontroller.md) — The custom input accessory view controller to display when the responder becomes the first responder.
- [- reloadInputViews](<reloadinputviews().md>) — Updates the custom input and accessory views when the object is the first responder.
